#!/usr/bin/env python3
"""
Google Trends 趋势图生成器
- 获取关键词过去1年的趋势数据
- 生成趋势图并发送到飞书
"""

import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from datetime import datetime, timedelta
import os

# ============= 配置 =============
KEYWORDS = [
    "pixel art generator", "color palette tool", "password generator",
    "gradient generator", "qr code generator", "favicon generator",
    "image compressor", "video compressor", "audio converter",
    "json formatter", "base64 encoder", "uuid generator",
    "crossword puzzle", "sudoku online", "emoji keyboard"
]

FEISHU_WEBHOOK = "YOUR_FEISHU_WEBHOOK_ID"
CHART_DIR = "/tmp/trends_charts"
os.makedirs(CHART_DIR, exist_ok=True)

def get_trend_data(keyword):
    """获取关键词过去1年的趋势数据"""
    pytrends = TrendReq(hl='en-US', tz=360)
    try:
        pytrends.build_payload(
            kw_list=[keyword],
            timeframe='today 12-m'
        )
        interest_over_time = pytrends.interest_over_time()
        if not interest_over_time.empty:
            return interest_over_time[keyword].tolist(), interest_over_time.index.tolist()
    except Exception as e:
        print(f"Error fetching {keyword}: {e}")
    return None, None

def generate_trend_chart(keyword, data, dates):
    """生成单个关键词趋势图"""
    if not data:
        return None
    
    plt.figure(figsize=(10, 4))
    plt.plot(dates, data, color='#4285f4', linewidth=2)
    plt.fill_between(dates, data, alpha=0.3, color='#4285f4')
    plt.title(f'{keyword.title()} - 过去1年趋势', fontsize=14, fontweight='bold')
    plt.xlabel('时间')
    plt.ylabel('搜索热度')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    filepath = f"{CHART_DIR}/{keyword.replace(' ', '_')}.png"
    plt.savefig(filepath, dpi=100)
    plt.close()
    return filepath

def main():
    print("📊 开始生成趋势图...")
    
    chart_files = []
    
    for kw in KEYWORDS[:10]:  # 只生成前10个
        print(f"  📈 {kw}...")
        data, dates = get_trend_data(kw)
        if data:
            filepath = generate_trend_chart(kw, data, dates)
            if filepath:
                chart_files.append((kw, filepath))
    
    print(f"\n✅ 生成了 {len(chart_files)} 张趋势图")
    
    # 打印数据摘要
    print("\n📊 趋势数据摘要:")
    for kw, filepath in chart_files:
        print(f"  ✅ {kw}")
    
    return chart_files

if __name__ == "__main__":
    main()
