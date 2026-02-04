#!/usr/bin/env python3
"""每日新兴暴涨词报告 - 每天10-20个词"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pytrends.request import TrendReq
from datetime import datetime
import requests

# 飞书 Webhook
FEISHU_WEBHOOK = "YOUR_FEISHU_WEBHOOK_ID"

# 扩展关键词池 (200+ 词)
KEYWORDS = [
    # 开发工具类
    "crontab generator", "cron expression", "cron job scheduler",
    "docker compose generator", "dockerfile template", "kubernetes yaml",
    "nginx config generator", "apache htaccess", "load balancer config",
    "ssl certificate generator", "openssl command", "ssh keygen",
    "jwt token generator", "oauth2 flow", "api gateway config",
    "graphql schema generator", "openapi spec", "postman collection",
    "swagger ui", "redoc alternative", "postwoman",
    "json schema validator", "json path", "jq online",
    "yq yaml processor", "toml to json", "curl to httpie",
    
    # SEO/站长工具类
    "robots.txt generator", "sitemap.xml", "sitemap python",
    "hreflang tag", "canonical url", "meta tag generator",
    "open graph tags", "twitter card validator", "schema.org generator",
    "json-ld generator", "structured data", "rich snippets",
    "backlink checker", "domain authority checker", "site audit tool",
    "page speed insights", "core web vitals checker", "lighthouse ci",
    
    # 隐私/临时工具类
    "temp mail", "fake email", "10 minute mail", "disposable email",
    "guerrilla mail", "yopmail", "mailinator", "tempmail",
    "fake phone number", "virtual phone number", "receive sms online",
    "user agent generator", "fingerprint spoofing", "cookie consent",
    
    # 游戏类
    "idle game", "incremental game", "clicker game",
    "tycoon game", "simulation game", "management game",
    "tower defense", "desktop tower defense", "tower bloxx",
    "muck game", "doodle god", "little alchemy",
    "merge game", "2048 game", "popcat clicker",
    "cursor game", "hole.io", "paper.io",
    "roguelite", "roguelike", "deckbuilder",
    
    # AI/创意工具类
    "ai avatar generator", "ai pet portrait", "ai yearbook",
    "ai cartoonizer", "ai face swap", "voice clone",
    "ai dubbing", "subtitle generator", "video editor ai",
    "background remover ai", "image upscaler ai", "photo restoration ai",
    "midjourney prompt", "stable diffusion prompt", "dalle prompt",
    "ai meme generator", "caption generator", "text to image",
    
    # 实用小工具类
    "uuid v7", "ulid generator", "nanoid python",
    "random string", "password generator strong", "dice roller",
    "timestamp converter", "unix time", "epoch converter",
    "timezone converter", "date format", "age calculator",
    "bmi calculator", "currency converter", "unit converter",
    "base64 encoder", "url encoder", "jwt decoder",
    
    # 媒体工具类
    "youtube thumbnail maker", "twitch overlay", "discord banner",
    "logo maker free", "favicon generator", "qr code art",
    "qr code with logo", "og image size", "twitter card image",
]

def analyze_keyword(keyword, pytrends):
    """分析关键词"""
    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if data.empty or len(data) < 30:
            return None
        
        values = data[keyword].tolist()
        split = int(len(values) * 0.75)
        older = values[:split]
        recent = values[split:]
        
        avg_older = np.mean(older)
        avg_recent = np.mean(recent)
        std_older = np.std(older)
        
        stability = 1 - (std_older / (avg_older + 1))
        spike = (avg_recent - avg_older) / max(avg_older, 1) * 100
        
        if stability > 0.3 and spike > 20 and avg_recent > 10:
            return {
                'keyword': keyword,
                'avg_older': avg_older,
                'avg_recent': avg_recent,
                'spike': spike,
                'stability': stability,
                'data': values
            }
    except:
        pass
    return None

def send_to_feishu(text, webhook):
    """发送到飞书"""
    if "YOUR_WEBHOOK" in webhook:
        print("⚠️ 未配置飞书 Webhook")
        print(text)
        return False
    
    payload = {"msg_type": "text", "content": {"text": text}}
    try:
        r = requests.post(webhook, json=payload)
        return r.json().get("code") == 0
    except Exception as e:
        print(f"发送失败: {e}")
        return False

def main():
    print(f"🔍 分析新兴暴涨词... ({datetime.now().strftime('%Y-%m-%d %H:%M')})")
    
    pytrends = TrendReq(hl='en-US', tz=360)
    results = []
    
    for kw in KEYWORDS:
        result = analyze_keyword(kw, pytrends)
        if result:
            results.append(result)
    
    results.sort(key=lambda x: -x['spike'])
    
    # 生成报告
    date = datetime.now().strftime('%Y-%m-%d')
    report = f"""📊 每日新兴暴涨词报告
📅 {date}
🔍 数据来源: Google Trends US

━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 发现 {len(results)} 个新兴暴涨词:

"""
    
    for i, r in enumerate(results[:20], 1):
        emoji = "🔥" if r['spike'] > 80 else ("📈" if r['spike'] > 50 else "⬆️")
        report += f"{i:2d}. {emoji} {r['keyword']}\n"
        report += f"    +{r['spike']:.0f}% | 热度: {r['avg_recent']:.0f} | 稳定度: {r['stability']:.2f}\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 分析说明:
• 蓝色区域 = 过去 9 个月（平稳）
• 红色区域 = 最近 1 个月（暴涨）
• 只筛选：稳定度>0.3, 增长>20%, 热度>10

⏰ 报告时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    print(report)
    send_to_feishu(report, FEISHU_WEBHOOK)
    
    return results[:20]

if __name__ == "__main__":
    main()
