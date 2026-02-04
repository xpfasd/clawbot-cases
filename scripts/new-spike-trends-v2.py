#!/usr/bin/env python3
"""扩展版 - 寻找真正的新兴暴涨词（之前平稳，最近暴涨）"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pytrends.request import TrendReq
import os

# ============= 扩展关键词池 =============
KEYWORDS = [
    # === 开发工具类 (新增) ===
    "crontab generator", "cron job scheduler", "celery beat",
    "docker compose generator", "dockerfile template", "kubernetes yaml",
    "nginx config generator", "apache htaccess", "load balancer config",
    "ssl certificate generator", "openssl command", "ssh keygen",
    "jwt token generator", "oauth2 flow", "api gateway config",
    "graphql schema generator", "openapi spec", "postman collection",
    "swagger ui", "redoc alternative", "api documentation tool",
    "curl to httpie", "httpie vs curl", "rest api client",
    "insomnia vs postman", "postwoman", "soapui alternative",
    "postman mock server", "json schema validator", "json path",
    "jq online", "jq command", "yq yaml processor",
    "toml to json", "hcl terraform", "pulumi vs terraform",
    
    # === SEO/站长工具类 (新增) ===
    "robots.txt generator", "sitemap.xml", "sitemap python",
    "hreflang tag", "canonical url", "meta tag generator",
    "open graph tags", "twitter card validator", "schema.org generator",
    "json-ld generator", "structured data", "rich snippets",
    "google search console api", "bing webmaster tools", "yandex webmaster",
    "ahrefs alternative", "semrush alternative", "moz alternative",
    "backlink checker", "domain authority checker", "spam score checker",
    "site audit tool", "crawler tool", "sitemap crawler",
    "page speed insights api", "core web vitals checker", "lighthouse ci",
    "gtmetrix alternative", "pingdom alternative", "uptime robot",
    
    # === 隐私/临时工具类 (新增) ===
    "temp mail", "fake email", "10 minute mail", "disposable email",
    "guerrilla mail", "yopmail", "mailinator", "tempmail",
    "fake phone number", "virtual phone number", "receive sms online",
    "otp bypass", "2fa simulator", "captcha solver",
    "user agent generator", "fingerprint spoofing", "canvas blocker",
    "adblock detection", "cookie consent", "gdpr compliance",
    
    # === 游戏类 (新增) ===
    "idle game", "incremental game", "clicker game",
    "tycoon game", "simulation game", "management game",
    "tower defense", "tower bloxx", "desktop tower defense",
    "muck game", "vomit game", "doodle god",
    "little alchemy", "alchemy game", "merge game",
    "merge dragons", "merge magic", "2048 game",
    "threes game", "2048 variants", "popcat clicker",
    "cursor game", "hole.io", "paper.io",
    "slither.io", "agar.io", "diep.io",
    "roblox online", "roblox unblocked", "roblox download",
    "minecraft unblocked", "minecraft classic", "terraria online",
    
    # === AI/创意工具类 (新增) ===
    "ai avatar generator", "ai pet portrait", "ai yearbook",
    "ai cartoonizer", "ai face swap", "deepfake video",
    "voice clone", "ai dubbing", "subtitle generator",
    "video editor ai", "background remover ai", "image upscaler ai",
    "image compressor ai", "photo restoration ai", "old photo colorizer",
    "painting generator", "sketch to image", "text to image",
    "midjourney prompt", "stable diffusion prompt", "dalle prompt",
    "ai meme generator", "caption generator", "twitter thread ai",
    
    # === 实用小工具类 (新增) ===
    "uuid v7", "ulid generator", "nanoid python",
    "random string", "password generator strong", "dice roller",
    "coin flipper", "random number generator", "lottery number generator",
    "timestamp converter", "unix time", "epoch converter",
    "timezone converter", "date format converter", "age calculator",
    "bmi calculator", "calorie calculator", "tax calculator",
    "currency converter", "unit converter", "base64 encoder",
    "url encoder", "html encoder", "jwt decoder",
    
    # === 媒体工具类 (新增) ===
    "youtube thumbnail maker", "twitch overlay", "discord banner",
    "steam banner maker", "instagram post size", "story size",
    "profile picture maker", "banner maker", "logo maker free",
    "favicon generator", "og image size", "twitter card image",
    "qr code art", "qr code with logo", "qr code generator custom",
    
    # === 复古/怀旧类 (新增) ===
    "retro game emulator", "nes emulator", "snes emulator",
    "genesis emulator", "arcade emulator", "dosbox online",
    "flash player online", "shockwave player", "java applet",
    "classic games online", "flash games archive", "newgrounds alternative",
]

def analyze_keyword(keyword, pytrends):
    """分析关键词：之前平稳 + 最近暴涨"""
    try:
        pytrends.build_payload(kw_list=[keyword], timeframe='today 12-m')
        data = pytrends.interest_over_time()
        if data.empty or len(data) < 30:
            return None
        
        values = data[keyword].tolist()
        if len(values) < 30:
            return None
        
        # 分段分析
        split = int(len(values) * 0.75)
        older = values[:split]
        recent = values[split:]
        
        avg_older = np.mean(older)
        avg_recent = np.mean(recent)
        std_older = np.std(older)
        
        # 稳定性：之前变化小
        stability = 1 - (std_older / (avg_older + 1))
        
        # 暴涨幅度
        spike = (avg_recent - avg_older) / max(avg_older, 1) * 100
        
        # 条件：稳定性>0.4, 暴涨>25%, 最近热度>15
        if stability > 0.4 and spike > 25 and avg_recent > 15:
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

def generate_chart(results, output_path):
    """生成趋势图"""
    top_12 = results[:12]
    cols = 3
    rows = (len(top_12) + cols - 1) // cols
    
    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    fig.suptitle('Google Trends - Emerging Spike Keywords\n(Stable Before, Spiked Recently)', fontsize=14, fontweight='bold')
    
    axes_flat = axes.flatten() if rows > 1 else [axes] if cols == 1 else list(axes)
    
    for idx, r in enumerate(top_12):
        ax = axes_flat[idx]
        data = r['data']
        split = int(len(data) * 0.75)
        
        ax.plot(range(split), data[:split], color='#4285f4', linewidth=2, alpha=0.7)
        ax.plot(range(split, len(data)), data[split:], color='#ff4444', linewidth=3)
        ax.axvline(x=split, color='#ff4444', linestyle='--', alpha=0.5)
        ax.fill_between(range(split), data[:split], alpha=0.2, color='#4285f4')
        ax.fill_between(range(split, len(data)), data[split:], alpha=0.3, color='#ff4444')
        
        emoji = "FIRE" if r['spike'] > 80 else ("UP" if r['spike'] > 50 else "UP")
        ax.set_title(f'{r["keyword"]}\n+{r["spike"]:.0f}% | Recent: {r["avg_recent"]:.0f}', fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Months')
    
    for idx in range(len(top_12), len(axes_flat)):
        axes_flat[idx].axis('off')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=120, bbox_inches='tight')
    plt.close()
    return True

def main():
    print("=" * 60)
    print("🔍 扩展关键词池 - 寻找真正的新兴暴涨词")
    print("   条件: 过去 9 个月平稳，最近 1 个月暴涨")
    print("=" * 60)
    
    pytrends = TrendReq(hl='en-US', tz=360)
    results = []
    
    for kw in KEYWORDS:
        result = analyze_keyword(kw, pytrends)
        if result:
            results.append(result)
    
    results.sort(key=lambda x: -x['spike'])
    
    print(f"\n📊 发现 {len(results)} 个符合条件的关键词:\n")
    for r in results[:20]:
        print(f"  +{r['spike']:.0f}% {r['keyword']} (Recent: {r['avg_recent']:.0f}, Stability: {r['stability']:.2f})")
    
    if results:
        print("\n📈 生成趋势图...")
        output_path = '/tmp/trends/extended_spike_keywords.png'
        if generate_chart(results[:12], output_path):
            print(f"✅ 图表已保存: {output_path}")
            print(f"📁 文件大小: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return results[:20]

if __name__ == "__main__":
    main()
