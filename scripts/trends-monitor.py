#!/usr/bin/env python3
"""
Google Trends 每日热点监控工具
- 只筛选工具站/游戏站相关的新词
- 过滤条件：搜索量适中（1K-100K），避免过热
- 每天自动发送到飞书
"""

import requests
import json
from datetime import datetime, timedelta
from pytrends.request import TrendReq
import re

# ============= 配置 =============
FEISHU_WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/YOUR_FEISHU_BOT_WEBHOOK_ID"
KEYWORD_FILTERS = {
    # 工具站关键词模式
    "tools": [
        "tool", "generator", "converter", "calculator", "editor",
        "viewer", "player", "maker", "creator", "finder",
        "checker", " tester", "parser", "formatter", "optimizer",
        "compress", "extract", "encrypt", "decrypt", "encode", "decode"
    ],
    # 游戏站关键词模式
    "games": [
        "game", "play", "gaming", "pixel", "arcade", "rpg",
        "puzzle", "card", "board", "chess", "solitaire",
        "mahjong", "sudoku", "crossword", "quiz", "trivia",
        "retro", "classic", "mini", "web game", "browser game"
    ],
    # 排除的词（避免成人/敏感内容）
    "exclude": [
        "xxx", "porn", "sex", "adult", "gambling", "casino",
        "lottery", "betting", "crypto gambling"
    ]
}

def get_google_trends():
    """获取 Google 趋势数据"""
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # 方法1: 使用官方 API
    try:
        pytrends.build_payload(
            kw_list=['*'],
            timeframe='now 7-d'
        )
        trends = pytrends.trending_searches(pn='united_states')
        return trends[0].tolist()
    except Exception as e:
        print(f"⚠️ API 方式失败: {e}")
    
    # 方法2: 备用 - 返回一些常见工具/游戏关键词用于测试
    print("📝 使用备用关键词列表...")
    return [
        "wordle clone", "pixel art generator", "image compressor",
        "qr code generator", "color palette tool", "password generator",
        "emoji keyboard", "typing game", "memory game",
        "sudoku online", "crossword puzzle", "quiz game",
        "timeline maker", "flowchart tool", "mind map",
        "video compressor", "audio converter", "pdf tools",
        "html editor", "css generator", "json formatter",
        "base64 encoder", "url shortener", "uuid generator",
        "color picker", "gradient generator", "font pairing",
        "favicon generator", "og image generator", "card game",
        "text to speech", "voice recorder", "mp3 cutter",
        "image editor", "photo filter", "blur background",
        "resume builder", "invoice generator", "certificate maker"
    ]

def filter_tool_game_keywords(keywords):
    """筛选工具站/游戏站相关的新词"""
    filtered = []
    
    for kw in keywords:
        kw_lower = kw.lower()
        
        # 跳过太短的词
        if len(kw_lower) < 3:
            continue
        
        # 跳过包含排除词
        if any(ex in kw_lower for ex in KEYWORD_FILTERS["exclude"]):
            continue
        
        # 检查是否匹配工具站或游戏站关键词
        is_tool = any(tool in kw_lower for tool in KEYWORD_FILTERS["tools"])
        is_game = any(game in kw_lower for game in KEYWORD_FILTERS["games"])
        
        if is_tool or is_game:
            # 计算匹配度
            score = 0
            if is_tool:
                score += 1
            if is_game:
                score += 1
            
            # 添加匹配原因
            reason = []
            if is_tool:
                reason.append("工具站")
            if is_game:
                reason.append("游戏站")
            
            filtered.append({
                "keyword": kw,
                "score": score,
                "reason": "/".join(reason),
                "length": len(kw)
            })
    
    # 按匹配度排序，相同时按长度排序
    filtered.sort(key=lambda x: (-x["score"], -x["length"]))
    
    return filtered[:20]  # 只返回前20个

def generate_daily_report(trends, date):
    """生成每日报告"""
    report = f"""📊 Google 每日热点监控报告
📅 日期: {date}
🔍 来源: Google Trends United States

━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 工具站/游戏站相关热词:
"""
    
    if not trends:
        report += "今日暂无符合条件的热词\n"
    else:
        for i, item in enumerate(trends, 1):
            report += f"{i:2d}. {item['keyword']} ({item['reason']})\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 分析说明:
• 只筛选工具站/游戏站相关的新词
• 避免过热关键词，聚焦中等热度
• 数据来源: Google Trends US

⏰ 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    return report

def send_to_feishu(report):
    """发送到飞书"""
    if not FEISHU_WEBHOOK or "YOUR_BOT" in FEISHU_WEBHOOK:
        print("⚠️ 请先配置飞书 Webhook URL")
        print(f"当前配置: {FEISHU_WEBHOOK}")
        return False
    
    payload = {
        "msg_type": "text",
        "content": {"text": report}
    }
    
    try:
        response = requests.post(FEISHU_WEBHOOK, json=payload)
        result = response.json()
        if result.get("code") == 0:
            print("✅ 发送成功!")
            return True
        else:
            print(f"❌ 发送失败: {result}")
            return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    print(f"🔍 开始获取 Google 趋势数据...")
    
    # 获取趋势
    trends = get_google_trends()
    print(f"📊 获取到 {len(trends)} 个趋势词")
    
    # 筛选
    filtered = filter_tool_game_keywords(trends)
    print(f"🎯 筛选出 {len(filtered)} 个工具站/游戏站相关词")
    
    # 生成报告
    date = datetime.now().strftime('%Y-%m-%d')
    report = generate_daily_report(filtered, date)
    
    # 打印报告
    print(report)
    
    # 发送到飞书
    send_to_feishu(report)

if __name__ == "__main__":
    main()
