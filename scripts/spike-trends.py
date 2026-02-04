#!/usr/bin/env python3
"""Google Trends 暴涨关键词发现器 - 过去1个月"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os

# 工具站/游戏站长尾关键词池
KEYWORDS = [
    # AI 工具类（近期暴涨）
    "ai headshot generator", "ai yearbook", "ai portrait generator",
    "ai photo editor", "ai image upscaler", "ai background remover",
    "ai voice generator", "ai song generator", "ai video generator",
    "chatgpt wrapper", "gpt wrapper", "llm interface",
    
    # 实用工具类
    "password strength checker", "fake email generator", "temp mail",
    "uuid v7 generator", "unix time converter", "epoch converter",
    "base64 image decoder", "url shortener custom", "qr code art",
    "favicon.io", "og image size", "twitter card validator",
    
    # 游戏类（休闲）
    "wordle unlimited", "globle game", "nerdle",
    "squirdle", "solitaire", "spider solitaire mobile",
    "mahjong connect", "bubble shooter", "match 3 games",
    "tower defense", "tower bloxx", "stickman games",
    
    # 创意工具
    "pixel art ai", "stable diffusion ui", "midjourney prompt",
    "dalle prompt", "ai coloring pages", "meme template",
    "tiktok downloader", "instagram reel download", "yt mp3",
    
    # 开发工具
    "json to yaml", "yaml to json", "toml to json",
    "curl converter", "postman alternative", "api testing tool",
    "regex101", "regex visualizer", "sql formatter online",
]

def get_spike_score(keyword, pytrends):
    """计算暴涨分数：最近7天 vs 之前21天"""
    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 1-m')
        data = pytrends.interest_over_time()
        if data.empty:
            return None
        
        values = data[keyword].tolist()
        if len(values) < 14:
            return None
        
        recent7 = sum(values[-7:]) / 7
        older14 = sum(values[:-7]) / max(len(values) - 7, 1)
        
        # 暴涨分数 = (增长倍数 + 绝对值) * 100
        spike_score = ((recent7 / max(older14, 1)) * recent7)
        
        return {
            'keyword': keyword,
            'recent_avg': recent7,
            'older_avg': older14,
            'growth': (recent7 - older14) / max(older14, 1) * 100,
            'spike_score': spike_score,
            'data': values
        }
    except Exception as e:
        return None

def generate_chart(results, output_path):
    """生成趋势图"""
    top_12 = results[:12]
    if len(top_12) < 4:
        print("数据不足，跳过图表生成")
        return False
    
    cols = 3
    rows = (len(top_12) + cols - 1) // cols
    
    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    fig.suptitle('Google Trends - 暴涨关键词 (过去1个月)', fontsize=16, fontweight='bold')
    
    axes_flat = axes.flatten() if rows > 1 else [axes] if cols == 1 else axes
    
    for idx, r in enumerate(top_12):
        ax = axes_flat[idx]
        data = r['data']
        
        # 绘制趋势线
        ax.plot(data, color='#ff6b6b', linewidth=2)
        ax.fill_between(range(len(data)), data, alpha=0.3, color='#ff6b6b')
        
        # 标注暴涨
        latest = data[-1] if data else 0
        growth = r['growth']
        spike = "🔥" if growth > 50 else ("📈" if growth > 20 else "")
        
        ax.set_title(f'{r["keyword"]}\n{spike} +{growth:.0f}% | Latest: {int(latest)}', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Days')
        ax.set_ylabel('Interest')
    
    # 隐藏多余的 subplot
    for idx in range(len(top_12), len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=120, bbox_inches='tight')
    plt.close()
    return True

def main():
    print("🔍 寻找最近一个月暴涨的关键词...")
    pytrends = TrendReq(hl='en-US', tz=360)
    results = []
    
    for kw in KEYWORDS:
        result = get_spike_score(kw, pytrends)
        if result and result['recent_avg'] > 5:  # 过滤太冷门的
            results.append(result)
    
    # 按暴涨分数排序
    results.sort(key=lambda x: -x['spike_score'])
    
    print(f"\n📊 发现 {len(results)} 个有潜力的关键词:\n")
    for r in results[:20]:
        spike = "🔥" if r['growth'] > 50 else "📈"
        print(f"  {spike} {r['keyword']}: +{r['growth']:.0f}% (热度: {r['recent_avg']:.1f})")
    
    # 生成图表
    print("\n📈 生成趋势图...")
    output_path = '/tmp/trends/spike_keywords.png'
    if generate_chart(results[:12], output_path):
        print(f"✅ 图表已保存: {output_path}")
        print(f"📁 文件大小: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return results[:20]

if __name__ == "__main__":
    main()
