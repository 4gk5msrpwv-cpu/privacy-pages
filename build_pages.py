#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KidsLearn 隐私政策 / 支持页 生成器

设计要点
--------
1. 站点结构：根目录 = 英文版（ASC「隐私政策网址」字段只能填一个，必须是英文，
   审核员在任何网络环境下打开都能读懂）；各语言位于 /{lang}/ 子目录。
2. 语言扩展：往 CONTENT 里加一个语种即可自动生成页面，App 侧在
   AppLanguage.privacyPath 里登记该语种目录名，未登记的语种自动回落英文。
3. 大陆站点剥离：App 只需改 AppLinks.siteBaseURL 一个常量，子路径保持不变。
4. 繁体由 opencc 从简体自动转换（pip install opencc-python-reimplemented）。

用法：python3 build_pages.py
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE = "https://4gk5msrpwv-cpu.github.io/privacy-pages"
EFFECTIVE = "2026-09-10"
DEV = "Frank Zhou"
MAIL = "Your.Kidslearn@outlook.com"

LANGS = ["en", "zh-Hans", "zh-Hant", "ja", "es", "pt-BR", "fr", "de", "ko", "ru"]
CANON = {l: ("" if l == "en" else "/" + l) for l in LANGS}   # 各语种路径
# 说明：en 恒为根目录（ASC「隐私政策网址」只有一个字段，必须是审核员可读的英文）。

SWITCH_LABEL = {
    "en": "English", "zh-Hans": "简体中文", "zh-Hant": "繁體中文", "ja": "日本語",
    "es": "Español", "pt-BR": "Português (BR)", "fr": "Français", "de": "Deutsch",
    "ko": "한국어", "ru": "Русский",
}

# ---------------------------------------------------------------------------
# 内容
# ---------------------------------------------------------------------------
CONTENT = {}

CONTENT["en"] = {
    "html_lang": "en",
    "title": "KidsLearn Privacy Policy & Support",
    "desc": "KidsLearn privacy policy and support: we collect no personal information; all data stays in your own iCloud.",
    "h1": "🎓 KidsLearn Privacy Policy & Support",
    "meta_line": "Effective Date: {d} ｜ Developer: {dev} ｜ Contact: {mail}",
    "nav": ["Privacy Policy", "Support & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>In short:</b> KidsLearn <b>does not collect any personal information</b>. There is no account system, no server and no third-party analytics or advertising SDK. Timetables, homework, habits, reminders and points you enter are <b>stored only in your own private iCloud database</b> (Apple CloudKit); the developer cannot read or export them. A <b>Child Device Lock (PIN)</b> is provided as a parental control, and all child-related content is created and managed by a parent.",
    "privacy_title": "Privacy Policy",
    "sections": [
        ("1. Overview", [
            ("p", "KidsLearn is a study-management tool for <b>parents</b>, offering timetables, homework tracking, habit check-ins, reminders and a points/rewards system. It is developed by an independent developer ({dev}) and has <b>no self-hosted server and no backend database</b>. This policy explains how we handle — in fact, do not handle — your information."),
        ]),
        ("2. What We Collect: Nothing", [
            ("p", "KidsLearn <b>does not collect any personal information</b>. Specifically:"),
            ("ul", [
                "<b>No sign-up, no login.</b> We do not request or receive your name, email, phone number, contacts, location, photos or any identifier.",
                "<b>Your data stays in your own iCloud.</b> Timetables, homework, habits, reminders, points and rewards you create are stored in the private iCloud database of your own Apple ID (Apple CloudKit, container <code>iCloud.com.frankzhou.KidLearn</code>). The data belongs to you and is held by Apple; <b>the developer cannot access, read or export it</b>.",
                "<b>Family Sharing &amp; child spaces.</b> Built on Apple CloudKit CKShare. Data is shared only with Apple IDs you explicitly invite (normally family members); you control and can revoke sharing at any time.",
            ]),
            ("p", "<b>Device capabilities and system permissions:</b>"),
            ("ul", [
                "<b>Notifications</b> — used solely to deliver the study reminders you set yourself; no advertising or marketing content. \"Remote notifications\" are used only as a <b>silent trigger for iCloud synchronisation</b> and never display a visible alert.",
                "<b>Photos (system photo picker)</b> — the homework \"scan text (OCR)\" feature picks an image through Apple's system photo picker (PhotosPicker). The app receives <b>only the single image you select</b>, cannot browse or access the rest of your library, and <b>requires no photo-library permission</b>. Recognition runs <b>entirely on device</b> via Apple's Vision framework; neither the image nor the result is <b>ever uploaded</b>, and the original image is not retained. <b>The app does not use the camera and does not request camera permission.</b> Setting a child's profile photo works the same way: only the single image you select is read, compressed and <b>stored solely in your own iCloud account</b> — never uploaded to any server.",
                "<b>Face ID / Touch ID / device passcode</b> — used only to authenticate on this device when a parent changes or resets the Child Device Lock PIN, or turns child mode off. Authentication is performed by iOS; <b>the app never receives, reads or stores any biometric data</b>.",
                "<b>Pasteboard</b> — read once, only when you actively tap \"Paste\", to build a homework list. The text is processed <b>on device</b>; it is <b>never uploaded or retained</b>. The app does not access the pasteboard at any other time.",
                "<b>Permissions we never request</b> — no location, contacts, calendars, reminders, microphone, camera or App Tracking authorisation. Apart from the items above, the app declares no other permissions.",
            ]),
        ]),
        ("3. Third Parties, Tracking and Advertising: None", [
            ("ul", [
                "<b>No third-party code at all</b> — the project depends on no Swift Package, no CocoaPods and no third-party library. There is no advertising SDK, no analytics SDK (no Firebase or similar), no crash-reporting, attribution or push-marketing component.",
                "<b>No tracking</b> — no IDFA, no App Tracking Transparency prompt, no cross-app or cross-site tracking, no tracking cookies, device fingerprinting or local identifiers.",
                "<b>We never sell, share or trade user data</b>, and we do not engage in any form of data monetisation. No data is used for advertising or user profiling.",
                "<b>Apart from loading this policy page, every network request goes to Apple services</b> — iCloud (CloudKit) synchronisation and App Store In-App Purchase (StoreKit). Both are governed by Apple's own privacy policy — see <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple Privacy Policy</a>. (The in-app “Privacy Policy” and “Support” entries open in a built-in reader with no address bar and never leave the app: only this page is loaded, JavaScript is disabled, no cookies or browsing data are written, and navigation to any other domain is blocked. This page is hosted on a third-party static host (GitHub Pages); loading it is the app’s only network request to a non-Apple service, and it carries no account or device identifier.)",
            ]),
        ]),
        ("4. Children's Privacy", [
            ("p", "KidsLearn is a <b>parent-facing management tool</b>, not an app made for children: all content is created and managed by parents. The app offers <b>no</b> chat, comments, public profiles, content discovery or recommendation, interaction with strangers, or public sharing of user-generated content."),
            ("ul", [
                "<b>We do not collect, sell or disclose children's personal information to any third party.</b> Children's study records (nickname, avatar, courses, homework, habits, points, etc.) are entered by parents and <b>stored only in the parent's own iCloud account</b>; the developer has no access to them.",
                "<b>No public user-generated content.</b> Text entered by parents is visible only to family members the parent <b>invites one-to-one</b> via iCloud private sharing (CKShare). There is no public audience, no stranger visibility, and no search or recommendation mechanism, so the app carries none of the social risks associated with public UGC.",
                "<b>Parental controls.</b> The app provides a \"Child Device Lock (PIN)\": once enabled, configuration features are hidden and exiting requires the PIN; changing or resetting the PIN requires system biometric or passcode authentication. Parents can use it to restrict children's access to settings and purchases.",
                "<b>Children's Apple IDs.</b> If a parent shares a child space with a child Apple ID, that account is created and managed by the parent under Apple's rules; sharing remains under the parent's control and can be stopped at any time.",
                "<b>On parental consent.</b> Because the app <b>collects no children's personal information at all</b>, the \"verifiable parental consent\" mechanisms required by COPPA (US), GDPR (children's provisions, EU) and China's Regulations on the Protection of Children's Personal Information Online do not apply, and we do not need to collect any parent identity information for that purpose. Parents may delete any child space and all of its data at any time; deletion takes effect immediately.",
                "We follow China's Personal Information Protection Law and the Regulations on the Protection of Children's Personal Information Online, and align with COPPA / GDPR principles: <b>data minimisation, parental control, no sharing, no selling, and no advertising or profiling</b>.",
                "Parents who wish to review, correct or permanently delete child-related information can do so inside the app, or email {mail} for assistance.",
            ]),
        ]),
        ("5. Data Storage, Security and Deletion", [
            ("ul", [
                "All data resides in the iCloud account of your Apple ID, protected by Apple's encryption and access controls. We keep no server-side copy.",
                "<b>Deleting the app does not automatically remove iCloud data</b> (so you can restore on a new device). To erase everything: on iPhone/iPad go to <i>Settings → your Apple ID → iCloud → Manage Account Storage → KidsLearn → Delete Data</i>; delete the corresponding child space inside the app under <i>Me → Child Spaces</i>; or email {mail} to request deletion assistance.",
                "A small number of interface preferences (language, display settings) are stored <b>locally on the device</b> (system UserDefaults). They never leave your device and are not synced to iCloud.",
                "Please keep your Apple ID and device passcode secure — they are the primary protection for this data.",
            ]),
        ]),
        ("6. Purchases and Payments", [
            ("p", "KidsLearn is free to download with a local 7-day trial. The full version is a <b>one-time purchase (non-consumable, non-subscription; no auto-renewal)</b>. All payments are processed by the Apple App Store (StoreKit). <b>We never receive or store your payment card details</b>, nor can we see your full account information. Family Sharing is enabled, so family members do not need to purchase again."),
        ]),
        ("7. Changes to This Policy", [
            ("p", "If this policy changes, we will update this page and revise the \"Effective Date\" shown at the top. Material changes (for example, introducing any new data collection) will also be announced prominently inside the app. Please review this page periodically for the latest version."),
        ]),
        ("8. Contact Us", [
            ("p", "For any question, complaint or deletion request regarding this policy or your data, email <b>{mail}</b>. We normally reply within <b>3 business days</b>."),
        ]),
    ],
    "support_title": "Support & FAQ",
    "support_rows": [
        ("New device / multi-device sync", "Sign in with the <b>same Apple ID</b> on each device with iCloud Drive enabled; data syncs automatically. If sync stalls, check <i>Settings → Apple ID → iCloud</i>."),
        ("Family / child space sharing", "Use \"Share child space\" in the app (Apple CloudKit CKShare); the recipient accepts with their own Apple ID. Two different Apple IDs are required for testing."),
        ("Restore purchases", "Tap \"Restore Purchases\" at the bottom of the paywall — no additional charge."),
        ("Delete all data", "See section 5 above. Deleting the app does not remove iCloud data."),
        ("Scan text (OCR)", "Runs fully on device via Apple Vision; no upload, no network required."),
        ("Supported languages", "10 languages: Simplified & Traditional Chinese, English, Japanese, Spanish, Portuguese (BR), French, German, Korean and Russian."),
        ("System requirements", "iOS / iPadOS 17.0 or later (iPhone and iPad, including home-screen widgets)."),
        ("Contact", "Email <b>{mail}</b> — replies within 3 business days."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["zh-Hans"] = {
    "html_lang": "zh-CN",
    "title": "KidsLearn 隐私政策与支持",
    "desc": "KidsLearn 隐私政策与支持：不收集任何个人信息，数据仅存储于用户本人 iCloud。",
    "h1": "🎓 KidsLearn 隐私政策与支持",
    "meta_line": "生效日期：{d} ｜ 开发者：{dev} ｜ 联系邮箱：{mail}",
    "nav": ["隐私政策", "支持与常见问题"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>一句话总结：</b>KidsLearn <b>不收集任何个人信息</b>。没有账号系统、没有服务器、没有第三方统计或广告 SDK。你录入的课程表、作业、习惯、提醒与积分数据，<b>只保存在你自己的 iCloud 私人数据库</b>（Apple CloudKit）中，开发者无法读取或导出。应用内置<b>儿童设备锁（PIN）</b>等家长控制功能，儿童相关内容一律由家长创建与管理。",
    "privacy_title": "隐私政策",
    "sections": [
        ("一、概述", [
            ("p", "KidsLearn 是一款面向<b>家长</b>的儿童学习管理工具，提供课程表、作业记录、习惯打卡、学习提醒与积分奖励等功能。本应用由个人开发者（{dev}）独立开发，<b>无自建服务器、无后台数据库</b>。本政策说明我们如何处理（事实上是：不处理）你的信息。"),
        ]),
        ("二、我们收集哪些信息：不收集", [
            ("p", "KidsLearn <b>不主动收集任何个人信息</b>。具体而言："),
            ("ul", [
                "<b>无需注册、无需登录</b>：不要求也不获取姓名、邮箱、手机号、通讯录、位置、相册、身份标识等信息。",
                "<b>学习数据仅存于你的 iCloud</b>：你创建的课程表、作业、习惯、提醒、积分与奖品等内容，保存在你本人 Apple ID 下的 iCloud 私人数据库（Apple CloudKit，容器 <code>iCloud.com.frankzhou.KidLearn</code>）。这些数据归你所有，由 Apple 保管，<b>开发者无法访问、读取或导出</b>。",
                "<b>家庭共享与「孩子空间」</b>：基于 Apple CloudKit 的 CKShare 实现，数据仅在你主动邀请的 Apple ID（通常是家庭成员）之间共享，共享范围完全由你控制，可随时停止共享。",
            ]),
            ("p", "<b>设备能力与系统权限：</b>"),
            ("ul", [
                "<b>通知</b>：用于展示你自行设定的学习提醒，仅在你开启后使用，不含任何广告或营销内容。其中「远程通知」仅用作 iCloud 数据同步的触发信号（静默通知），不会产生任何可见提示，也不承载任何内容。",
                "<b>相册（系统照片选择器）</b>：作业清单的「图片识字」功能通过 Apple 系统照片选择器（PhotosPicker）挑选图片，<b>App 只会拿到你选中的那一张</b>，无法浏览或访问相册中的其他照片，<b>也无需你授予相册权限</b>。文字识别由 Apple Vision 框架<b>完全在设备端</b>完成，图片与识别结果<b>不上传</b>任何服务器，识别后不保留原图。<b>本应用不使用相机，也不申请相机权限。</b>为孩子设置头像照片也走同一机制：同样只拿你选中的那一张，压缩后<b>仅存于你自己的 iCloud 账户</b>，不上传任何服务器。",
                "<b>面容 ID / 触控 ID / 设备密码</b>：仅在家长修改或重置「儿童设备锁 PIN」、以及关闭儿童模式时，用于本机身份验证。验证由 iOS 系统完成，<b>App 不会收到、也无法读取或存储任何生物特征信息</b>。",
                "<b>剪贴板</b>：仅在你主动点击「粘贴」按钮时读取一次剪贴板中的文字，用于生成作业清单；读取后即在设备端处理，<b>不上传、不长期保存</b>。除此之外本应用不会访问剪贴板。",
                "<b>不申请的权限</b>：本应用不申请、不使用定位、通讯录、日历、提醒事项、麦克风、相机、蓝牙跟踪（App 追踪透明度）等权限，工程内除上述项外无任何权限声明。",
            ]),
        ]),
        ("三、第三方服务、追踪与广告：无", [
            ("ul", [
                "本应用<b>不含任何第三方代码库或 SDK</b>：工程不依赖任何第三方包（无 Swift Package、无 CocoaPods），也不含广告 SDK、数据分析 SDK（如 Firebase、友盟等）、崩溃统计、归因或推送营销组件。",
                "<b>不追踪</b>：不使用 IDFA，不申请 App 追踪透明度授权，不进行跨应用或跨网站追踪，不设置用于追踪的 Cookie、设备指纹或本地标识。",
                "<b>不出售、不共享、不交易</b>任何用户数据；本应用不参与任何形式的数据商业化，也不将数据用于广告投放或用户画像。",
                "除加载本隐私政策页面外，应用发起的<b>全部网络请求均指向 Apple 官方服务</b>：iCloud（CloudKit）数据同步，以及 App Store 内购（StoreKit）。二者均由 Apple 按其自身隐私政策处理，详见 <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple 隐私政策</a>。（应用内「隐私政策」「支持与反馈」通过内置阅读器打开，不显示地址栏，也不跳转到外部浏览器：仅加载本页面，已禁用 JavaScript，不写入 Cookie 或任何浏览数据，跳转到其他域名一律拦截。本页面托管于第三方静态托管服务（GitHub Pages），加载它是本应用唯一一次指向非 Apple 服务的网络请求，且该请求不携带任何账号或设备标识。）",
            ]),
        ]),
        ("四、儿童（未成年人）信息保护", [
            ("p", "KidsLearn 定位为<b>面向家长的管理工具</b>，而非儿童向应用：所有内容由家长创建与管理。应用<b>不提供</b>聊天、评论、公开主页、内容推荐/发现、陌生人互动或用户生成内容的公开发布功能。"),
            ("ul", [
                "<b>我们不收集、不出售、不向第三方披露儿童个人信息</b>。儿童相关的学习记录（昵称、头像、课程、作业、习惯、积分等）全部由家长录入，<b>仅存储在家长自己的 iCloud 账户中</b>，开发者不接触、不可见。",
                "<b>无公开用户生成内容</b>：家长录入的文字内容仅在家长通过 iCloud 隐私共享（CKShare）<b>一对一邀请</b>的家庭成员之间可见，不向公众开放、无陌生人可见渠道、无搜索或推荐机制，因此本应用不涉及公开用户生成内容（UGC）相关的社交风险。",
                "<b>家长控制工具</b>：应用提供「儿童设备锁（PIN 保护）」——开启后配置类功能被隐藏，退出需输入 PIN；修改或重置 PIN 需通过系统生物识别或设备密码验证。家长可借此限制儿童对设置与购买的访问。",
                "<b>儿童 Apple ID</b>：若家长把孩子空间共享给儿童 Apple ID，该账号依法由家长创建与管理，共享范围始终由家长掌控，可随时停止共享。",
                "<b>关于家长同意</b>：由于本应用<b>完全不收集儿童个人信息</b>，美国 COPPA、欧盟 GDPR（儿童条款）以及中国《儿童个人信息网络保护规定》所要求的「可验证家长同意」机制在本应用中不适用；我们也不需要为此收集家长身份信息。家长可随时删除任一「孩子空间」及其全部数据，删除即刻生效。",
                "我们遵循中国《个人信息保护法》《儿童个人信息网络保护规定》，并参照 COPPA、GDPR 对儿童数据的保护原则：<b>最小必要、家长控制、不共享、不出售、不用于广告或画像</b>。",
                "如家长希望查询、更正或彻底删除与儿童相关的信息，可在应用内直接操作，或发送邮件至 {mail}，我们将提供协助。",
            ]),
        ]),
        ("五、数据存储、安全与删除", [
            ("ul", [
                "全部数据保存在你的 Apple ID 对应的 iCloud 账户中，受 Apple 的加密与访问控制保护，我们没有任何服务端副本。",
                "<b>卸载 App 不会自动删除 iCloud 中的数据</b>（便于换机恢复）。如需彻底删除：在 iPhone/iPad 进入「设置 → 顶部 Apple ID → iCloud → 管理账户储存空间 → KidsLearn → 删除数据」；或在 App 内进入「我的 → 孩子空间」，删除对应空间；也可发邮件至 {mail} 请求删除协助。",
                "少量界面偏好（如语言、展示设置）保存在<b>设备本地</b>（系统 UserDefaults），不会离开你的设备，也不与 iCloud 同步。",
                "请妥善保管你的 Apple ID 与设备锁屏密码，这是保护这些数据的主要手段。",
            ]),
        ]),
        ("六、购买与付款", [
            ("p", "KidsLearn 免费下载并提供本地 7 天试用；完整版为<b>一次性买断（非订阅型内购，无自动续费）</b>。所有支付由 Apple App Store（StoreKit）处理，<b>我们不会收到或存储你的支付卡信息</b>，也看不到你的完整账户信息。内购已开启「家人共享」，家庭成员无需重复购买。"),
        ]),
        ("七、政策更新", [
            ("p", "如本政策发生变更，我们会更新本页面并修改顶部的「生效日期」；若涉及重大变更（例如新增数据收集），将在应用内以显著方式提示。建议你定期查看本页面以获取最新内容。"),
        ]),
        ("八、联系我们", [
            ("p", "如你对本政策或数据处理有任何疑问、投诉或删除请求，请发送邮件至 <b>{mail}</b>，我们通常在 <b>3 个工作日</b>内回复。"),
        ]),
    ],
    "support_title": "支持与常见问题",
    "support_rows": [
        ("换机 / 多设备同步", "在各设备上登录<b>同一个 Apple ID</b> 并开启 iCloud 云盘后打开 KidsLearn，数据会自动同步。若长时间未同步，请检查系统「设置 → Apple ID → iCloud」是否已登录且网络正常。"),
        ("家人 / 孩子空间共享", "在 App 内使用「孩子空间分享」（基于 Apple CloudKit CKShare）生成链接，对方用其 Apple ID 接受即可。需要两个不同的 Apple ID 才能完成测试。"),
        ("恢复购买", "打开付费页，点击底部「恢复购买」，按系统提示用购买时使用的 Apple ID 验证即可，不会重复扣费。"),
        ("彻底删除数据", "见上方「数据存储、安全与删除」章节。卸载 App 不会删除 iCloud 数据。"),
        ("拍照识字（OCR）", "使用 Apple Vision 在设备端识别，无需联网，图片不上传。"),
        ("支持的语言", "简体中文、繁体中文、English、日本語、Español、Português (BR)、Français、Deutsch、한국어、Русский（共 10 种）。"),
        ("系统要求", "iOS / iPadOS 17.0 或更高版本（iPhone 与 iPad 通用，含桌面小组件）。"),
        ("联系我们", "邮箱：<b>{mail}</b>（一般 3 个工作日内回复）。"),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["ja"] = {
    "html_lang": "ja",
    "title": "KidsLearn プライバシーポリシーとサポート",
    "desc": "KidsLearn のプライバシーポリシーとサポート：個人情報は一切収集しません。データはお客様ご自身の iCloud にのみ保存されます。",
    "h1": "🎓 KidsLearn プライバシーポリシーとサポート",
    "meta_line": "施行日：{d} ｜ 開発者：{dev} ｜ 連絡先：{mail}",
    "nav": ["プライバシーポリシー", "サポート・よくあるご質問"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>要約：</b>KidsLearn は<b>個人情報を一切収集しません</b>。アカウント登録も、サーバーも、第三者による解析・広告 SDK もありません。入力された時間割・宿題・習慣・リマインダー・ポイントのデータは、<b>お客様ご自身のプライベート iCloud データベース</b>（Apple CloudKit）にのみ保存され、開発者が閲覧・書き出しすることはできません。<b>こどもモード（PIN ロック）</b>などの保護者向け管理機能を備え、こどもに関する内容はすべて保護者が作成・管理します。",
    "privacy_title": "プライバシーポリシー",
    "sections": [
        ("1. 概要", [
            ("p", "KidsLearn は<b>保護者</b>向けの学習管理アプリです。時間割、宿題の記録、習慣のチェック、学習リマインダー、ポイント報酬などの機能を提供します。個人開発者（{dev}）が開発しており、<b>自社サーバーもバックエンドデータベースもありません</b>。本ポリシーは、私たちがお客様の情報をどのように扱うか（実際には扱わないか）を説明するものです。"),
        ]),
        ("2. 収集する情報：ありません", [
            ("p", "KidsLearn は<b>個人情報を一切収集しません</b>。具体的には："),
            ("ul", [
                "<b>登録不要・ログイン不要。</b>氏名、メールアドレス、電話番号、連絡先、位置情報、写真、識別子などを求めることも取得することもありません。",
                "<b>データはお客様の iCloud にのみ。</b>作成された時間割・宿題・習慣・リマインダー・ポイント・ごほうびは、お客様ご自身の Apple ID のプライベート iCloud データベース（Apple CloudKit、コンテナ <code>iCloud.com.frankzhou.KidLearn</code>）に保存されます。データはお客様に帰属し Apple が保管します。<b>開発者がアクセス・閲覧・書き出しすることはできません</b>。",
                "<b>ファミリー共有と「こどもスペース」。</b>Apple CloudKit の CKShare を使用し、お客様が明示的に招待した Apple ID（通常はご家族）とのみ共有されます。共有範囲はお客様が管理し、いつでも停止できます。",
            ]),
            ("p", "<b>端末機能とシステム権限：</b>"),
            ("ul", [
                "<b>通知</b>：お客様が設定した学習リマインダーの表示のみに使用し、広告やマーケティング内容は含まれません。「リモート通知」は iCloud 同期の<b>きっかけ（サイレント通知）</b>としてのみ使われ、画面に表示されることはありません。",
                "<b>写真（システムの写真選択）</b>：宿題の「文字認識」機能は Apple のシステム写真選択（PhotosPicker）で画像を選びます。アプリが受け取るのは<b>選択された 1 枚のみ</b>で、ライブラリ全体を参照することはできず、<b>写真ライブラリの権限も不要</b>です。認識は Apple Vision により<b>すべて端末内</b>で行われ、画像も結果も<b>サーバーに送信されません</b>。認識後に元画像を保持することもありません。<b>カメラは使用せず、カメラ権限も要求しません。</b>こどものアバター写真の設定も同じ仕組みです：選択した 1 枚だけを読み取り、圧縮して<b>保護者自身の iCloud アカウントにのみ</b>保存し、サーバーへは一切送信しません。",
                "<b>Face ID / Touch ID / 端末パスコード</b>：保護者が「こどもモード PIN」を変更・再設定する場合や、こどもモードを解除する場合の本人確認にのみ使用します。認証は iOS が行い、<b>アプリが生体情報を取得・読み取り・保存することはありません</b>。",
                "<b>ペーストボード</b>：お客様が「貼り付け」をタップしたときに 1 度だけテキストを読み取り、宿題リストの作成に使います。<b>端末内</b>で処理し、<b>送信も保存もありません</b>。それ以外の場面でペーストボードにアクセスすることはありません。",
                "<b>要求しない権限</b>：位置情報、連絡先、カレンダー、リマインダー、マイク、カメラ、App トラッキングなどの権限は要求も使用もしません。",
            ]),
        ]),
        ("3. 第三者サービス・トラッキング・広告：なし", [
            ("ul", [
                "<b>第三者のコードは一切なし</b>：Swift Package や CocoaPods など第三者ライブラリに依存せず、広告 SDK、解析 SDK（Firebase 等）、クラッシュ収集、アトリビューション、マーケティング配信の仕組みもありません。",
                "<b>トラッキングなし</b>：IDFA を使用せず、App トラッキングの許可も要求しません。アプリ間・サイト間のトラッキング、トラッキング用 Cookie、指紋認証、ローカル識別子も使用しません。",
                "<b>データの販売・共有・取引は一切行いません。</b>広告配信やユーザープロファイリングにも利用しません。",
                "本ポリシーページの読み込みを除き、<b>すべての通信は Apple のサービス宛てのみ</b>：iCloud（CloudKit）同期と App Store のアプリ内課金（StoreKit）です。いずれも Apple のプライバシーポリシーに従い処理されます。<a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple のプライバシーポリシー</a>をご確認ください。（アプリ内の「プライバシーポリシー」「サポート」はアドレスバーを表示しない内蔵リーダーで開き、外部ブラウザへは移動しません。読み込むのは本ページのみで、JavaScript は無効化され、Cookie や閲覧データは一切書き込まれず、他ドメインへの遷移はブロックされます。本ページは第三者の静的ホスティング（GitHub Pages）でホストされており、この読み込みが本アプリから Apple 以外のサービスへの唯一の通信です。アカウントや端末の識別子は送信されません。）",
            ]),
        ]),
        ("4. こども（未成年者）の情報保護", [
            ("p", "KidsLearn は<b>保護者向けの管理ツール</b>であり、こども向けアプリではありません。すべての内容は保護者が作成・管理します。チャット、コメント、公開プロフィール、コンテンツの発見・レコメンド、見知らぬ人との交流、ユーザー生成コンテンツの公開共有機能は<b>ありません</b>。"),
            ("ul", [
                "<b>こどもの個人情報を収集・販売・第三者開示することはありません。</b>こどもの学習記録（ニックネーム、アバター、教科、宿題、習慣、ポイント等）は保護者が入力し、<b>保護者自身の iCloud アカウントにのみ</b>保存されます。開発者はアクセスできません。",
                "<b>公開されるユーザー生成コンテンツはありません。</b>保護者が入力したテキストは、保護者が iCloud プライベート共有（CKShare）で<b>1 対 1 で招待した</b>家族にのみ表示されます。一般公開も、見知らぬ人への公開も、検索・レコメンドもありません。",
                "<b>保護者による管理機能。</b>「こどもモード（PIN）」をオンにすると設定機能が隠され、解除には PIN が必要です。PIN の変更・再設定には生体認証または端末パスコードが必要です。",
                "<b>こども用 Apple ID。</b>保護者がこども用 Apple ID にスペースを共有した場合、そのアカウントは Apple の規約に従い保護者が作成・管理するものであり、共有は常に保護者が管理し、いつでも停止できます。",
                "<b>保護者の同意について。</b>本アプリは<b>こどもの個人情報を一切収集しない</b>ため、米国 COPPA、EU GDPR（こどもに関する規定）、中国「児童個人情報ネットワーク保護規定」が定める「検証可能な保護者の同意」の仕組みは適用されず、そのために保護者の身元情報を収集することもありません。保護者はいつでもこどもスペースとその全データを削除でき、即時に反映されます。",
                "中国「個人情報保護法」「児童個人情報ネットワーク保護規定」に従い、COPPA / GDPR の原則にも準拠します：<b>最小限の収集、保護者による管理、共有しない、販売しない、広告やプロファイリングに利用しない</b>。",
                "こどもに関する情報の閲覧・訂正・完全削除をご希望の場合は、アプリ内で操作いただくか、{mail} までご連絡ください。",
            ]),
        ]),
        ("5. データの保存・保護・削除", [
            ("ul", [
                "すべてのデータはお客様の Apple ID の iCloud アカウントに保存され、Apple の暗号化とアクセス制御で保護されます。サーバー側にコピーは保持しません。",
                "<b>アプリを削除しても iCloud のデータは自動的には消えません</b>（機種変更時の復元のため）。完全に消去する場合は、iPhone / iPad の「設定 → Apple ID → iCloud → アカウントのストレージを管理 → KidsLearn → データを削除」、またはアプリ内の「マイページ → こどもスペース」から該当スペースを削除してください。{mail} までご連絡いただいても対応します。",
                "一部の表示設定（言語など）は<b>端末内の</b>システム UserDefaults に保存されます。端末外に出ることはなく、iCloud とも同期しません。",
                "Apple ID と端末のロック解除パスコードを適切に管理してください。これらがデータを守る主な手段です。",
            ]),
        ]),
        ("6. 購入とお支払い", [
            ("p", "KidsLearn は無料でダウンロードでき、7 日間のローカル試用期間があります。完全版は<b>買い切り型（非消費型・非サブスクリプション、自動更新なし）</b>です。お支払いは Apple App Store（StoreKit）が処理し、<b>クレジットカード情報を取得・保存することはありません</b>。ファミリー共有に対応しているため、ご家族が重複して購入する必要はありません。"),
        ]),
        ("7. ポリシーの変更", [
            ("p", "本ポリシーを変更した場合は、このページを更新し上部の「施行日」を改めます。重要な変更（新しいデータ収集の開始など）については、アプリ内でも目立つ形でお知らせします。最新の内容をご確認いただくため、定期的にこのページをご覧ください。"),
        ]),
        ("8. お問い合わせ", [
            ("p", "本ポリシーやデータの取り扱いに関するご質問・苦情・削除のご要望は <b>{mail}</b> までご連絡ください。通常 <b>3 営業日</b>以内に返信いたします。"),
        ]),
    ],
    "support_title": "サポート・よくあるご質問",
    "support_rows": [
        ("機種変更・複数端末での同期", "各端末で<b>同じ Apple ID</b> でサインインし、iCloud ドライブを有効にすると自動的に同期されます。同期しない場合は「設定 → Apple ID → iCloud」をご確認ください。"),
        ("家族・こどもスペースの共有", "アプリ内の「こどもスペースを共有」（Apple CloudKit CKShare）を使用し、相手が自分の Apple ID で受け入れます。テストには 2 つの異なる Apple ID が必要です。"),
        ("購入の復元", "購入画面下部の「購入を復元」をタップしてください。重複して課金されることはありません。"),
        ("データの完全削除", "上記「5. データの保存・保護・削除」をご覧ください。アプリの削除では iCloud のデータは消えません。"),
        ("文字認識（OCR）", "Apple Vision により端末内で処理します。アップロードもネットワーク接続も不要です。"),
        ("対応言語", "簡体字中国語、繁体字中国語、英語、日本語、スペイン語、ポルトガル語（ブラジル）、フランス語、ドイツ語、韓国語、ロシア語（全 10 言語）。"),
        ("システム要件", "iOS / iPadOS 17.0 以降（iPhone と iPad 対応、ホーム画面ウィジェットを含む）。"),
        ("お問い合わせ", "メール：<b>{mail}</b>（通常 3 営業日以内に返信）。"),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["es"] = {
    "html_lang": "es",
    "title": "Política de privacidad y soporte de KidsLearn",
    "desc": "Política de privacidad y soporte de KidsLearn: no recopilamos ninguna información personal; todos los datos permanecen en tu propio iCloud.",
    "h1": "🎓 Política de privacidad y soporte de KidsLearn",
    "meta_line": "Fecha de entrada en vigor: {d} ｜ Desarrollador: {dev} ｜ Contacto: {mail}",
    "nav": ["Política de privacidad", "Soporte y preguntas frecuentes"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>En resumen:</b> KidsLearn <b>no recopila ninguna información personal</b>. No hay sistema de cuentas, ni servidor, ni SDK de analítica o publicidad de terceros. Los horarios, tareas, hábitos, recordatorios y puntos que introduzcas se <b>guardan únicamente en tu propia base de datos privada de iCloud</b> (Apple CloudKit); el desarrollador no puede leerlos ni exportarlos. Se incluye un <b>Bloqueo infantil del dispositivo (PIN)</b> como control parental, y todo el contenido relacionado con menores es creado y gestionado por un progenitor.",
    "privacy_title": "Política de privacidad",
    "sections": [
        ("1. Descripción general", [
            ("p", "KidsLearn es una herramienta de gestión de estudios para <b>padres y madres</b>, que ofrece horarios, registro de tareas, control de hábitos, recordatorios de estudio y un sistema de puntos y recompensas. Está desarrollada por un desarrollador independiente ({dev}) y <b>no tiene servidor propio ni base de datos en backend</b>. Esta política explica cómo tratamos —en realidad, cómo no tratamos— tu información."),
        ]),
        ("2. Qué recopilamos: nada", [
            ("p", "KidsLearn <b>no recopila ninguna información personal</b>. En concreto:"),
            ("ul", [
                "<b>Sin registro, sin inicio de sesión.</b> No solicitamos ni recibimos tu nombre, correo electrónico, teléfono, contactos, ubicación, fotos ni ningún identificador.",
                "<b>Tus datos permanecen en tu propio iCloud.</b> Los horarios, tareas, hábitos, recordatorios, puntos y recompensas que creas se guardan en la base de datos privada de iCloud de tu propio Apple ID (Apple CloudKit, contenedor <code>iCloud.com.frankzhou.KidLearn</code>). Los datos te pertenecen y los custodia Apple; <b>el desarrollador no puede acceder a ellos, leerlos ni exportarlos</b>.",
                "<b>Compartir en familia y «espacios infantiles».</b> Basado en CKShare de Apple CloudKit. Los datos solo se comparten con los Apple ID que invites explícitamente (normalmente familiares); tú controlas el uso compartido y puedes revocarlo en cualquier momento.",
            ]),
            ("p", "<b>Funciones del dispositivo y permisos del sistema:</b>"),
            ("ul", [
                "<b>Notificaciones</b>: se usan únicamente para mostrar los recordatorios de estudio que tú mismo configuras; no incluyen publicidad ni contenido de marketing. Las «notificaciones remotas» se usan solo como <b>señal silenciosa para la sincronización con iCloud</b> y nunca muestran un aviso visible.",
                "<b>Fotos (selector de fotos del sistema)</b>: la función «escanear texto (OCR)» de las tareas selecciona una imagen mediante el selector de fotos del sistema de Apple (PhotosPicker). La app recibe <b>solo la imagen que seleccionas</b>, no puede explorar ni acceder al resto de tu biblioteca y <b>no requiere permiso de la fototeca</b>. El reconocimiento se realiza <b>íntegramente en el dispositivo</b> con el marco Vision de Apple; ni la imagen ni el resultado se <b>envían nunca</b> a ningún servidor y la imagen original no se conserva. <b>La app no usa la cámara ni solicita permiso de cámara.</b> Definir la foto de avatar de un menor sigue el mismo mecanismo: solo se lee la imagen seleccionada, se comprime y se guarda <b>únicamente en tu propia cuenta de iCloud</b>; nunca se sube a ningún servidor.",
                "<b>Face ID / Touch ID / código del dispositivo</b>: se usa solo para verificar la identidad en este dispositivo cuando un progenitor cambia o restablece el PIN del Bloqueo infantil, o desactiva el modo infantil. La autenticación la realiza iOS; <b>la app nunca recibe, lee ni almacena ningún dato biométrico</b>.",
                "<b>Portapapeles</b>: se lee una sola vez, únicamente cuando tocas activamente «Pegar», para crear una lista de tareas. El texto se procesa <b>en el dispositivo</b>; <b>nunca se envía ni se conserva</b>. La app no accede al portapapeles en ningún otro momento.",
                "<b>Permisos que nunca solicitamos</b>: ubicación, contactos, calendarios, recordatorios, micrófono, cámara ni autorización de seguimiento de apps. Aparte de lo anterior, la app no declara ningún otro permiso.",
            ]),
        ]),
        ("3. Terceros, seguimiento y publicidad: ninguno", [
            ("ul", [
                "<b>Ningún código de terceros</b>: el proyecto no depende de ningún paquete Swift, ni CocoaPods, ni biblioteca de terceros. No hay SDK de publicidad, ni SDK de analítica (ni Firebase ni similares), ni recopilación de informes de fallos, atribución ni marketing push.",
                "<b>Sin seguimiento</b>: no se usa IDFA, no se solicita la autorización de App Tracking Transparency, no hay seguimiento entre apps ni entre sitios, ni cookies de seguimiento, huella digital del dispositivo ni identificadores locales.",
                "<b>Nunca vendemos, compartimos ni comercializamos datos de usuarios</b>, y no participamos en ninguna forma de monetización de datos. Ningún dato se usa para publicidad ni para elaborar perfiles de usuario.",
                "<b>Salvo la carga de esta página, todas las solicitudes de red se dirigen únicamente a servicios de Apple</b>: sincronización con iCloud (CloudKit) y compras integradas de la App Store (StoreKit). Ambas se rigen por la política de privacidad de Apple: consulta la <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">política de privacidad de Apple</a>. (Las entradas «Política de privacidad» y «Soporte» se abren en un lector integrado sin barra de direcciones y no salen de la app: solo se carga esta página, JavaScript está desactivado, no se escriben cookies ni datos de navegación y se bloquea la navegación a cualquier otro dominio. Esta página se aloja en un servicio de alojamiento estático de terceros (GitHub Pages); cargarla es la única solicitud de red de la app a un servicio ajeno a Apple y no incluye ningún identificador de cuenta o de dispositivo.)",
            ]),
        ]),
        ("4. Privacidad de los menores", [
            ("p", "KidsLearn es una <b>herramienta de gestión para progenitores</b>, no una app dirigida a menores: todo el contenido lo crean y gestionan los padres o tutores. La app <b>no</b> ofrece chat, comentarios, perfiles públicos, descubrimiento ni recomendación de contenidos, interacción con desconocidos, ni publicación pública de contenido generado por los usuarios."),
            ("ul", [
                "<b>No recopilamos, vendemos ni divulgamos a terceros información personal de menores.</b> Los registros de estudio de los menores (apodo, avatar, asignaturas, tareas, hábitos, puntos, etc.) los introducen los progenitores y se <b>guardan únicamente en la cuenta de iCloud del progenitor</b>; el desarrollador no tiene acceso a ellos.",
                "<b>Sin contenido público generado por usuarios.</b> El texto introducido por los progenitores solo es visible para los familiares que el progenitor <b>invita individualmente</b> mediante el uso compartido privado de iCloud (CKShare). No hay audiencia pública, ni visibilidad para desconocidos, ni mecanismos de búsqueda o recomendación, por lo que la app no presenta ninguno de los riesgos sociales asociados al contenido público generado por usuarios.",
                "<b>Controles parentales.</b> La app ofrece un «Bloqueo infantil del dispositivo (PIN)»: una vez activado, las funciones de configuración se ocultan y salir requiere el PIN; cambiar o restablecer el PIN exige autenticación biométrica del sistema o el código del dispositivo. Los progenitores pueden usarlo para restringir el acceso de los menores a los ajustes y a las compras.",
                "<b>Apple ID de menores.</b> Si un progenitor comparte un espacio infantil con el Apple ID de un menor, esa cuenta la crea y gestiona el progenitor conforme a las normas de Apple; el uso compartido permanece bajo su control y puede detenerse en cualquier momento.",
                "<b>Sobre el consentimiento parental.</b> Dado que la app <b>no recopila ninguna información personal de menores</b>, los mecanismos de «consentimiento parental verificable» exigidos por la COPPA (EE. UU.), el RGPD (disposiciones sobre menores, UE) y la normativa china sobre protección de la información personal de menores en línea no resultan de aplicación, y no necesitamos recopilar información de identidad de los progenitores para ello. Los progenitores pueden eliminar cualquier espacio infantil y todos sus datos en cualquier momento; la eliminación surte efecto inmediato.",
                "Cumplimos la Ley de Protección de la Información Personal de China y la normativa sobre protección de la información personal de menores en línea, y seguimos los principios de la COPPA y el RGPD: <b>minimización de datos, control parental, no compartir, no vender, sin publicidad ni elaboración de perfiles</b>.",
                "Los progenitores que deseen consultar, corregir o eliminar definitivamente la información relativa a un menor pueden hacerlo desde la app o escribir a {mail} para solicitar ayuda.",
            ]),
        ]),
        ("5. Almacenamiento, seguridad y eliminación de datos", [
            ("ul", [
                "Todos los datos residen en la cuenta de iCloud de tu Apple ID, protegidos por el cifrado y los controles de acceso de Apple. No conservamos ninguna copia en servidores.",
                "<b>Eliminar la app no borra automáticamente los datos de iCloud</b> (para que puedas restaurarlos en un dispositivo nuevo). Para borrar todo: en iPhone/iPad ve a <i>Ajustes → tu Apple ID → iCloud → Gestionar el almacenamiento de la cuenta → KidsLearn → Eliminar datos</i>; elimina el espacio infantil correspondiente dentro de la app en <i>Yo → Espacios infantiles</i>; o escribe a {mail} para solicitar ayuda con la eliminación.",
                "Un pequeño número de preferencias de interfaz (idioma, ajustes de visualización) se guarda <b>localmente en el dispositivo</b> (UserDefaults del sistema). Nunca salen de tu dispositivo y no se sincronizan con iCloud.",
                "Mantén seguros tu Apple ID y el código del dispositivo: son la protección principal de estos datos.",
            ]),
        ]),
        ("6. Compras y pagos", [
            ("p", "KidsLearn se descarga gratis e incluye una prueba local de 7 días. La versión completa es una <b>compra única (no consumible, sin suscripción ni renovación automática)</b>. Todos los pagos los procesa la App Store de Apple (StoreKit). <b>Nunca recibimos ni almacenamos los datos de tu tarjeta</b>, ni podemos ver la información completa de tu cuenta. «Compartir en familia» está activado, por lo que los familiares no necesitan volver a comprar."),
        ]),
        ("7. Cambios en esta política", [
            ("p", "Si esta política cambia, actualizaremos esta página y modificaremos la «Fecha de entrada en vigor» que aparece arriba. Los cambios sustanciales (por ejemplo, la introducción de cualquier nueva recopilación de datos) también se anunciarán de forma destacada dentro de la app. Te recomendamos revisar esta página periódicamente para conocer la versión más reciente."),
        ]),
        ("8. Contacto", [
            ("p", "Para cualquier pregunta, reclamación o solicitud de eliminación relativa a esta política o a tus datos, escribe a <b>{mail}</b>. Normalmente respondemos en un plazo de <b>3 días laborables</b>."),
        ]),
    ],
    "support_title": "Soporte y preguntas frecuentes",
    "support_rows": [
        ("Dispositivo nuevo / sincronización en varios dispositivos", "Inicia sesión con el <b>mismo Apple ID</b> en cada dispositivo con iCloud Drive activado; los datos se sincronizan automáticamente. Si la sincronización se detiene, revisa <i>Ajustes → Apple ID → iCloud</i>."),
        ("Compartir en familia / espacio infantil", "Usa «Compartir espacio infantil» en la app (CKShare de Apple CloudKit); el destinatario acepta con su propio Apple ID. Se necesitan dos Apple ID distintos para probarlo."),
        ("Restaurar compras", "Toca «Restaurar compras» en la parte inferior de la pantalla de compra: no se realiza ningún cargo adicional."),
        ("Eliminar todos los datos", "Consulta la sección 5. Eliminar la app no borra los datos de iCloud."),
        ("Escanear texto (OCR)", "Se ejecuta íntegramente en el dispositivo con Apple Vision; sin subidas ni conexión de red."),
        ("Idiomas admitidos", "10 idiomas: chino simplificado y tradicional, inglés, japonés, español, portugués (Brasil), francés, alemán, coreano y ruso."),
        ("Requisitos del sistema", "iOS / iPadOS 17.0 o posterior (iPhone y iPad, incluidos los widgets de la pantalla de inicio)."),
        ("Contacto", "Escribe a <b>{mail}</b>: respondemos en un plazo de 3 días laborables."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["pt-BR"] = {
    "html_lang": "pt-BR",
    "title": "Política de Privacidade e Suporte do KidsLearn",
    "desc": "Política de privacidade e suporte do KidsLearn: não coletamos nenhuma informação pessoal; todos os dados ficam no seu próprio iCloud.",
    "h1": "🎓 Política de Privacidade e Suporte do KidsLearn",
    "meta_line": "Data de vigência: {d} ｜ Desenvolvedor: {dev} ｜ Contato: {mail}",
    "nav": ["Política de Privacidade", "Suporte e Perguntas Frequentes"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Em resumo:</b> o KidsLearn <b>não coleta nenhuma informação pessoal</b>. Não há sistema de contas, nem servidor, nem SDK de análise ou publicidade de terceiros. Os horários, tarefas, hábitos, lembretes e pontos que você cadastra ficam <b>armazenados apenas no seu próprio banco de dados privado do iCloud</b> (Apple CloudKit); o desenvolvedor não pode lê-los nem exportá-los. Há um <b>Bloqueio Infantil do Dispositivo (PIN)</b> como controle parental, e todo o conteúdo relacionado a crianças é criado e gerenciado por um dos pais ou responsável.",
    "privacy_title": "Política de Privacidade",
    "sections": [
        ("1. Visão geral", [
            ("p", "O KidsLearn é uma ferramenta de gestão de estudos para <b>pais e responsáveis</b>, com horários, registro de tarefas, acompanhamento de hábitos, lembretes de estudo e um sistema de pontos e recompensas. É desenvolvido por um desenvolvedor independente ({dev}) e <b>não possui servidor próprio nem banco de dados de backend</b>. Esta política explica como tratamos — na verdade, como não tratamos — as suas informações."),
        ]),
        ("2. O que coletamos: nada", [
            ("p", "O KidsLearn <b>não coleta nenhuma informação pessoal</b>. Especificamente:"),
            ("ul", [
                "<b>Sem cadastro, sem login.</b> Não solicitamos nem recebemos seu nome, e-mail, telefone, contatos, localização, fotos ou qualquer identificador.",
                "<b>Seus dados ficam no seu próprio iCloud.</b> Os horários, tarefas, hábitos, lembretes, pontos e recompensas que você cria são armazenados no banco de dados privado do iCloud do seu próprio Apple ID (Apple CloudKit, contêiner <code>iCloud.com.frankzhou.KidLearn</code>). Os dados pertencem a você e são mantidos pela Apple; <b>o desenvolvedor não pode acessá-los, lê-los nem exportá-los</b>.",
                "<b>Compartilhamento familiar e «espaços infantis».</b> Baseado no CKShare do Apple CloudKit. Os dados são compartilhados apenas com os Apple IDs que você convidar explicitamente (normalmente familiares); você controla o compartilhamento e pode revogá-lo a qualquer momento.",
            ]),
            ("p", "<b>Recursos do dispositivo e permissões do sistema:</b>"),
            ("ul", [
                "<b>Notificações</b>: usadas apenas para exibir os lembretes de estudo que você mesmo define; sem publicidade ou conteúdo de marketing. As «notificações remotas» são usadas somente como <b>gatilho silencioso para a sincronização com o iCloud</b> e nunca exibem um alerta visível.",
                "<b>Fotos (seletor de fotos do sistema)</b>: a função «ler texto (OCR)» das tarefas escolhe uma imagem pelo seletor de fotos do sistema da Apple (PhotosPicker). O app recebe <b>apenas a imagem que você seleciona</b>, não pode navegar nem acessar o restante da sua biblioteca e <b>não exige permissão da biblioteca de fotos</b>. O reconhecimento é feito <b>inteiramente no dispositivo</b> com o framework Vision da Apple; nem a imagem nem o resultado são <b>enviados</b> a qualquer servidor, e a imagem original não é mantida. <b>O app não usa a câmera e não solicita permissão de câmera.</b> Definir a foto de avatar da criança segue o mesmo mecanismo: apenas a imagem selecionada é lida, comprimida e armazenada <b>unicamente na sua própria conta do iCloud</b>; nada é enviado a servidores.",
                "<b>Face ID / Touch ID / código do dispositivo</b>: usado apenas para autenticar neste dispositivo quando um responsável altera ou redefine o PIN do Bloqueio Infantil, ou desativa o modo infantil. A autenticação é feita pelo iOS; <b>o app nunca recebe, lê nem armazena qualquer dado biométrico</b>.",
                "<b>Área de transferência</b>: lida uma única vez, apenas quando você toca ativamente em «Colar», para montar uma lista de tarefas. O texto é processado <b>no dispositivo</b>; <b>nunca é enviado nem retido</b>. O app não acessa a área de transferência em nenhum outro momento.",
                "<b>Permissões que nunca solicitamos</b>: localização, contatos, calendários, lembretes, microfone, câmera e autorização de rastreamento de apps. Além dos itens acima, o app não declara nenhuma outra permissão.",
            ]),
        ]),
        ("3. Terceiros, rastreamento e publicidade: nenhum", [
            ("ul", [
                "<b>Nenhum código de terceiros</b>: o projeto não depende de nenhum pacote Swift, CocoaPods ou biblioteca de terceiros. Não há SDK de publicidade, nem SDK de análise (nem Firebase ou similar), nem coleta de relatórios de falhas, atribuição ou marketing por push.",
                "<b>Sem rastreamento</b>: não usamos IDFA, não solicitamos a autorização de App Tracking Transparency, não fazemos rastreamento entre apps ou entre sites, nem usamos cookies de rastreamento, impressão digital do dispositivo ou identificadores locais.",
                "<b>Nunca vendemos, compartilhamos ou negociamos dados de usuários</b>, e não participamos de nenhuma forma de monetização de dados. Nenhum dado é usado para publicidade ou criação de perfis.",
                "<b>Exceto o carregamento desta página, todas as requisições de rede vão apenas para serviços da Apple</b>: sincronização com o iCloud (CloudKit) e compras integradas da App Store (StoreKit). Ambas são regidas pela política de privacidade da Apple: veja a <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Política de Privacidade da Apple</a>. (As entradas «Política de Privacidade» e «Suporte» abrem em um leitor integrado, sem barra de endereço, e não saem do app: apenas esta página é carregada, o JavaScript está desativado, nenhum cookie ou dado de navegação é gravado e a navegação para qualquer outro domínio é bloqueada. Esta página está hospedada em um serviço de hospedagem estática de terceiros (GitHub Pages); carregá-la é a única requisição de rede do app a um serviço fora da Apple e não contém nenhum identificador de conta ou de dispositivo.)",
            ]),
        ]),
        ("4. Privacidade de crianças e adolescentes", [
            ("p", "O KidsLearn é uma <b>ferramenta de gestão para pais e responsáveis</b>, não um app voltado a crianças: todo o conteúdo é criado e gerenciado pelos pais ou responsável. O app <b>não</b> oferece chat, comentários, perfis públicos, descoberta ou recomendação de conteúdo, interação com desconhecidos, nem publicação pública de conteúdo gerado por usuários."),
            ("ul", [
                "<b>Não coletamos, vendemos nem divulgamos a terceiros informações pessoais de crianças.</b> Os registros de estudo das crianças (apelido, avatar, matérias, tarefas, hábitos, pontos etc.) são inseridos pelos responsáveis e <b>armazenados apenas na conta de iCloud do responsável</b>; o desenvolvedor não tem acesso a eles.",
                "<b>Sem conteúdo público gerado por usuários.</b> O texto inserido pelos responsáveis é visível apenas para os familiares que o responsável <b>convidar individualmente</b> pelo compartilhamento privado do iCloud (CKShare). Não há público aberto, nem visibilidade para desconhecidos, nem mecanismos de busca ou recomendação, de modo que o app não apresenta os riscos sociais associados ao conteúdo público gerado por usuários.",
                "<b>Controles parentais.</b> O app oferece o «Bloqueio Infantil do Dispositivo (PIN)»: quando ativado, as funções de configuração ficam ocultas e sair exige o PIN; alterar ou redefinir o PIN exige autenticação biométrica do sistema ou o código do dispositivo. Os responsáveis podem usá-lo para restringir o acesso de crianças a ajustes e compras.",
                "<b>Apple IDs de crianças.</b> Se um responsável compartilhar um espaço infantil com o Apple ID de uma criança, essa conta é criada e gerenciada pelo responsável segundo as regras da Apple; o compartilhamento permanece sob seu controle e pode ser encerrado a qualquer momento.",
                "<b>Sobre o consentimento dos pais.</b> Como o app <b>não coleta nenhuma informação pessoal de crianças</b>, os mecanismos de «consentimento parental verificável» exigidos pela COPPA (EUA), pelo GDPR (disposições sobre crianças, UE) e pela regulamentação chinesa de proteção de informações pessoais de crianças on-line não se aplicam, e não precisamos coletar informações de identidade dos pais para isso. Os responsáveis podem excluir qualquer espaço infantil e todos os seus dados a qualquer momento; a exclusão tem efeito imediato.",
                "Seguimos a Lei de Proteção de Informações Pessoais da China e a regulamentação de proteção de informações pessoais de crianças on-line, alinhados aos princípios da COPPA e do GDPR: <b>minimização de dados, controle parental, não compartilhar, não vender, sem publicidade ou criação de perfis</b>.",
                "Os responsáveis que desejarem consultar, corrigir ou excluir definitivamente informações relacionadas a uma criança podem fazê-lo no app ou escrever para {mail} para obter ajuda.",
            ]),
        ]),
        ("5. Armazenamento, segurança e exclusão de dados", [
            ("ul", [
                "Todos os dados ficam na conta de iCloud do seu Apple ID, protegidos pela criptografia e pelos controles de acesso da Apple. Não mantemos nenhuma cópia em servidores.",
                "<b>Excluir o app não remove automaticamente os dados do iCloud</b> (para permitir a restauração em um dispositivo novo). Para apagar tudo: no iPhone/iPad vá a <i>Ajustes → seu Apple ID → iCloud → Gerenciar Armazenamento da Conta → KidsLearn → Excluir Dados</i>; exclua o espaço infantil correspondente no app em <i>Eu → Espaços Infantis</i>; ou escreva para {mail} para solicitar ajuda com a exclusão.",
                "Algumas preferências de interface (idioma, configurações de exibição) são armazenadas <b>localmente no dispositivo</b> (UserDefaults do sistema). Nunca saem do seu dispositivo e não são sincronizadas com o iCloud.",
                "Mantenha seu Apple ID e o código do dispositivo em segurança: eles são a principal proteção desses dados.",
            ]),
        ]),
        ("6. Compras e pagamentos", [
            ("p", "O KidsLearn é gratuito para baixar e inclui um teste local de 7 dias. A versão completa é uma <b>compra única (não consumível, sem assinatura e sem renovação automática)</b>. Todos os pagamentos são processados pela App Store da Apple (StoreKit). <b>Nunca recebemos nem armazenamos os dados do seu cartão</b>, e não conseguimos ver as informações completas da sua conta. O Compartilhamento Familiar está ativado, de modo que os familiares não precisam comprar novamente."),
        ]),
        ("7. Alterações nesta política", [
            ("p", "Se esta política mudar, atualizaremos esta página e revisaremos a «Data de vigência» exibida no topo. Alterações relevantes (por exemplo, a introdução de qualquer nova coleta de dados) também serão anunciadas de forma destacada dentro do app. Recomendamos revisar esta página periodicamente para conhecer a versão mais recente."),
        ]),
        ("8. Contato", [
            ("p", "Para qualquer dúvida, reclamação ou pedido de exclusão relativo a esta política ou aos seus dados, escreva para <b>{mail}</b>. Normalmente respondemos em até <b>3 dias úteis</b>."),
        ]),
    ],
    "support_title": "Suporte e Perguntas Frequentes",
    "support_rows": [
        ("Dispositivo novo / sincronização em vários dispositivos", "Entre com o <b>mesmo Apple ID</b> em cada dispositivo com o iCloud Drive ativado; os dados sincronizam automaticamente. Se a sincronização travar, verifique <i>Ajustes → Apple ID → iCloud</i>."),
        ("Compartilhamento familiar / espaço infantil", "Use «Compartilhar espaço infantil» no app (CKShare do Apple CloudKit); o destinatário aceita com o próprio Apple ID. São necessários dois Apple IDs diferentes para testar."),
        ("Restaurar compras", "Toque em «Restaurar Compras» na parte inferior da tela de compra: não há cobrança adicional."),
        ("Excluir todos os dados", "Veja a seção 5 acima. Excluir o app não remove os dados do iCloud."),
        ("Ler texto (OCR)", "Executado inteiramente no dispositivo com o Apple Vision; sem envio e sem necessidade de rede."),
        ("Idiomas suportados", "10 idiomas: chinês simplificado e tradicional, inglês, japonês, espanhol, português (Brasil), francês, alemão, coreano e russo."),
        ("Requisitos do sistema", "iOS / iPadOS 17.0 ou posterior (iPhone e iPad, incluindo widgets na tela de início)."),
        ("Contato", "E-mail: <b>{mail}</b> (resposta em até 3 dias úteis)."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["fr"] = {
    "html_lang": "fr",
    "title": "Politique de confidentialité et assistance KidsLearn",
    "desc": "Politique de confidentialité et assistance de KidsLearn : nous ne collectons aucune information personnelle ; toutes les données restent dans votre propre iCloud.",
    "h1": "🎓 Politique de confidentialité et assistance KidsLearn",
    "meta_line": "Date d'entrée en vigueur : {d} ｜ Développeur : {dev} ｜ Contact : {mail}",
    "nav": ["Politique de confidentialité", "Assistance et FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>En résumé :</b> KidsLearn <b>ne collecte aucune information personnelle</b>. Pas de système de compte, pas de serveur, aucun SDK tiers d'analyse ou de publicité. Les emplois du temps, devoirs, habitudes, rappels et points que vous saisissez sont <b>stockés uniquement dans votre propre base de données privée iCloud</b> (Apple CloudKit) ; le développeur ne peut ni les lire ni les exporter. Un <b>verrouillage enfant de l'appareil (code PIN)</b> est fourni comme contrôle parental, et tout le contenu relatif aux enfants est créé et géré par un parent.",
    "privacy_title": "Politique de confidentialité",
    "sections": [
        ("1. Présentation", [
            ("p", "KidsLearn est un outil de gestion des études destiné aux <b>parents</b>, offrant emplois du temps, suivi des devoirs, validation d'habitudes, rappels d'étude et un système de points et de récompenses. Il est développé par un développeur indépendant ({dev}) et ne dispose <b>d'aucun serveur propre ni de base de données d'arrière-plan</b>. La présente politique explique comment nous traitons — en réalité, comment nous ne traitons pas — vos informations."),
        ]),
        ("2. Ce que nous collectons : rien", [
            ("p", "KidsLearn <b>ne collecte aucune information personnelle</b>. Plus précisément :"),
            ("ul", [
                "<b>Aucune inscription, aucune connexion.</b> Nous ne demandons ni ne recevons votre nom, e-mail, numéro de téléphone, contacts, position, photos ou tout autre identifiant.",
                "<b>Vos données restent dans votre propre iCloud.</b> Les emplois du temps, devoirs, habitudes, rappels, points et récompenses que vous créez sont stockés dans la base de données privée iCloud de votre propre identifiant Apple (Apple CloudKit, conteneur <code>iCloud.com.frankzhou.KidLearn</code>). Les données vous appartiennent et sont conservées par Apple ; <b>le développeur ne peut y accéder, les lire ni les exporter</b>.",
                "<b>Partage familial et « espaces enfants ».</b> Reposant sur CKShare d'Apple CloudKit. Les données ne sont partagées qu'avec les identifiants Apple que vous invitez explicitement (généralement des membres de la famille) ; vous contrôlez le partage et pouvez le révoquer à tout moment.",
            ]),
            ("p", "<b>Fonctions de l'appareil et autorisations système :</b>"),
            ("ul", [
                "<b>Notifications</b> : utilisées uniquement pour afficher les rappels d'étude que vous définissez vous-même ; aucune publicité ni contenu marketing. Les « notifications distantes » servent uniquement de <b>déclencheur silencieux pour la synchronisation iCloud</b> et n'affichent jamais d'alerte visible.",
                "<b>Photos (sélecteur de photos système)</b> : la fonction « numériser du texte (OCR) » des devoirs sélectionne une image via le sélecteur de photos système d'Apple (PhotosPicker). L'app reçoit <b>uniquement l'image que vous sélectionnez</b>, ne peut ni parcourir ni accéder au reste de votre bibliothèque et <b>ne requiert aucune autorisation d'accès à la photothèque</b>. La reconnaissance est effectuée <b>entièrement sur l'appareil</b> via le framework Vision d'Apple ; ni l'image ni le résultat ne sont <b>jamais téléversés</b>, et l'image d'origine n'est pas conservée. <b>L'app n'utilise pas l'appareil photo et ne demande pas d'autorisation d'appareil photo.</b> Définir la photo d'avatar d'un enfant suit le même mécanisme : seule l'image sélectionnée est lue, compressée et stockée <b>uniquement dans votre propre compte iCloud</b> ; rien n'est envoyé à un serveur.",
                "<b>Face ID / Touch ID / code de l'appareil</b> : utilisé uniquement pour authentifier sur cet appareil lorsqu'un parent modifie ou réinitialise le code PIN du verrouillage enfant, ou désactive le mode enfant. L'authentification est effectuée par iOS ; <b>l'app ne reçoit, ne lit ni ne stocke jamais de donnée biométrique</b>.",
                "<b>Presse-papiers</b> : lu une seule fois, uniquement lorsque vous touchez activement « Coller », pour constituer une liste de devoirs. Le texte est traité <b>sur l'appareil</b> ; il n'est <b>jamais téléversé ni conservé</b>. L'app n'accède au presse-papiers à aucun autre moment.",
                "<b>Autorisations que nous ne demandons jamais</b> : localisation, contacts, calendriers, rappels, microphone, appareil photo ou autorisation de suivi d'apps. En dehors des éléments ci-dessus, l'app ne déclare aucune autre autorisation.",
            ]),
        ]),
        ("3. Tiers, suivi et publicité : aucun", [
            ("ul", [
                "<b>Aucun code tiers</b> : le projet ne dépend d'aucun paquet Swift, d'aucun CocoaPods ni d'aucune bibliothèque tierce. Il n'y a aucun SDK publicitaire, aucun SDK d'analyse (ni Firebase ni équivalent), aucun composant de rapport d'incident, d'attribution ou de marketing push.",
                "<b>Aucun suivi</b> : pas d'IDFA, pas de demande d'autorisation App Tracking Transparency, pas de suivi inter-applications ou inter-sites, pas de cookie de suivi, d'empreinte d'appareil ou d'identifiant local.",
                "<b>Nous ne vendons, ne partageons ni n'échangeons jamais les données des utilisateurs</b>, et nous ne participons à aucune forme de monétisation des données. Aucune donnée n'est utilisée à des fins publicitaires ou de profilage.",
                "<b>Hormis le chargement de cette page, toutes les requêtes réseau sont destinées uniquement aux services Apple</b> : synchronisation iCloud (CloudKit) et achats intégrés App Store (StoreKit). Les deux sont régis par la politique de confidentialité d'Apple : voir la <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">politique de confidentialité d'Apple</a>. (Les entrées « Politique de confidentialité » et « Assistance » s'ouvrent dans un lecteur intégré sans barre d'adresse et ne quittent pas l'app : seule cette page est chargée, le JavaScript est désactivé, aucun cookie ni donnée de navigation n'est écrit et la navigation vers tout autre domaine est bloquée. Cette page est hébergée sur un service d'hébergement statique tiers (GitHub Pages) ; son chargement est la seule requête réseau de l'app vers un service non-Apple et ne contient aucun identifiant de compte ou d'appareil.)",
            ]),
        ]),
        ("4. Confidentialité des mineurs", [
            ("p", "KidsLearn est un <b>outil de gestion destiné aux parents</b>, et non une application conçue pour les enfants : tout le contenu est créé et géré par les parents. L'app ne propose <b>ni</b> messagerie, ni commentaires, ni profils publics, ni découverte ou recommandation de contenu, ni interaction avec des inconnus, ni partage public de contenu généré par les utilisateurs."),
            ("ul", [
                "<b>Nous ne collectons, ne vendons ni ne divulguons à des tiers les informations personnelles des mineurs.</b> Les relevés d'études des mineurs (surnom, avatar, matières, devoirs, habitudes, points, etc.) sont saisis par les parents et <b>stockés uniquement dans le compte iCloud du parent</b> ; le développeur n'y a pas accès.",
                "<b>Aucun contenu public généré par les utilisateurs.</b> Le texte saisi par les parents n'est visible que pour les membres de la famille que le parent <b>invite individuellement</b> via le partage privé iCloud (CKShare). Il n'y a ni audience publique, ni visibilité pour des inconnus, ni mécanisme de recherche ou de recommandation : l'app ne présente donc aucun des risques sociaux liés au contenu public généré par les utilisateurs.",
                "<b>Contrôles parentaux.</b> L'app propose un « verrouillage enfant de l'appareil (PIN) » : une fois activé, les fonctions de configuration sont masquées et la sortie exige le code PIN ; la modification ou la réinitialisation du PIN requiert l'authentification biométrique du système ou le code de l'appareil. Les parents peuvent l'utiliser pour restreindre l'accès des enfants aux réglages et aux achats.",
                "<b>Identifiants Apple d'enfants.</b> Si un parent partage un espace enfant avec l'identifiant Apple d'un enfant, ce compte est créé et géré par le parent selon les règles d'Apple ; le partage reste sous son contrôle et peut être interrompu à tout moment.",
                "<b>À propos du consentement parental.</b> Étant donné que l'app <b>ne collecte aucune information personnelle d'enfants</b>, les mécanismes de « consentement parental vérifiable » exigés par la COPPA (États-Unis), le RGPD (dispositions relatives aux enfants, UE) et la réglementation chinoise sur la protection des informations personnelles des enfants en ligne ne s'appliquent pas, et nous n'avons pas besoin de collecter d'informations d'identité parentale à cette fin. Les parents peuvent supprimer à tout moment un espace enfant et toutes ses données ; la suppression prend effet immédiatement.",
                "Nous respectons la loi chinoise sur la protection des informations personnelles et la réglementation sur la protection des informations personnelles des enfants en ligne, et suivons les principes de la COPPA et du RGPD : <b>minimisation des données, contrôle parental, pas de partage, pas de vente, ni publicité ni profilage</b>.",
                "Les parents souhaitant consulter, corriger ou supprimer définitivement des informations relatives à un enfant peuvent le faire depuis l'app ou écrire à {mail} pour obtenir de l'aide.",
            ]),
        ]),
        ("5. Stockage, sécurité et suppression des données", [
            ("ul", [
                "Toutes les données résident dans le compte iCloud de votre identifiant Apple, protégées par le chiffrement et les contrôles d'accès d'Apple. Nous ne conservons aucune copie côté serveur.",
                "<b>La suppression de l'app n'efface pas automatiquement les données iCloud</b> (afin de permettre la restauration sur un nouvel appareil). Pour tout effacer : sur iPhone/iPad, allez dans <i>Réglages → votre identifiant Apple → iCloud → Gérer le stockage du compte → KidsLearn → Supprimer les données</i> ; supprimez l'espace enfant correspondant dans l'app sous <i>Moi → Espaces enfants</i> ; ou écrivez à {mail} pour demander une assistance à la suppression.",
                "Un petit nombre de préférences d'interface (langue, paramètres d'affichage) sont stockées <b>localement sur l'appareil</b> (UserDefaults système). Elles ne quittent jamais votre appareil et ne sont pas synchronisées avec iCloud.",
                "Conservez votre identifiant Apple et le code de votre appareil en sécurité : ils constituent la protection principale de ces données.",
            ]),
        ]),
        ("6. Achats et paiements", [
            ("p", "KidsLearn est téléchargeable gratuitement avec un essai local de 7 jours. La version complète est un <b>achat unique (non consommable, sans abonnement ni renouvellement automatique)</b>. Tous les paiements sont traités par l'App Store d'Apple (StoreKit). <b>Nous ne recevons ni ne stockons jamais les informations de votre carte de paiement</b>, et nous ne pouvons pas voir les informations complètes de votre compte. Le partage familial est activé : les membres de la famille n'ont donc pas besoin de racheter."),
        ]),
        ("7. Modifications de cette politique", [
            ("p", "Si cette politique change, nous mettrons cette page à jour et modifierons la « date d'entrée en vigueur » affichée en haut. Les modifications importantes (par exemple, l'introduction d'une nouvelle collecte de données) seront également annoncées de manière visible dans l'app. Nous vous invitons à consulter régulièrement cette page pour connaître la dernière version."),
        ]),
        ("8. Nous contacter", [
            ("p", "Pour toute question, réclamation ou demande de suppression concernant cette politique ou vos données, écrivez à <b>{mail}</b>. Nous répondons généralement sous <b>3 jours ouvrés</b>."),
        ]),
    ],
    "support_title": "Assistance et FAQ",
    "support_rows": [
        ("Nouvel appareil / synchronisation multi-appareils", "Connectez-vous avec le <b>même identifiant Apple</b> sur chaque appareil avec iCloud Drive activé ; les données se synchronisent automatiquement. Si la synchronisation s'arrête, vérifiez <i>Réglages → identifiant Apple → iCloud</i>."),
        ("Partage familial / espace enfant", "Utilisez « Partager l'espace enfant » dans l'app (CKShare d'Apple CloudKit) ; le destinataire accepte avec son propre identifiant Apple. Deux identifiants Apple différents sont nécessaires pour tester."),
        ("Restaurer les achats", "Touchez « Restaurer les achats » en bas de l'écran d'achat : aucun débit supplémentaire."),
        ("Supprimer toutes les données", "Voir la section 5 ci-dessus. Supprimer l'app n'efface pas les données iCloud."),
        ("Numériser du texte (OCR)", "Exécuté entièrement sur l'appareil via Apple Vision ; aucun téléversement ni connexion réseau."),
        ("Langues prises en charge", "10 langues : chinois simplifié et traditionnel, anglais, japonais, espagnol, portugais (Brésil), français, allemand, coréen et russe."),
        ("Configuration requise", "iOS / iPadOS 17.0 ou version ultérieure (iPhone et iPad, y compris les widgets de l'écran d'accueil)."),
        ("Contact", "E-mail : <b>{mail}</b> (réponse sous 3 jours ouvrés)."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["de"] = {
    "html_lang": "de",
    "title": "KidsLearn Datenschutzerklärung und Support",
    "desc": "Datenschutzerklärung und Support von KidsLearn: Wir erfassen keine personenbezogenen Daten; alle Daten bleiben in Ihrem eigenen iCloud-Speicher.",
    "h1": "🎓 KidsLearn Datenschutzerklärung und Support",
    "meta_line": "Inkrafttreten: {d} ｜ Entwickler: {dev} ｜ Kontakt: {mail}",
    "nav": ["Datenschutzerklärung", "Support und Häufige Fragen"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kurz gesagt:</b> KidsLearn <b>erfasst keine personenbezogenen Daten</b>. Es gibt kein Kontosystem, keinen Server und keine Analyse- oder Werbe-SDKs von Drittanbietern. Stundenpläne, Hausaufgaben, Gewohnheiten, Erinnerungen und Punkte, die Sie eingeben, werden <b>ausschließlich in Ihrer eigenen privaten iCloud-Datenbank</b> (Apple CloudKit) gespeichert; der Entwickler kann sie weder lesen noch exportieren. Eine <b>Kindersperre (PIN)</b> dient als Kindersicherung, und alle kinderbezogenen Inhalte werden von einem Elternteil erstellt und verwaltet.",
    "privacy_title": "Datenschutzerklärung",
    "sections": [
        ("1. Überblick", [
            ("p", "KidsLearn ist ein Lernverwaltungs-Werkzeug für <b>Eltern</b> mit Stundenplänen, Hausaufgabenverfolgung, Gewohnheits-Check-ins, Lernerinnerungen sowie einem Punkt- und Belohnungssystem. Es wird von einem unabhängigen Entwickler ({dev}) entwickelt und hat <b>keinen eigenen Server und keine Backend-Datenbank</b>. Diese Erklärung beschreibt, wie wir mit Ihren Informationen umgehen – genau genommen: nicht umgehen."),
        ]),
        ("2. Was wir erfassen: nichts", [
            ("p", "KidsLearn <b>erfasst keine personenbezogenen Daten</b>. Im Einzelnen:"),
            ("ul", [
                "<b>Keine Registrierung, keine Anmeldung.</b> Wir fragen Ihren Namen, Ihre E-Mail-Adresse, Telefonnummer, Kontakte, Ihren Standort, Fotos oder Kennungen weder ab noch erhalten wir sie.",
                "<b>Ihre Daten bleiben in Ihrem eigenen iCloud-Speicher.</b> Stundenpläne, Hausaufgaben, Gewohnheiten, Erinnerungen, Punkte und Belohnungen, die Sie anlegen, werden in der privaten iCloud-Datenbank Ihrer eigenen Apple-ID gespeichert (Apple CloudKit, Container <code>iCloud.com.frankzhou.KidLearn</code>). Die Daten gehören Ihnen und werden von Apple verwahrt; <b>der Entwickler kann nicht darauf zugreifen, sie lesen oder exportieren</b>.",
                "<b>Familienfreigabe und „Kinderbereiche“.</b> Basiert auf CKShare von Apple CloudKit. Daten werden nur mit Apple-IDs geteilt, die Sie ausdrücklich einladen (in der Regel Familienmitglieder); Sie behalten die Kontrolle und können die Freigabe jederzeit widerrufen.",
            ]),
            ("p", "<b>Gerätefunktionen und Systemberechtigungen:</b>"),
            ("ul", [
                "<b>Benachrichtigungen</b> – dienen ausschließlich der Anzeige der Lernerinnerungen, die Sie selbst festlegen; keine Werbung oder Marketinginhalte. „Remote-Benachrichtigungen“ werden nur als <b>stiller Auslöser für die iCloud-Synchronisierung</b> verwendet und zeigen niemals eine sichtbare Meldung an.",
                "<b>Fotos (System-Fotoauswahl)</b> – die Funktion „Text scannen (OCR)“ für Hausaufgaben wählt ein Bild über die System-Fotoauswahl von Apple (PhotosPicker). Die App erhält <b>nur das von Ihnen ausgewählte Bild</b>, kann die übrige Mediathek weder durchsuchen noch darauf zugreifen und <b>benötigt keine Fotobibliothek-Berechtigung</b>. Die Texterkennung erfolgt <b>vollständig auf dem Gerät</b> über das Vision-Framework von Apple; weder Bild noch Ergebnis werden <b>jemals hochgeladen</b>, und das Originalbild wird nicht aufbewahrt. <b>Die App verwendet die Kamera nicht und fordert keine Kameraberechtigung an.</b> Auch das Festlegen eines Kinder-Avatarfotos nutzt denselben Mechanismus: Nur das ausgewählte Bild wird gelesen, komprimiert und <b>ausschließlich in Ihrem eigenen iCloud-Konto gespeichert</b> – nie auf einen Server hochgeladen.",
                "<b>Face ID / Touch ID / Gerätecode</b> – wird nur zur Authentifizierung auf diesem Gerät verwendet, wenn ein Elternteil die PIN der Kindersperre ändert oder zurücksetzt oder den Kindermodus ausschaltet. Die Authentifizierung erfolgt durch iOS; <b>die App erhält, liest oder speichert niemals biometrische Daten</b>.",
                "<b>Zwischenablage</b> – wird einmalig gelesen, und zwar nur wenn Sie aktiv auf „Einsetzen“ tippen, um eine Hausaufgabenliste zu erstellen. Der Text wird <b>auf dem Gerät</b> verarbeitet und <b>weder hochgeladen noch gespeichert</b>. Zu keinem anderen Zeitpunkt greift die App auf die Zwischenablage zu.",
                "<b>Berechtigungen, die wir nie anfordern</b> – Standort, Kontakte, Kalender, Erinnerungen, Mikrofon, Kamera oder App-Tracking-Berechtigung. Außer den oben genannten Punkten deklariert die App keine weiteren Berechtigungen.",
            ]),
        ]),
        ("3. Drittanbieter, Tracking und Werbung: keine", [
            ("ul", [
                "<b>Kein einziger Drittanbieter-Code</b> – das Projekt nutzt kein Swift-Paket, kein CocoaPods und keine Drittanbieter-Bibliothek. Es gibt kein Werbe-SDK, kein Analyse-SDK (kein Firebase o. Ä.), keine Absturzberichte, Attribution oder Push-Marketing-Komponenten.",
                "<b>Kein Tracking</b> – keine IDFA, keine Abfrage der App-Tracking-Berechtigung, kein app- oder websiteübergreifendes Tracking, keine Tracking-Cookies, Geräte-Fingerprints oder lokalen Kennungen.",
                "<b>Wir verkaufen, teilen oder handeln niemals Nutzerdaten</b> und betreiben keinerlei Datenmonetarisierung. Keine Daten werden für Werbung oder Nutzerprofile verwendet.",
                "<b>Mit Ausnahme des Ladens dieser Seite gehen alle Netzwerkzugriffe ausschließlich an Apple-Dienste</b> – iCloud-Synchronisierung (CloudKit) und In-App-Käufe (StoreKit). Beide unterliegen der Datenschutzerklärung von Apple: siehe <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple Datenschutzerklärung</a>. (Die Einträge „Datenschutzerklärung“ und „Support“ öffnen sich in einem integrierten Reader ohne Adressleiste und verlassen die App nicht: Es wird nur diese Seite geladen, JavaScript ist deaktiviert, es werden weder Cookies noch Browserdaten geschrieben und die Navigation zu anderen Domains wird blockiert. Diese Seite wird bei einem statischen Hosting-Dienst eines Drittanbieters (GitHub Pages) gehostet; ihr Laden ist die einzige Netzwerkanfrage der App an einen Nicht-Apple-Dienst und enthält keine Konto- oder Gerätekennung.)",
            ]),
        ]),
        ("4. Schutz von Kindern und Jugendlichen", [
            ("p", "KidsLearn ist ein <b>Verwaltungswerkzeug für Eltern</b> und keine App für Kinder: Sämtliche Inhalte werden von Eltern erstellt und verwaltet. Die App bietet <b>keine</b> Chat-, Kommentar-, öffentlichen Profil-, Entdeckungs- oder Empfehlungsfunktionen, keinen Kontakt mit Fremden und keine öffentliche Veröffentlichung nutzergenerierter Inhalte."),
            ("ul", [
                "<b>Wir erfassen, verkaufen oder offenbaren keine personenbezogenen Daten von Kindern an Dritte.</b> Lerndaten von Kindern (Spitzname, Avatar, Fächer, Hausaufgaben, Gewohnheiten, Punkte usw.) werden von Eltern eingegeben und <b>ausschließlich im iCloud-Konto des Elternteils</b> gespeichert; der Entwickler hat keinen Zugriff darauf.",
                "<b>Keine öffentlichen nutzergenerierten Inhalte.</b> Von Eltern eingegebene Texte sind nur für Familienmitglieder sichtbar, die der Elternteil <b>einzeln</b> über die private iCloud-Freigabe (CKShare) einlädt. Es gibt keine öffentliche Sichtbarkeit, keine Sichtbarkeit für Fremde sowie keine Such- oder Empfehlungsmechanismen – die App birgt daher keines der mit öffentlichen nutzergenerierten Inhalten verbundenen sozialen Risiken.",
                "<b>Kindersicherung.</b> Die App bietet eine „Kindersperre (PIN)“: Ist sie aktiviert, werden Konfigurationsfunktionen ausgeblendet und zum Verlassen ist die PIN erforderlich; zum Ändern oder Zurücksetzen der PIN ist eine biometrische Authentifizierung oder der Gerätecode nötig. Eltern können so den Zugriff von Kindern auf Einstellungen und Käufe beschränken.",
                "<b>Apple-IDs von Kindern.</b> Wenn ein Elternteil einen Kinderbereich mit der Apple-ID eines Kindes teilt, wird dieses Konto vom Elternteil gemäß den Apple-Regeln erstellt und verwaltet; die Freigabe bleibt unter seiner Kontrolle und kann jederzeit beendet werden.",
                "<b>Zur elterlichen Einwilligung.</b> Da die App <b>keinerlei personenbezogene Daten von Kindern erfasst</b>, sind die Mechaniken zur „überprüfbaren elterlichen Einwilligung“ nach COPPA (USA), DSGVO (Kinderbestimmungen, EU) und der chinesischen Verordnung zum Schutz personenbezogener Daten von Kindern im Netz nicht anwendbar, und wir müssen hierfür keine Identitätsdaten der Eltern erheben. Eltern können jeden Kinderbereich samt aller Daten jederzeit löschen; die Löschung wirkt sofort.",
                "Wir beachten das chinesische Gesetz zum Schutz personenbezogener Daten sowie die Verordnung zum Schutz personenbezogener Daten von Kindern im Netz und richten uns nach den Grundsätzen von COPPA und DSGVO: <b>Datenminimierung, elterliche Kontrolle, kein Teilen, kein Verkauf, keine Werbung und kein Profiling</b>.",
                "Eltern, die kinderbezogene Informationen einsehen, berichtigen oder endgültig löschen möchten, können dies in der App tun oder sich per E-Mail an {mail} wenden.",
            ]),
        ]),
        ("5. Datenspeicherung, Sicherheit und Löschung", [
            ("ul", [
                "Alle Daten liegen im iCloud-Konto Ihrer Apple-ID und sind durch Verschlüsselung und Zugriffskontrollen von Apple geschützt. Wir halten keine serverseitige Kopie vor.",
                "<b>Das Löschen der App entfernt die iCloud-Daten nicht automatisch</b> (damit eine Wiederherstellung auf einem neuen Gerät möglich ist). Um alles zu löschen: auf iPhone/iPad zu <i>Einstellungen → Ihre Apple-ID → iCloud → Account-Speicher verwalten → KidsLearn → Daten löschen</i>; oder löschen Sie den betreffenden Kinderbereich in der App unter <i>Ich → Kinderbereiche</i>; oder schreiben Sie an {mail}, um Unterstützung bei der Löschung zu erhalten.",
                "Einige wenige Anzeigeeinstellungen (Sprache, Darstellung) werden <b>lokal auf dem Gerät</b> (System-UserDefaults) gespeichert. Sie verlassen Ihr Gerät niemals und werden nicht mit iCloud synchronisiert.",
                "Bewahren Sie Ihre Apple-ID und den Gerätecode sicher auf – sie sind der wichtigste Schutz dieser Daten.",
            ]),
        ]),
        ("6. Käufe und Zahlungen", [
            ("p", "KidsLearn ist kostenlos erhältlich und bietet eine lokale 7-Tage-Testphase. Die Vollversion ist ein <b>einmaliger Kauf (nicht verbrauchbar, kein Abonnement, keine automatische Verlängerung)</b>. Alle Zahlungen werden über den Apple App Store (StoreKit) abgewickelt. <b>Wir erhalten oder speichern niemals Ihre Kartendaten</b> und können Ihre vollständigen Kontoinformationen nicht einsehen. Die Familienfreigabe ist aktiviert, sodass Familienmitglieder nicht erneut kaufen müssen."),
        ]),
        ("7. Änderungen dieser Erklärung", [
            ("p", "Bei Änderungen aktualisieren wir diese Seite und passen das oben angezeigte Datum des „Inkrafttretens“ an. Wesentliche Änderungen (etwa die Aufnahme einer neuen Datenerhebung) werden zusätzlich deutlich sichtbar in der App angekündigt. Bitte prüfen Sie diese Seite regelmäßig, um die aktuelle Version zu kennen."),
        ]),
        ("8. Kontakt", [
            ("p", "Bei Fragen, Beschwerden oder Löschanfragen zu dieser Erklärung oder Ihren Daten schreiben Sie bitte an <b>{mail}</b>. Wir antworten in der Regel innerhalb von <b>3 Werktagen</b>."),
        ]),
    ],
    "support_title": "Support und Häufige Fragen",
    "support_rows": [
        ("Neues Gerät / Synchronisierung mehrerer Geräte", "Melden Sie sich auf jedem Gerät mit <b>derselben Apple-ID</b> an und aktivieren Sie iCloud Drive; die Daten werden automatisch synchronisiert. Stockt die Synchronisierung, prüfen Sie <i>Einstellungen → Apple-ID → iCloud</i>."),
        ("Familienfreigabe / Kinderbereich teilen", "Nutzen Sie „Kinderbereich teilen“ in der App (Apple CloudKit CKShare); die empfangende Person nimmt mit ihrer eigenen Apple-ID an. Zum Testen sind zwei verschiedene Apple-IDs erforderlich."),
        ("Käufe wiederherstellen", "Tippen Sie unten auf der Kaufseite auf „Käufe wiederherstellen“ – es werden keine zusätzlichen Kosten berechnet."),
        ("Alle Daten löschen", "Siehe Abschnitt 5. Das Löschen der App entfernt die iCloud-Daten nicht."),
        ("Text scannen (OCR)", "Läuft vollständig auf dem Gerät über Apple Vision; kein Upload, keine Netzwerkverbindung erforderlich."),
        ("Unterstützte Sprachen", "10 Sprachen: vereinfachtes und traditionelles Chinesisch, Englisch, Japanisch, Spanisch, Portugiesisch (Brasilien), Französisch, Deutsch, Koreanisch und Russisch."),
        ("Systemvoraussetzungen", "iOS / iPadOS 17.0 oder neuer (iPhone und iPad, einschließlich Home-Bildschirm-Widgets)."),
        ("Kontakt", "E-Mail: <b>{mail}</b> (Antwort in der Regel innerhalb von 3 Werktagen)."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["ko"] = {
    "html_lang": "ko",
    "title": "KidsLearn 개인정보 처리방침 및 지원",
    "desc": "KidsLearn 개인정보 처리방침 및 지원: 어떤 개인정보도 수집하지 않으며, 모든 데이터는 사용자 본인의 iCloud에만 저장됩니다.",
    "h1": "🎓 KidsLearn 개인정보 처리방침 및 지원",
    "meta_line": "시행일: {d} ｜ 개발자: {dev} ｜ 문의: {mail}",
    "nav": ["개인정보 처리방침", "지원 및 자주 묻는 질문"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>요약:</b> KidsLearn은 <b>어떠한 개인정보도 수집하지 않습니다</b>. 계정 시스템, 서버, 제3자 분석·광고 SDK가 없습니다. 입력하신 시간표, 숙제, 습관, 알림, 포인트 데이터는 <b>오직 본인의 개인 iCloud 데이터베이스</b>(Apple CloudKit)에만 저장되며, 개발자는 이를 읽거나 내보낼 수 없습니다. 보호자 관리를 위한 <b>어린이 기기 잠금(PIN)</b>을 제공하며, 아동 관련 모든 콘텐츠는 보호자가 생성하고 관리합니다.",
    "privacy_title": "개인정보 처리방침",
    "sections": [
        ("1. 개요", [
            ("p", "KidsLearn은 시간표, 숙제 기록, 습관 체크, 학습 알림, 포인트·보상 기능을 제공하는 <b>학부모용</b> 학습 관리 도구입니다. 개인 개발자({dev})가 개발했으며, <b>자체 서버와 백엔드 데이터베이스가 없습니다</b>. 본 방침은 저희가 회원님의 정보를 어떻게 처리하는지(정확히는 처리하지 않는지)를 설명합니다."),
        ]),
        ("2. 수집하는 정보: 없음", [
            ("p", "KidsLearn은 <b>어떠한 개인정보도 수집하지 않습니다</b>. 구체적으로:"),
            ("ul", [
                "<b>가입 없음, 로그인 없음.</b> 이름, 이메일, 전화번호, 연락처, 위치, 사진, 식별자 등을 요청하거나 받지 않습니다.",
                "<b>데이터는 본인의 iCloud에만 보관됩니다.</b> 시간표, 숙제, 습관, 알림, 포인트, 보상 등은 본인 Apple ID의 개인 iCloud 데이터베이스(Apple CloudKit, 컨테이너 <code>iCloud.com.frankzhou.KidLearn</code>)에 저장됩니다. 데이터는 회원님의 소유이며 Apple이 보관합니다. <b>개발자는 접근·열람·내보내기를 할 수 없습니다</b>.",
                "<b>가족 공유 및 ‘아이 공간’.</b> Apple CloudKit의 CKShare를 기반으로 하며, 회원님이 명시적으로 초대한 Apple ID(통상 가족)하고만 공유됩니다. 공유 범위는 회원님이 관리하며 언제든 취소할 수 있습니다.",
            ]),
            ("p", "<b>기기 기능 및 시스템 권한:</b>"),
            ("ul", [
                "<b>알림</b>: 회원님이 직접 설정한 학습 알림을 표시하는 데만 사용되며 광고나 마케팅 내용이 포함되지 않습니다. ‘원격 알림’은 iCloud 동기화를 위한 <b>무음 트리거</b>로만 사용되며 눈에 보이는 알림을 표시하지 않습니다.",
                "<b>사진(시스템 사진 선택기)</b>: 숙제의 ‘텍스트 스캔(OCR)’ 기능은 Apple 시스템 사진 선택기(PhotosPicker)로 이미지를 선택합니다. 앱은 <b>선택한 한 장만</b> 받으며 보관함 전체를 훑어보거나 접근할 수 없고, <b>사진 보관함 권한도 필요하지 않습니다</b>. 인식은 Apple Vision 프레임워크로 <b>전적으로 기기 내에서</b> 수행되며 이미지와 결과는 <b>어떤 서버로도 전송되지 않고</b> 원본 이미지도 보관하지 않습니다. <b>본 앱은 카메라를 사용하지 않으며 카메라 권한도 요청하지 않습니다.</b> 아동 아바타 사진 설정도 같은 방식입니다: 선택한 한 장만 읽어 압축한 뒤 <b>보호자 본인의 iCloud 계정에만</b> 저장되며, 어떤 서버로도 전송되지 않습니다.",
                "<b>Face ID / Touch ID / 기기 암호</b>: 보호자가 ‘어린이 모드 PIN’을 변경·재설정하거나 어린이 모드를 해제할 때 기기 본인 확인에만 사용됩니다. 인증은 iOS가 수행하며, <b>앱은 어떤 생체 정보도 수신·읽기·저장하지 않습니다</b>.",
                "<b>클립보드</b>: 회원님이 직접 ‘붙여넣기’를 탭했을 때 한 번만 읽어 숙제 목록을 만드는 데 사용합니다. 텍스트는 <b>기기 내에서</b> 처리되며 <b>전송되거나 보관되지 않습니다</b>. 그 외에는 클립보드에 접근하지 않습니다.",
                "<b>절대 요청하지 않는 권한</b>: 위치, 연락처, 캘린더, 미리 알림, 마이크, 카메라, 앱 추적 권한. 위 항목 외에 앱이 선언한 권한은 없습니다.",
            ]),
        ]),
        ("3. 제3자 서비스, 추적, 광고: 없음", [
            ("ul", [
                "<b>제3자 코드 없음</b>: 프로젝트는 어떤 Swift 패키지, CocoaPods, 제3자 라이브러리에도 의존하지 않습니다. 광고 SDK, 분석 SDK(Firebase 등), 크래시 수집, 어트리뷰션, 푸시 마케팅 구성요소가 없습니다.",
                "<b>추적 없음</b>: IDFA를 사용하지 않고 앱 추적 투명성 권한을 요청하지 않으며, 앱 간·사이트 간 추적, 추적용 쿠키, 기기 지문, 로컬 식별자를 사용하지 않습니다.",
                "<b>사용자 데이터를 판매·공유·거래하지 않습니다.</b> 어떤 형태의 데이터 수익화에도 참여하지 않으며 광고나 사용자 프로파일링에 사용하지 않습니다.",
                "<b>이 정책 페이지를 불러오는 경우를 제외한 모든 네트워크 요청은 Apple 서비스로만 향합니다</b>: iCloud(CloudKit) 동기화와 App Store 인앱 구매(StoreKit)입니다. 두 서비스는 Apple의 개인정보 처리방침에 따릅니다. <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple 개인정보 처리방침</a>을 참조하세요. (앱 내 ‘개인정보 처리방침’과 ‘지원’ 항목은 주소 표시줄이 없는 내장 리더에서 열리며 외부 브라우저로 이동하지 않습니다. 이 페이지만 불러오고 JavaScript는 비활성화되며, 쿠키나 브라우징 데이터를 저장하지 않고 다른 도메인으로의 이동은 차단됩니다. 이 페이지는 제3자 정적 호스팅(GitHub Pages)에서 호스팅되며, 이를 불러오는 것이 앱에서 Apple 외 서비스로 향하는 유일한 네트워크 요청이고 계정·기기 식별자를 포함하지 않습니다.)",
            ]),
        ]),
        ("4. 아동(미성년자) 정보 보호", [
            ("p", "KidsLearn은 아동용 앱이 아닌 <b>보호자용 관리 도구</b>이며, 모든 콘텐츠는 보호자가 생성하고 관리합니다. 앱은 채팅, 댓글, 공개 프로필, 콘텐츠 탐색·추천, 낯선 이와의 상호작용, 사용자 생성 콘텐츠의 공개 공유 기능을 <b>제공하지 않습니다</b>."),
            ("ul", [
                "<b>아동의 개인정보를 수집·판매하거나 제3자에게 공개하지 않습니다.</b> 아동의 학습 기록(별명, 아바타, 과목, 숙제, 습관, 포인트 등)은 보호자가 입력하며 <b>보호자 본인의 iCloud 계정에만</b> 저장됩니다. 개발자는 접근할 수 없습니다.",
                "<b>공개되는 사용자 생성 콘텐츠 없음.</b> 보호자가 입력한 텍스트는 보호자가 iCloud 개인 공유(CKShare)로 <b>일대일 초대한</b> 가족에게만 표시됩니다. 공개 대상도, 낯선 이에 대한 공개도, 검색·추천 기능도 없어 공개 UGC와 관련된 사회적 위험이 없습니다.",
                "<b>보호자 관리 기능.</b> ‘어린이 기기 잠금(PIN)’을 켜면 설정 기능이 숨겨지고 해제하려면 PIN이 필요합니다. PIN 변경·재설정에는 시스템 생체 인증 또는 기기 암호가 필요합니다.",
                "<b>아동용 Apple ID.</b> 보호자가 아동용 Apple ID에 아이 공간을 공유하는 경우, 해당 계정은 Apple 규정에 따라 보호자가 생성·관리하며 공유는 항상 보호자가 관리하고 언제든 중단할 수 있습니다.",
                "<b>보호자 동의에 관하여.</b> 본 앱은 <b>아동의 개인정보를 전혀 수집하지 않으므로</b>, 미국 COPPA, EU GDPR(아동 관련 조항), 중국 ‘아동 개인정보 네트워크 보호 규정’이 요구하는 ‘확인 가능한 보호자 동의’ 절차가 적용되지 않으며, 이를 위해 보호자의 신원 정보를 수집할 필요도 없습니다. 보호자는 언제든 아이 공간과 그 모든 데이터를 삭제할 수 있으며 삭제는 즉시 반영됩니다.",
                "중국 「개인정보 보호법」과 「아동 개인정보 네트워크 보호 규정」을 준수하고 COPPA / GDPR 원칙에 맞춥니다: <b>최소 수집, 보호자 통제, 미공유, 미판매, 광고·프로파일링 미사용</b>.",
                "아동 관련 정보를 열람·정정·완전 삭제하려는 보호자는 앱 내에서 직접 처리하거나 {mail}로 문의하여 도움을 받을 수 있습니다.",
            ]),
        ]),
        ("5. 데이터 저장, 보안 및 삭제", [
            ("ul", [
                "모든 데이터는 회원님 Apple ID의 iCloud 계정에 저장되며 Apple의 암호화 및 접근 제어로 보호됩니다. 서버 측 복사본은 보관하지 않습니다.",
                "<b>앱을 삭제해도 iCloud 데이터는 자동으로 지워지지 않습니다</b>(새 기기 복원을 위해). 모두 지우려면 iPhone/iPad에서 <i>설정 → Apple ID → iCloud → 계정 저장 공간 관리 → KidsLearn → 데이터 삭제</i>로 이동하거나, 앱 내 <i>나 → 아이 공간</i>에서 해당 공간을 삭제하거나, {mail}로 삭제 지원을 요청하세요.",
                "일부 화면 설정(언어, 표시 설정)은 <b>기기 로컬</b>(시스템 UserDefaults)에 저장됩니다. 기기를 떠나지 않으며 iCloud와 동기화되지 않습니다.",
                "Apple ID와 기기 잠금 암호를 안전하게 보관하세요. 이 데이터를 보호하는 주된 수단입니다.",
            ]),
        ]),
        ("6. 구매 및 결제", [
            ("p", "KidsLearn은 무료로 다운로드할 수 있고 7일 로컬 체험판을 제공합니다. 전체 버전은 <b>1회 구매(비소모성, 구독 아님, 자동 갱신 없음)</b>입니다. 모든 결제는 Apple App Store(StoreKit)가 처리하며, <b>결제 카드 정보를 받거나 저장하지 않습니다</b>. 가족 공유가 활성화되어 있어 가족이 다시 구매할 필요가 없습니다."),
        ]),
        ("7. 본 방침의 변경", [
            ("p", "본 방침이 변경되면 이 페이지를 갱신하고 상단의 ‘시행일’을 수정합니다. 중대한 변경(예: 새로운 데이터 수집 도입)은 앱 내에서도 눈에 띄는 방식으로 안내합니다. 최신 내용을 확인하려면 정기적으로 이 페이지를 방문해 주세요."),
        ]),
        ("8. 문의", [
            ("p", "본 방침이나 데이터에 관한 질문, 불만, 삭제 요청은 <b>{mail}</b>로 보내주세요. 통상 <b>영업일 3일</b> 이내에 회신합니다."),
        ]),
    ],
    "support_title": "지원 및 자주 묻는 질문",
    "support_rows": [
        ("새 기기 / 여러 기기 동기화", "각 기기에서 <b>동일한 Apple ID</b>로 로그인하고 iCloud 드라이브를 켜면 자동으로 동기화됩니다. 동기화가 멈추면 <i>설정 → Apple ID → iCloud</i>를 확인하세요."),
        ("가족 / 아이 공간 공유", "앱에서 ‘아이 공간 공유’(Apple CloudKit CKShare)를 사용하고, 상대가 자신의 Apple ID로 수락합니다. 테스트에는 서로 다른 Apple ID 2개가 필요합니다."),
        ("구매 복원", "결제 화면 하단의 ‘구매 복원’을 탭하세요. 추가 요금이 부과되지 않습니다."),
        ("모든 데이터 삭제", "위 5항을 참조하세요. 앱 삭제는 iCloud 데이터를 지우지 않습니다."),
        ("텍스트 스캔(OCR)", "Apple Vision으로 기기 내에서 전부 처리됩니다. 업로드도 네트워크 연결도 필요 없습니다."),
        ("지원 언어", "간체·번체 중국어, 영어, 일본어, 스페인어, 포르투갈어(브라질), 프랑스어, 독일어, 한국어, 러시아어(총 10개)."),
        ("시스템 요구 사항", "iOS / iPadOS 17.0 이상(iPhone·iPad 공용, 홈 화면 위젯 포함)."),
        ("문의", "이메일: <b>{mail}</b>(통상 영업일 3일 이내 회신)."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

CONTENT["ru"] = {
    "html_lang": "ru",
    "title": "Политика конфиденциальности и поддержка KidsLearn",
    "desc": "Политика конфиденциальности и поддержка KidsLearn: мы не собираем никаких персональных данных; все данные хранятся только в вашем собственном iCloud.",
    "h1": "🎓 Политика конфиденциальности и поддержка KidsLearn",
    "meta_line": "Дата вступления в силу: {d} ｜ Разработчик: {dev} ｜ Контакт: {mail}",
    "nav": ["Политика конфиденциальности", "Поддержка и часто задаваемые вопросы"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Коротко:</b> KidsLearn <b>не собирает никаких персональных данных</b>. Нет системы учётных записей, нет сервера, нет сторонних SDK для аналитики или рекламы. Расписания, домашние задания, привычки, напоминания и баллы, которые вы вводите, <b>хранятся только в вашей собственной личной базе данных iCloud</b> (Apple CloudKit); разработчик не может прочитать или экспортировать их. В качестве родительского контроля предусмотрена <b>блокировка устройства ребёнка (PIN-код)</b>, а весь контент, связанный с детьми, создаётся и управляется родителем.",
    "privacy_title": "Политика конфиденциальности",
    "sections": [
        ("1. Общие сведения", [
            ("p", "KidsLearn — это инструмент управления учебой для <b>родителей</b>: расписания, учёт домашних заданий, отметки о привычках, напоминания о занятиях, а также система баллов и наград. Приложение разработано независимым разработчиком ({dev}) и <b>не имеет собственного сервера и серверной базы данных</b>. Настоящая политика объясняет, как мы обрабатываем — точнее, не обрабатываем — вашу информацию."),
        ]),
        ("2. Что мы собираем: ничего", [
            ("p", "KidsLearn <b>не собирает никаких персональных данных</b>. В частности:"),
            ("ul", [
                "<b>Без регистрации и входа.</b> Мы не запрашиваем и не получаем ваше имя, электронную почту, телефон, контакты, местоположение, фотографии или какие-либо идентификаторы.",
                "<b>Ваши данные остаются в вашем iCloud.</b> Расписания, домашние задания, привычки, напоминания, баллы и награды хранятся в личной базе данных iCloud вашего собственного Apple ID (Apple CloudKit, контейнер <code>iCloud.com.frankzhou.KidLearn</code>). Данные принадлежат вам и хранятся Apple; <b>разработчик не может получить к ним доступ, прочитать или экспортировать их</b>.",
                "<b>Семейный доступ и «детские пространства».</b> Реализовано на основе CKShare из Apple CloudKit. Данные доступны только тем Apple ID, которых вы явно пригласили (как правило, членам семьи); вы управляете доступом и можете в любой момент его отозвать.",
            ]),
            ("p", "<b>Возможности устройства и системные разрешения:</b>"),
            ("ul", [
                "<b>Уведомления</b> — используются только для показа напоминаний о занятиях, которые вы настроили сами; никакой рекламы или маркетингового контента. «Удалённые уведомления» служат лишь <b>тихим сигналом для синхронизации iCloud</b> и никогда не показывают видимых оповещений.",
                "<b>Фото (системный выбор фотографий)</b> — функция «распознать текст (OCR)» в домашних заданиях выбирает изображение через системный инструмент выбора фото Apple (PhotosPicker). Приложение получает <b>только выбранное вами изображение</b>, не может просматривать или получать доступ к остальной библиотеке и <b>не требует разрешения на доступ к фотографиям</b>. Распознавание выполняется <b>полностью на устройстве</b> средствами фреймворка Apple Vision; ни изображение, ни результат <b>никогда не загружаются</b> на сервер, а исходное изображение не сохраняется. <b>Приложение не использует камеру и не запрашивает разрешение на камеру.</b> Установка фото-аватара ребёнка работает так же: читается только выбранное изображение, оно сжимается и хранится <b>исключительно в вашем собственном аккаунте iCloud</b> — ни на какой сервер не загружается.",
                "<b>Face ID / Touch ID / код-пароль устройства</b> — используется только для подтверждения личности на этом устройстве, когда родитель меняет или сбрасывает PIN-код блокировки ребёнка либо отключает детский режим. Проверку выполняет iOS; <b>приложение никогда не получает, не читает и не хранит биометрические данные</b>.",
                "<b>Буфер обмена</b> — считывается один раз, только когда вы намеренно нажимаете «Вставить», чтобы составить список заданий. Текст обрабатывается <b>на устройстве</b> и <b>не загружается и не сохраняется</b>. В остальное время приложение не обращается к буферу обмена.",
                "<b>Разрешения, которые мы никогда не запрашиваем</b> — местоположение, контакты, календари, напоминания, микрофон, камера и разрешение на отслеживание в приложениях. Кроме перечисленного, приложение не объявляет других разрешений.",
            ]),
        ]),
        ("3. Сторонние сервисы, отслеживание и реклама: отсутствуют", [
            ("ul", [
                "<b>Никакого стороннего кода</b> — проект не зависит ни от одного Swift-пакета, CocoaPods или сторонней библиотеки. Нет рекламных SDK, аналитических SDK (ни Firebase, ни аналогичных), нет сбора отчётов о сбоях, атрибуции или push-маркетинга.",
                "<b>Никакого отслеживания</b> — не используется IDFA, не запрашивается разрешение App Tracking Transparency, нет отслеживания между приложениями или сайтами, нет трекинговых cookie, отпечатков устройства или локальных идентификаторов.",
                "<b>Мы никогда не продаём, не передаём и не обмениваем пользовательские данные</b> и не участвуем ни в какой форме монетизации данных. Данные не используются для рекламы или профилирования.",
                "<b>Кроме загрузки этой страницы, все сетевые запросы идут только к сервисам Apple</b> — синхронизация iCloud (CloudKit) и встроенные покупки App Store (StoreKit). Оба сервиса регулируются политикой конфиденциальности Apple: см. <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">политику конфиденциальности Apple</a>. (Разделы «Политика конфиденциальности» и «Поддержка» открываются во встроенном средстве просмотра без адресной строки и не покидают приложение: загружается только эта страница, JavaScript отключён, cookie и данные просмотра не записываются, а переход на любые другие домены блокируется. Страница размещена на стороннем статическом хостинге (GitHub Pages); её загрузка — единственный сетевой запрос приложения к сервису, не принадлежащему Apple, и он не содержит идентификаторов учётной записи или устройства.)",
            ]),
        ]),
        ("4. Защита информации несовершеннолетних", [
            ("p", "KidsLearn — это <b>инструмент управления для родителей</b>, а не приложение для детей: весь контент создаётся и управляется родителями. В приложении <b>нет</b> чата, комментариев, публичных профилей, подборки или рекомендаций контента, общения с незнакомцами и публичного распространения пользовательского контента."),
            ("ul", [
                "<b>Мы не собираем, не продаём и не раскрываем персональные данные детей третьим лицам.</b> Учебные записи детей (псевдоним, аватар, предметы, домашние задания, привычки, баллы и т. д.) вводятся родителями и <b>хранятся только в собственном аккаунте iCloud родителя</b>; разработчик не имеет к ним доступа.",
                "<b>Никакого публичного пользовательского контента.</b> Введённый родителем текст виден только тем членам семьи, которых родитель <b>пригласил индивидуально</b> через приватный общий доступ iCloud (CKShare). Нет публичной аудитории, нет видимости для незнакомцев, нет механизмов поиска или рекомендаций, поэтому приложение не несёт социальных рисков, связанных с публичным пользовательским контентом.",
                "<b>Родительский контроль.</b> Приложение предлагает «блокировку устройства ребёнка (PIN)»: после включения функции настройки скрываются, а для выхода требуется PIN-код; изменение или сброс PIN-кода требует биометрической проверки системы или код-пароля устройства. Родители могут использовать это для ограничения доступа детей к настройкам и покупкам.",
                "<b>Детские Apple ID.</b> Если родитель открывает доступ к детскому пространству для Apple ID ребёнка, этот аккаунт создаётся и управляется родителем по правилам Apple; доступ остаётся под его контролем и может быть прекращён в любой момент.",
                "<b>О согласии родителей.</b> Поскольку приложение <b>вообще не собирает персональные данные детей</b>, механизмы «проверяемого согласия родителей», предусмотренные COPPA (США), GDPR (положения о детях, ЕС) и китайскими правилами защиты персональной информации детей в интернете, не применяются, и нам не требуется собирать данные о личности родителей для этой цели. Родители могут в любой момент удалить любое детское пространство вместе со всеми его данными; удаление вступает в силу немедленно.",
                "Мы соблюдаем Закон КНР о защите персональной информации и правила защиты персональной информации детей в интернете, а также следуем принципам COPPA и GDPR: <b>минимизация данных, родительский контроль, отсутствие передачи и продажи, отсутствие рекламы и профилирования</b>.",
                "Родители, которые хотят просмотреть, исправить или окончательно удалить информацию, связанную с ребёнком, могут сделать это в приложении или написать на {mail} для получения помощи.",
            ]),
        ]),
        ("5. Хранение, безопасность и удаление данных", [
            ("ul", [
                "Все данные находятся в учётной записи iCloud вашего Apple ID и защищены шифрованием и средствами контроля доступа Apple. Мы не храним копий на сервере.",
                "<b>Удаление приложения не приводит к автоматическому удалению данных из iCloud</b> (чтобы их можно было восстановить на новом устройстве). Чтобы стереть всё: на iPhone/iPad откройте <i>Настройки → ваш Apple ID → iCloud → Управление хранилищем учётной записи → KidsLearn → Удалить данные</i>; либо удалите нужное детское пространство в приложении в разделе <i>Я → Детские пространства</i>; либо напишите на {mail}, чтобы запросить помощь с удалением.",
                "Небольшое число настроек интерфейса (язык, параметры отображения) хранится <b>локально на устройстве</b> (системные UserDefaults). Они никогда не покидают ваше устройство и не синхронизируются с iCloud.",
                "Храните свой Apple ID и код-пароль устройства в безопасности — это основная защита этих данных.",
            ]),
        ]),
        ("6. Покупки и платежи", [
            ("p", "KidsLearn можно загрузить бесплатно; предусмотрена локальная пробная версия на 7 дней. Полная версия приобретается <b>разовой покупкой (нерасходуемый товар, без подписки и автопродления)</b>. Все платежи обрабатываются Apple App Store (StoreKit). <b>Мы никогда не получаем и не храним данные вашей банковской карты</b> и не видим полную информацию о вашей учётной записи. Включён семейный доступ, поэтому членам семьи не нужно покупать повторно."),
        ]),
        ("7. Изменения настоящей политики", [
            ("p", "В случае изменений мы обновим эту страницу и изменим указанную выше «дату вступления в силу». Существенные изменения (например, появление нового сбора данных) также будут заметно объявлены в приложении. Рекомендуем периодически просматривать эту страницу, чтобы знать актуальную версию."),
        ]),
        ("8. Связаться с нами", [
            ("p", "По любым вопросам, жалобам или запросам на удаление, касающимся настоящей политики или ваших данных, пишите на <b>{mail}</b>. Обычно мы отвечаем в течение <b>3 рабочих дней</b>."),
        ]),
    ],
    "support_title": "Поддержка и часто задаваемые вопросы",
    "support_rows": [
        ("Новое устройство / синхронизация между устройствами", "Войдите с <b>одним и тем же Apple ID</b> на всех устройствах и включите iCloud Drive — данные синхронизируются автоматически. Если синхронизация прекратилась, проверьте <i>Настройки → Apple ID → iCloud</i>."),
        ("Семейный доступ / общее детское пространство", "Используйте «Поделиться детским пространством» в приложении (CKShare из Apple CloudKit); получатель принимает приглашение своим Apple ID. Для проверки нужны два разных Apple ID."),
        ("Восстановить покупки", "Нажмите «Восстановить покупки» в нижней части экрана покупки — повторного списания не будет."),
        ("Удалить все данные", "См. раздел 5 выше. Удаление приложения не удаляет данные из iCloud."),
        ("Распознавание текста (OCR)", "Полностью выполняется на устройстве средствами Apple Vision; без загрузки и без подключения к сети."),
        ("Поддерживаемые языки", "10 языков: упрощённый и традиционный китайский, английский, японский, испанский, португальский (Бразилия), французский, немецкий, корейский и русский."),
        ("Системные требования", "iOS / iPadOS 17.0 или новее (iPhone и iPad, включая виджеты домашнего экрана)."),
        ("Контакт", "Электронная почта: <b>{mail}</b> (обычно отвечаем в течение 3 рабочих дней)."),
    ],
    "footer": "© 2026 {dev} · KidsLearn",
}

# 非英文页面底部声明：译本与英文版冲突时以英文版为准
DISCLAIMER = {
    "zh-Hans": "本页为英文版的中文译本，如译文与英文版存在歧义，以 <a href=\"{en}\">英文版</a> 为准。",
    "zh-Hant": "本頁為英文版的中文譯本，如譯文與英文版有歧義，以 <a href=\"{en}\">英文版</a> 為準。",
    "ja": "本ページは英文版の日本語訳です。訳文と英文版に相違がある場合は <a href=\"{en}\">英文版</a> を正とします。",
    "es": "Esta página es una traducción al español de la versión en inglés. En caso de discrepancia, prevalecerá la <a href=\"{en}\">versión en inglés</a>.",
    "pt-BR": "Esta página é uma tradução para o português da versão em inglês. Em caso de divergência, prevalece a <a href=\"{en}\">versão em inglês</a>.",
    "fr": "Cette page est une traduction française de la version anglaise. En cas de divergence, la <a href=\"{en}\">version anglaise</a> prévaut.",
    "de": "Diese Seite ist eine deutsche Übersetzung der englischen Fassung. Bei Abweichungen gilt die <a href=\"{en}\">englische Fassung</a>.",
    "ko": "본 페이지는 영문판을 한국어로 번역한 것입니다. 번역과 영문판이 다를 경우 <a href=\"{en}\">영문판</a>을 기준으로 합니다.",
    "ru": "Эта страница — перевод англоязычной версии на русский язык. В случае расхождений преимущественную силу имеет <a href=\"{en}\">англоязычная версия</a>.",
}

CSS = """
  :root{--bg:#f5f6f8;--card:#ffffff;--ink:#1d2129;--sub:#6b7280;--blue:#2563eb;
        --blue-bg:#eff6ff;--green:#16a34a;--green-bg:#f0fdf4;--line:#e5e7eb;--tab:#374151;}
  *{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth}
  body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans","Microsoft YaHei","Helvetica Neue",Arial,sans-serif;
       background:var(--bg);color:var(--ink);line-height:1.8;font-size:15px}
  header{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
  .head-inner{max-width:860px;margin:0 auto;padding:14px 20px 0}
  h1{font-size:19px}
  .head-meta{font-size:12.5px;color:var(--sub);margin:4px 0 8px}
  .langbar{display:flex;flex-wrap:wrap;gap:6px;padding-bottom:8px}
  .langbar a{font-size:12.5px;text-decoration:none;color:var(--tab);border:1px solid var(--line);
             border-radius:999px;padding:3px 11px;background:#fff}
  .langbar a.on{color:#fff;background:var(--blue);border-color:var(--blue)}
  main{max-width:860px;margin:0 auto;padding:22px 20px 60px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-bottom:16px}
  .summary{background:var(--green-bg);border:1px solid #bbf7d0;border-radius:12px;padding:16px 20px;margin-bottom:18px;font-size:14.5px;color:#166534}
  h2{font-size:20px;margin:26px 0 12px;display:flex;align-items:center;gap:8px;scroll-margin-top:110px}
  h2::before{content:"";width:4px;height:20px;background:var(--blue);border-radius:2px}
  h3{font-size:15.5px;margin:18px 0 6px;color:#111827}
  p{margin:8px 0}
  ul{margin:8px 0 8px 20px}
  li{margin:4px 0}
  code{background:#f3f4f6;border-radius:4px;padding:1px 6px;font-family:ui-monospace,Menlo,monospace;font-size:13px;word-break:break-all}
  a{color:var(--blue)}
  table{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0;background:var(--card)}
  th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
  th{background:#f9fafb;font-weight:600;white-space:nowrap;width:130px}
  footer{max-width:860px;margin:0 auto;padding:0 20px 40px;color:var(--sub);font-size:12.5px}
  .disc{font-size:12.5px;color:var(--sub);margin-top:10px}
  @media (max-width:600px){body{font-size:14.5px}.card{padding:16px 16px}h2{font-size:18px}}
"""


def fmt(s, d, mail=MAIL, dev=DEV, en_url=SITE + "/"):
    return s.replace("{d}", d).replace("{mail}", mail).replace("{dev}", dev).replace("{en}", en_url)


def render(lang, c):
    path = CANON[lang]
    switch = "".join(
        '<a href="{u}" class="{cls}">{t}</a>'.format(
            u=(SITE + CANON[l] + "/") if l != "en" else (SITE + "/"),
            cls="on" if l == lang else "", t=SWITCH_LABEL[l])
        for l in LANGS)
    alternates = "".join(
        '\n  <link rel="alternate" hreflang="{l}" href="{u}">'.format(
            l=l, u=(SITE + "/") if l == "en" else (SITE + "/" + l + "/"))
        for l in LANGS)
    alternates += '\n  <link rel="alternate" hreflang="x-default" href="{}">'.format(SITE + "/")

    body = []
    body.append('  <div class="summary">{}</div>'.format(fmt(c["summary"], EFFECTIVE)))
    body.append('<h2 id="privacy">{}</h2>'.format(c["privacy_title"]))
    body.append('  <div class="card">')
    for title, items in c["sections"]:
        body.append('    <h3>{}</h3>'.format(fmt(title, EFFECTIVE)))
        for kind, val in items:
            if kind == "p":
                body.append('    <p>{}</p>'.format(fmt(val, EFFECTIVE)))
            elif kind == "ul":
                body.append('    <ul>')
                for li in val:
                    body.append('      <li>{}</li>'.format(fmt(li, EFFECTIVE)))
                body.append('    </ul>')
    body.append('  </div>')
    body.append('<h2 id="support">{}</h2>'.format(c["support_title"]))
    body.append('  <div class="card">')
    body.append('    <table>')
    for th, td in c["support_rows"]:
        body.append('      <tr><th>{}</th><td>{}</td></tr>'.format(
            fmt(th, EFFECTIVE), fmt(td, EFFECTIVE)))
    body.append('    </table>')
    body.append('  </div>')
    if lang in DISCLAIMER:
        body.append('  <div class="disc">{}</div>'.format(fmt(DISCLAIMER[lang], EFFECTIVE)))

    url_self = SITE + ("/" if path == "" else path + "/")
    html = """<!DOCTYPE html>
<html lang="{hl}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{self}">{alt}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<style>{css}</style>
</head>
<body>
<header>
  <div class="head-inner">
    <h1>{h1}</h1>
    <div class="head-meta">{meta}</div>
    <div class="langbar">{switch}</div>
  </div>
</header>
<main>
{body}
</main>
<footer>{footer}</footer>
</body>
</html>
""".format(hl=c["html_lang"], title=c["title"], desc=c["desc"], self=url_self,
           alt=alternates, css=CSS, h1=c["h1"], meta=fmt(c["meta_line"], EFFECTIVE),
           switch=switch, body="\n".join(body), footer=fmt(c["footer"], EFFECTIVE))
    return html


# s2twp 之后的少量台湾用词修正（opencc 未覆盖的异体字）
TW_FIX = [("賬戶", "帳戶"), ("賬號", "帳號"), ("賬", "帳"),
          ("許可權", "權限"), ("郵箱", "電子郵件"), ("手機號", "手機號碼"),
          ("字串", "字串")]


def to_traditional(text):
    # 🔴 禁止静默降级：opencc 缺失时若返回原文，整页会以简体上线（2026-09-11 事故）。
    # 必须 fail loud——转换失败就让构建立刻失败，而不是发出坏页面。
    try:
        import opencc
    except ImportError as e:
        raise RuntimeError(
            "opencc 未安装（用带 opencc 的 Python 运行本脚本，"
            "如 ~/.workbuddy/binaries/python/envs/default/bin/python）：繁体页将输出简体原文，禁止继续构建"
        ) from e
    out = opencc.OpenCC("s2twp").convert(text)
    for a, b in TW_FIX:
        out = out.replace(a, b)
    return out


def main():
    # 繁体：由简体自动转换（含标题、正文、表格）
    zh = CONTENT["zh-Hans"]
    tr = {k: (to_traditional(v) if isinstance(v, str) else v) for k, v in zh.items()}
    tr["html_lang"] = "zh-TW"
    tr["sections"] = [
        (to_traditional(t),
         [(k, ([to_traditional(x) for x in v] if k == "ul" else to_traditional(v)))
          for k, v in items])
        for t, items in zh["sections"]]
    tr["support_rows"] = [(to_traditional(a), to_traditional(b)) for a, b in zh["support_rows"]]
    tr["nav"] = [to_traditional(x) for x in zh["nav"]]
    CONTENT["zh-Hant"] = tr

    for lang in LANGS:
        c = CONTENT[lang]
        html = render(lang, c)
        if lang == "en":
            targets = [os.path.join(BASE_DIR, "index.html"),
                       os.path.join(BASE_DIR, "en", "index.html")]
        else:
            targets = [os.path.join(BASE_DIR, lang, "index.html")]
        for t in targets:
            os.makedirs(os.path.dirname(t), exist_ok=True)
            with open(t, "w", encoding="utf-8") as f:
                f.write(html)
            print("written:", os.path.relpath(t, BASE_DIR), len(html), "chars")


if __name__ == "__main__":
    main()
