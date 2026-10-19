# -*- coding: utf-8 -*-
"""LearnNest 隐私政策 11 新语内容（da/fil/id/it/ms + nb/nl/pl/sv/tr/vi）——1.0.3 扩语
结构与 build_pages.py 的 CONTENT 字典完全一致；由 build_pages.py 合并后统一渲染。
"""

CONTENT11A = {}

CONTENT11A["da"] = {
    "html_lang": "da",
    "title": "LearnNest Privatlivspolitik & Support",
    "desc": "LearnNest privatlivspolitik og support: vi indsamler ingen personlige oplysninger; alle data forbliver i din egen iCloud.",
    "h1": "🎓 LearnNest Privatlivspolitik & Support",
    "meta_line": "Ikrafttrædelsesdato: {d} ｜ Udvikler: {dev} ｜ Kontakt: {mail}",
    "nav": ["Privatlivspolitik", "Support & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kort sagt:</b> LearnNest <b>indsamler ingen personlige oplysninger</b>. Der er ingen konto, ingen server og ingen tredjepartsanalyse eller reklame. Skemaer, lektier, vaner, påmindelser og point, du indtaster, gemmes <b>kun i din egen private iCloud-database</b> (Apple CloudKit); udvikleren kan ikke læse eller eksportere dem. En <b>enhedslås (PIN)</b> er tilgængelig som forældrekontrol, og alt læringsindhold oprettes og styres af en forælder.",
    "privacy_title": "Privatlivspolitik",
    "sections": [
        ("1. Oversigt", [
            ("p", "LearnNest er et studieorganiseringsværktøj til <b>forældre</b> med skemaer, lektiesporing, vanetjek, påmindelser og et point-/belønningssystem. Det er udviklet af en uafhængig udvikler ({dev}) og har <b>ingen egen server og ingen backend-database</b>. Denne politik forklarer, hvordan vi håndterer – faktisk ikke håndterer – dine oplysninger."),
        ]),
        ("2. Hvad vi indsamler: ingenting", [
            ("p", "LearnNest <b>indsamler ingen personlige oplysninger</b>. Konkret:"),
            ("ul", [
                "<b>Ingen tilmelding, ingen login.</b> Vi anmoder ikke om eller modtager dit navn, din e-mail, dit telefonnummer, kontakter, placering, fotos eller andre identifikatorer.",
                "<b>Dine data forbliver i din egen iCloud.</b> Skemaer, lektier, vaner, påmindelser, point og belønninger gemmes i den private iCloud-database for din egen Apple-ID (Apple CloudKit, container <code>iCloud.com.frankzhou.KidLearn</code>). Data tilhører dig og opbevares af Apple; <b>udvikleren kan ikke få adgang til, læse eller eksportere dem</b>.",
                "<b>Familiedeling &amp; studierum.</b> Bygger på Apple CloudKit CKShare. Data deles kun med de Apple-ID'er, du eksplicit inviterer (normalt familiemedlemmer); du styrer og kan tilbagekalde deling når som helst.",
            ]),
            ("p", "<b>Enhedsegenskaber og systemtilladelser:</b>"),
            ("ul", [
                "<b>Notifikationer</b> – bruges udelukkende til at levere de studiepåmindelser, du selv har oprettet; intet reklame- eller markedsføringsindhold. \"Fjernnotifikationer\" bruges kun som <b>lydløs udløser for iCloud-synkronisering</b> og viser aldrig en synlig alarm.",
                "<b>Fotos (systemets fotovælger)</b> – lektiefunktionen \"scan tekst (OCR)\" vælger et billede via Apples systemfotovælger (PhotosPicker). Appen modtager <b>kun det enkelte billede, du vælger</b>, kan ikke gennemsøge resten af dit bibliotek og <b>kræver ingen fotobibliotekstilladelse</b>. Genkendelsen kører <b>helt på enheden</b> via Apples Vision-ramme; hverken billedet eller resultatet <b>uploades nogensinde</b>, og originalbilledet gemmes ikke. <b>Appen bruger ikke kameraet og anmoder ikke om kameratilladelse.</b> Profilfoto til et studierum fungerer på samme måde: kun det valgte billede læses, komprimeres og <b>gemmes udelukkende i din egen iCloud-konto</b> – aldrig uploadet til nogen server.",
                "<b>Face ID / Touch ID / enhedskode</b> – bruges kun til at godkende på denne enhed, når en forælder ændrer eller nulstiller enhedslåsens PIN eller slår lås fra. Godkendelsen udføres af iOS; <b>appen modtager, læser eller gemmer aldrig biometriske data</b>.",
                "<b>Udklipsholder</b> – læses én gang, kun når du aktivt trykker \"Indsæt\", for at opbygge en lektieliste. Teksten behandles <b>på enheden</b>; den <b>uploades eller gemmes aldrig</b>. Appen tilgår ikke udklipsholderen på noget andet tidspunkt.",
                "<b>Tilladelser, vi aldrig anmoder om</b> – ingen placering, kontakter, kalendere, påmindelser, mikrofon, kamera eller appsporing. Udover ovenstående erklærer appen ingen andre tilladelser.",
            ]),
        ]),
        ("3. Tredjeparter, sporing og reklame: ingen", [
            ("ul", [
                "<b>Ingen tredjepartskode overhovedet</b> – projektet afhænger af ingen Swift Package, CocoaPods eller tredjepartsbibliotek. Ingen reklame-SDK, intet analyse-SDK (ingen Firebase e.l.), ingen crashrapportering, attribuering eller push-markedsføring.",
                "<b>Ingen sporing</b> – ingen IDFA, ingen App Tracking Transparency-dialog, ingen sporing på tværs af apps eller sider, ingen sporingscookies, enhedsfingeraftryk eller lokale identifikatorer.",
                "<b>Vi sælger, deler eller handler aldrig med brugerdata</b> og deltager ikke i nogen form for datamonetisering. Ingen data bruges til reklame eller brugerprofilering.",
                "<b>Udover indlæsning af denne politikside går alle netværksanmodninger til Apple-tjenester</b> – iCloud (CloudKit)-synkronisering og App Store-køb (StoreKit). Begge er omfattet af Apples egen privatlivspolitik – se <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apples privatlivspolitik</a>. (Appens indgange \"Privatlivspolitik\" og \"Support\" åbner i en indbygget læser uden adresselinje og forlader aldrig appen: kun denne side indlæses, JavaScript er deaktiveret, ingen cookies eller browserdata skrives, og navigation til andre domæner blokeres. Siden hostes på en tredjeparts statisk vært (GitHub Pages); indlæsning af den er appens eneste netværksanmodning til en ikke-Apple-tjeneste og indeholder ingen konto- eller enhedsidentifikator.)",
            ]),
        ]),
        ("4. Mindres privatliv", [
            ("p", "LearnNest er et <b>styringsværktøj for forældre</b>, ikke en app lavet direkte til mindreårige: alt indhold oprettes og styres af forældre. Appen tilbyder <b>ingen</b> chat, kommentarer, offentlige profiler, indholdsopdagelse eller anbefaling, kontakt med fremmede eller offentlig deling af brugerindhold."),
            ("ul", [
                "<b>Vi indsamler, sælger eller videregiver ikke mindreåriges personlige oplysninger til tredjepart.</b> Studieregistreringer (kaldenavn, avatar, kurser, lektier, vaner, point osv.) indtastes af forældre og <b>gemmes kun i forælderens egen iCloud-konto</b>; udvikleren har ingen adgang.",
                "<b>Ingen offentligt brugerindhold.</b> Tekst indtastet af forældre er kun synlig for familiemedlemmer, som forælderen <b>inviterer én til én</b> via iCloud-privatdeling (CKShare). Der er intet offentligt publikum, ingen fremmede kan se noget, og der er ingen søge- eller anbefalingsmekanisme, så appen har ingen af de sociale risici ved offentligt brugerindhold.",
                "<b>Forældrekontrol.</b> Appen tilbyder en \"Enhedslås (PIN)\": når den er aktiveret, skjules konfigurationsfunktioner, og forladelse kræver PIN; ændring eller nulstilling kræver systembiometri eller adgangskode. Forældre kan bruge den til at begrænse adgang til indstillinger og køb.",
                "<b>Mindreåriges Apple-ID'er.</b> Hvis en forælder deler et studierum med en mindreårigs Apple-ID, oprettes og styres kontoen af forælderen under Apples regler; deling forbliver under forælderens kontrol og kan stoppes når som helst.",
                "<b>Om forældresamtykke.</b> Fordi appen <b>slet ikke indsamler mindreåriges personlige oplysninger</b>, gælder de \"verificerbare forældresamtykke\"-mekanismer, der kræves af COPPA (USA), GDPR (mindreåriges bestemmelser, EU) og Kinas regler om beskyttelse af mindreåriges personlige oplysninger online, ikke, og vi behøver ikke at indsamle forældreidentitet til det formål. Forældre kan slette ethvert studierum og alle dets data når som helst; sletning træder i kraft straks.",
                "Vi følger Kinas lov om beskyttelse af personlige oplysninger og Kinas regler om beskyttelse af mindreåriges personlige oplysninger online og er i overensstemmelse med COPPA/GDPR-principperne: <b>dataminimering, forældrekontrol, ingen deling, intet salg og ingen reklame eller profilering</b>.",
                "Forældre, der ønsker at gennemse, rette eller permanent slette oplysninger i deres studierum, kan gøre det i appen eller skrive til {mail} for hjælp.",
            ]),
        ]),
        ("5. Datalagring, sikkerhed og sletning", [
            ("ul", [
                "Alle data findes i iCloud-kontoen for dit Apple-ID, beskyttet af Apples kryptering og adgangskontrol. Vi opbevarer ingen serverkopi.",
                "<b>Sletning af appen fjerner ikke automatisk iCloud-data</b> (så du kan gendanne på en ny enhed). For at slette alt: på iPhone/iPad gå til <i>Indstillinger → dit Apple-ID → iCloud → Administrer lagerplads → LearnNest → Slet data</i>; slet det pågældende studierum i appen under <i>Mine → Studierum</i>; eller skriv til {mail} for slettehjælp.",
                "Et lille antal grænsefladeindstillinger (sprog, visning) gemmes <b>lokalt på enheden</b> (systemets UserDefaults). De forlader aldrig din enhed og synkroniseres ikke til iCloud.",
                "Beskyt dit Apple-ID og din enhedskode – de er den vigtigste beskyttelse af disse data.",
            ]),
        ]),
        ("6. Køb og betalinger", [
            ("p", "LearnNest er gratis at downloade med en lokal 7-dages prøveperiode. Fuld version er et <b>engangskøb (ikke-forbrugende, ikke-abonnement; ingen automatisk fornyelse)</b>. Alle betalinger behandles af Apple App Store (StoreKit). <b>Vi modtager eller gemmer aldrig dine betalingskortoplysninger</b> og kan ikke se dine fulde kontooplysninger. Familiedeling er aktiveret, så familiemedlemmer behøver ikke at købe igen."),
        ]),
        ("7. Ændringer af denne politik", [
            ("p", "Hvis denne politik ændres, opdaterer vi denne side og reviderer \"ikrafttrædelsesdatoen\" øverst. Væsentlige ændringer (f.eks. indførelse af ny dataindsamling) annonceres også tydeligt i appen. Se regelmæssigt denne side for den nyeste version."),
        ]),
        ("8. Kontakt os", [
            ("p", "Ved spørgsmål, klager eller anmodning om sletning vedrørende denne politik eller dine data: skriv til <b>{mail}</b>. Vi svarer normalt inden for <b>3 hverdage</b>."),
        ]),
    ],
    "support_title": "Support & FAQ",
    "support_rows": [
        ("Ny enhed / synkronisering mellem enheder", "Log ind med <b>samme Apple-ID</b> på hver enhed med iCloud Drive aktiveret; data synkroniseres automatisk. Hvis synkroniseringen hænger, tjek <i>Indstillinger → Apple-ID → iCloud</i>."),
        ("Familie-/studierumsdeling", "Brug \"Del rum\" i appen (Apple CloudKit CKShare); modtageren accepterer med sit eget Apple-ID. Der kræves to forskellige Apple-ID'er til test."),
        ("Gendan køb", "Tryk \"Gendan køb\" i bunden af betalingsvæggen – intet ekstra gebyr."),
        ("Slet alle data", "Se afsnit 5 ovenfor. Sletning af appen fjerner ikke iCloud-data."),
        ("Scan tekst (OCR)", "Kører helt på enheden via Apple Vision; ingen upload, intet netværk påkrævet."),
        ("Understøttede sprog", "21 sprog: forenklet og traditionelt kinesisk, engelsk, japansk, koreansk, spansk, portugisisk (BR), fransk, tysk, italiensk, hollandsk, polsk, svensk, norsk (bokmål), dansk, indonesisk, malaysisk, filippinsk, tyrkisk, vietnamesisk og russisk."),
        ("Systemkrav", "iOS / iPadOS 17.0 eller nyere (iPhone og iPad, inklusive hjemmeskærmswidgets)."),
        ("Kontakt", "E-mail <b>{mail}</b> – svar inden for 3 hverdage."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["fil"] = {
    "html_lang": "fil",
    "title": "LearnNest Patakaran sa Privacy at Suporta",
    "desc": "Patakaran sa privacy at suporta ng LearnNest: walang kinokolektang personal na impormasyon; nananatili sa iyong sariling iCloud ang lahat ng data.",
    "h1": "🎓 LearnNest Patakaran sa Privacy at Suporta",
    "meta_line": "Petsa ng Pagkakabisa: {d} ｜ Developer: {dev} ｜ Contact: {mail}",
    "nav": ["Patakaran sa Privacy", "Suporta & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Sa maikling salita:</b> ang LearnNest <b>ay hindi kumokolekta ng anumang personal na impormasyon</b>. Walang account system, walang server, walang third-party analytics o advertising SDK. Ang timetable, takdang-aralin, gawi, paalala at puntos na ilalagay mo ay <b>imbak lamang sa iyong sariling pribadong iCloud database</b> (Apple CloudKit); hindi ito mababasa o mai-e-export ng developer. May <b>Device Lock (PIN)</b> bilang parental control, at ang lahat ng nilalaman ay ginagawa at pinamamahalaan ng magulang.",
    "privacy_title": "Patakaran sa Privacy",
    "sections": [
        ("1. Pangkalahatan", [
            ("p", "Ang LearnNest ay study-management tool para sa <b>mga magulang</b>: timetable, pagsubaybay sa takdang-aralin, pag-check-in ng gawi, mga paalala at sistema ng puntos/gantimpala. Ginawa ito ng isang independent developer ({dev}) at <b>walang sariling server at walang backend database</b>. Ipinapaliwanag ng patakaran kung paano namin hina-handle — sa katunayan, hindi hinahandle — ang iyong impormasyon."),
        ]),
        ("2. Ano ang kinokolekta namin: wala", [
            ("p", "Ang LearnNest <b>ay hindi kumokolekta ng anumang personal na impormasyon</b>. Partikular:"),
            ("ul", [
                "<b>Walang sign-up, walang login.</b> Hindi kami humihiling o tumatanggap ng pangalan, email, numero ng telepono, mga contact, lokasyon, larawan o anumang identifier.",
                "<b>Nasa iyong sariling iCloud ang data.</b> Ang timetable, takdang-aralin, gawi, paalala, puntos at gantimpala na gagawin mo ay naka-imbak sa pribadong iCloud database ng iyong sariling Apple ID (Apple CloudKit, container <code>iCloud.com.frankzhou.KidLearn</code>). Sa iyo ang data at hawak ito ng Apple; <b>hindi maa-access, mababasa o ma-e-export ng developer</b>.",
                "<b>Family Sharing &amp; study spaces.</b> Batay sa Apple CloudKit CKShare. Ang data ay ibinabahagi lamang sa mga Apple ID na dapat mong imbitahan (karaniwang miyembro ng pamilya); ikaw ang kontrol at maaari mong kanselahin anumang oras.",
            ]),
            ("p", "<b>Mga kakayahan ng device at pahintulot ng sistema:</b>"),
            ("ul", [
                "<b>Mga notification</b> — para lamang sa mga study reminder na ikaw ang nagtakda; walang advertising o marketing content. Ang \"remote notifications\" ay <b>tahimik na trigger para sa iCloud sync</b> lamang at hindi kailanman nagpapakita ng nakikitang alerto.",
                "<b>Mga larawan (system photo picker)</b> — ang tampok na \"scan text (OCR)\" ng takdang-aralin ay kumukuha ng larawan sa system photo picker ng Apple (PhotosPicker). Ang app ay tumatanggap <b>lamang ng solong larawang pinili mo</b>, hindi maaaring mag-browse sa natitira ng iyong library, at <b>hindi nangangailangan ng photo-library permission</b>. Ang recognition ay <b>buong gagawin sa device</b> sa Apple Vision framework; ang larawan man o resulta ay <b>hindi kailanman ina-upload</b>, at hindi pinapanatili ang orihinal na larawan. <b>Hindi gumagamit ang app ng camera at hindi humihingi ng camera permission.</b> Ang profile photo ng study space ay pareho: ang piling larawan lamang ang binabasa, kinukompres at <b>imbak lamang sa iyong sariling iCloud account</b> — hindi kailanman ina-upload sa anumang server.",
                "<b>Face ID / Touch ID / device passcode</b> — para lamang sa pag-authenticate sa device kapag nagbago o nag-reset ang magulang ng Device Lock PIN o nag-off ng lock mode. Ginagawa ng iOS ang authentication; <b>hindi kailanman natatanggap, nababasa o naiimbak ng app ang anumang biometric data</b>.",
                "<b>Pasteboard</b> — binabasa nang isang beses, kapag pinindot mo ang \"Paste\", para bumuo ng listahan ng takdang-aralin. Ang teksto ay pinoproseso <b>sa device</b>; <b>hindi kailanman ina-upload o pinapanatili</b>. Hindi tinatanggal ng app ang pasteboard sa anumang ibang pagkakataon.",
                "<b>Mga permission na hindi kami hihilingin</b> — walang lokasyon, contacts, kalendaryo, paalala, mikropono, kamera o App Tracking authorization. Maliban sa mga nabanggit, walang ibang deklaradong permission ang app.",
            ]),
        ]),
        ("3. Ikatlong partido, tracking at advertising: wala", [
            ("ul", [
                "<b>Walang third-party code kahit isa</b> — walang Swift Package, CocoaPods o third-party library ang proyekto. Walang advertising SDK, walang analytics SDK (walang Firebase at katulad), walang crash reporting, attribution o push marketing.",
                "<b>Walang tracking</b> — walang IDFA, walang App Tracking Transparency prompt, walang cross-app o cross-site tracking, walang tracking cookies, device fingerprinting o lokal na identifier.",
                "<b>Hindi kami kailanman nagbebenta, nagbabahagi o nagpapalit ng user data</b>, at hindi kami sangkot sa anumang data monetization. Walang data na ginagamit para sa advertising o user profiling.",
                "<b>Maliban sa pag-load ng pahinang ito, ang bawat network request ay papunta sa mga serbisyo ng Apple</b> — iCloud (CloudKit) sync at App Store In-App Purchase (StoreKit). Saklaw ng sariling privacy policy ng Apple ang dalawa — tingnan ang <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple Privacy Policy</a>. (Ang mga entry na \"Privacy Policy\" at \"Support\" sa app ay bumubukas sa built-in reader na walang address bar at hindi lumalabas ng app: ang pahinang ito lamang ang ni-lo-load, naka-disable ang JavaScript, walang cookies o browsing data, at hinarang ang pag-navigate sa ibang domain. Naka-host ang pahina sa third-party static host (GitHub Pages); ang pag-load nito ang tanging network request ng app sa serbisyong hindi Apple at walang account o device identifier.)",
            ]),
        ]),
        ("4. Privacy ng mga menor de edad", [
            ("p", "Ang LearnNest ay <b>management tool para sa mga magulang</b>, hindi app na gawa direkta para sa mga menor de edad: lahat ng nilalaman ay ginagawa at pinamamahalaan ng magulang. Walang chat, komento, pampublikong profile, content discovery o rekomendasyon, pakikipag-ugnayan sa mga di-kilala, o pampublikong pagbabahagi ng user-generated content."),
            ("ul", [
                "<b>Hindi kami kumokolekta, nagbebenta o nagbubunyag ng personal na impormasyon ng menor de edad sa ikatlong partido.</b> Ang mga tala (palayaw, avatar, kurso, takdang-aralin, gawi, puntos, atbp.) ay inilalagay ng magulang at <b>naka-imbak lamang sa sariling iCloud account ng magulang</b>; walang access ang developer.",
                "<b>Walang pampublikong user-generated content.</b> Ang tekstong inilagay ng magulang ay nakikita lamang ng mga miyembro ng pamilya na <b>imbitado nang isa-isa</b> sa pamamagitan ng iCloud private sharing (CKShare). Walang publikong audience, walang visibility sa mga di-kilala, at walang mekanismo ng search o rekomendasyon, kaya walang social risks na kaakibat ng public UGC.",
                "<b>Parental controls.</b> May \"Device Lock (PIN)\": kapag naka-on, nakatago ang mga configuration feature at ang paglabas ay nangangailangan ng PIN; ang pagbago o pag-reset ay nangangailangan ng system biometric o passcode. Magagamit ito ng magulang para limitahan ang access sa settings at pagbili.",
                "<b>Mga Apple ID ng menor de edad.</b> Kung magbabahagi ang magulang ng study space sa Apple ID ng menor de edad, ang account na iyon ay ginawa at pinamamahalaan ng magulang sa ilalim ng mga patakaran ng Apple; nananatili sa kontrol ng magulang ang pagbabahagi at maaaring ihinto anumang oras.",
                "<b>Tungkol sa parental consent.</b> Dahil <b>walang anumang personal na impormasyon ng menor de edad ang kinolecta ng app</b>, hindi nalalapat ang mga \"verifiable parental consent\" na mekanismo na kinakailangan ng COPPA (US), GDPR (mga probisyon sa menor de edad, EU) at mga regulasyon ng Tsina sa proteksyon ng personal na impormasyon ng menor de edad online, at hindi kami kailangang kumuha ng anumang impormasyon ng pagkakakilanlan ng magulang para diyan. Maaaring tanggalin ng magulang ang anumang study space at lahat ng data nito anumang oras; agad na nagkakabisa ang pagtanggal.",
                "Sinusunod namin ang Personal Information Protection Law ng Tsina at mga regulasyon nito sa proteksyon ng personal na impormasyon ng menor de edad online, at nakahanay sa mga prinsipyo ng COPPA/GDPR: <b>data minimization, parental control, walang pagbabahagi, walang pagbebenta, at walang advertising o profiling</b>.",
                "Ang mga magulang na nais suriin, itama o permanenteng burahin ang impormasyon sa kanilang mga study space ay maaaring gawin ito sa app, o mag-email sa {mail} para sa tulong.",
            ]),
        ]),
        ("5. Pag-iimbak ng data, seguridad at pagbubura", [
            ("ul", [
                "Ang lahat ng data ay nasa iCloud account ng iyong Apple ID, protektado ng encryption at access control ng Apple. Walang server-side na kopya ang napanatili namin.",
                "<b>Ang pag-delete ng app ay hindi awtomatikong nagbubura ng iCloud data</b> (para ma-restore sa bagong device). Para burahin ang lahat: sa iPhone/iPad pumunta sa <i>Settings → iyong Apple ID → iCloud → Manage Account Storage → LearnNest → Delete Data</i>; burahin ang study space sa app sa ilalim ng <i>Me → Study Spaces</i>; o mag-email sa {mail} para sa tulong sa pagbubura.",
                "Ang kaunting kagustuhan sa interface (wika, display settings) ay naka-imbak <b>lokal sa device</b> (system UserDefaults). Hindi ito lumalabas sa iyong device at hindi naka-sync sa iCloud.",
                "Panatilihing ligtas ang iyong Apple ID at device passcode — ang mga ito ang pangunahing proteksyon ng data na ito.",
            ]),
        ]),
        ("6. Mga pagbili at pagbabayad", [
            ("p", "Libreng i-download ang LearnNest na may lokal na 7-araw na trial. Ang full version ay <b>isang beses na pagbili (non-consumable, hindi subscription; walang auto-renewal)</b>. Ang lahat ng pagbabayad ay pinoproseso ng Apple App Store (StoreKit). <b>Hindi kailanman natatanggap o naiimbak ng app ang detalye ng iyong payment card</b>, at hindi namin nakikita ang buong impormasyon ng iyong account. Naka-enable ang Family Sharing, kaya hindi na kailangang bumili muli ng mga miyembro ng pamilya."),
        ]),
        ("7. Mga pagbabago sa patakarang ito", [
            ("p", "Kung magbabago ang patakarang ito, i-a-update namin ang pahinang ito at babaguhin ang \"Petsa ng Pagkakabisa\" sa itaas. Ang mahahalagang pagbabago (halimbawa, pagdaragdag ng anumang bagong data collection) ay iaanunsyo rin nang malinaw sa loob ng app. Tingnan paminsan-minsan ang pahinang ito para sa pinakabagong bersyon."),
        ]),
        ("8. Makipag-ugnayan sa amin", [
            ("p", "Para sa anumang katanungan, reklamo o kahilingan sa pagbura tungkol sa patakarang ito o sa iyong data, mag-email sa <b>{mail}</b>. Karaniwang sumasagot kami sa loob ng <b>3 araw na negosyo</b>."),
        ]),
    ],
    "support_title": "Suporta & FAQ",
    "support_rows": [
        ("Bagong device / multi-device sync", "Mag-sign in gamit ang <b>parehong Apple ID</b> sa bawat device na naka-enable ang iCloud Drive; awtomatikong nag-s-sync ang data. Kung na-stall ang sync, tingnan ang <i>Settings → Apple ID → iCloud</i>."),
        ("Pagbabahagi ng pamilya / study space", "Gamitin ang \"Share Space\" sa app (Apple CloudKit CKShare); tatanggapin ng tatanggap gamit ang sariling Apple ID. Dalawang magkaibang Apple ID ang kailangan para sa pagsubok."),
        ("I-restore ang mga pagbili", "I-tap ang \"Restore Purchases\" sa ibaba ng paywall — walang dagdag na singil."),
        ("Burahin ang lahat ng data", "Tingnan ang seksyon 5 sa itaas. Hindi inaalis ng pag-delete ng app ang iCloud data."),
        ("Scan text (OCR)", "Ganap na tumatakbo sa device sa Apple Vision; walang upload, walang kinakailangang network."),
        ("Mga sinusuportahang wika", "21 wika: Simplified at Traditional Chinese, English, Japanese, Korean, Spanish, Portuguese (BR), French, German, Italian, Dutch, Polish, Swedish, Norwegian (Bokmål), Danish, Indonesian, Malay, Filipino, Turkish, Vietnamese at Russian."),
        ("Mga kinakailangan ng sistema", "iOS / iPadOS 17.0 o mas bago (iPhone at iPad, kasama ang home-screen widgets)."),
        ("Kontakt", "Mag-email sa <b>{mail}</b> — sumasagot sa loob ng 3 araw na negosyo."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["id"] = {
    "html_lang": "id",
    "title": "Kebijakan Privasi & Dukungan LearnNest",
    "desc": "Kebijakan privasi dan dukungan LearnNest: kami tidak mengumpulkan informasi pribadi; semua data tetap di iCloud Anda sendiri.",
    "h1": "🎓 Kebijakan Privasi & Dukungan LearnNest",
    "meta_line": "Tanggal Berlaku: {d} ｜ Pengembang: {dev} ｜ Kontak: {mail}",
    "nav": ["Kebijakan Privasi", "Dukungan & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Ringkasnya:</b> LearnNest <b>tidak mengumpulkan informasi pribadi apa pun</b>. Tidak ada sistem akun, tidak ada server, dan tidak ada SDK analitik atau iklan pihak ketiga. Jadwal, PR, kebiasaan, pengingat, dan poin yang Anda masukkan <b>hanya tersimpan di basis data iCloud pribadi Anda sendiri</b> (Apple CloudKit); pengembang tidak dapat membaca atau mengekspornya. <b>Kunci Perangkat (PIN)</b> tersedia sebagai kontrol orang tua, dan semua konten pembelajaran dibuat dan dikelola oleh orang tua.",
    "privacy_title": "Kebijakan Privasi",
    "sections": [
        ("1. Ikhtisar", [
            ("p", "LearnNest adalah alat manajemen belajar untuk <b>orang tua</b>: jadwal, pencatatan PR, centang kebiasaan, pengingat, dan sistem poin/hadiah. Dikembangkan oleh pengembang independen ({dev}) dan <b>tidak memiliki server sendiri maupun basis data backend</b>. Kebijakan ini menjelaskan bagaimana kami menangani — sebenarnya, tidak menangani — informasi Anda."),
        ]),
        ("2. Yang Kami Kumpulkan: Tidak Ada", [
            ("p", "LearnNest <b>tidak mengumpulkan informasi pribadi apa pun</b>. Secara khusus:"),
            ("ul", [
                "<b>Tidak ada pendaftaran, tidak ada masuk.</b> Kami tidak meminta atau menerima nama, email, nomor telepon, kontak, lokasi, foto, atau pengenal apa pun.",
                "<b>Data Anda tetap di iCloud Anda sendiri.</b> Jadwal, PR, kebiasaan, pengingat, poin, dan hadiah yang Anda buat tersimpan di basis data iCloud pribadi Apple ID Anda sendiri (Apple CloudKit, kontainer <code>iCloud.com.frankzhou.KidLearn</code>). Data itu milik Anda dan dipegang oleh Apple; <b>pengembang tidak dapat mengakses, membaca, atau mengekspornya</b>.",
                "<b>Family Sharing &amp; ruang belajar.</b> Dibangun di atas Apple CloudKit CKShare. Data hanya dibagikan dengan Apple ID yang Anda undang secara eksplisit (biasanya anggota keluarga); Anda mengendalikan dan dapat mencabut berbagi kapan saja.",
            ]),
            ("p", "<b>Kemampuan perangkat dan izin sistem:</b>"),
            ("ul", [
                "<b>Notifikasi</b> — hanya untuk mengirimkan pengingat belajar yang Anda atur sendiri; tanpa konten iklan atau pemasaran. \"Notifikasi jarak jauh\" hanya digunakan sebagai <b>pemicu senyap untuk sinkronisasi iCloud</b> dan tidak pernah menampilkan peringatan yang terlihat.",
                "<b>Foto (pemilih foto sistem)</b> — fitur \"pindai teks (OCR)\" PR mengambil gambar melalui pemilih foto sistem Apple (PhotosPicker). Aplikasi hanya menerima <b>satu gambar yang Anda pilih</b>, tidak dapat menelusuri sisa pustaka Anda, dan <b>tidak memerlukan izin pustaka foto</b>. Pengenalan berjalan <b>sepenuhnya di perangkat</b> melalui kerangka Apple Vision; baik gambar maupun hasilnya <b>tidak pernah diunggah</b>, dan gambar asli tidak disimpan. <b>Aplikasi tidak menggunakan kamera dan tidak meminta izin kamera.</b> Foto profil ruang belajar bekerja dengan cara yang sama: hanya gambar yang Anda pilih yang dibaca, dikompresi, dan <b>disimpan hanya di akun iCloud Anda sendiri</b> — tidak pernah diunggah ke server mana pun.",
                "<b>Face ID / Touch ID / kode sandi perangkat</b> — hanya untuk autentikasi di perangkat ini ketika orang tua mengubah atau mengatur ulang PIN Kunci Perangkat, atau mematikan mode kunci. Autentikasi dilakukan oleh iOS; <b>aplikasi tidak pernah menerima, membaca, atau menyimpan data biometrik apa pun</b>.",
                "<b>Papan klip</b> — dibaca sekali, hanya saat Anda mengetuk \"Tempel\", untuk menyusun daftar PR. Teks diproses <b>di perangkat</b>; <b>tidak pernah diunggah atau disimpan</b>. Aplikasi tidak mengakses papan klip pada waktu lain.",
                "<b>Izin yang tidak pernah kami minta</b> — tidak ada lokasi, kontak, kalender, pengingat, mikrofon, kamera, atau otorisasi Pelacakan Aplikasi. Selain butir di atas, aplikasi tidak mendeklarasikan izin lain.",
            ]),
        ]),
        ("3. Pihak Ketiga, Pelacakan, dan Iklan: Tidak Ada", [
            ("ul", [
                "<b>Tidak ada kode pihak ketiga sama sekali</b> — proyek ini tidak bergantung pada Swift Package, CocoaPods, atau pustaka pihak ketiga. Tidak ada SDK iklan, tidak ada SDK analitik (tidak ada Firebase atau semacamnya), tidak ada pelaporan crash, atribusi, atau pemasaran push.",
                "<b>Tidak ada pelacakan</b> — tidak ada IDFA, tidak ada permintaan App Tracking Transparency, tidak ada pelacakan lintas aplikasi atau lintas situs, tidak ada cookie pelacakan, sidik jari perangkat, atau pengenal lokal.",
                "<b>Kami tidak pernah menjual, membagikan, atau memperdagangkan data pengguna</b>, dan kami tidak terlibat dalam monetisasi data dalam bentuk apa pun. Tidak ada data yang digunakan untuk iklan atau pembuatan profil pengguna.",
                "<b>Selain memuat halaman kebijakan ini, setiap permintaan jaringan menuju layanan Apple</b> — sinkronisasi iCloud (CloudKit) dan Pembelian Dalam Aplikasi App Store (StoreKit). Keduanya diatur oleh kebijakan privasi Apple sendiri — lihat <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Kebijakan Privasi Apple</a>. (Entri \"Kebijakan Privasi\" dan \"Dukungan\" di dalam aplikasi terbuka di pembaca bawaan tanpa bilah alamat dan tidak pernah keluar dari aplikasi: hanya halaman ini yang dimuat, JavaScript dinonaktifkan, tidak ada cookie atau data penjelajahan yang ditulis, dan navigasi ke domain lain diblokir. Halaman ini dihosting di host statis pihak ketiga (GitHub Pages); memuatnya adalah satu-satunya permintaan jaringan aplikasi ke layanan non-Apple, dan tidak membawa pengenal akun atau perangkat.)",
            ]),
        ]),
        ("4. Privasi Anak di Bawah Umur", [
            ("p", "LearnNest adalah <b>alat manajemen untuk orang tua</b>, bukan aplikasi yang dibuat langsung untuk anak di bawah umur: semua konten dibuat dan dikelola oleh orang tua. Aplikasi ini <b>tidak menawarkan</b> obrolan, komentar, profil publik, penemuan atau rekomendasi konten, interaksi dengan orang asing, atau berbagi konten buatan pengguna secara publik."),
            ("ul", [
                "<b>Kami tidak mengumpulkan, menjual, atau mengungkapkan informasi pribadi anak di bawah umur kepada pihak ketiga.</b> Catatan belajar (nama panggilan, avatar, pelajaran, PR, kebiasaan, poin, dll.) dimasukkan oleh orang tua dan <b>hanya tersimpan di akun iCloud orang tua itu sendiri</b>; pengembang tidak memiliki akses.",
                "<b>Tidak ada konten buatan pengguna yang bersifat publik.</b> Teks yang dimasukkan orang tua hanya terlihat oleh anggota keluarga yang diundang <b>satu per satu</b> melalui berbagi pribadi iCloud (CKShare). Tidak ada audiens publik, tidak ada visibilitas orang asing, dan tidak ada mekanisme pencarian atau rekomendasi, sehingga aplikasi tidak memiliki risiko sosial yang terkait dengan konten publik.",
                "<b>Kontrol orang tua.</b> Aplikasi menyediakan \"Kunci Perangkat (PIN)\": setelah diaktifkan, fitur konfigurasi disembunyikan dan keluar memerlukan PIN; mengubah atau mengatur ulang PIN memerlukan autentikasi biometrik atau kode sandi sistem. Orang tua dapat menggunakannya untuk membatasi akses ke pengaturan dan pembelian.",
                "<b>Apple ID anak di bawah umur.</b> Jika orang tua membagikan ruang belajar dengan Apple ID anak di bawah umur, akun tersebut dibuat dan dikelola oleh orang tua di bawah aturan Apple; berbagi tetap di bawah kendali orang tua dan dapat dihentikan kapan saja.",
                "<b>Tentang persetujuan orang tua.</b> Karena aplikasi <b>sama sekali tidak mengumpulkan informasi pribadi anak di bawah umur</b>, mekanisme \"persetujuan orang tua yang dapat diverifikasi\" yang disyaratkan COPPA (AS), GDPR (ketentuan anak di bawah umur, UE), dan peraturan Tiongkok tentang perlindungan informasi pribadi anak di bawah umur secara online tidak berlaku, dan kami tidak perlu mengumpulkan informasi identitas orang tua untuk itu. Orang tua dapat menghapus ruang belajar apa pun beserta seluruh datanya kapan saja; penghapusan berlaku segera.",
                "Kami mengikuti Undang-Undang Perlindungan Informasi Pribadi Tiongkok dan peraturan Tiongkok tentang perlindungan informasi pribadi anak di bawah umur secara online, serta selaras dengan prinsip COPPA/GDPR: <b>minimisasi data, kontrol orang tua, tanpa berbagi, tanpa penjualan, dan tanpa iklan atau pembuatan profil</b>.",
                "Orang tua yang ingin meninjau, memperbaiki, atau menghapus secara permanen informasi di ruang belajar mereka dapat melakukannya di dalam aplikasi, atau mengirim email ke {mail} untuk bantuan.",
            ]),
        ]),
        ("5. Penyimpanan Data, Keamanan, dan Penghapusan", [
            ("ul", [
                "Semua data berada di akun iCloud Apple ID Anda, dilindungi enkripsi dan kontrol akses Apple. Kami tidak menyimpan salinan di sisi server.",
                "<b>Menghapus aplikasi tidak secara otomatis menghapus data iCloud</b> (sehingga Anda dapat memulihkannya di perangkat baru). Untuk menghapus semuanya: di iPhone/iPad buka <i>Pengaturan → Apple ID Anda → iCloud → Kelola Penyimpanan Akun → LearnNest → Hapus Data</i>; hapus ruang belajar terkait di dalam aplikasi di <i>Saya → Ruang Belajar</i>; atau kirim email ke {mail} untuk meminta bantuan penghapusan.",
                "Sejumlah kecil preferensi antarmuka (bahasa, pengaturan tampilan) disimpan <b>lokal di perangkat</b> (UserDefaults sistem). Itu tidak pernah keluar dari perangkat Anda dan tidak disinkronkan ke iCloud.",
                "Jaga keamanan Apple ID dan kode sandi perangkat Anda — itu adalah perlindungan utama untuk data ini.",
            ]),
        ]),
        ("6. Pembelian dan Pembayaran", [
            ("p", "LearnNest dapat diunduh gratis dengan uji coba lokal 7 hari. Versi lengkap adalah <b>pembelian sekali (non-consumable, bukan langganan; tanpa perpanjangan otomatis)</b>. Semua pembayaran diproses oleh Apple App Store (StoreKit). <b>Kami tidak pernah menerima atau menyimpan detail kartu pembayaran Anda</b>, dan tidak dapat melihat informasi akun lengkap Anda. Family Sharing diaktifkan, sehingga anggota keluarga tidak perlu membeli lagi."),
        ]),
        ("7. Perubahan Kebijakan Ini", [
            ("p", "Jika kebijakan ini berubah, kami akan memperbarui halaman ini dan merevisi \"Tanggal Berlaku\" di bagian atas. Perubahan material (misalnya, memperkenalkan pengumpulan data baru) juga akan diumumkan secara menonjol di dalam aplikasi. Silakan tinjau halaman ini secara berkala untuk versi terbaru."),
        ]),
        ("8. Hubungi Kami", [
            ("p", "Untuk pertanyaan, keluhan, atau permintaan penghapusan terkait kebijakan ini atau data Anda, kirim email ke <b>{mail}</b>. Kami biasanya membalas dalam <b>3 hari kerja</b>."),
        ]),
    ],
    "support_title": "Dukungan & FAQ",
    "support_rows": [
        ("Perangkat baru / sinkronisasi multi-perangkat", "Masuk dengan <b>Apple ID yang sama</b> di setiap perangkat dengan iCloud Drive aktif; data tersinkronisasi otomatis. Jika sinkronisasi macet, periksa <i>Pengaturan → Apple ID → iCloud</i>."),
        ("Berbagi keluarga / ruang belajar", "Gunakan \"Bagikan Ruang\" di aplikasi (Apple CloudKit CKShare); penerima menerima dengan Apple ID mereka sendiri. Dua Apple ID berbeda diperlukan untuk pengujian."),
        ("Pulihkan pembelian", "Ketuk \"Pulihkan Pembelian\" di bagian bawah paywall — tanpa biaya tambahan."),
        ("Hapus semua data", "Lihat bagian 5 di atas. Menghapus aplikasi tidak menghapus data iCloud."),
        ("Pindai teks (OCR)", "Berjalan sepenuhnya di perangkat melalui Apple Vision; tanpa unggahan, tanpa jaringan."),
        ("Bahasa yang didukung", "21 bahasa: Mandarin Sederhana & Tradisional, Inggris, Jepang, Korea, Spanyol, Portugis (BR), Prancis, Jerman, Italia, Belanda, Polandia, Swedia, Norwegia (Bokmål), Denmark, Indonesia, Melayu, Filipina, Turki, Vietnam, dan Rusia."),
        ("Persyaratan sistem", "iOS / iPadOS 17.0 atau lebih baru (iPhone dan iPad, termasuk widget layar utama)."),
        ("Kontak", "Email <b>{mail}</b> — balasan dalam 3 hari kerja."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["nb"] = {
    "html_lang": "nb",
    "title": "LearnNest Personvernerklæring & Support",
    "desc": "LearnNest personvernerklæring og support: vi samler ikke inn personopplysninger; alle data forblir i din egen iCloud.",
    "h1": "🎓 LearnNest Personvernerklæring & Support",
    "meta_line": "Ikrafttredelsesdato: {d} ｜ Utvikler: {dev} ｜ Kontakt: {mail}",
    "nav": ["Personvernerklæring", "Support & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kort fortalt:</b> LearnNest <b>samler ikke inn personopplysninger</b>. Ingen konto, ingen server og ingen tredjepartsanalyse eller reklame. Timeplan, lekser, vaner, påminnelser og poeng du legger inn, lagres <b>kun i din egen private iCloud-database</b> (Apple CloudKit); utvikleren kan ikke lese eller eksportere dem. En <b>enhetslås (PIN)</b> er tilgjengelig som foreldrekontroll, og alt læringsinnhold opprettes og styres av en forelder.",
    "privacy_title": "Personvernerklæring",
    "sections": [
        ("1. Oversikt", [
            ("p", "LearnNest er et studieorganiseringsverktøy for <b>foreldre</b>: timeplan, lekseoppfølging, vanesjekk, påminnelser og et poeng-/belønningssystem. Utviklet av en uavhengig utvikler ({dev}) med <b>ingen egen server og ingen backend-database</b>. Denne erklæringen forklarer hvordan vi håndterer – egentlig ikke håndterer – informasjonen din."),
        ]),
        ("2. Hva vi samler inn: ingenting", [
            ("p", "LearnNest <b>samler ikke inn personopplysninger</b>. Konkret:"),
            ("ul", [
                "<b>Ingen registrering, ingen innlogging.</b> Vi ber ikke om eller mottar navn, e-post, telefonnummer, kontakter, plassering, bilder eller andre identifikatorer.",
                "<b>Dataene dine forblir i din egen iCloud.</b> Timeplan, lekser, vaner, påminnelser, poeng og belønninger lagres i den private iCloud-databasen for din egen Apple-ID (Apple CloudKit, beholder <code>iCloud.com.frankzhou.KidLearn</code>). Dataene tilhører deg og oppbevares av Apple; <b>utvikleren kan ikke få tilgang til, lese eller eksportere dem</b>.",
                "<b>Familiendeling &amp; studierom.</b> Bygger på Apple CloudKit CKShare. Data deles kun med Apple-ID-er du eksplisitt inviterer (normalt familiemedlemmer); du styrer og kan trekke tilbake deling når som helst.",
            ]),
            ("p", "<b>Enhetsfunksjoner og systemtillatelser:</b>"),
            ("ul", [
                "<b>Varsler</b> – brukes utelukkende til å levere studiepåminnelser du selv har opprettet; intet reklame- eller markedsføringsinnhold. \"Fjernvarsler\" brukes kun som <b>lydløs utløser for iCloud-synkronisering</b> og viser aldri et synlig varsel.",
                "<b>Bilder (systemets bildevelger)</b> – leksjefunksjonen \"skann tekst (OCR)\" velger et bilde via Apples systembildeforvalger (PhotosPicker). Appen mottar <b>kun det enkelte bildet du velger</b>, kan ikke bla gjennom resten av biblioteket ditt og <b>krever ingen fotobibliotektillatelse</b>. Gjenkjenningen kjører <b>helt på enheten</b> via Apples Vision-rammeverk; verken bildet eller resultatet <b>lastes noen gang opp</b>, og originalbildet lagres ikke. <b>Appen bruker ikke kameraet og ber ikke om kameratillatelse.</b> Profilbilde til et studierom fungerer likt: bare det valgte bildet leses, komprimeres og <b>lagres utelukkende i din egen iCloud-konto</b> – aldri lastet opp til noen server.",
                "<b>Face ID / Touch ID / enhetskode</b> – brukes kun til å autentisere på denne enheten når en forelder endrer eller nullstiller PIN for enhetslåsen, eller slår av låsemodus. Autentiseringen utføres av iOS; <b>appen mottar, leser eller lagrer aldri biometriske data</b>.",
                "<b>Utklippstavle</b> – leses én gang, bare når du aktivt trykker \"Lim inn\", for å bygge en lekseliste. Teksten behandles <b>på enheten</b>; den <b>lastes aldri opp eller lagres</b>. Appen får ikke tilgang til utklippstavlen på noe annet tidspunkt.",
                "<b>Tillatelser vi aldri ber om</b> – ingen plassering, kontakter, kalender, påminnelser, mikrofon, kamera eller Appsporing. Utover ovenstående erklærer appen ingen andre tillatelser.",
            ]),
        ]),
        ("3. Tredjeparter, sporing og reklame: ingen", [
            ("ul", [
                "<b>Ingen tredjepartskode i det hele tatt</b> – prosjektet avhenger av ingen Swift Package, CocoaPods eller tredjepartsbibliotek. Ingen reklame-SDK, ingen analyse-SDK (ingen Firebase e.l.), ingen krasjrapportering, attribusjon eller push-markedsføring.",
                "<b>Ingen sporing</b> – ingen IDFA, ingen App Tracking Transparency-dialog, ingen sporing på tvers av apper eller sider, ingen sporingscookies, enhetsfingeravtrykk eller lokale identifikatorer.",
                "<b>Vi selger, deler eller handler aldri med brukerdata</b> og driver ingen form for datamonetisering. Ingen data brukes til reklame eller brukerprofilering.",
                "<b>Bortsett fra innlasting av denne erklæringssiden går alle nettverksforespørsler til Apple-tjenester</b> – iCloud (CloudKit)-synkronisering og App Store-kjøp (StoreKit). Begge reguleres av Apples egen personvernerklæring – se <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apples personvernerklæring</a>. (Appens innganger \"Personvernerklæring\" og \"Support\" åpnes i en innebygd leser uten adresselinje og forlater aldri appen: bare denne siden lastes, JavaScript er deaktivert, ingen cookies eller nettleserdata skrives, og navigasjon til andre domener blokkeres. Siden hostes på en tredjeparts statisk vert (GitHub Pages); innlasting av den er appens eneste nettverksforespørsel til en ikke-Apple-tjeneste og inneholder ingen konto- eller enhetsidentifikator.)",
            ]),
        ]),
        ("4. Mindres personvern", [
            ("p", "LearnNest er et <b>styringsverktøy for foreldre</b>, ikke en app laget direkte for mindreårige: alt innhold opprettes og styres av foreldre. Appen tilbyr <b>ingen</b> chat, kommentarer, offentlige profiler, innholdsoppdagelse eller anbefaling, kontakt med fremmede eller offentlig deling av brukerinnhold."),
            ("ul", [
                "<b>Vi samler ikke inn, selger eller utleverer mindreåriges personopplysninger til tredjepart.</b> Studieregistreringer (kallenavn, avatar, fag, lekser, vaner, poeng osv.) legges inn av foreldre og <b>lagres kun i forelderens egen iCloud-konto</b>; utvikleren har ingen tilgang.",
                "<b>Ingen offentlig brukerinnhold.</b> Tekst lagt inn av foreldre er kun synlig for familiemedlemmer som forelderen <b>inviterer én til én</b> via iCloud-privatdeling (CKShare). Det er ikke noe offentlig publikum, ingen fremmede kan se noe, og det finnes ingen søke- eller anbefalingsmekanisme, så appen har ingen av de sosiale risikoene ved offentlig brukerinnhold.",
                "<b>Foreldrekontroll.</b> Appen tilbyr en \"Enhetlås (PIN)\": når den er aktivert, skjules konfigurasjonsfunksjoner, og avslutning krever PIN; endring eller nullstilling krever systembiometri eller passkode. Foreldre kan bruke den til å begrense tilgang til innstillinger og kjøp.",
                "<b>Mindreåriges Apple-ID-er.</b> Hvis en forelder deler et studierom med en mindreårigs Apple-ID, opprettes og styres kontoen av forelderen etter Apples regler; deling forblir under forelderens kontroll og kan stoppes når som helst.",
                "<b>Om foreldresamtykke.</b> Fordi appen <b>ikke samler inn mindreåriges personopplysninger i det hele tatt</b>, gjelder ikke \"verifiserbart foreldresamtykke\"-mekanismene som kreves av COPPA (USA), GDPR (mindreåriges bestemmelser, EU) og Kinas regler om beskyttelse av mindreåriges personopplysninger på nett, og vi trenger ikke å samle inn foreldreidentitet til det formålet. Foreldre kan slette ethvert studierom og alle dets data når som helst; sletting trer i kraft umiddelbart.",
                "Vi følger Kinas lov om beskyttelse av personopplysninger og Kinas regler om beskyttelse av mindreåriges personopplysninger på nett, og er i samsvar med COPPA/GDPR-prinsippene: <b>dataminimering, foreldrekontroll, ingen deling, intet salg og ingen reklame eller profilering</b>.",
                "Foreldre som ønsker å se, rette eller permanent slette informasjon i studierommene sine, kan gjøre det i appen, eller sende e-post til {mail} for hjelp.",
            ]),
        ]),
        ("5. Datalagring, sikkerhet og sletting", [
            ("ul", [
                "Alle data ligger i iCloud-kontoen til Apple-ID-en din, beskyttet av Apples kryptering og tilgangskontroll. Vi oppbevarer ingen serverkopi.",
                "<b>Sletting av appen fjerner ikke automatisk iCloud-data</b> (så du kan gjenopprette på en ny enhet). For å slette alt: på iPhone/iPad gå til <i>Innstillinger → din Apple-ID → iCloud → Administrer lagring → LearnNest → Slett data</i>; slett det aktuelle studieromet i appen under <i>Mitt → Studierom</i>; eller send e-post til {mail} for slettehjelp.",
                "Et lite antall grensesnittinnstillinger (språk, visning) lagres <b>lokal på enheten</b> (systemets UserDefaults). De forlater aldri enheten din og synkroniseres ikke til iCloud.",
                "Beskytt Apple-ID-en og enhetskoden din – de er den viktigste beskyttelsen av disse dataene.",
            ]),
        ]),
        ("6. Kjøp og betalinger", [
            ("p", "LearnNest er gratis å laste ned med en lokal 7-dagers prøveperiode. Fullversjonen er et <b>engangskjøp (ikke-forbrukende, ikke-abonnement; ingen automatisk fornyelse)</b>. Alle betalinger behandles av Apple App Store (StoreKit). <b>Vi mottar eller lagrer aldri betalingskortopplysningene dine</b>, og kan ikke se full kontoinformasjon. Familiendeling er aktivert, så familiemedlemmer trenger ikke å kjøpe igjen."),
        ]),
        ("7. Endringer i denne erklæringen", [
            ("p", "Hvis denne erklæringen endres, oppdaterer vi denne siden og reviderer \"ikrafttredelsesdatoen\" øverst. Vesentlige endringer (for eksempel innføring av ny datainnsamling) kunngjøres også tydelig i appen. Se regelmessig på denne siden for den nyeste versjonen."),
        ]),
        ("8. Kontakt oss", [
            ("p", "Ved spørsmål, klager eller sletteforespørsel vedrørende denne erklæringen eller dataene dine: send e-post til <b>{mail}</b>. Vi svarer normalt innen <b>3 virkedager</b>."),
        ]),
    ],
    "support_title": "Support & FAQ",
    "support_rows": [
        ("Ny enhet / synkronisering mellom enheter", "Logg inn med <b>samme Apple-ID</b> på hver enhet med iCloud Drive aktivert; dataene synkroniseres automatisk. Hvis synkroniseringen stopper opp, sjekk <i>Innstillinger → Apple-ID → iCloud</i>."),
        ("Familie-/studieromsdeling", "Bruk \"Del rom\" i appen (Apple CloudKit CKShare); mottakeren godtar med sin egen Apple-ID. To forskjellige Apple-ID-er kreves for testing."),
        ("Gjenopprett kjøp", "Trykk \"Gjenopprett kjøp\" nederst i betalingsveggen – intet ekstra gebyr."),
        ("Slett alle data", "Se avsnitt 5 ovenfor. Sletting av appen fjerner ikke iCloud-data."),
        ("Skann tekst (OCR)", "Kjører helt på enheten via Apple Vision; ingen opplasting, ingen nettverk påkrevd."),
        ("Støttede språk", "21 språk: forenklet og tradisjonelt kinesisk, engelsk, japansk, koreansk, spansk, portugisisk (BR), fransk, tysk, italiensk, nederlandsk, polsk, svensk, norsk (bokmål), dansk, indonesisk, malayisk, filippinsk, tyrkisk, vietnamesisk og russisk."),
        ("Systemkrav", "iOS / iPadOS 17.0 eller nyere (iPhone og iPad, inkludert hjemskjerm-widgets)."),
        ("Kontakt", "Send e-post til <b>{mail}</b> – svar innen 3 virkedager."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["nl"] = {
    "html_lang": "nl",
    "title": "LearnNest Privacybeleid & Ondersteuning",
    "desc": "Privacybeleid en ondersteuning van LearnNest: we verzamelen geen persoonlijke gegevens; alle data blijven in je eigen iCloud.",
    "h1": "🎓 LearnNest Privacybeleid & Ondersteuning",
    "meta_line": "Ingangsdatum: {d} ｜ Ontwikkelaar: {dev} ｜ Contact: {mail}",
    "nav": ["Privacybeleid", "Ondersteuning & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kort gezegd:</b> LearnNest <b>verzamelt geen persoonlijke gegevens</b>. Er is geen account, geen server en geen third-party analytics of reclame. Roosters, huiswerk, gewoontes, herinneringen en punten die je invoert, worden <b>alleen opgeslagen in je eigen privé-iCloud-database</b> (Apple CloudKit); de ontwikkelaar kan ze niet lezen of exporteren. Een <b>apparaatslot (PIN)</b> is beschikbaar als ouderlijk toezicht, en alle leerinhoud wordt door een ouder aangemaakt en beheerd.",
    "privacy_title": "Privacybeleid",
    "sections": [
        ("1. Overzicht", [
            ("p", "LearnNest is een studiebeheertool voor <b>ouders</b>: roosters, huiswerkregistratie, gewoonte-afvinkingen, herinneringen en een punten/beloningsysteem. Gemaakt door een onafhankelijke ontwikkelaar ({dev}) met <b>geen eigen server en geen backend-database</b>. Dit beleid legt uit hoe wij omgaan — in feite: niet omgaan — met je informatie."),
        ]),
        ("2. Wat we verzamelen: niets", [
            ("p", "LearnNest <b>verzamelt geen persoonlijke gegevens</b>. Concreet:"),
            ("ul", [
                "<b>Geen registratie, geen login.</b> We vragen niet om en ontvangen geen naam, e-mail, telefoonnummer, contacten, locatie, foto's of andere identificatiegegevens.",
                "<b>Je data blijven in je eigen iCloud.</b> Roosters, huiswerk, gewoontes, herinneringen, punten en beloningen die je aanmaakt, worden opgeslagen in de privé-iCloud-database van je eigen Apple ID (Apple CloudKit, container <code>iCloud.com.frankzhou.KidLearn</code>). De data zijn van jou en worden bewaard door Apple; <b>de ontwikkelaar kan er niet bij, ze niet lezen of exporteren</b>.",
                "<b>Delen met familie &amp; studieruimtes.</b> Gebouwd op Apple CloudKit CKShare. Data worden alleen gedeeld met Apple ID's die je expliciet uitnodigt (normaal gezinsleden); jij beheert en kunt delen op elk moment intrekken.",
            ]),
            ("p", "<b>Apparaatfuncties en systeemrechten:</b>"),
            ("ul", [
                "<b>Meldingen</b> — uitsluitend om de studieherinneringen af te leveren die je zelf instelt; geen reclame- of marketinginhoud. \"Externe meldingen\" worden alleen gebruikt als <b>stille trigger voor iCloud-synchronisatie</b> en tonen nooit een zichtbare waarschuwing.",
                "<b>Foto's (systeemfotokiezer)</b> — de huiswerkfunctie \"tekst scannen (OCR)\" kiest een afbeelding via de systeemfotokiezer van Apple (PhotosPicker). De app ontvangt <b>alleen de ene afbeelding die je kiest</b>, kan de rest van je bibliotheek niet doorzoeken en <b>vereist geen fotobibliotheektoestemming</b>. De herkenning werkt <b>volledig op het apparaat</b> via Apple's Vision-framework; noch de afbeelding noch het resultaat wordt <b>ooit geüpload</b>, en het originele beeld wordt niet bewaard. <b>De app gebruikt de camera niet en vraagt geen cameratoestemming.</b> Een profielfoto voor een studieruimte werkt hetzelfde: alleen de gekozen afbeelding wordt gelezen, gecomprimeerd en <b>uitsluitend in je eigen iCloud-account opgeslagen</b> — nooit geüpload naar een server.",
                "<b>Face ID / Touch ID / apparaatcode</b> — alleen om je op dit apparaat te authenticeren wanneer een ouder de PIN van het apparaatslot wijzigt of herstelt, of de vergrendelmodus uitzet. De authenticatie wordt door iOS uitgevoerd; <b>de app ontvangt, leest of slaat nooit biometrische gegevens op</b>.",
                "<b>Klembord</b> — eenmaal gelezen, alleen als je zelf op \"Plakken\" tikt, om een huiswerklijst op te bouwen. De tekst wordt <b>op het apparaat</b> verwerkt; hij wordt <b>nooit geüpload of bewaard</b>. De app heeft op geen enkel ander moment toegang tot het klembord.",
                "<b>Rechten die we nooit vragen</b> — geen locatie, contacten, agenda, herinneringen, microfoon, camera of Apptrackingautorisatie. Naast het bovenstaande declareert de app geen andere rechten.",
            ]),
        ]),
        ("3. Derden, tracking en reclame: geen", [
            ("ul", [
                "<b>Helemaal geen third-party code</b> — het project is afhankelijk van geen enkel Swift Package, CocoaPods of third-party bibliotheek. Geen advertentie-SDK, geen analytics-SDK (geen Firebase e.d.), geen crashrapportage, attributie of pushmarketing.",
                "<b>Geen tracking</b> — geen IDFA, geen App Tracking Transparency-prompt, geen tracking over apps of sites heen, geen trackingcookies, apparaatvingerafdruk of lokale identificatoren.",
                "<b>We verkopen, delen of verhandelen nooit gebruikersgegevens</b> en doen geen enkele vorm van datamonetisatie. Geen data worden gebruikt voor reclame of gebruikersprofilering.",
                "<b>Afgezien van het laden van deze beleidspagina gaan alle netwerkverzoeken naar Apple-diensten</b> — iCloud (CloudKit)-synchronisatie en App Store-in-app-aankopen (StoreKit). Beide vallen onder het eigen privacybeleid van Apple — zie <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple Privacybeleid</a>. (De items \"Privacybeleid\" en \"Ondersteuning\" in de app openen in een ingebouwde lezer zonder adresbalk en verlaten nooit de app: alleen deze pagina wordt geladen, JavaScript is uitgeschakeld, er worden geen cookies of browsergegevens geschreven en navigatie naar andere domeinen wordt geblokkeerd. De pagina wordt gehost op een statische host van een derde partij (GitHub Pages); het laden ervan is het enige netwerkverzoek van de app naar een niet-Apple-dienst en bevat geen account- of apparaatidentificator.)",
            ]),
        ]),
        ("4. Privacy van minderjarigen", [
            ("p", "LearnNest is een <b>beheertool voor ouders</b>, geen app rechtstreeks voor minderjarigen: alle inhoud wordt door ouders aangemaakt en beheerd. De app biedt <b>geen</b> chat, reacties, openbare profielen, inhoudsontdekking of aanbeveling, contact met vreemden of openbaar delen van door gebruikers gegenereerde inhoud."),
            ("ul", [
                "<b>We verzamelen, verkopen of verstrekken geen persoonlijke gegevens van minderjarigen aan derden.</b> Studieregistraties (bijnaam, avatar, vakken, huiswerk, gewoontes, punten enz.) worden door ouders ingevoerd en <b>alleen opgeslagen in de eigen iCloud-account van de ouder</b>; de ontwikkelaar heeft er geen toegang toe.",
                "<b>Geen openbare gebruikersinhoud.</b> Door ouders ingevoerde tekst is alleen zichtbaar voor gezinsleden die de ouder <b>één-op-één uitnodigt</b> via privé delen van iCloud (CKShare). Er is geen publiek publiek, geen zichtbaarheid voor vreemden en geen zoek- of aanbevelingsmechanisme, dus de app heeft geen van de sociale risico's van openbare UGC.",
                "<b>Ouderlijk toezicht.</b> De app biedt een \"Apparaatslot (PIN)\": eenmaal ingeschakeld worden configuratiefuncties verborgen en vereist afsluiten de PIN; wijzigen of herstellen vereist systeem-biometrie of een code. Ouders kunnen het gebruiken om toegang tot instellingen en aankopen te beperken.",
                "<b>Apple ID's van minderjarigen.</b> Als een ouder een studieruimte deelt met het Apple ID van een minderjarige, wordt dat account door de ouder aangemaakt en beheerd volgens de regels van Apple; delen blijft onder controle van de ouder en kan op elk moment worden gestopt.",
                "<b>Over ouderlijke toestemming.</b> Omdat de app <b>helemaal geen persoonlijke gegevens van minderjarigen verzamelt</b>, zijn de \"verifieerbare ouderlijke toestemming\"-mechanismen die vereist zijn door COPPA (VS), GDPR (bepalingen voor minderjarigen, EU) en de Chinese regels voor bescherming van online persoonlijke gegevens van minderjarigen niet van toepassing, en hoeven we geen identiteitsgegevens van ouders te verzamelen. Ouders kunnen elke studieruimte met alle gegevens op elk moment verwijderen; verwijdering werkt onmiddellijk.",
                "We volgen de Chinese Personal Information Protection Law en de Chinese regels voor bescherming van online persoonlijke gegevens van minderjarigen, en sluiten aan bij COPPA/GDPR-principes: <b>databeperking, ouderlijk toezicht, geen delen, geen verkoop en geen reclame of profilering</b>.",
                "Ouders die informatie in hun studieruimtes willen inzien, corrigeren of permanent verwijderen, kunnen dat in de app doen of e-mailen naar {mail} voor hulp.",
            ]),
        ]),
        ("5. Gegevensopslag, beveiliging en verwijdering", [
            ("ul", [
                "Alle gegevens staan in de iCloud-account van je Apple ID, beschermd door Apples versleuteling en toegangscontrole. We bewaren geen serverkopie.",
                "<b>De app verwijderen verwijdert niet automatisch iCloud-gegevens</b> (zodat je op een nieuw apparaat kunt herstellen). Om alles te wissen: ga op iPhone/iPad naar <i>Instellingen → je Apple ID → iCloud → Accountopslag beheren → LearnNest → Verwijder data</i>; verwijder de betreffende studieruimte in de app onder <i>Ik → Studieruimtes</i>; of e-mail naar {mail} voor verwijderhulp.",
                "Een klein aantal voorkeuren (taal, weergave) wordt <b>lokaal op het apparaat</b> opgeslagen (systeem-UserDefaults). Ze verlaten nooit je apparaat en worden niet gesynchroniseerd met iCloud.",
                "Houd je Apple ID en apparaatcode veilig — dat is de belangrijkste bescherming van deze gegevens.",
            ]),
        ]),
        ("6. Aankopen en betalingen", [
            ("p", "LearnNest is gratis te downloaden met een lokale proefperiode van 7 dagen. De volledige versie is een <b>eenmalige aankoop (niet-consumerbaar, geen abonnement; geen automatische verlenging)</b>. Alle betalingen worden verwerkt door de Apple App Store (StoreKit). <b>We ontvangen of bewaren nooit je betaalkaartgegevens</b> en kunnen je volledige accountinformatie niet zien. Delen met familie is ingeschakeld, dus gezinsleden hoeven niet opnieuw te kopen."),
        ]),
        ("7. Wijzigingen in dit beleid", [
            ("p", "Als dit beleid verandert, werken we deze pagina bij en herzien we de \"ingangsdatum\" bovenaan. Wezenlijke wijzigingen (bijvoorbeeld het introduceren van nieuwe gegevensverzameling) worden ook prominent in de app aangekondigd. Bekijk deze pagina regelmatig voor de nieuwste versie."),
        ]),
        ("8. Contact opnemen", [
            ("p", "Voor vragen, klachten of een verzoek tot verwijdering over dit beleid of je gegevens: e-mail naar <b>{mail}</b>. Wij reageren normaal binnen <b>3 werkdagen</b>."),
        ]),
    ],
    "support_title": "Ondersteuning & FAQ",
    "support_rows": [
        ("Nieuw apparaat / synchroniseren tussen apparaten", "Meld aan met <b>hetzelfde Apple ID</b> op elk apparaat met iCloud Drive ingeschakeld; gegevens synchroniseren automatisch. Als de synchronisatie vastloopt, controleer <i>Instellingen → Apple ID → iCloud</i>."),
        ("Delen met familie / studieruimtes", "Gebruik \"Ruimte delen\" in de app (Apple CloudKit CKShare); de ontvanger accepteert met zijn eigen Apple ID. Er zijn twee verschillende Apple ID's nodig om te testen."),
        ("Aankopen herstellen", "Tik onderaan de betaalmuur op \"Aankopen herstellen\" — zonder extra kosten."),
        ("Alle gegevens verwijderen", "Zie paragraaf 5 hierboven. De app verwijderen verwijdert geen iCloud-gegevens."),
        ("Tekst scannen (OCR)", "Werkt volledig op het apparaat via Apple Vision; geen upload, geen netwerk nodig."),
        ("Ondersteunde talen", "21 talen: vereenvoudigd en traditioneel Chinees, Engels, Japans, Koreaans, Spaans, Portugees (BR), Frans, Duits, Italiaans, Nederlands, Pools, Zweeds, Noors (Bokmål), Deens, Indonesisch, Maleis, Filipijns, Turks, Vietnamees en Russisch."),
        ("Systeemvereisten", "iOS / iPadOS 17.0 of nieuwer (iPhone en iPad, inclusief startscherm-widgets)."),
        ("Kontakt", "E-mail naar <b>{mail}</b> — reactie binnen 3 werkdagen."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["pl"] = {
    "html_lang": "pl",
    "title": "LearnNest Polityka prywatności & Wsparcie",
    "desc": "Polityka prywatności i wsparcie LearnNest: nie zbieramy danych osobowych; wszystkie dane pozostają w Twoim własnym iCloud.",
    "h1": "🎓 LearnNest Polityka prywatności & Wsparcie",
    "meta_line": "Data wejścia w życie: {d} ｜ Deweloper: {dev} ｜ Kontakt: {mail}",
    "nav": ["Polityka prywatności", "Wsparcie & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>w skrócie:</b> LearnNest <b>nie zbiera żadnych danych osobowych</b>. Brak systemu kont, brak serwera, brak zewnętrznej analityki czy reklam. Plan lekcji, zadania, nawyki, przypomnienia i punkty, które wprowadzasz, są <b>przechowywane wyłącznie w Twojej prywatnej bazie iCloud</b> (Apple CloudKit); deweloper nie może ich czytać ani eksportować. <b>Blokada urządzenia (PIN)</b> służy jako kontrola rodzicielska, a cała treść edukacyjna jest tworzona i zarządzana przez rodzica.",
    "privacy_title": "Polityka prywatności",
    "sections": [
        ("1. Przegląd", [
            ("p", "LearnNest to narzędzie do organizacji nauki dla <b>rodziców</b>: plan lekcji, śledzenie zadań, odhaczanie nawyków, przypomnienia i system punktów/nagród. Stworzone przez niezależnego dewelopera ({dev}) — <b>bez własnego serwera i bez bazy danych backend</b>. Ta polityka wyjaśnia, jak obchodzimy się — a właściwie jak się nie obchodzimy — z Twoimi informacjami."),
        ]),
        ("2. Co zbieramy: nic", [
            ("p", "LearnNest <b>nie zbiera żadnych danych osobowych</b>. Konkretnie:"),
            ("ul", [
                "<b>Brak rejestracji, brak logowania.</b> Nie prosimy o ani nie otrzymujemy imienia i nazwiska, e-maila, numeru telefonu, kontaktów, lokalizacji, zdjęć ani żadnych identyfikatorów.",
                "<b>Twoje dane pozostają w Twoim własnym iCloud.</b> Plan lekcji, zadania, nawyki, przypomnienia, punkty i nagrody, które tworzysz, są przechowywane w prywatnej bazie iCloud Twojego własnego Apple ID (Apple CloudKit, kontener <code>iCloud.com.frankzhou.KidLearn</code>). Dane należą do Ciebie i przechowuje je Apple; <b>deweloper nie ma do nich dostępu, nie może ich czytać ani eksportować</b>.",
                "<b>Udostępnianie rodzinne &amp; przestrzenie nauki.</b> Oparte na Apple CloudKit CKShare. Dane są udostępniane tylko Apple ID, które wyraźnie zaprosisz (zwykle członkowie rodziny); Ty to kontrolujesz i możesz w każdej chwili cofnąć udostępnianie.",
            ]),
            ("p", "<b>Funkcje urządzenia i uprawnienia systemowe:</b>"),
            ("ul", [
                "<b>Powiadomienia</b> — wyłącznie do dostarczania przypomnień o nauce, które sam ustawisz; bez treści reklamowych i marketingowych. \"Powiadomienia zdalne\" służą tylko jako <b>cichy wyzwalacz synchronizacji iCloud</b> i nigdy nie wyświetlają widocznego alertu.",
                "<b>Zdjęcia (systemowa przeglądarka zdjęć)</b> — funkcja \"zeskanuj tekst (OCR)\" zadań wybiera obraz przez systemową przeglądarkę zdjęć Apple (PhotosPicker). Aplikacja otrzymuje <b>tylko ten jeden obraz, który wybierzesz</b>, nie może przeglądać reszty Twojej biblioteki i <b>nie wymaga uprawnienia do biblioteki zdjęć</b>. Rozpoznawanie działa <b>w całości na urządzeniu</b> za pomocą frameworka Apple Vision; ani obraz, ani wynik <b>nigdy nie są wysyłane</b>, a oryginalny obraz nie jest przechowywany. <b>Aplikacja nie używa aparatu i nie prosi o uprawnienie do aparatu.</b> Zdjęcie profilowe przestrzeni nauki działa tak samo: czytany jest tylko wybrany obraz, kompresowany i <b>przechowywany wyłącznie w Twoim własnym koncie iCloud</b> — nigdy wysyłany na żaden serwer.",
                "<b>Face ID / Touch ID / kod urządzenia</b> — tylko do uwierzytelnienia na tym urządzeniu, gdy rodzic zmienia lub resetuje PIN blokady urządzenia albo wyłącza tryb blokady. Uwierzytelnienie wykonuje iOS; <b>aplikacja nigdy nie otrzymuje, nie czyta i nie przechowuje danych biometrycznych</b>.",
                "<b>Schowek</b> — odczytywany raz, tylko gdy sam tapniesz \"Wklej\", aby zbudować listę zadań. Tekst jest przetwarzany <b>na urządzeniu</b>; <b>nigdy nie jest wysyłany ani przechowywany</b>. Aplikacja nie sięga do schowka w żadnym innym momencie.",
                "<b>Uprawnienia, o które nigdy nie prosimy</b> — brak lokalizacji, kontaktów, kalendarza, przypomnień, mikrofonu, aparatu ani autoryzacji śledzenia aplikacji. Poza powyższym aplikacja nie deklaruje innych uprawnień.",
            ]),
        ]),
        ("3. Strony trzecie, śledzenie i reklamy: brak", [
            ("ul", [
                "<b>Żadnego kodu stron trzecich</b> — projekt nie zależy od żadnego Swift Package, CocoaPods ani biblioteki zewnętrznej. Brak SDK reklam, brak SDK analityki (brak Firebase i podobnych), brak raportowania awarii, atrybucji czy marketingu push.",
                "<b>Brak śledzenia</b> — bez IDFA, bez monitu App Tracking Transparency, bez śledzenia między aplikacjami ani stronami, bez ciasteczek śledzących, odcisku palca urządzenia czy lokalnych identyfikatorów.",
                "<b>Nigdy nie sprzedajemy, nie udostępniamy i nie handlujemy danymi użytkowników</b> i nie uczestniczymy w żadnej monetyzacji danych. Żadne dane nie są używane do reklam ani profilowania użytkowników.",
                "<b>Poza załadowaniem tej strony polityki każde żądanie sieciowe kierowane jest do usług Apple</b> — synchronizacja iCloud (CloudKit) i zakupy w aplikacji App Store (StoreKit). Obie reguluje własna polityka prywatności Apple — zobacz <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Politykę prywatności Apple</a>. (Pozycje \"Polityka prywatności\" i \"Wsparcie\" w aplikacji otwierają się w wbudowanej przeglądarce bez paska adresu i nigdy nie opuszczają aplikacji: ładowana jest tylko ta strona, JavaScript jest wyłączony, nie zapisują się cookies ani dane przeglądania, a nawigacja do innych domen jest zablokowana. Strona jest hostowana na zewnętrznym hostingu statycznym (GitHub Pages); jej załadowanie to jedyne żądanie sieciowe aplikacji do usługi innej niż Apple i nie zawiera identyfikatora konta ani urządzenia.)",
            ]),
        ]),
        ("4. Prywatność małoletnich", [
            ("p", "LearnNest to <b>narzędzie zarządzania dla rodziców</b>, a nie aplikacja stworzona bezpośrednio dla małoletnich: cała treść jest tworzona i zarządzana przez rodziców. Aplikacja nie oferuje <b>żadnego</b> czatu, komentarzy, publicznych profili, odkrywania ani rekomendacji treści, kontaktu z nieznajomymi ani publicznego udostępniania treści tworzonych przez użytkowników."),
            ("ul", [
                "<b>Nie zbieramy, nie sprzedajemy i nie ujawniamy nikomu danych osobowych małoletnich.</b> Zapisky nauki (pseudonim, awatar, przedmioty, zadania, nawyki, punkty itd.) wprowadzają rodzice i są <b>przechowywane wyłącznie we własnym koncie iCloud rodzica</b>; deweloper nie ma do nich dostępu.",
                "<b>Brak publicznych treści od użytkowników.</b> Tekst wprowadzony przez rodzica jest widoczny tylko dla członków rodziny, których rodzic <b>zaprasza jeden na jeden</b> przez prywatne udostępnianie iCloud (CKShare). Nie ma publicznej widowni, brak widoczności dla nieznajomych ani mechanizmu wyszukiwania czy rekomendacji, więc aplikacja nie niesie żadnych ryzyk społecznych związanych z publicznym UGC.",
                "<b>Kontrola rodzicielska.</b> Aplikacja oferuje \"Blokadę urządzenia (PIN)\": po włączeniu funkcje konfiguracji są ukryte, a wyjście wymaga PIN-u; zmiana lub reset wymaga biometrii systemowej lub kodu. Rodzice mogą nią ograniczyć dostęp do ustawień i zakupów.",
                "<b>Apple ID małoletnich.</b> Jeśli rodzic udostępni przestrzeń nauki Apple ID małoletniego, to konto jest tworzone i zarządzane przez rodzica według zasad Apple; udostępnianie pozostaje pod kontrolą rodzica i może być w każdej chwili zatrzymane.",
                "<b>O zgodzie rodzicielskiej.</b> Ponieważ aplikacja <b>w ogóle nie zbiera danych osobowych małoletnich</b>, mechanizmy \"weryfikowalnej zgody rodzicielskiej\" wymagane przez COPPA (USA), RODO (przepisy o małoletnich, UE) oraz chińskie przepisy o ochronie danych osobowych małoletnich w internecie nie mają zastosowania, a my nie musimy zbierać żadnych danych tożsamości rodzica w tym celu. Rodzice mogą w każdej chwili usunąć dowolną przestrzeń nauki i wszystkie jej dane; usunięcie działa natychmiast.",
                "Stosujemy chińską ustawę o ochronie danych osobowych i chińskie przepisy o ochronie danych osobowych małoletnich w internecie oraz jesteśmy zgodni z zasadami COPPA/RODO: <b>minimalizacja danych, kontrola rodzicielska, brak udostępniania, brak sprzedaży oraz brak reklam i profilowania</b>.",
                "Rodzice, którzy chcą przejrzeć, poprawić lub trwale usunąć informacje w swoich przestrzeniach nauki, mogą to zrobić w aplikacji lub napisać na {mail} po pomoc.",
            ]),
        ]),
        ("5. Przechowywanie danych, bezpieczeństwo i usuwanie", [
            ("ul", [
                "Wszystkie dane znajdują się w koncie iCloud Twojego Apple ID, chronione szyfrowaniem i kontrolą dostępu Apple. Nie przechowujemy kopii na serwerze.",
                "<b>Usunięcie aplikacji nie usuwa automatycznie danych iCloud</b> (dzięki temu możesz je przywrócić na nowym urządzeniu). Aby usunąć wszystko: na iPhone/iPad przejdź do <i>Ustawienia → Twoje Apple ID → iCloud → Zarządzaj miejscem → LearnNest → Usuń dane</i>; usuń daną przestrzeń nauki w aplikacji w <i>Ja → Przestrzenie nauki</i>; lub napisz na {mail} z prośbą o pomoc w usunięciu.",
                "Niewielka liczba preferencji interfejsu (język, ustawienia wyświetlania) jest przechowywana <b>lokalnie na urządzeniu</b> (systemowe UserDefaults). Nigdy nie opuszczają Twojego urządzenia i nie są synchronizowane z iCloud.",
                "Dbaj o bezpieczeństwo swojego Apple ID i kodu urządzenia — to podstawowa ochrona tych danych.",
            ]),
        ]),
        ("6. Zakupy i płatności", [
            ("p", "LearnNest jest darmowy do pobrania z lokalnym 7-dniowym okresem próbnym. Pełna wersja to <b>jednorazowy zakup (niekonsumowalny, bez subskrypcji; bez automatycznego odnawiania)</b>. Wszystkie płatności obsługuje Apple App Store (StoreKit). <b>Nigdy nie otrzymujemy ani nie przechowujemy danych Twojej karty płatniczej</b> i nie widzimy pełnych informacji o Twoim koncie. Udostępnianie rodzinne jest włączone, więc członkowie rodziny nie muszą kupować ponownie."),
        ]),
        ("7. Zmiany tej polityki", [
            ("p", "Jeśli ta polityka się zmieni, zaktualizujemy tę stronę i zrewidujemy \"datę wejścia w życie\" na górze. Istotne zmiany (na przykład wprowadzenie nowego zbierania danych) ogłosimy też wyraźnie w aplikacji. Sprawdzaj tę stronę okresowo, aby zobaczyć najnowszą wersję."),
        ]),
        ("8. Skontaktuj się z nami", [
            ("p", "W sprawie pytań, skarg lub próśb o usunięcie dotyczących tej polityki lub Twoich danych napisz na <b>{mail}</b>. Zwykle odpowiadamy w ciągu <b>3 dni roboczych</b>."),
        ]),
    ],
    "support_title": "Wsparcie & FAQ",
    "support_rows": [
        ("Nowe urządzenie / synchronizacja między urządzeniami", "Zaloguj się <b>tym samym Apple ID</b> na każdym urządzeniu z włączonym iCloud Drive; dane synchronizują się automatycznie. Jeśli synchronizacja utknie, sprawdź <i>Ustawienia → Apple ID → iCloud</i>."),
        ("Udostępnianie rodzinie / przestrzeni nauki", "Użyj \"Udostępnij przestrzeń\" w aplikacji (Apple CloudKit CKShare); odbiorca akceptuje własnym Apple ID. Do testowania potrzeba dwóch różnych Apple ID."),
        ("Przywróć zakupy", "Tapnij \"Przywróć zakupy\" na dole paywalla — bez dodatkowych opłat."),
        ("Usuń wszystkie dane", "Zobacz sekcję 5 powyżej. Usunięcie aplikacji nie usuwa danych iCloud."),
        ("Skanuj tekst (OCR)", "Działa w całości na urządzeniu przez Apple Vision; bez wysyłania, bez sieci."),
        ("Obsługiwane języki", "21 języków: chiński uproszczony i tradycyjny, angielski, japoński, koreański, hiszpański, portugalski (BR), francuski, niemiecki, włoski, niderlandzki, polski, szwedzki, norweski (bokmål), duński, indonezyjski, malajski, filipiński, turecki, wietnamski i rosyjski."),
        ("Wymagania systemowe", "iOS / iPadOS 17.0 lub nowszy (iPhone i iPad, w tym widżety ekranu głównego)."),
        ("Kontakt", "Napisz na <b>{mail}</b> — odpowiadamy w ciągu 3 dni roboczych."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["sv"] = {
    "html_lang": "sv",
    "title": "LearnNest Integritetspolicy & Support",
    "desc": "LearnNests integritetspolicy och support: vi samlar inte in personuppgifter; alla data finns kvar i ditt eget iCloud.",
    "h1": "🎓 LearnNest Integritetspolicy & Support",
    "meta_line": "Ikraftträdandedatum: {d} ｜ Utvecklare: {dev} ｜ Kontakt: {mail}",
    "nav": ["Integritetspolicy", "Support & FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kort sagt:</b> LearnNest <b>samlar inte in några personuppgifter</b>. Inget kontosystem, ingen server och ingen tredjepartsanalys eller reklam. Schema, läxor, vanor, påminnelser och poeng som du anger lagras <b>endast i din egen privata iCloud-databas</b> (Apple CloudKit); utvecklaren kan inte läsa eller exportera dem. Ett <b>enhetslås (PIN-kod)</b> finns som föräldrakontroll, och allt lärande innehåll skapas och hanteras av en förälder.",
    "privacy_title": "Integritetspolicy",
    "sections": [
        ("1. Översikt", [
            ("p", "LearnNest är ett studieorganiseringsverktyg för <b>föräldrar</b>: schema, läxhantering, vanor, påminnelser och ett poäng-/belöningssystem. Utvecklat av en oberoende utvecklare ({dev}) — <b>utan egen server och utan backend-databas</b>. Denna policy förklarar hur vi hanterar — egentligen inte hanterar — din information."),
        ]),
        ("2. Vad vi samlar in: ingenting", [
            ("p", "LearnNest <b>samlar inte in några personuppgifter</b>. Konkret:"),
            ("ul", [
                "<b>Ingen registrering, ingen inloggning.</b> Vi begär inte och tar inte emot namn, e-post, telefonnummer, kontakter, plats, bilder eller andra identifierare.",
                "<b>Dina data finns kvar i ditt eget iCloud.</b> Schema, läxor, vanor, påminnelser, poäng och belöningar du skapar lagras i den privata iCloud-databasen för ditt eget Apple-ID (Apple CloudKit, container <code>iCloud.com.frankzhou.KidLearn</code>). Data tillhör dig och hålls av Apple; <b>utvecklaren kan inte komma åt, läsa eller exportera dem</b>.",
                "<b>Familjedelning &amp; studierum.</b> Bygger på Apple CloudKit CKShare. Data delas endast med Apple-ID:n du uttryckligen bjuder in (normalt familjemedlemmar); du styr och kan återkalla delning när som helst.",
            ]),
            ("p", "<b>Enhetsfunktioner och systembehörigheter:</b>"),
            ("ul", [
                "<b>Notiser</b> — enbart för att leverera de studiepåminnelser du själv skapat; inget reklam- eller marknadsföringsinnehåll. \"Fjärrnotiser\" används endast som <b>tyst utlösare för iCloud-synk</b> och visar aldrig en synlig varning.",
                "<b>Bilder (systemets bildväljare)</b> — läxfunktionen \"skanna text (OCR)\" väljer en bild via Apples systembildväljare (PhotosPicker). Appen tar <b>endast emot den enskilda bild du väljer</b>, kan inte bläddra i resten av ditt bibliotek och <b>kräver inget fotobibliotekstillstånd</b>. Igenkänningen körs <b>helt på enheten</b> via Apples Vision-ramverk; varken bilden eller resultatet <b>laddas någonsin upp</b>, och originalbilden sparas inte. <b>Appen använder inte kameran och begär inte kameratillstånd.</b> Profilbild för ett studierum fungerar likadant: endast den valda bilden läses, komprimeras och <b>lagras uteslutande i ditt eget iCloud-konto</b> — aldrig uppladdad till någon server.",
                "<b>Face ID / Touch ID / enhetskod</b> — endast för att autentisera på denna enhet när en förälder ändrar eller återställer PIN-koden för enhetslåset, eller stänger av låsläget. Autentiseringen utförs av iOS; <b>appen tar aldrig emot, läser eller lagrar biometrisk data</b>.",
                "<b>Urklipp</b> — läses en gång, endast när du själv trycker \"Klistra in\", för att bygga en läxlista. Texten bearbetas <b>på enheten</b>; den <b>laddas aldrig upp eller sparas</b>. Appen använder inte urklipp vid något annat tillfälle.",
                "<b>Behörigheter vi aldrig begär</b> — ingen plats, kontakter, kalender, påminnelser, mikrofon, kamera eller Appspårning. Utöver ovanstående deklarerar appen inga andra behörigheter.",
            ]),
        ]),
        ("3. Tredje part, spårning och reklam: ingen", [
            ("ul", [
                "<b>Ingen tredjepartskod alls</b> — projektet beror på inget Swift Package, CocoaPods eller tredjepartsbibliotek. Ingen reklam-SDK, ingen analys-SDK (ingen Firebase e.d.), ingen kraschrapportering, attribuering eller push-marknadsföring.",
                "<b>Ingen spårning</b> — ingen IDFA, ingen App Tracking Transparency-prompt, ingen spårning över appar eller webbplatser, inga spårcookies, enhetsfingeravtryck eller lokala identifierare.",
                "<b>Vi säljer, delar eller handlar aldrig med användardata</b> och deltar inte i någon form av datamonetarisering. Ingen data används för reklam eller användarprofilering.",
                "<b>Förutom inläsning av denna policysida går alla nätverksförfrågningar till Apples tjänster</b> — iCloud (CloudKit)-synk och App Store-köp (StoreKit). Båda regleras av Apples egen integritetspolicy — se <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apples integritetspolicy</a>. (Appens poster \"Integritetspolicy\" och \"Support\" öppnas i en inbyggd läsare utan adressfält och lämnar aldrig appen: endast denna sida läses in, JavaScript är avstängt, inga cookies eller webbdata skrivs och navigering till andra domäner blockeras. Sidan hostas på en tredjeparts statisk värd (GitHub Pages); inläsning av den är appens enda nätverksförfrågan till en icke-Apple-tjänst och innehåller ingen konto- eller enhetsidentifierare.)",
            ]),
        ]),
        ("4. Mindreårigas integritet", [
            ("p", "LearnNest är ett <b>hanteringsverktyg för föräldrar</b>, inte en app gjord direkt för minderåriga: allt innehåll skapas och hanteras av föräldrar. Appen erbjuder <b>ingen</b> chatt, kommentarer, offentliga profiler, innehållsutforskning eller rekommendation, kontakt med främlingar eller offentlig delning av användarskapat innehåll."),
            ("ul", [
                "<b>Vi samlar inte in, säljer eller utlämnar minderårigas personuppgifter till tredje part.</b> Studieregistreringar (smeknamn, avatar, ämnen, läxor, vanor, poäng osv.) anges av föräldrar och <b>lagras endast i förälderns eget iCloud-konto</b>; utvecklaren har ingen åtkomst.",
                "<b>Inget offentligt användarskapat innehåll.</b> Text som anges av föräldrar är endast synlig för familjemedlemmar som föräldern <b>bjuder in en-till-en</b> via privat iCloud-delning (CKShare). Det finns ingen offentlig publik, ingen synlighet för främlingar och ingen sök- eller rekommendationsmekanism, så appen bär ingen av de sociala riskerna med offentligt innehåll.",
                "<b>Föräldrakontroll.</b> Appen erbjuder ett \"Enhetslås (PIN-kod)\": när det är aktiverat döljs konfigurationsfunktioner och utgång kräver PIN-koden; ändring eller återställning kräver systembiometri eller kod. Föräldrar kan använda det för att begränsa åtkomst till inställningar och köp.",
                "<b>Minderårigas Apple-ID:n.</b> Om en förälder delar ett studierum med en minderårigs Apple-ID skapas och hanteras det kontot av föräldern enligt Apples regler; delningen förblir under förälderns kontroll och kan stoppas när som helst.",
                "<b>Om föräldrasamtycke.</b> Eftersom appen <b>inte samlar in några personuppgifter om minderåriga alls</b> gäller inte de \"verifierbara föräldrasamtycke\"-mekanismer som krävs av COPPA (USA), GDPR (bestämmelser om minderåriga, EU) och Kinas regler om skydd av minderårigas personuppgifter online, och vi behöver inte samla in någon förälders identitetsinformation för det ändamålet. Föräldrar kan när som helst radera vilket studierum som helst med alla dess data; raderingen träder i kraft omedelbart.",
                "Vi följer Kinas lag om skydd av personuppgifter och Kinas regler om skydd av minderårigas personuppgifter online, och stämmer överens med COPPA/GDPR-principerna: <b>dataminimering, föräldrakontroll, ingen delning, ingen försäljning samt ingen reklam eller profilering</b>.",
                "Föräldrar som vill granska, korrigera eller permanent radera information i sina studierum kan göra det i appen, eller mejla till {mail} för hjälp.",
            ]),
        ]),
        ("5. Datalagring, säkerhet och radering", [
            ("ul", [
                "Alla data finns i iCloud-kontot för ditt Apple-ID, skyddade av Apples kryptering och åtkomstkontroll. Vi sparar ingen serverkopia.",
                "<b>Att radera appen tar inte automatiskt bort iCloud-data</b> (så att du kan återställa på en ny enhet). För att radera allt: på iPhone/iPad gå till <i>Inställningar → ditt Apple-ID → iCloud → Hantera lagring → LearnNest → Radera data</i>; radera aktuellt studierum i appen under <i>Jag → Studierum</i>; eller mejla till {mail} för raderingshjälp.",
                "Ett litet antal gränssnittsinställningar (språk, visning) lagras <b>lokalt på enheten</b> (systemets UserDefaults). De lämnar aldrig din enhet och synkas inte till iCloud.",
                "Håll ditt Apple-ID och din enhetskod säkra — de är det viktigaste skyddet för dessa data.",
            ]),
        ]),
        ("6. Köp och betalningar", [
            ("p", "LearnNest är gratis att ladda ner med en lokal 7-dagars provperiod. Fullversionen är ett <b>engångsköp (icke-konsumerbart, ingen prenumeration; ingen automatisk förnyelse)</b>. Alla betalningar hanteras av Apple App Store (StoreKit). <b>Vi tar aldrig emot eller sparar dina betalkortsuppgifter</b> och kan inte se fullständig kontoinformation. Familjedelning är aktiverat, så familjemedlemmer behöver inte köpa igen."),
        ]),
        ("7. Ändringar av denna policy", [
            ("p", "Om denna policy ändras uppdaterar vi denna sida och reviderar \"ikraftträdandedatum\" högst upp. Väsentliga ändringar (till exempel införande av ny datainsamling) meddelas även tydligt i appen. Se regelbundet över denna sida för den senaste versionen."),
        ]),
        ("8. Kontakta oss", [
            ("p", "Frågor, klagomål eller begäran om radering gällande denna policy eller dina data: mejla till <b>{mail}</b>. Vi svarar normalt inom <b>3 arbetsdagar</b>."),
        ]),
    ],
    "support_title": "Support & FAQ",
    "support_rows": [
        ("Ny enhet / synk mellan enheter", "Logga in med <b>samma Apple-ID</b> på varje enhet med iCloud Drive aktiverat; data synkas automatiskt. Om synken fastnar, kontrollera <i>Inställningar → Apple-ID → iCloud</i>."),
        ("Familje-/studierumsdelning", "Använd \"Dela rum\" i appen (Apple CloudKit CKShare); mottagaren accepterar med sitt eget Apple-ID. Två olika Apple-ID:n krävs för test."),
        ("Återställ köp", "Tryck \"Återställ köp\" längst ner i betalningsmuren — utan extra avgift."),
        ("Radera all data", "Se avsnitt 5 ovan. Att radera appen tar inte bort iCloud-data."),
        ("Skanna text (OCR)", "Körs helt på enheten via Apple Vision; ingen uppladdning, inget nätverk krävs."),
        ("Stödda språk", "21 språk: förenklad och traditionell kinesiska, engelska, japanska, koreanska, spanska, portugisiska (BR), franska, tyska, italienska, nederländska, polska, svenska, norska (bokmål), danska, indonesiska, malajiska, filippinska, turkiska, vietnamesiska och ryska."),
        ("Systemkrav", "iOS / iPadOS 17.0 eller senare (iPhone och iPad, inklusive hemskärmswidgets)."),
        ("Kontakt", "Mejla till <b>{mail}</b> — svar inom 3 arbetsdagar."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["it"] = {
    "html_lang": "it",
    "title": "LearnNest Informativa sulla privacy e supporto",
    "desc": "Informativa sulla privacy e supporto di LearnNest: non raccogliamo dati personali; tutti i dati restano nel tuo iCloud.",
    "h1": "🎓 LearnNest Informativa sulla privacy e supporto",
    "meta_line": "Data di entrata in vigore: {d} ｜ Sviluppatore: {dev} ｜ Contatto: {mail}",
    "nav": ["Informativa sulla privacy", "Supporto e FAQ"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>In breve:</b> LearnNest <b>non raccoglie alcun dato personale</b>. Nessun sistema di account, nessun server e nessuna analisi o pubblicità di terze parti. Orario, compiti, abitudini, promemoria e punti inseriti vengono archiviati <b>solo nel tuo database iCloud privato</b> (Apple CloudKit); lo sviluppatore non può leggerli né esportarli. È disponibile un <b>blocco dispositivo (codice PIN)</b> come controllo genitori e tutti i contenuti didattici sono creati e gestiti da un genitore.",
    "privacy_title": "Informativa sulla privacy",
    "sections": [
        ("1. Panoramica", [
            ("p", "LearnNest è uno strumento di organizzazione dello studio per <b>genitori</b>: orario scolastico, gestione dei compiti, abitudini, promemoria e un sistema di punti/ricompense. Sviluppato da uno sviluppatore indipendente ({dev}) — <b>senza server proprio e senza database backend</b>. Questa informativa spiega come gestiamo — o più precisamente non gestiamo — le tue informazioni."),
        ]),
        ("2. Cosa raccogliamo: niente", [
            ("p", "LearnNest <b>non raccoglie alcun dato personale</b>. In concreto:"),
            ("ul", [
                "<b>Nessuna registrazione, nessun accesso.</b> Non richiediamo né riceviamo nomi, e-mail, numeri di telefono, contatti, posizione, foto o altri identificatori.",
                "<b>I tuoi dati restano nel tuo iCloud.</b> Orario, compiti, abitudini, promemoria, punti e ricompense creati vengono archiviati nel database iCloud privato del tuo Apple ID (Apple CloudKit, contenitore <code>iCloud.com.frankzhou.KidLearn</code>). I dati appartengono a te e sono custoditi da Apple; <b>lo sviluppatore non può accedervi, leggerli né esportarli</b>.",
                "<b>Condivisione familiare e studio in gruppo.</b> Basata su Apple CloudKit CKShare. I dati sono condivisi solo con gli Apple ID che invit esplicitamente (di norma familiari); ne mantieni il controllo e puoi revocare la condivisione in qualsiasi momento.",
            ]),
            ("p", "<b>Funzioni del dispositivo e permessi di sistema:</b>"),
            ("ul", [
                "<b>Notifiche</b> — solo per recapitare i promemoria di studio creati da te; nessun contenuto pubblicitario o promozionale. Le \"notifiche remote\" sono usate solo come <b>trigger silenzioso per la sincronizzazione iCloud</b> e non mostrano mai un avviso visibile.",
                "<b>Foto (selettore di sistema)</b> — la funzione compiti \"scansione testo (OCR)\" sceglie un'immagine tramite il selettore foto di sistema di Apple (PhotosPicker). L'app <b>riceve solo l'immagine che selezioni</b>, non può sfogliare il resto della tua libreria e <b>non richiede l'autorizzazione alla libreria foto</b>. Il riconoscimento avviene <b>completamente sul dispositivo</b> tramite il framework Vision di Apple; né l'immagine né il risultato vengono <b>mai caricati</b> e l'immagine originale non viene salvata. <b>L'app non usa la fotocamera e non richiede l'autorizzazione alla fotocamera.</b> La foto profilo di un gruppo di studio funziona allo stesso modo: viene letta e compressa solo l'immagine scelta e <b>archiviata esclusivamente nel tuo account iCloud</b> — mai caricata su un server.",
                "<b>Face ID / Touch ID / codice dispositivo</b> — solo per autenticarti su questo dispositivo quando un genitore modifica o reimposta il PIN del blocco dispositivo o disattiva il blocco. L'autenticazione è eseguita da iOS; <b>l'app non riceve, legge o archivia mai dati biometrici</b>.",
                "<b>Appunti</b> — letti una sola volta, solo quando premi \"Incolla\", per creare un elenco di compiti. Il testo è elaborato <b>sul dispositivo</b>; <b>non viene mai caricato o salvato</b>. L'app non usa gli appunti in nessun altro momento.",
                "<b>Autorizzazioni che non richiediamo mai</b> — posizione, contatti, calendario, promemoria, microfono, fotocamera o tracciamento delle app. Oltre a quanto sopra, l'app non dichiara altri permessi.",
            ]),
        ]),
        ("3. Terze parti, tracciamento e pubblicità: nessuno", [
            ("ul", [
                "<b>Nessun codice di terze parti</b> — il progetto non dipende da alcun Swift Package, CocoaPods o libreria di terze parti. Nessun SDK pubblicitario, nessun SDK di analisi (nessun Firebase o simile), nessuna segnalazione di arresti anomali, attribuzione o push marketing.",
                "<b>Nessun tracciamento</b> — nessun IDFA, nessuna richiesta App Tracking Transparency, nessun tracciamento tra app o siti web, nessun cookie di tracciamento, fingerprinting o identificatore locale.",
                "<b>Non vendiamo, condividiamo né scambiamo dati degli utenti</b> e non partecipiamo a alcuna forma di monetizzazione dei dati. Nessun dato è usato per pubblicità o profilazione degli utenti.",
                "<b>A parte il caricamento di questa pagina informativa, tutte le richieste di rete vanno ai servizi di Apple</b> — sincronizzazione iCloud (CloudKit) e acquisti App Store (StoreKit). Entrambi sono regolati dall'informativa sulla privacy di Apple — vedi <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">l'informativa sulla privacy di Apple</a>. (Le voci dell'app \"Informativa sulla privacy\" e \"Supporto\" si aprono in un lettore integrato senza barra degli indirizzi e non escono mai dall'app: viene caricata solo questa pagina, JavaScript è disattivato, non vengono scritti cookie o dati web e la navigazione verso altri domini è bloccata. La pagina è ospitata su un servizio di hosting statico di terze parti (GitHub Pages); il suo caricamento è l'unica richiesta di rete dell'app verso un servizio non Apple e non contiene identificatori di account o dispositivo.)",
            ]),
        ]),
        ("4. Privacy dei minori", [
            ("p", "LearnNest è uno <b>strumento di gestione per genitori</b>, non un'app pensata direttamente per i minori: tutti i contenuti sono creati e gestiti dai genitori. L'app non offre <b>nessuna</b> chat, commenti, profili pubblici, esplorazione o raccomandazione di contenuti, contatti con estranei o condivisione pubblica di contenuti generati dagli utenti."),
            ("ul", [
                "<b>Non raccogliamo, vendiamo né trasferiamo a terzi dati personali di minori.</b> Le registrazioni di studio (soprannome, avatar, materie, compiti, abitudini, punti ecc.) sono inserite dai genitori e <b>archiviate solo nell'account iCloud del genitore</b>; lo sviluppatore non ha alcun accesso.",
                "<b>Nessun contenuto generato dagli utenti pubblico.</b> Il testo inserito dai genitori è visibile solo ai familiari che il genitore <b>invita uno a uno</b> tramite la condivisione iCloud privata (CKShare). Non esiste pubblico, visibilità per estranei, meccanismo di ricerca o raccomandazione: l'app non presenta i rischi sociali dei contenuti pubblici.",
                "<b>Controllo genitori.</b> L'app offre un \"Blocco dispositivo (codice PIN)\": quando attivo, nasconde le funzioni di configurazione e l'uscita richiede il PIN; la modifica o il ripristino richiedono biometria di sistema o codice. I genitori possono usarlo per limitare l'accesso a impostazioni e acquisti.",
                "<b>Apple ID dei minori.</b> Se un genitore condivide un gruppo di studio con l'Apple ID di un minore, quell'account è creato e gestito dal genitore secondo le regole di Apple; la condivisione resta sotto il controllo del genitore e può essere interrotta in qualsiasi momento.",
                "<b>Sul consenso dei genitori.</b> Poiché l'app <b>non raccoglie alcun dato personale di minori</b>, i meccanismi di \"consenso genitoriale verificabile\" richiesti da COPPA (USA), GDPR (norme sui minori, UE) e dalle regole cinesi sulla protezione online dei dati personali dei minori non si applicano, e non dobbiamo raccogliere l'identità di alcun genitore a tale scopo. I genitori possono in qualsiasi momento eliminare qualsiasi gruppo di studio con tutti i suoi dati; l'eliminazione ha effetto immediato.",
                "Rispettiamo la legge cinese sulla protezione dei dati personali e le regole cinesi sulla protezione online dei dati personali dei minori, in linea con i principi COPPA/GDPR: <b>minimizzazione dei dati, controllo genitori, nessuna condivisione, nessuna vendita, nessuna pubblicità o profilazione</b>.",
                "I genitori che vogliono verificare, correggere o eliminare definitivamente le informazioni dei propri gruppi di studio possono farlo nell'app, oppure scrivere a {mail} per assistenza.",
            ]),
        ]),
        ("5. Conservazione dei dati, sicurezza ed eliminazione", [
            ("ul", [
                "Tutti i dati sono nell'account iCloud del tuo Apple ID, protetti dalla crittografia e dal controllo degli accessi di Apple. Non conserviamo alcuna copia sul server.",
                "<b>L'eliminazione dell'app non rimuove automaticamente i dati iCloud</b> (così puoi ripristinarli su un nuovo dispositivo). Per eliminare tutto: su iPhone/iPad vai in <i>Impostazioni → il tuo Apple ID → iCloud → Gestisci spazio → LearnNest → Elimina dati</i>; elimina il gruppo di studio nell'app in <i>Io → Gruppi di studio</i>; oppure scrivi a {mail} per assistenza all'eliminazione.",
                "Poche impostazioni dell'interfaccia (lingua, visualizzazione) sono archiviate <b>localmente sul dispositivo</b> (UserDefaults di sistema). Non lasciano mai il dispositivo e non sono sincronizzate con iCloud.",
                "Proteggi il tuo Apple ID e il codice del dispositivo — sono la protezione più importante per questi dati.",
            ]),
        ]),
        ("6. Acquisti e pagamenti", [
            ("p", "LearnNest è gratuito da scaricare con una prova locale di 7 giorni. La versione completa è un <b>acquisto una tantum (non consumabile, nessun abbonamento; nessun rinnovo automatico)</b>. Tutti i pagamenti sono gestiti dall'App Store di Apple (StoreKit). <b>Non riceviamo né archiviamo mai i dati della tua carta</b> e non possiamo vedere le informazioni complete dell'account. La Condivisione familiare è attiva, quindi i familiari non devono acquistare di nuovo."),
        ]),
        ("7. Modifiche a questa informativa", [
            ("p", "Se questa informativa viene modificata, aggiorneremo questa pagina e la \"data di entrata in vigore\" in alto. Le modifiche sostanziali (per esempio l'introduzione di una nuova raccolta di dati) saranno annunciate anche chiaramente nell'app. Consulta regolarmente questa pagina per la versione più recente."),
        ]),
        ("8. Contattaci", [
            ("p", "Domande, reclami o richieste di eliminazione riguardanti questa informativa o i tuoi dati: scrivi a <b>{mail}</b>. Rispondiamo di norma entro <b>3 giorni lavorativi</b>."),
        ]),
    ],
    "support_title": "Supporto e FAQ",
    "support_rows": [
        ("Nuovo dispositivo / sincronizzazione", "Accedi con lo <b>stesso Apple ID</b> su ogni dispositivo con iCloud Drive attivo; i dati si sincronizzano automaticamente. Se la sincronizzazione si blocca, controlla <i>Impostazioni → Apple ID → iCloud</i>."),
        ("Condivisione familiare / gruppo di studio", "Usa \"Condividi gruppo\" nell'app (Apple CloudKit CKShare); il destinatario accetta con il proprio Apple ID. Servono due Apple ID diversi per il test."),
        ("Ripristina acquisti", "Premi \"Ripristina acquisti\" in fondo al paywall — senza costi aggiuntivi."),
        ("Elimina tutti i dati", "Vedi la sezione 5 qui sopra. Eliminare l'app non rimuove i dati iCloud."),
        ("Scansione testo (OCR)", "Funziona interamente sul dispositivo tramite Apple Vision; nessun caricamento, nessuna rete richiesta."),
        ("Lingue supportate", "21 lingue: cinese semplificato e tradizionale, inglese, giapponese, coreano, spagnolo, portoghese (BR), francese, tedesco, italiano, olandese, polacco, svedese, norvegese (bokmål), danese, indonesiano, malese, filippino, turco, vietnamita e russo."),
        ("Requisiti di sistema", "iOS / iPadOS 17.0 o successivo (iPhone e iPad, incluse le widget nella schermata Home)."),
        ("Contatto", "Scrivi a <b>{mail}</b> — risposta entro 3 giorni lavorativi."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["ms"] = {
    "html_lang": "ms",
    "title": "LearnNest Dasar Privasi & Sokongan",
    "desc": "Dasar privasi dan sokongan LearnNest: kami tidak mengumpul data peribadi; semua data kekal dalam iCloud anda sendiri.",
    "h1": "🎓 LearnNest Dasar Privasi & Sokongan",
    "meta_line": "Tarikh Berkuat Kuasa: {d} ｜ Pembangun: {dev} ｜ Hubungi: {mail}",
    "nav": ["Dasar Privasi", "Sokongan & Soalan Lazim"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Ringkasnya:</b> LearnNest <b>tidak mengumpul sebarang data peribadi</b>. Tiada sistem akaun, tiada pelayan dan tiada analitik atau iklan pihak ketiga. Jadual, kerja rumah, tabiat, peringatan dan mata yang anda masukkan disimpan <b>hanya dalam pangkalan data iCloud peribadi anda sendiri</b> (Apple CloudKit); pembangun tidak boleh membaca atau mengeksportnya. <b>Kunci peranti (kod PIN)</b> disediakan sebagai kawalan ibu bapa, dan semua kandungan pembelajaran dicipta dan diurus oleh ibu bapa.",
    "privacy_title": "Dasar Privasi",
    "sections": [
        ("1. Gambaran Keseluruhan", [
            ("p", "LearnNest ialah alat pengurusan pembelajaran untuk <b>ibu bapa</b>: jadual waktu, pengurusan kerja rumah, tabiat, peringatan dan sistem mata/ganjaran. Dibangunkan oleh pembangun bebas ({dev}) — <b>tanpa pelayan sendiri dan tanpa pangkalan data bahagian belakang</b>. Dasar ini menerangkan bagaimana kami mengendalikan — sebenarnya tidak mengendalikan — maklumat anda."),
        ]),
        ("2. Apa yang kami kumpul: tiada apa-apa", [
            ("p", "LearnNest <b>tidak mengumpul sebarang data peribadi</b>. Secara khusus:"),
            ("ul", [
                "<b>Tiada pendaftaran, tiada log masuk.</b> Kami tidak meminta atau menerima nama, e-mel, nombor telefon, kenalan, lokasi, gambar atau pengecam lain.",
                "<b>Data anda kekal dalam iCloud anda sendiri.</b> Jadual, kerja rumah, tabiat, peringatan, mata dan ganjaran yang anda cipta disimpan dalam pangkalan data iCloud peribadi Apple ID anda sendiri (Apple CloudKit, bekas <code>iCloud.com.frankzhou.KidLearn</code>). Data itu milik anda dan dijaga oleh Apple; <b>pembangun tidak boleh mengakses, membaca atau mengeksportnya</b>.",
                "<b>Kongsi Keluarga & bilik pembelajaran.</b> Berasaskan Apple CloudKit CKShare. Data dikongsi hanya dengan Apple ID yang anda jemput secara jelas (biasanya ahli keluarga); anda mengawal dan boleh menarik balik perkongsian pada bila-bila masa.",
            ]),
            ("p", "<b>Fungsi peranti dan kebenaran sistem:</b>"),
            ("ul", [
                "<b>Notifikasi</b> — semata-mata untuk menghantar peringatan pembelajaran yang anda cipta sendiri; tiada kandungan iklan atau promosi. \"Notifikasi jauh\" digunakan hanya sebagai <b>pencetus senyap untuk penyegerakan iCloud</b> dan tidak pernah menunjukkan amaran yang kelihatan.",
                "<b>Gambar (pemilih sistem)</b> — fungsi kerja rumah \"imbas teks (OCR)\" memilih imej melalui pemilih foto sistem Apple (PhotosPicker). Aplikasi <b>hanya menerima imej tunggal yang anda pilih</b>, tidak boleh melayari bahagian lain perpustakaan anda dan <b>tidak meminta kebenaran perpustakaan foto</b>. Pengecaman dijalankan <b>sepenuhnya pada peranti</b> melalui rangka kerja Vision Apple; imej dan hasilnya <b>tidak pernah dimuat naik</b>, dan imej asal tidak disimpan. <b>Aplikasi tidak menggunakan kamera dan tidak meminta kebenaran kamera.</b> Gambar profil bilik pembelajaran berfungsi sama: hanya imej yang dipilih dibaca, dimampatkan dan <b>disimpan semata-mata dalam akaun iCloud anda sendiri</b> — tidak pernah dimuat naik ke mana-mana pelayan.",
                "<b>Face ID / Touch ID / kod peranti</b> — hanya untuk mengesahkan anda pada peranti ini apabila ibu bapa mengubah atau menetapkan semula PIN kunci peranti, atau mematikan mod kunci. Pengesahan dilakukan oleh iOS; <b>aplikasi tidak pernah menerima, membaca atau menyimpan data biometrik</b>.",
                "<b>Papan klip</b> — dibaca sekali, hanya apabila anda sendiri menekan \"Tampal\", untuk membina senarai kerja rumah. Teks diproses <b>pada peranti</b>; ia <b>tidak pernah dimuat naik atau disimpan</b>. Aplikasi tidak menggunakan papan klip pada waktu lain.",
                "<b>Kebenaran yang tidak pernah kami minta</b> — tiada lokasi, kenalan, kalendar, peringatan, mikrofon, kamera atau penjejakan aplikasi. Selain perkara di atas, aplikasi tidak mengisytiharkan kebenaran lain.",
            ]),
        ]),
        ("3. Pihak ketiga, penjejakan dan iklan: tiada", [
            ("ul", [
                "<b>Tiada kod pihak ketiga langsung</b> — projek ini tidak bergantung pada sebarang Swift Package, CocoaPods atau pustaka pihak ketiga. Tiada SDK iklan, tiada SDK analitik (tiada Firebase dan sebagainya), tiada laporan ranap, atribusi atau pemasaran push.",
                "<b>Tiada penjejakan</b> — tiada IDFA, tiada gesaan App Tracking Transparency, tiada penjejakan merentasi apl atau tapak web, tiada kuki penjejakan, cap jari peranti atau pengecam setempat.",
                "<b>Kami tidak pernah menjual, berkongsi atau menukar data pengguna</b> dan tidak menyertai sebarang bentuk pemonetisasi data. Tiada data digunakan untuk iklan atau pemrofilan pengguna.",
                "<b>Selain memuatkan halaman dasar ini, semua permintaan rangkaian menuju ke perkhidmatan Apple</b> — penyegerakan iCloud (CloudKit) dan pembelian App Store (StoreKit). Kedua-duanya tertakluk pada dasar privasi Apple sendiri — lihat <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Dasar Privasi Apple</a>. (Entri aplikasi \"Dasar Privasi\" dan \"Sokongan\" dibuka dalam pembaca terbina dalam tanpa bar alamat dan tidak pernah meninggalkan aplikasi: hanya halaman ini dimuatkan, JavaScript dimatikan, tiada kuki atau data web ditulis dan navigasi ke domain lain disekat. Halaman ini dihoskan pada perkhidmatan pengehosan statik pihak ketiga (GitHub Pages); pemuatannya ialah satu-satunya permintaan rangkaian aplikasi kepada perkhidmatan bukan Apple dan tidak mengandungi pengecam akaun atau peranti.)",
            ]),
        ]),
        ("4. Privasi Kanak-Kanak Bawah Umur", [
            ("p", "LearnNest ialah <b>alat pengurusan untuk ibu bapa</b>, bukan aplikasi yang dibina terus untuk kanak-kanak bawah umur: semua kandungan dicipta dan diurus oleh ibu bapa. Aplikasi ini <b>tidak</b> menawarkan sebarang sembang, komen, profil awam, penerokaan atau cadangan kandungan, hubungan dengan orang asing atau perkongsian awam kandungan yang dicipta pengguna."),
            ("ul", [
                "<b>Kami tidak mengumpul, menjual atau mendedahkan data peribadi kanak-kanak bawah umur kepada pihak ketiga.</b> Rekod pembelajaran (nama panggilan, avatar, mata pelajaran, kerja rumah, tabiat, mata dan sebagainya) dimasukkan oleh ibu bapa dan <b>disimpan hanya dalam akaun iCloud ibu bapa</b>; pembangun tiada akses.",
                "<b>Tiada kandungan pengguna yang awam.</b> Teks yang dimasukkan ibu bapa hanya kelihatan kepada ahli keluarga yang ibu bapa <b>jemput satu demi satu</b> melalui perkongsian iCloud peribadi (CKShare). Tiada penonton awam, tiada keterlihatan kepada orang asing dan tiada mekanisme carian atau cadangan, jadi aplikasi ini tidak membawa risiko sosial kandungan awam.",
                "<b>Kawalan ibu bapa.</b> Aplikasi ini menawarkan \"Kunci Peranti (kod PIN)\": apabila diaktifkan, fungsi konfigurasi disembunyikan dan keluar memerlukan PIN; perubahan atau tetapan semula memerlukan biometrik sistem atau kod. Ibu bapa boleh menggunakannya untuk mengehadkan akses kepada tetapan dan pembelian.",
                "<b>Apple ID kanak-kanak bawah umur.</b> Jika ibu bapa berkongsi bilik pembelajaran dengan Apple ID kanak-kanak bawah umur, akaun itu dicipta dan diurus oleh ibu bapa mengikut peraturan Apple; perkongsian kekal di bawah kawalan ibu bapa dan boleh dihentikan pada bila-bila masa.",
                "<b>Tentuan persetujuan ibu bapa.</b> Memandangkan aplikasi ini <b>tidak mengumpul sebarang data peribadi kanak-kanak bawah umur langsung</b>, mekanisme \"persetujuan ibu bapa yang boleh disahkan\" yang diwajibkan oleh COPPA (AS), GDPR (peruntukan kanak-kanak bawah umur, EU) dan peraturan China tentang perlindungan dalam talian data peribadi kanak-kanak bawah umur tidak terpakai, dan kami tidak perlu mengumpulkan maklumat identiti mana-mana ibu bapa untuk tujuan itu. Ibu bapa boleh pada bila-bila masa memadamkan mana-mana bilik pembelajaran bersama semua datanya; pemadaman berkuat kuasa serta-merta.",
                "Kami mematuhi undang-undang perlindungan data peribadi China dan peraturan China tentang perlindungan dalam talian data peribadi kanak-kanak bawah umur, selaras dengan prinsip COPPA/GDPR: <b>minimum data, kawalan ibu bapa, tiada perkongsian, tiada penjualan serta tiada iklan atau pemrofilan</b>.",
                "Ibu bapa yang ingin menyemak, membetulkan atau memadamkan secara kekal maklumat dalam bilik pembelajaran mereka boleh berbuat demikian dalam aplikasi, atau e-mel kepada {mail} untuk bantuan.",
            ]),
        ]),
        ("5. Penyimpanan, Keselamatan dan Pemadaman Data", [
            ("ul", [
                "Semua data berada dalam akaun iCloud Apple ID anda, dilindungi oleh penyulitan dan kawalan akses Apple. Kami tidak menyimpan salinan pelayan.",
                "<b>Memadamkan aplikasi tidak secara automatik memadamkan data iCloud</b> (supaya anda boleh memulihkannya pada peranti baharu). Untuk memadam semuanya: pada iPhone/iPad pergi ke <i>Tetapan → Apple ID anda → iCloud → Urus Storan → LearnNest → Padam Data</i>; padamkan bilik pembelajaran dalam aplikasi di <i>Saya → Bilik Pembelajaran</i>; atau e-mel kepada {mail} untuk bantuan pemadaman.",
                "Beberapa tetapan antara muka (bahasa, paparan) disimpan <b>secara setempat pada peranti</b> (UserDefaults sistem). Ia tidak pernah meninggalkan peranti anda dan tidak disegerak ke iCloud.",
                "Jaga Apple ID dan kod peranti anda dengan baik — itulah perlindungan terpenting bagi data ini.",
            ]),
        ]),
        ("6. Pembelian dan Pembayaran", [
            ("p", "LearnNest percuma untuk dimuat turun dengan percubaan setempat 7 hari. Versi penuh ialah <b>pembelian sekali sahaja (bukan penggunaan, tiada langganan; tiada pembaharuan automatik)</b>. Semua pembayaran dikendalikan oleh Apple App Store (StoreKit). <b>Kami tidak pernah menerima atau menyimpan butiran kad pembayaran anda</b> dan tidak dapat melihat maklumat akaun penuh. Kongsi Keluarga didayakan, jadi ahli keluarga tidak perlu membeli semula."),
        ]),
        ("7. Perubahan kepada Dasar Ini", [
            ("p", "Jika dasar ini diubah, kami akan mengemas kini halaman ini dan \"tarikh berkuat kuasa\" di bahagian atas. Perubahan ketara (contohnya pengenalan pengumpulan data baharu) turut diumumkan dengan jelas dalam aplikasi. Semak halaman ini secara berkala untuk versi terkini."),
        ]),
        ("8. Hubungi Kami", [
            ("p", "Soalan, aduan atau permintaan pemadaman mengenai dasar ini atau data anda: e-mel kepada <b>{mail}</b>. Kami biasanya menjawab dalam masa <b>3 hari bekerja</b>."),
        ]),
    ],
    "support_title": "Sokongan & Soalan Lazim",
    "support_rows": [
        ("Peranti baharu / segera antara peranti", "Log masuk dengan <b>Apple ID yang sama</b> pada setiap peranti dengan iCloud Drive didayakan; data disegerak secara automatik. Jika penyegerakan tersekat, semak <i>Tetapan → Apple ID → iCloud</i>."),
        ("Perkongsian keluarga / bilik pembelajaran", "Gunakan \"Kongsi Bilik\" dalam aplikasi (Apple CloudKit CKShare); penerima menerima dengan Apple ID sendiri. Dua Apple ID berbeza diperlukan untuk ujian."),
        ("Pulihkan pembelian", "Tekan \"Pulihkan Pembelian\" di bahagian bawah dinding bayaran — tanpa caj tambahan."),
        ("Padam semua data", "Sila lihat seksyen 5 di atas. Memadamkan aplikasi tidak memadamkan data iCloud."),
        ("Imbas teks (OCR)", "Berjalan sepenuhnya pada peranti melalui Apple Vision; tiada muat naik, tiada rangkaian diperlukan."),
        ("Bahasa yang disokong", "21 bahasa: Cina mudah dan tradisional, Inggeris, Jepun, Korea, Sepanyol, Portugis (BR), Perancis, Jerman, Itali, Belanda, Poland, Sweden, Norway (bokmål), Denmark, Indonesia, Melayu, Filipina, Turki, Vietnam dan Rusia."),
        ("Keperluan sistem", "iOS / iPadOS 17.0 atau lebih baharu (iPhone dan iPad, termasuk widget skrin utama)."),
        ("Hubungi", "E-mel kepada <b>{mail}</b> — jawapan dalam 3 hari bekerja."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["tr"] = {
    "html_lang": "tr",
    "title": "LearnNest Gizlilik Politikası ve Destek",
    "desc": "LearnNest gizlilik politikası ve desteği: kişisel veri toplamıyoruz; tüm veriler sizin kendi iCloud'unuzda kalır.",
    "h1": "🎓 LearnNest Gizlilik Politikası ve Destek",
    "meta_line": "Yürürlük Tarihi: {d} ｜ Geliştirici: {dev} ｜ İletişim: {mail}",
    "nav": ["Gizlilik Politikası", "Destek ve SSS"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Kısaca:</b> LearnNest <b>hiçbir kişisel veri toplamaz</b>. Hesap sistemi yok, sunucu yok, üçüncü taraf analiz veya reklam yok. Girdiğiniz ders programı, ödevler, alışkanlıklar, hatırlatıcılar ve puanlar <b>yalnızca sizin kendi özel iCloud veritabanınızda</b> (Apple CloudKit) saklanır; geliştirici bunları okuyamaz veya dışa aktaramaz. Ebeveyn denetimi olarak bir <b>cihaz kilidi (PIN kodu)</b> sunulur ve tüm ders içerikleri bir ebeveyn tarafından oluşturulup yönetilir.",
    "privacy_title": "Gizlilik Politikası",
    "sections": [
        ("1. Genel Bakış", [
            ("p", "LearnNest <b>ebeveynler</b> için bir ders düzenleme aracıdır: ders programı, ödev yönetimi, alışkanlıklar, hatırlatıcılar ve bir puan/ödül sistemi. Bağımsız bir geliştirici ({dev}) tarafından geliştirilmiştir — <b>kendi sunucusu ve arka uç veritabanı yoktur</b>. Bu politika, bilgilerinizi nasıl işlediğimizi — daha doğrusu işlemediğimizi — açıklar."),
        ]),
        ("2. Topladığımız şey: hiçbir şey", [
            ("p", "LearnNest <b>hiçbir kişisel veri toplamaz</b>. Somut olarak:"),
            ("ul", [
                "<b>Kayıt yok, giriş yok.</b> İsim, e-posta, telefon numarası, kişiler, konum, fotoğraflar veya başka tanımlayıcılar talep etmeyiz veya almayız.",
                "<b>Verileriniz kendi iCloud'unuzda kalır.</b> Oluşturduğunuz ders programı, ödevler, alışkanlıklar, hatırlatıcılar, puanlar ve ödüller kendi Apple Kimliğinizin özel iCloud veritabanında (Apple CloudKit, kapsayıcı <code>iCloud.com.frankzhou.KidLearn</code>) saklanır. Veriler size aittir ve Apple tarafından barındırılır; <b>geliştirici bunlara erişemez, okuyamaz veya dışa aktaramaz</b>.",
                "<b>Aile Paylaşımı ve çalışma odaları.</b> Apple CloudKit CKShare üzerine kuruludur. Veriler yalnızca açıkça davet ettiğiniz Apple Kimlikleriyle (normalde aile üyeleri) paylaşılır; kontrol sizdedir ve paylaşımı dilediğiniz an iptal edebilirsiniz.",
            ]),
            ("p", "<b>Cihaz özellikleri ve sistem izinleri:</b>"),
            ("ul", [
                "<b>Bildirimler</b> — yalnızca kendi oluşturduğunuz ders hatırlatıcılarını iletmek için; reklam veya promosyon içeriği yoktur. \"Uzak bildirimler\" yalnızca <b>iCloud senkronizasyonu için sessiz tetikleyici</b> olarak kullanılır ve asla görünür bir uyarı göstermez.",
                "<b>Fotoğraflar (sistem seçici)</b> — ödev özelliği \"metin tara (OCR)\" Apple'ın sistem fotoğraf seçicisi (PhotosPicker) üzerinden bir görsel seçer. Uygulama <b>yalnızca seçtiğiniz tek görseli alır</b>, kitaplığınızın geri kalanına göz atamaz ve <b>fotoğraf kitaplığı izni istemez</b>. Tanıma, Apple'ın Vision çerçevesiyle <b>tümüyle cihaz üzerinde</b> çalışır; görsel de sonuç da <b>asla yüklenmez</b> ve özgün görsel kaydedilmez. <b>Uygulama kamerayı kullanmaz ve kamera izni istemez.</b> Bir çalışma odasının profil fotoğrafı da aynı şekilde çalışır: yalnızca seçilen görsel okunur, sıkıştırılır ve <b>yalnızca kendi iCloud hesabınızda saklanır</b> — hiçbir sunucuya asla yüklenmez.",
                "<b>Face ID / Touch ID / cihaz kodu</b> — yalnızca bir ebeveyn cihaz kilidi PIN'ini değiştirdiğinde veya sıfırladığında ya da kilitleme modunu kapattığında bu cihazda kimliğinizi doğrulamak için. Kimlik doğrulamayı iOS yapar; <b>uygulama asla biyometrik veri almaz, okumaz veya saklamaz</b>.",
                "<b>Pano</b> — yalnızca siz \"Yapıştır\"a bastığınızda, bir ödev listesi oluşturmak için bir kez okunur. Metin <b>cihaz üzerinde</b> işlenir; <b>asla yüklenmez veya kaydedilmez</b>. Uygulama başka hiçbir zamanda panoyu kullanmaz.",
                "<b>Asla istemediğimiz izinler</b> — konum, kişiler, takvim, hatırlatıcılar, mikrofon, kamera veya uygulama izleme yoktur. Bunların dışında uygulama başka izin bildirmez.",
            ]),
        ]),
        ("3. Üçüncü taraflar, izleme ve reklam: yok", [
            ("ul", [
                "<b>Hiç üçüncü taraf kodu yok</b> — proje hiçbir Swift Package, CocoaPods veya üçüncü taraf kitapliğine bağlı değildir. Reklam SDK'sı yok, analiz SDK'sı yok (Firebase vb. yok), çökme raporlama, atıflandırma veya push pazarlaması yok.",
                "<b>İzleme yok</b> — IDFA yok, App Tracking Transparency istemi yok, uygulama veya web siteleri arası izleme yok, izleme çerezi, cihaz parmak izi veya yerel tanımlayıcı yok.",
                "<b>Kullanıcı verilerini asla satmayız, paylaşmayız veya takas etmeyiz</b> ve hiçbir veri para kazanma biçimine katılmayız. Veri, reklam veya kullanıcı profilleme için kullanılmaz.",
                "<b>Bu politika sayfasının yüklenmesi dışında tüm ağ istekleri Apple'ın hizmetlerine gider</b> — iCloud (CloudKit) senkronizasyonu ve App Store satın alımları (StoreKit). Her ikisi de Apple'ın kendi gizlilik politikasına tabidir — bkz. <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple Gizlilik Politikası</a>. (Uygulamadaki \"Gizlilik Politikası\" ve \"Destek\" girdileri, adres çubuğu olmayan yerleşik bir okuyucuda açılır ve uygulamadan asla çıkmaz: yalnızca bu sayfa yüklenir, JavaScript kapalıdır, hiçbir çerez veya web verisi yazılmaz ve diğer alan adlarına gezinme engellenir. Sayfa üçüncü taraf bir statik barındırma hizmetinde (GitHub Pages) barındırılır; yüklenmesi, uygulamanın Apple dışı bir hizmete yaptığı tek ağ isteğidir ve hesap ya da cihaz tanımlayıcı içermez.)",
            ]),
        ]),
        ("4. Reşit Olmayanların Gizliliği", [
            ("p", "LearnNest, <b>ebeveynler için bir yönetim aracıdır</b>, doğrudan reşit olmayanlara yönelik bir uygulama değildir: tüm içerikler ebeveynler tarafından oluşturulup yönetilir. Uygulama <b>hiçbir</b> sohbet, yorum, genel profil, içerik keşfi veya öneri, yabancılarla temas ya da kullanıcı tarafından üretilen içeriğin genel paylaşımını sunmaz."),
            ("ul", [
                "<b>Reşit olmayanların kişisel verilerini toplamayız, satmayız veya üçüncü taraflara açmayız.</b> Ders kayıtları (takma ad, avatar, dersler, ödevler, alışkanlıklar, puanlar vb.) ebeveynler tarafından girilir ve <b>yalnızca ebeveynin kendi iCloud hesabında saklanır</b>; geliştiricinin erişimi yoktur.",
                "<b>Genel kullanıcı içeriği yok.</b> Ebeveynlerin girdiği metin, yalnızca ebeveynin özel iCloud paylaşımıyla (CKShare) <b>tek tek davet ettiği</b> aile üyelerine görünür. Genel izleyici, yabancı görünurluğu, arama veya öneri mekanizması yoktur; bu nedenle uygulama genel içeriğin sosyal risklerini taşımaz.",
                "<b>Ebeveyn denetimi.</b> Uygulama bir \"Cihaz Kilidi (PIN kodu)\" sunar: etkinleştirildiğinde yapılandırma işlevleri gizlenir ve çıkmak PIN ister; değiştirme veya sıfırlama sistem biyometrisi veya kod ister. Ebeveynler bunu ayarlara ve satın almalara erişimi sınırlamak için kullanabilir.",
                "<b>Reşit olmayanların Apple Kimlikleri.</b> Bir ebeveyn bir çalışma odasını reşit olmayan birinin Apple Kimliğiyle paylaşırsa, o hesap Apple'ın kurallarına göre ebeveyn tarafından oluşturulur ve yönetilir; paylaşım ebeveynin kontrolünde kalır ve dilediğiniz an durdurulabilir.",
                "<b>Ebeveyn onayı hakkında.</b> Uygulama <b>reşit olmayanlara dair hiçbir kişisel veri toplamadığından</b>, COPPA'nın (ABD), GDPR'ın (reşit olmayanlara ilişkin hükümler, AB) ve Çin'in reşit olmayanların kişisel verilerinin çevrimiçi korunmasına dair kurallarının gerektirdiği \"doğrulanabilir ebeveyn onayı\" mekanizmaları uygulanmaz ve bu amaçla hiçbir ebeveynin kimlik bilgisini toplamamız gerekmez. Ebeveynler dilediği an herhangi bir çalışma odasını tüm verileriyle birlikte silebilir; silme anında geçerli olur.",
                "Çin'in kişisel verileri koruma yasasına ve reşit olmayanların kişisel verilerinin çevrimiçi korunmasına dair kurallarına uyarız ve COPPA/GDPR ilkeleriyle örtüşürüz: <b>veri azaltma, ebeveyn denetimi, paylaşım yok, satış yok, reklam veya profilleme yok</b>.",
                "Çalışma odalarındaki bilgileri incelemek, düzeltmek veya kalıcı olarak silmek isteyen ebeveynler bunu uygulamada yapabilir veya yardım için {mail} adresine e-posta gönderebilir.",
            ]),
        ]),
        ("5. Veri Saklama, Güvenlik ve Silme", [
            ("ul", [
                "Tüm veriler, Apple Kimliğinizin iCloud hesabındadır; Apple'ın şifrelemesi ve erişim denetimiyle korunur. Sunucu kopyası saklamayız.",
                "<b>Uygulamayı silmek iCloud verilerini otomatik olarak silmez</b> (böylece yeni bir cihazda geri yükleyebilirsiniz). Her şeyi silmek için: iPhone/iPad'de <i>Ayarlar → Apple Kimliğiniz → iCloud → Depolamayı Yönet → LearnNest → Verileri Sil</i> yolunu izleyin; uygulamada <i>Ben → Çalışma Odaları</i> altından ilgili odayı silin; veya silme yardımı için {mail} adresine e-posta gönderin.",
                "Birkaç arayüz ayarı (dil, görünüm) <b>cihazda yerel olarak</b> (sistem UserDefaults) saklanır. Cihazınızdan asla ayrılmaz ve iCloud'a senkronize edilmez.",
                "Apple Kimliğinizi ve cihaz kodunuzu güvende tutun — bunlar bu verilerin en önemli korumasıdır.",
            ]),
        ]),
        ("6. Satın Alma ve Ödemeler", [
            ("p", "LearnNest, 7 günlük yerel deneme süresiyle ücretsiz indirilir. Tam sürüm <b>tek seferlik bir satın almadır (tüketilemez, abonelik yok; otomatik yenileme yok)</b>. Tüm ödemeler Apple App Store (StoreKit) tarafından işlenir. <b>Kart bilgilerinizi asla almayız veya saklamayız</b> ve tam hesap bilgilerini göremeyiz. Aile Paylaşımı etkindir; aile üyelerinin yeniden satın almasına gerek yoktur."),
        ]),
        ("7. Bu Politikanın Değişiklikleri", [
            ("p", "Bu politika değişirse bu sayfayı ve üstteki \"yürürlük tarihi\"ni güncelleriz. Önemli değişiklikler (örneğin yeni bir veri toplama başlatılması) uygulamada da açıkça duyurulur. En güncel sürüm için bu sayfayı düzenli olarak kontrol edin."),
        ]),
        ("8. Bize Ulaşın", [
            ("p", "Bu politika veya verilerinizle ilgili soru, şikâyet veya silme talepleri için: <b>{mail}</b> adresine e-posta gönderin. Normalde <b>3 iş günü</b> içinde yanıt veririz."),
        ]),
    ],
    "support_title": "Destek ve SSS",
    "support_rows": [
        ("Yeni cihaz / cihazlar arası senkronizasyon", "Her cihazda iCloud Drive açıkken <b>aynı Apple Kimliğiyle</b> giriş yapın; veriler otomatik senkronize olur. Senkronizasyon takılırsa <i>Ayarlar → Apple Kimliği → iCloud</i> bölümünü kontrol edin."),
        ("Aile / çalışma odası paylaşımı", "Uygulamada \"Odayı Paylaş\"ı kullanın (Apple CloudKit CKShare); alıcı kendi Apple Kimliğiyle kabul eder. Test için iki farklı Apple Kimliği gerekir."),
        ("Satın almaları geri yükle", "Ödeme duvarının altındaki \"Satın Almaları Geri Yükle\"ye dokunun — ek ücret yok."),
        ("Tüm verileri sil", "Yukarıdaki 5. bölüme bakın. Uygulamayı silmek iCloud verilerini silmez."),
        ("Metin tara (OCR)", "Apple Vision ile tümüyle cihaz üzerinde çalışır; yükleme yok, ağ gerekmez."),
        ("Desteklenen diller", "21 dil: basitleştirilmiş ve geleneksel Çince, İngilizce, Japonca, Korece, İspanyolca, Portekizce (BR), Fransızca, Almanca, İtalyanca, Felemenkçe, Lehçe, İsveççe, Norveççe (bokmål), Danca, Endonezce, Malayca, Filipince, Türkçe, Vietnamca ve Rusça."),
        ("Sistem gereksinimleri", "iOS / iPadOS 17.0 veya sonrası (iPhone ve iPad, ana ekran widget'ları dahil)."),
        ("İletişim", "<b>{mail}</b> adresine e-posta gönderin — 3 iş günü içinde yanıt."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}

CONTENT11A["vi"] = {
    "html_lang": "vi",
    "title": "LearnNest Chính sách quyền riêng tư & Hỗ trợ",
    "desc": "Chính sách quyền riêng tư và hỗ trợ của LearnNest: chúng tôi không thu thập dữ liệu cá nhân; mọi dữ liệu đều nằm trong iCloud của bạn.",
    "h1": "🎓 LearnNest Chính sách quyền riêng tư & Hỗ trợ",
    "meta_line": "Ngày hiệu lực: {d} ｜ Nhà phát triển: {dev} ｜ Liên hệ: {mail}",
    "nav": ["Chính sách quyền riêng tư", "Hỗ trợ & Câu hỏi thường gặp"],
    "nav_id": ["privacy", "support"],
    "summary": "<b>Tóm tắt:</b> LearnNest <b>không thu thập bất kỳ dữ liệu cá nhân nào</b>. Không có hệ thống tài khoản, không có máy chủ và không có phân tích hay quảng cáo bên thứ ba. Thời khóa biểu, bài tập, thói quen, nhắc việc và điểm bạn nhập được lưu <b>chỉ trong cơ sở dữ liệu iCloud riêng tư của chính bạn</b> (Apple CloudKit); nhà phát triển không thể đọc hay xuất chúng. Ứng dụng cung cấp <b>khóa thiết bị (mã PIN)</b> làm kiểm soát của phụ huynh, và toàn bộ nội dung học do phụ huynh tạo và quản lý.",
    "privacy_title": "Chính sách quyền riêng tư",
    "sections": [
        ("1. Tổng quan", [
            ("p", "LearnNest là công cụ tổ chức việc học dành cho <b>phụ huynh</b>: thời khóa biểu, quản lý bài tập về nhà, thói quen, nhắc việc và hệ thống điểm/khen thưởng. Do một nhà phát triển độc lập ({dev}) phát triển — <b>không có máy chủ riêng và không có cơ sở dữ liệu backend</b>. Chính sách này giải thích cách chúng tôi xử lý — thực ra là không xử lý — thông tin của bạn."),
        ]),
        ("2. Chúng tôi thu thập gì: không có gì", [
            ("p", "LearnNest <b>không thu thập bất kỳ dữ liệu cá nhân nào</b>. Cụ thể:"),
            ("ul", [
                "<b>Không đăng ký, không đăng nhập.</b> Chúng tôi không yêu cầu hay nhận tên, e-mail, số điện thoại, danh bạ, vị trí, ảnh hoặc các định danh khác.",
                "<b>Dữ liệu của bạn nằm trong iCloud của chính bạn.</b> Thời khóa biểu, bài tập, thói quen, nhắc việc, điểm và phần thưởng bạn tạo được lưu trong cơ sở dữ liệu iCloud riêng tư của Apple ID của bạn (Apple CloudKit, vùng chứa <code>iCloud.com.frankzhou.KidLearn</code>). Dữ liệu thuộc về bạn và do Apple lưu giữ; <b>nhà phát triển không thể truy cập, đọc hoặc xuất chúng</b>.",
                "<b>Chia sẻ gia đình & phòng học.</b> Dựa trên Apple CloudKit CKShare. Dữ liệu chỉ được chia sẻ với các Apple ID mà bạn rõ ràng mời (thường là thành viên gia đình); bạn kiểm soát và có thể thu hồi việc chia sẻ bất cứ lúc nào.",
            ]),
            ("p", "<b>Tính năng thiết bị và quyền hệ thống:</b>"),
            ("ul", [
                "<b>Thông báo</b> — chỉ để gửi các nhắc việc học do chính bạn tạo; không có nội dung quảng cáo hay tiếp thị. \"Thông báo từ xa\" chỉ được dùng làm <b>kích hoạt im lặng cho đồng bộ iCloud</b> và không bao giờ hiển thị cảnh báo nhìn thấy được.",
                "<b>Ảnh (bộ chọn hệ thống)</b> — tính năng bài tập \"quét chữ (OCR)\" chọn ảnh qua bộ chọn ảnh hệ thống của Apple (PhotosPicker). Ứng dụng <b>chỉ nhận duy nhất bức ảnh bạn chọn</b>, không thể duyệt phần còn lại của thư viện và <b>không yêu cầu quyền thư viện ảnh</b>. Việc nhận dạng chạy <b>hoàn toàn trên thiết bị</b> bằng khung Vision của Apple; cả ảnh lẫn kết quả <b>không bao giờ được tải lên</b>, và ảnh gốc không được lưu. <b>Ứng dụng không dùng camera và không yêu cầu quyền camera.</b> Ảnh đại diện của phòng học cũng hoạt động tương tự: chỉ ảnh được chọn được đọc, nén và <b>lưu duy nhất trong tài khoản iCloud của bạn</b> — không bao giờ tải lên máy chủ nào.",
                "<b>Face ID / Touch ID / mã thiết bị</b> — chỉ để xác thực bạn trên thiết bị này khi phụ huynh thay đổi hoặc đặt lại mã PIN khóa thiết bị, hoặc tắt chế độ khóa. Việc xác thực do iOS thực hiện; <b>ứng dụng không bao giờ nhận, đọc hay lưu dữ liệu sinh trắc học</b>.",
                "<b>Bộ nhớ tạm (clipboard)</b> — chỉ được đọc một lần, chỉ khi bạn tự nhấn \"Dán\", để tạo danh sách bài tập. Văn bản được xử lý <b>trên thiết bị</b>; <b>không bao giờ được tải lên hay lưu lại</b>. Ứng dụng không dùng bộ nhớ tạm vào lúc nào khác.",
                "<b>Các quyền chúng tôi không bao giờ yêu cầu</b> — không vị trí, danh bạ, lịch, nhắc việc, micrô, camera hay theo dõi ứng dụng. Ngoài những điều trên, ứng dụng không khai báo quyền nào khác.",
            ]),
        ]),
        ("3. Bên thứ ba, theo dõi và quảng cáo: không có", [
            ("ul", [
                "<b>Không có mã bên thứ ba nào cả</b> — dự án không phụ thuộc vào bất kỳ Swift Package, CocoaPods hay thư viện bên thứ ba nào. Không SDK quảng cáo, không SDK phân tích (không Firebase v.v.), không báo cáo sự cố, đo lường nguồn chuyển đổi hay tiếp thị đẩy.",
                "<b>Không theo dõi</b> — không IDFA, không hộp thoại App Tracking Transparency, không theo dõi chéo ứng dụng hay trang web, không cookie theo dõi, vân tay thiết bị hay định danh cục bộ.",
                "<b>Chúng tôi không bao giờ bán, chia sẻ hay trao đổi dữ liệu người dùng</b> và không tham gia bất kỳ hình thức kiếm tiền từ dữ liệu nào. Không có dữ liệu nào được dùng cho quảng cáo hay lập hồ sơ người dùng.",
                "<b>Ngoài việc tải trang chính sách này, mọi yêu cầu mạng đều đi đến dịch vụ của Apple</b> — đồng bộ iCloud (CloudKit) và mua hàng App Store (StoreKit). Cả hai đều chịu sự điều chỉnh của chính sách quyền riêng tư của Apple — xem <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Chính sách quyền riêng tư của Apple</a>. (Các mục \"Chính sách quyền riêng tư\" và \"Hỗ trợ\" trong ứng dụng mở trong trình đọc tích hợp không có thanh địa chỉ và không bao giờ rời khỏi ứng dụng: chỉ trang này được tải, JavaScript bị tắt, không ghi cookie hay dữ liệu web và việc điều hướng sang tên miền khác bị chặn. Trang được lưu trữ trên dịch vụ lưu trữ tĩnh bên thứ ba (GitHub Pages); việc tải nó là yêu cầu mạng duy nhất của ứng dụng tới dịch vụ không phải Apple và không chứa định danh tài khoản hay thiết bị.)",
            ]),
        ]),
        ("4. Quyền riêng tư của người chưa thành niên", [
            ("p", "LearnNest là <b>công cụ quản lý dành cho phụ huynh</b>, không phải ứng dụng dựng trực tiếp cho người chưa thành niên: toàn bộ nội dung do phụ huynh tạo và quản lý. Ứng dụng <b>không</b> cung cấp bất kỳ trò chuyện, bình luận, hồ sơ công khai, khám phá hay gợi ý nội dung, liên lạc với người lạ hay chia sẻ công khai nội dung do người dùng tạo nào."),
            ("ul", [
                "<b>Chúng tôi không thu thập, bán hay tiết lộ dữ liệu cá nhân của người chưa thành niên cho bên thứ ba.</b> Các bản ghi học tập (biệt danh, ảnh đại diện, môn học, bài tập, thói quen, điểm v.v.) do phụ huynh nhập và <b>chỉ được lưu trong tài khoản iCloud của phụ huynh</b>; nhà phát triển không có quyền truy cập.",
                "<b>Không có nội dung do người dùng tạo ở chế độ công khai.</b> Văn bản phụ huynh nhập chỉ hiển thị với các thành viên gia đình mà phụ huynh <b>mời từng người một</b> qua chia sẻ iCloud riêng tư (CKShare). Không có khán giả công khai, không bị người lạ nhìn thấy, không có cơ chế tìm kiếm hay gợi ý — nên ứng dụng không mang rủi ro xã hội của nội dung công khai.",
                "<b>Kiểm soát của phụ huynh.</b> Ứng dụng cung cấp \"Khóa thiết bị (mã PIN)\": khi bật, các chức năng cấu hình bị ẩn và thoát ứng dụng yêu cầu mã PIN; thay đổi hay đặt lại yêu cầu sinh trắc học hệ thống hoặc mã. Phụ huynh có thể dùng nó để hạn chế truy cập cài đặt và mua hàng.",
                "<b>Apple ID của người chưa thành niên.</b> Nếu phụ huynh chia sẻ phòng học với Apple ID của người chưa thành niên, tài khoản đó do phụ huynh tạo và quản lý theo quy định của Apple; việc chia sẻ vẫn nằm dưới sự kiểm soát của phụ huynh và có thể dừng bất cứ lúc nào.",
                "<b>Về sự đồng ý của phụ huynh.</b> Vì ứng dụng <b>không thu thập bất kỳ dữ liệu cá nhân nào của người chưa thành niên</b>, các cơ chế \"sự đồng ý xác thực được của phụ huynh\" theo COPPA (Mỹ), GDPR (quy định về người chưa thành niên, EU) và quy định của Trung Quốc về bảo vệ dữ liệu cá nhân của người chưa thành niên trên môi trường trực tuyến không áp dụng, và chúng tôi không cần thu thập thông tin định danh của phụ huynh cho mục đích đó. Phụ huynh có thể bất cứ lúc nào xóa bất kỳ phòng học nào cùng toàn bộ dữ liệu của nó; việc xóa có hiệu lực ngay lập tức.",
                "Chúng tôi tuân thủ luật bảo vệ dữ liệu cá nhân của Trung Quốc và quy định về bảo vệ dữ liệu cá nhân của người chưa thành niên trên môi trường trực tuyến, phù hợp với các nguyên tắc COPPA/GDPR: <b>giảm thiểu dữ liệu, kiểm soát của phụ huynh, không chia sẻ, không bán, cũng như không quảng cáo hay lập hồ sơ</b>.",
                "Phụ huynh muốn xem xét, sửa đổi hoặc xóa vĩnh viễn thông tin trong phòng học của mình có thể làm ngay trong ứng dụng, hoặc gửi e-mail tới {mail} để được trợ giúp.",
            ]),
        ]),
        ("5. Lưu trữ, bảo mật và xóa dữ liệu", [
            ("ul", [
                "Mọi dữ liệu nằm trong tài khoản iCloud của Apple ID của bạn, được bảo vệ bởi mã hóa và kiểm soát truy cập của Apple. Chúng tôi không lưu bản sao trên máy chủ.",
                "<b>Xóa ứng dụng không tự động xóa dữ liệu iCloud</b> (để bạn có thể khôi phục trên thiết bị mới). Để xóa tất cả: trên iPhone/iPad vào <i>Cài đặt → Apple ID của bạn → iCloud → Quản lý dung lượng → LearnNest → Xóa dữ liệu</i>; xóa phòng học trong ứng dụng tại <i>Tôi → Phòng học</i>; hoặc gửi e-mail tới {mail} để được trợ giúp xóa.",
                "Một số ít cài đặt giao diện (ngôn ngữ, hiển thị) được lưu <b>cục bộ trên thiết bị</b> (UserDefaults của hệ thống). Chúng không bao giờ rời khỏi thiết bị của bạn và không đồng bộ lên iCloud.",
                "Hãy giữ an toàn Apple ID và mã thiết bị của bạn — đó là lớp bảo vệ quan trọng nhất cho các dữ liệu này.",
            ]),
        ]),
        ("6. Mua hàng và thanh toán", [
            ("p", "LearnNest tải về miễn phí với thời gian dùng thử cục bộ 7 ngày. Bản đầy đủ là <b>mua một lần (không tiêu hao, không gói đăng ký; không tự động gia hạn)</b>. Mọi thanh toán do Apple App Store (StoreKit) xử lý. <b>Chúng tôi không bao giờ nhận hay lưu thông tin thẻ thanh toán của bạn</b> và không thể xem đầy đủ thông tin tài khoản. Chia sẻ gia đình đã được bật nên thành viên gia đình không cần mua lại."),
        ]),
        ("7. Thay đổi chính sách này", [
            ("p", "Nếu chính sách này thay đổi, chúng tôi sẽ cập nhật trang này và \"ngày hiệu lực\" ở đầu trang. Các thay đổi quan trọng (ví dụ bắt đầu thu thập dữ liệu mới) cũng được thông báo rõ ràng trong ứng dụng. Hãy kiểm tra trang này thường xuyên để có phiên bản mới nhất."),
        ]),
        ("8. Liên hệ với chúng tôi", [
            ("p", "Câu hỏi, khiếu nại hoặc yêu cầu xóa liên quan đến chính sách này hoặc dữ liệu của bạn: gửi e-mail tới <b>{mail}</b>. Chúng tôi thường trả lời trong vòng <b>3 ngày làm việc</b>."),
        ]),
    ],
    "support_title": "Hỗ trợ & Câu hỏi thường gặp",
    "support_rows": [
        ("Thiết bị mới / đồng bộ giữa các thiết bị", "Đăng nhập bằng <b>cùng một Apple ID</b> trên mỗi thiết bị có bật iCloud Drive; dữ liệu tự động đồng bộ. Nếu đồng bộ bị treo, kiểm tra <i>Cài đặt → Apple ID → iCloud</i>."),
        ("Chia sẻ gia đình / phòng học", "Dùng \"Chia sẻ phòng\" trong ứng dụng (Apple CloudKit CKShare); người nhận chấp nhận bằng Apple ID của riêng mình. Cần hai Apple ID khác nhau để kiểm thử."),
        ("Khôi phục mua hàng", "Nhấn \"Khôi phục mua hàng\" ở cuối trang thanh toán — không mất thêm phí."),
        ("Xóa tất cả dữ liệu", "Xem mục 5 ở trên. Xóa ứng dụng không xóa dữ liệu iCloud."),
        ("Quét chữ (OCR)", "Chạy hoàn toàn trên thiết bị bằng Apple Vision; không tải lên, không cần mạng."),
        ("Ngôn ngữ được hỗ trợ", "21 ngôn ngữ: tiếng Trung giản thể và phồn thể, tiếng Anh, tiếng Nhật, tiếng Hàn, tiếng Tây Ban Nha, tiếng Bồ Đào Nha (BR), tiếng Pháp, tiếng Đức, tiếng Ý, tiếng Hà Lan, tiếng Ba Lan, tiếng Thụy Điển, tiếng Na Uy (bokmål), tiếng Đan Mạch, tiếng Indonesia, tiếng Mã Lai, tiếng Philippines, tiếng Thổ Nhĩ Kỳ, tiếng Việt và tiếng Nga."),
        ("Yêu cầu hệ thống", "iOS / iPadOS 17.0 trở lên (iPhone và iPad, bao gồm widget màn hình chính)."),
        ("Liên hệ", "Gửi e-mail tới <b>{mail}</b> — trả lời trong 3 ngày làm việc."),
    ],
    "footer": "© 2026 {dev} · LearnNest",
}


