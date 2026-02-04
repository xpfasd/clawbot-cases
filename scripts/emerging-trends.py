#!/usr/bin/env python3
"""Google Trends 新兴关键词发现器"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os

KEYWORDS = [
    "pixel art generator", "color palette generator", "gradient generator",
    "qr code generator", "favicon generator", "avatar generator",
    "image compressor", "video compressor", "audio converter",
    "base64 encoder", "json formatter", "password generator",
    "uuid generator", "timestamp converter", "emoji keyboard",
    "text to speech", "voice to text", "code editor",
    "sudoku online", "crossword puzzle", "wordle clone",
    "mahjong online", "solitaire online", "quiz game",
    "idle game", "clicker game", "pixel art game",
    "mini games", "browser games", "html5 games"
]

def get_trend_data(keyword, pytrends):
    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if not data.empty:
            return data[keyword].tolist(), data.index.tolist()
    except:
        pass
    return None, None

def main():
    print("分析新兴关键词...")
    pytrends = TrendReq(hl='en-US', tz=360)
    results = []
    
    for kw in KEYWORDS:
        data, _ = get_trend_data(kw, pytrends)
        if data and sum(data) > 0:
            recent = data[-30:] if len(data) > 30 else data
            older = data[:-30] if len(data) > 30 else data
            recent_avg = sum(recent) / len(recent)
            older_avg = sum(older) / len(older) if older else 0
            growth = (recent_avg - older_avg) / max(older_avg, 1) * 100 if older_avg > 0 else 100
            
            results.append({
                'keyword': kw,
                'recent': recent_avg,
                'growth': growth,
                'data': data
            })
    
    results.sort(key=lambda x: (-x['growth'], -x['recent']))
    
    print(f"\n发现 {len(results)} 个关键词:")
    for r in results[:15]:
        print(f"  {r['keyword']}: growth={r['growth']:.0f}%, recent={r['recent']:.1f}")
    
    # 生成趋势图
    print("\n生成趋势图...")
    top_kw = [r['keyword'] for r in results[:12]]
    
    fig, axes = plt.subplots(4, 3, figsize=(16, 14))
    fig.suptitle('Google Trends - Emerging Keywords (Past 1 Year)', fontsize=16, fontweight='bold')
    
    for idx, kw in enumerate(top_kw):
        ax = axes[idx // 3, idx % 3]
        data, dates = get_trend_data(kw, pytrends)
        
        if data:
            ax.plot(dates, data, color='#4285f4', linewidth=2)
            ax.fill_between(dates, data, alpha=0.3, color='#4285f4')
            latest = data[-1] if data else 0
            avg = sum(data) / len(data)
            trend = "UP" if latest > avg else "DOWN"
            ax.set_title(f'{kw}\nLatest: {int(latest)} | Avg: {int(avg)} [{trend}]', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    output_path = '/tmp/trends/emerging_keywords.png'
    plt.savefig(output_path, dpi=120, bbox_inches='tight')
    plt.close()
    
    print(f"保存: {output_path}")
    return results[:15]

if __name__ == "__main__":
    main()
