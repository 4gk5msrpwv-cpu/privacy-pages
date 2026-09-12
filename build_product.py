# -*- coding: utf-8 -*-
"""
KidsLearn 产品介绍页生成器（/product/ 路径）。
- 第一版 3 语：en（根）/ zh-Hans / zh-Hant；其余语言二期随中国备案一起补齐并迁移自有域名。
- 截图来自 ACC 素材（iPhone 6.9"，已压缩至 620px 宽 JPEG），目录 product/shots/<lang>/。
- 纯静态、无 JS；改文案只改本文件再运行：
  ~/.workbuddy/binaries/python/envs/default/bin/python build_product.py
  （不依赖 opencc，繁中为手写台湾用语；系统 Python 亦可运行）
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# App Store 链接：上架后把整组替换为真实产品页 URL（各店面自动跳转可用 apps.apple.com 通用链接）
APPSTORE_URL = "https://apps.apple.com/"  # TODO: 上架后替换
PRIV_BASE = "https://4gk5msrpwv-cpu.github.io/privacy-pages"

CSS = """
:root{--blue:#0a7cff;--ink:#1c2330;--sub:#5b6472;--line:#e8ecf2;--bg:#f7f9fc;--card:#ffffff;--amber:#f59e0b}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","PingFang SC","PingFang TC","Helvetica Neue",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}
a{color:var(--blue);text-decoration:none}
.wrap{max-width:1060px;margin:0 auto;padding:0 22px}
header{position:sticky;top:0;background:rgba(247,249,252,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);z-index:10}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:56px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px}
.brand img{width:30px;height:30px;border-radius:8px}
nav.langs{display:flex;gap:14px;font-size:14px}
nav.langs a.on{font-weight:700;color:var(--ink)}
.hero{text-align:center;padding:64px 0 40px}
.hero h1{font-size:34px;line-height:1.25;letter-spacing:.2px}
.hero p.sub{color:var(--sub);font-size:18px;margin:14px auto 6px;max-width:640px}
.badges{margin-top:18px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.pill{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:13px;color:var(--sub)}
.cta{display:inline-block;margin-top:22px;background:var(--ink);color:#fff;font-weight:600;font-size:16px;padding:12px 26px;border-radius:12px}
.cta:hover{opacity:.9}
.shots-hero{margin-top:44px;display:flex;justify-content:center;gap:18px;flex-wrap:wrap}
.shot{width:220px;background:#fff;border:1px solid var(--line);border-radius:24px;padding:8px;box-shadow:0 12px 30px rgba(28,35,48,.08)}
.shot img{width:100%;border-radius:18px;display:block}
section{padding:52px 0}
section h2{font-size:26px;text-align:center}
section p.lead{color:var(--sub);text-align:center;margin:8px auto 30px;max-width:600px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}
.feat{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px;display:flex;gap:16px;align-items:flex-start}
.feat img{width:118px;border-radius:14px;border:1px solid var(--line);flex:none}
.feat h3{font-size:16px;margin-bottom:4px}
.feat p{font-size:14px;color:var(--sub)}
.hl{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:20px 22px}
.hl h3{font-size:15.5px;margin-bottom:4px}
.hl p{font-size:14px;color:var(--sub)}
.hlgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
dl.faq{max-width:760px;margin:0 auto}
dl.faq dt{font-weight:700;margin-top:18px;font-size:15.5px}
dl.faq dd{color:var(--sub);font-size:14.5px;margin-top:4px}
footer{border-top:1px solid var(--line);padding:26px 0 40px;color:var(--sub);font-size:13.5px}
footer .wrap{display:flex;flex-direction:column;gap:6px}
@media (max-width:640px){.hero h1{font-size:26px}.hero p.sub{font-size:16px}.feat{flex-direction:column}.feat img{width:100%}}
"""

ICON = "data:image/svg+xml,"  # 占位：页头不放图，纯文字品牌，避免引入二进制依赖


def page(lang, t, hreflang_map):
    # 截图目录相对路径：en 根页在 /product/ 下，语言子目录页在 /product/<lang>/ 下，
    # 后者必须先回上一级，否则解析成 /product/<lang>/shots/... 404（2026-09-12 线上事故）
    shots = "shots/en" if lang == "en" else f"../shots/{lang}"
    lang_nav = " · ".join(
        f'<a href="{u}"{" class=\"on\"" if k == lang else ""}>{label}</a>'
        for k, u, label in hreflang_map
    )
    feats = "".join(
        f'<div class="feat"><img src="{shots}/{s}" alt="{alt}"><div><h3>{h}</h3><p>{p}</p></div></div>'
        for s, alt, h, p in t["features"]
    )
    hls = "".join(f'<div class="hl"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["highlights"])
    faqs = "".join(f"<dt>{q}</dt><dd>{a}</dd>" for q, a in t["faq"])
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
{{HREFLANG}}
<link rel="canonical" href="{t['canonical']}">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
  <div class="brand">KidsLearn</div>
  <nav class="langs">{lang_nav}</nav>
</div></header>

<div class="hero"><div class="wrap">
  <h1>{t['hero_h1']}</h1>
  <p class="sub">{t['hero_sub']}</p>
  <div class="badges">
    <span class="pill">{t['pill1']}</span>
    <span class="pill">{t['pill2']}</span>
    <span class="pill">{t['pill3']}</span>
  </div>
  <a class="cta" href="{APPSTORE_URL}">{t['cta']}</a>
  <div class="shots-hero">
    <div class="shot"><img src="{shots}/01_today.jpg" alt="{t['alt1']}"></div>
    <div class="shot"><img src="{shots}/02_timetable.jpg" alt="{t['alt2']}"></div>
    <div class="shot"><img src="{shots}/06_rewards.jpg" alt="{t['alt3']}"></div>
  </div>
</div></div>

<section><div class="wrap">
  <h2>{t['feat_h2']}</h2>
  <p class="lead">{t['feat_lead']}</p>
  <div class="grid">{feats}</div>
</div></section>

<section style="background:#eef3fb"><div class="wrap">
  <h2>{t['hl_h2']}</h2>
  <p class="lead">{t['hl_lead']}</p>
  <div class="hlgrid">{hls}</div>
</div></section>

<section><div class="wrap">
  <h2>{t['faq_h2']}</h2>
  <p class="lead">{t['faq_lead']}</p>
  <dl class="faq">{faqs}</dl>
</div></section>

<footer><div class="wrap">
  <div>© 2026 KidsLearn · {t['made']}</div>
  <div><a href="{t['privacy_url']}">{t['privacy_label']}</a> · {t['contact_label']} Your.Kidslearn@outlook.com</div>
</div></footer>
</body>
</html>"""


def main():
    zh_features = [
        ("01_today.jpg", "今日一览", "今日一览", "今天的课程、待完成作业、习惯打卡和可兑换奖品，一屏全部掌握。"),
        ("02_timetable.jpg", "课程表", "课程表", "周一到周日多课表，上午、下午与午休自由安排，节次时间随心定义。"),
        ("03_homework.jpg", "作业管理", "作业管理", "按科目记录作业与截止日期，完成打勾，逾期一目了然。"),
        ("04_habits.jpg", "习惯养成", "习惯养成", "每日打卡、连续天数与成就徽章，让好习惯看得见。"),
        ("05_focus.jpg", "专注计时", "专注计时", "25/35/45 分钟或自定义时长，完成自动记录，培养专注力。"),
        ("06_rewards.jpg", "积分与奖励", "积分与奖励", "完成任务赚积分，兑换家长设置的奖品，正向激励孩子坚持。"),
    ]
    zh_highlights = [
        ("☁️ iCloud 家庭共享", "父母双方 App 实时同步，共同管理孩子的课表与奖励，还能邀请祖辈一起查看。"),
        ("👨‍👩‍👧‍👦 多孩子空间", "每个孩子独立的课程表、作业、习惯和积分，切换即看，互不干扰。"),
        ("🌍 10 种语言", "简体中文、繁體中文、English、日本語、Español、Français、Deutsch、한국어、Русский、Português。"),
        ("🔒 儿童设备锁", "PIN 码保护配置页面，孩子拿到设备也只能看不能改。"),
        ("🛡️ 隐私优先", "无账号、无服务器、无广告追踪。所有数据只存在你自己的 iCloud 私人数据库里。"),
        ("📴 离线可用", "没有网络也能正常查看课程表、记录作业与打卡，联网后自动同步。"),
    ]
    zh_faq = [
        ("孩子的数据存在哪里？安全吗？", "全部数据只保存在你自己的 iCloud 私人数据库（Apple CloudKit）中，开发者无法读取或导出；App 没有账号系统，也没有第三方统计或广告 SDK。"),
        ("需要注册账号吗？", "不需要。下载后直接使用，登录你的 iCloud 即可自动同步与家庭共享。"),
        ("免费试用是怎么样的？", "下载即可免费使用全部功能 7 天；试用结束后需一次性买断解锁，无订阅、无内购陷阱。"),
        ("支持哪些设备？", "支持 iPhone 与 iPad，界面针对两种尺寸分别适配；数据通过 iCloud 在多台设备间同步。"),
    ]
    zh = dict(
        html_lang="zh-Hans",
        title="KidsLearn — 儿童学习管理：课程表 · 作业 · 习惯 · 专注 · 积分奖励",
        desc="KidsLearn 是为家长与孩子设计的学习管理 App：课程表、作业、习惯打卡、专注计时与积分奖励，iCloud 家庭共享同步，隐私优先，免费试用 7 天，一次性买断。",
        hero_h1="让孩子的每一天，井井有条",
        hero_sub="课程表 · 作业 · 习惯 · 专注 · 积分奖励 —— 一款为家庭设计的学习管理 App，孩子和家长都爱用。",
        pill1="免费下载 · 7 天全功能试用", pill2="一次性买断 · 无订阅", pill3="数据只在你的 iCloud",
        cta="App Store 下载",
        alt1="今日一览", alt2="课程表", alt3="积分与奖励",
        feat_h2="一个 App，搞定孩子的学习日常",
        feat_lead="六大功能环环相扣：安排课程、记录作业、坚持习惯、保持专注，再用积分奖励形成正循环。",
        hl_h2="为家庭而设计",
        hl_lead="不只是孩子的工具，更是家长的管理台。",
        faq_h2="常见问题",
        faq_lead="关于数据、账号与购买，你想知道的都在这里。",
        made="用心做的儿童学习管理 App",
        privacy_label="隐私政策与支持",
        contact_label="联系我们：",
        privacy_url=f"{PRIV_BASE}/zh-Hans/",
        canonical=f"{PRIV_BASE}/product/zh-Hans/",
        features=zh_features, highlights=zh_highlights, faq=zh_faq,
    )

    def zht_from_zh(zh):
        # 繁中（台湾用语）手写覆写：仅覆写与简中不同的字符串级字段
        t = dict(zh)
        t.update(html_lang="zh-TW",
                 title="KidsLearn — 兒童學習管理：課程表 · 作業 · 習慣 · 專注 · 點數獎勵",
                 desc="KidsLearn 是為家長與孩子設計的學習管理 App：課程表、作業、習慣打卡、專注計時與點數獎勵，iCloud 家庭共享同步，隱私優先，免費試用 7 天，一次性買斷。",
                 hero_h1="讓孩子的每一天，井井有條",
                 hero_sub="課程表 · 作業 · 習慣 · 專注 · 點數獎勵 —— 一款為家庭設計的學習管理 App，孩子和家長都愛用。",
                 pill1="免費下載 · 7 天全功能試用", pill2="一次性買斷 · 無訂閱", pill3="資料只在你的 iCloud",
                 cta="App Store 下載",
                 alt1="今日一覽", alt2="課程表", alt3="點數與獎勵",
                 feat_h2="一個 App，搞定孩子的學習日常",
                 feat_lead="六大功能環環相扣：安排課程、記錄作業、堅持習慣、保持專注，再用點數獎勵形成正向循環。",
                 hl_h2="為家庭而設計",
                 hl_lead="不只是孩子的工具，更是家長的管理台。",
                 faq_h2="常見問題",
                 faq_lead="關於資料、帳號與購買，你想知道的都在這裡。",
                 made="用心做的兒童學習管理 App",
                 privacy_label="隱私政策與支援",
                 contact_label="聯絡我們：",
                 privacy_url=f"{PRIV_BASE}/zh-Hant/",
                 canonical=f"{PRIV_BASE}/product/zh-Hant/",
                 features=[
                     ("01_today.jpg", "今日一覽", "今日一覽", "今天的課程、待完成作業、習慣打卡和可兌換獎品，一螢幕全部掌握。"),
                     ("02_timetable.jpg", "課程表", "課程表", "週一到週日多課表，上午、下午與午休自由安排，節次時間隨心定義。"),
                     ("03_homework.jpg", "作業管理", "作業管理", "按科目記錄作業與截止日期，完成打勾，逾期一目瞭然。"),
                     ("04_habits.jpg", "習慣養成", "習慣養成", "每日打卡、連續天數與成就徽章，讓好習慣看得見。"),
                     ("05_focus.jpg", "專注計時", "專注計時", "25/35/45 分鐘或自訂時長，完成自動記錄，培養專注力。"),
                     ("06_rewards.jpg", "點數與獎勵", "點數與獎勵", "完成任務賺點數，兌換家長設定的獎品，正向激勵孩子堅持。"),
                 ],
                 highlights=[
                     ("☁️ iCloud 家庭共享", "父母雙方 App 即時同步，共同管理孩子的課表與獎勵，還能邀請祖輩一起查看。"),
                     ("👨‍👩‍👧‍👦 多孩子空間", "每個孩子獨立的課程表、作業、習慣和點數，切換即看，互不干擾。"),
                     ("🌍 10 種語言", "簡體中文、繁體中文、English、日本語、Español、Français、Deutsch、한국어、Русский、Português。"),
                     ("🔒 兒童裝置鎖", "PIN 碼保護設定頁面，孩子拿到裝置也只能看不能改。"),
                     ("🛡️ 隱私優先", "無帳號、無伺服器、無廣告追蹤。所有資料只存在你自己的 iCloud 私人資料庫裡。"),
                     ("📴 離線可用", "沒有網路也能正常查看課程表、記錄作業與打卡，連網後自動同步。"),
                 ],
                 faq=[
                     ("孩子的資料存在哪裡？安全嗎？", "全部資料只保存在你自己的 iCloud 私人資料庫（Apple CloudKit）中，開發者無法讀取或匯出；App 沒有帳號系統，也沒有第三方統計或廣告 SDK。"),
                     ("需要註冊帳號嗎？", "不需要。下載後直接使用，登入你的 iCloud 即可自動同步與家庭共享。"),
                     ("免費試用是怎麼樣的？", "下載即可免費使用全部功能 7 天；試用結束後需一次性買斷解鎖，無訂閱、無內購陷阱。"),
                     ("支援哪些裝置？", "支援 iPhone 與 iPad，介面針對兩種尺寸分別最佳化；資料透過 iCloud 在多台裝置間同步。"),
                 ])
        return t

    en = dict(
        html_lang="en",
        title="KidsLearn — Kids' Learning Manager: Timetable · Homework · Habits · Focus · Rewards",
        desc="KidsLearn is a learning manager for families: timetable, homework, habit tracking, focus timer and points rewards. Private by design — everything stays in your own iCloud. Free 7-day trial, one-time purchase.",
        hero_h1="Every school day, beautifully organized",
        hero_sub="Timetable · Homework · Habits · Focus · Points & rewards — a learning manager designed for the whole family.",
        pill1="Free download · 7-day full trial", pill2="One-time purchase · No subscription", pill3="Your data stays in your iCloud",
        cta="Download on the App Store",
        alt1="Today at a glance", alt2="Timetable", alt3="Points & rewards",
        feat_h2="One app for your child's school day",
        feat_lead="Six features that work together: plan classes, track homework, build habits, stay focused — and keep it going with rewards.",
        hl_h2="Designed for families",
        hl_lead="Not just a tool for kids — a dashboard for parents.",
        faq_h2="FAQ",
        faq_lead="Everything you want to know about data, accounts and purchasing.",
        made="A learning manager made with care",
        privacy_label="Privacy Policy & Support",
        contact_label="Contact us:",
        privacy_url=f"{PRIV_BASE}/",
        canonical=f"{PRIV_BASE}/product/",
        features=[
            ("01_today.jpg", "Today at a glance", "Today at a glance", "Today's classes, pending homework, habit check-ins and redeemable rewards — all on one screen."),
            ("02_timetable.jpg", "Timetable", "Timetable", "Monday-to-Sunday timetables with morning, afternoon and lunch break — period times are fully customizable."),
            ("03_homework.jpg", "Homework", "Homework", "Track assignments by subject with due dates; check them off and nothing slips through."),
            ("04_habits.jpg", "Habit building", "Habit building", "Daily check-ins, streaks and achievement badges make good habits visible."),
            ("05_focus.jpg", "Focus timer", "Focus timer", "25/35/45 minutes or a custom length; completed sessions are logged automatically."),
            ("06_rewards.jpg", "Points & rewards", "Points & rewards", "Earn points for finished tasks and redeem rewards parents have set up — positive motivation that sticks."),
        ],
        highlights=[
            ("☁️ iCloud Family Sharing", "Syncs in real time between both parents — manage timetables and rewards together, and invite grandparents to view."),
            ("👨‍👩‍👧‍👦 Multiple kids", "Each child gets an independent timetable, homework, habits and points. Switch with one tap."),
            ("🌍 10 languages", "English, 简体中文, 繁體中文, 日本語, Español, Français, Deutsch, 한국어, Русский, Português."),
            ("🔒 Kids' device lock", "A PIN protects the settings area — hand the device to your child without worry."),
            ("🛡️ Private by design", "No account, no server, no ad tracking. Everything lives only in your own private iCloud database."),
            ("📴 Works offline", "View the timetable, log homework and check in habits without network; changes sync when you're back online."),
        ],
        faq=[
            ("Where is my child's data stored? Is it safe?", "All data lives only in your own private iCloud database (Apple CloudKit). The developer cannot read or export it. There is no account system and no third-party analytics or ad SDK."),
            ("Do I need to sign up?", "No. Just download and start — sign in to iCloud and syncing plus family sharing work automatically."),
            ("How does the free trial work?", "All features are free for 7 days. After the trial, a one-time purchase unlocks everything — no subscription, no surprises."),
            ("Which devices are supported?", "iPhone and iPad, each with a tailored layout. Data syncs across your devices via iCloud."),
        ],
    )

    hreflang = [
        ("en", f"{PRIV_BASE}/product/", "English"),
        ("zh-Hans", f"{PRIV_BASE}/product/zh-Hans/", "简体中文"),
        ("zh-Hant", f"{PRIV_BASE}/product/zh-Hant/", "繁體中文"),
    ]
    pages = [("en", en), ("zh-Hans", zh), ("zh-Hant", zht_from_zh(zh))]

    refs = "".join(f'<link rel="alternate" hreflang="{k}" href="{u}">' for k, u, _ in hreflang)
    refs += f'<link rel="alternate" hreflang="x-default" href="{PRIV_BASE}/product/">'
    for lang, t in pages:
        out_dir = os.path.join(BASE_DIR, "product") if lang == "en" else os.path.join(BASE_DIR, "product", lang)
        os.makedirs(out_dir, exist_ok=True)
        html = page(lang, t, hreflang).replace("{HREFLANG}", refs)
        path = os.path.join(out_dir, "index.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"written: {os.path.relpath(path, BASE_DIR)} {len(html)} chars")


if __name__ == "__main__":
    main()
