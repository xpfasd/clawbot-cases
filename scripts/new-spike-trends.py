#!/usr/bin/env python3
"""寻找真正的新兴暴涨词 - 之前平稳，最近一个月暴涨"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pytrends.request import TrendReq
import os

# 大范围关键词池
KEYWORDS = [
    # AI 类新词（2024-2025新出现的）
    "ai yearbook", "ai headshot", "ai portrait ai", "ai pet portrait",
    "ai coloring pages", "ai cartoonizer", "ai undress", "deepnude",
    "face swap free", "voice clone", "voice.ai", "elevenlabs alternative",
    "suno ai", "udio ai", "musicgen", "musicfy",
    
    # 游戏类新词
    "globle", "nerdle", "squirdle", "octordle", "duotrigordle",
    "worldle", "lewdle", "spamle", "crosswordle",
    "idle breakout", "towers", "desktop tower defense",
    "survivor.io", "bloxd", "rabbids", "muck",
    
    # 工具类新词
    "temp mail", "fake email generator", "10 minute mail",
    "guerrilla mail", "yopmail", "mailinator",
    "qr code art", "qr code with logo", "qr code generator custom",
    "favicon generator", "og image generator", "twitter card validator",
    "sitemap generator", "robots.txt generator", "meta tag generator",
    
    # 开发工具
    "postwoman", "postman alternative", "insomnia alternative",
    "hoppscotch", "jsonviewer", "json formatter",
    "base64 image decoder", "url encoder", "jwt decoder",
    "cron generator", "cron expression", "timestamp converter unix",
    
    # 创意工具
    "meme generator free", "meme maker", "caption generator",
    "thumbnail maker", "youtube thumbnail", "twitch overlay maker",
    "banner maker", "discord banner", "steam banner maker",
    
    # 实用工具
    "password generator strong", "uuid v7", "ulid python",
    "nanoid python", "random string generator", "fake data generator",
    "fake address generator", "fake phone number", "fake credit card",
    
    # 新兴游戏
    "pixel art game", "incremental game", "idle game",
    "clicker game", "tycoon game", "roguelike",
    "roguelite", "deckbuilder", "auto battler",
]

def analyze_keyword(keyword, pytrends):
    """分析关键词是否属于：之前平稳 + 最近暴涨"""
    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if data.empty or len(data) < 30:
            return None
        
        values = data[keyword].tolist()
        if len(values) < 30:
            return None
        
        # 分成三段：前6个月、中间3个月、最近1个月
        month1 = values[:int(len(values)*0.4)]  # 前4个月
        month2 = values[int(len(values)*0.4):int(len(values)*0.75)]  # 中间
        month3 = values[int(len(values)*0.75):]  # 最近1个月
        
        avg1 = np.mean(month1)
        avg2 = np.mean(month2)
        avg3 = np.mean(month3)
        
        # 计算平稳度（前9个月变化小）
        stability = 1 - (np.std(month1 + month2) / (max(avg1, avg2) + 1))
        
        # 计算暴涨幅度（最近1个月vs之前）
        if avg3 > avg2:
            spike = (avg3 - avg2) / max(avg2, 1) * 100
        else:
            spike = 0
        
        # 综合评分：稳定性 * 暴涨幅度
        # 条件：前9个月平稳（稳定性>0.3），最近暴涨（spike>30%）
        if stability > 0.3 and spike > 30 and avg3 > 10:
            return {
                'keyword': keyword,
                'avg_early': avg1,
                'avg_recent': avg3,
                'spike': spike,
                'stability': stability,
                'score': stability * spike * (avg3 / 100),
                'data': values
            }
    except Exception as e:
        pass
    return None

def generate_chart(results, output_path):
    """生成趋势图"""
    top_12 = results[:12]
    if len(top_12) < 4:
        return False
    
    cols = 3
    rows = (len(top_12) + cols - 1) // cols
    
    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    fig.suptitle('Google Trends - 真正的新兴暴涨词\n(之前平稳，近期暴涨)', fontsize=14, fontweight='bold')
    
    axes_flat = axes.flatten() if rows > 1 else [axes] if cols == 1 else list(axes)
    
    for idx, r in enumerate(top_12):
        ax = axes_flat[idx]
        data = r['data']
        
        # 标注暴涨区域
        split_point = int(len(data) * 0.75)
        
        ax.plot(range(split_point), data[:split_point], color='#4285f4', linewidth=2, alpha=0.7)
        ax.plot(range(split_point, len(data)), data[split_point:], color='#ff4444', linewidth=3)
        ax.axvline(x=split_point, color='#ff4444', linestyle='--', alpha=0.5)
        
        ax.fill_between(range(split_point), data[:split_point], alpha=0.2, color='#4285f4')
        ax.fill_between(range(split_point, len(data)), data[split_point:], alpha=0.3, color='#ff4444')
        
        spike_emoji = "🔥" if r['spike'] > 100 else ("📈" if r['spike'] > 50 else "⬆️")
        ax.set_title(f'{r["keyword"]}\n{spike_emoji} +{r["spike"]:.0f}% | Recent: {r["avg_recent"]:.0f}', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Months (12 months ago → Now)')
    
    for idx in range(len(top_12), len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=120, bbox_inches='tight')
    plt.close()
    return True

def main():
    print("🔍 寻找真正的新兴暴涨词...")
    print("   条件: 过去1年大部分时间平稳，最近1个月暴涨\n")
    
    pytrends = TrendReq(hl='en-US', tz=360)
    results = []
    
    for kw in KEYWORDS:
        result = analyze_keyword(kw, pytrends)
        if result:
            results.append(result)
    
    # 按暴涨分数排序
    results.sort(key=lambda x: -x['spike'])
    
    print(f"📊 发现 {len(results)} 个符合条件的关键词:\n")
    for r in results[:15]:
        spike = "🔥" if r['spike'] > 100 else ("📈" if r['spike'] > 50 else "⬆️")
        print(f"  {spike} {r['keyword']}: +{r['spike']:.0f}% (热度: {r['avg_recent']:.1f}, 稳定度: {r['stability']:.2f})")
    
    # 生成图表
    print("\n📈 生成趋势图...")
    output_path = '/tmp/trends/new_spike_keywords.png'
    if generate_chart(results[:12], output_path):
        print(f"✅ 图表已保存: {output_path}")
        print(f"📁 文件大小: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return results[:15]

if __name__ == "__main__":
    main()
