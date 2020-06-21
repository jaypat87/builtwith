{
  "$schema": "../schema.json",
  "apps": {
    "1C-Bitrix": {
      "cats": [
        1,
        6
      ],
      "headers": {
        "Set-Cookie": "BITRIX_",
        "X-Powered-CMS": "Bitrix Site Manager"
      },
      "html": "(?:<link[^>]+components/bitrix|(?:src|href)=\"/bitrix/(?:js|templates))",
      "icon": "1C-Bitrix.png",
      "implies": "PHP",
      "script": "1c-bitrix",
      "website": "http://www.1c-bitrix.ru"
    },
    "3dCart": {
      "cats": [
        1,
        6
      ],
      "cookies": {
        "3dvisit": ""
      },
      "headers": {
        "X-Powered-By": "3DCART"
      },
      "icon": "3dCart.png",
      "script": "(?:twlh(?:track)?\\.asp|3d_upsell\\.js)",
      "website": "http://www.3dcart.com"
    },
    "91App": {
      "cats": [
        6
      ],
      "icon": "91app.png",
      "script": "https\\:\\/\\/track\\.91app\\.io\\/track\\.js\\?",
      "website": "https://www.91app.com/"
    },
    "A-Frame": {
      "cats": [
        25
      ],
      "html": "<a-scene[^<>]*>",
      "icon": "A-Frame.svg",
      "implies": "three.js",
      "js": {
        "AFRAME.version": "^(.+)$\\;version:\\1"
      },
      "script": "/?([\\d.]+)?/aframe(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://aframe.io"
    },
    "AD EBiS": {
      "cats": [
        10
      ],
      "html": [
        "<!-- EBiS contents tag",
        "<!--EBiS tag",
        "<!-- Tag EBiS",
        "<!-- EBiS common tag"
      ],
      "icon": "ebis.png",
      "website": "http://www.ebis.ne.jp"
    },
    "ADPLAN": {
      "cats": [
        10
      ],
      "icon": "ADPLAN.png",
      "script": [
        "^https?://[^.]+\\.adplan7\\.com/\\;version:7",
        "^https?://(?!o\\.)\\w+\\.advg\\.jp/"
      ],
      "website": "https://www.adplan7.com/"
    },
    "AMP": {
      "cats": [
        12
      ],
      "html": "<html[^>]* (?:amp|⚡)[^-]",
      "icon": "Accelerated-Mobile-Pages.svg",
      "website": "https://www.amp.dev"
    },
    "AMP Plugin": {
      "cats": [
        1,
        5
      ],
      "icon": "Accelerated-Mobile-Pages.svg",
      "implies": "WordPress",
      "meta": {
        "generator": "^AMP Plugin v(\\d+\\.\\d+.*)$\\;version:\\1"
      },
      "website": "https://amp-wp.org"
    },
    "AOLserver": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:aol:aolserver",
      "headers": {
        "Server": "AOLserver/?([\\d.]+)?\\;version:\\1"
      },
      "icon": "AOLserver.png",
      "website": "http://aolserver.com"
    },
    "AT Internet Analyzer": {
      "cats": [
        10
      ],
      "icon": "AT Internet.png",
      "js": {
        "ATInternet": "",
        "xtsite": ""
      },
      "website": "http://atinternet.com/en"
    },
    "AT Internet XiTi": {
      "cats": [
        10
      ],
      "icon": "AT Internet.png",
      "js": {
        "xt_click": ""
      },
      "script": "xiti\\.com/hit\\.xiti",
      "website": "http://atinternet.com/en"
    },
    "AWStats": {
      "cats": [
        10
      ],
      "cpe": "cpe:/a:laurent_destailleur:awstats",
      "icon": "AWStats.png",
      "implies": "Perl",
      "meta": {
        "generator": "AWStats ([\\d.]+(?: \\(build [\\d.]+\\))?)\\;version:\\1"
      },
      "website": "http://awstats.sourceforge.net"
    },
    "Acquia Cloud": {
      "cats": [
        62
      ],
      "headers": {
        "X-AH-Environment": "^\\w+$"
      },
      "icon": "acquia-cloud.png",
      "implies": [
        "Drupal\\;confidence:95",
        "Apache",
        "Percona",
        "Amazon EC2"
      ],
      "website": "https://www.acquia.com/"
    },
    "Act-On": {
      "cats": [
        32
      ],
      "icon": "ActOn.png",
      "js": {
        "ActOn": ""
      },
      "website": "http://act-on.com"
    },
    "AdInfinity": {
      "cats": [
        36
      ],
      "icon": "AdInfinity.png",
      "script": "adinfinity\\.com\\.au",
      "website": "http://adinfinity.com.au"
    },
    "AdOcean": {
      "cats": [
        36
      ],
      "icon": "AdOcean.png",
      "implies": "Gemius",
      "js": {
        "ado.master": "",
        "ado.placement": "",
        "ado.slave": ""
      },
      "script": [
        "adocean\\.pl/files/js/ado\\.js",
        "adocean\\.pl\\;confidence:80"
      ],
      "website": "https://adocean-global.com"
    },
    "AdRiver": {
      "cats": [
        36
      ],
      "html": "(?:<embed[^>]+(?:src=\"https?://mh\\d?\\.adriver\\.ru/|flashvars=\"[^\"]*(?:http:%3A//(?:ad|mh\\d?)\\.adriver\\.ru/|adriver_banner))|<(?:(?:iframe|img)[^>]+src|a[^>]+href)=\"https?://ad\\.adriver\\.ru/)",
      "icon": "AdRiver.png",
      "js": {
        "adriver": ""
      },
      "script": "(?:adriver\\.core\\.\\d\\.js|https?://(?:content|ad|masterh\\d)\\.adriver\\.ru/)",
      "website": "http://adriver.ru"
    },
    "AdRoll": {
      "cats": [
        36
      ],
      "icon": "AdRoll.svg",
      "js": {
        "adroll_adv_id": "",
        "adroll_pix_id": ""
      },
      "script": "(?:a|s)\\.adroll\\.com",
      "website": "http://adroll.com"
    },
    "Adcash": {
      "cats": [
        36
      ],
      "icon": "Adcash.svg",
      "js": {
        "SuLoaded": "",
        "SuUrl": "",
        "ac_bgclick_URL": "",
        "ct_nOpp": "",
        "ct_nSuUrl": "",
        "ct_siteunder": "",
        "ct_tag": ""
      },
      "script": "^[^\\/]*//(?:[^\\/]+\\.)?adcash\\.com/(?:script|ad)/",
      "url": "^https?://(?:[^\\/]+\\.)?adcash\\.com/script/pop_",
      "website": "http://adcash.com"
    },
    "AddShoppers": {
      "cats": [
        5
      ],
      "icon": "AddShoppers.png",
      "script": "cdn\\.shop\\.pe/widget/",
      "website": "http://www.addshoppers.com"
    },
    "AddThis": {
      "cats": [
        5
      ],
      "icon": "AddThis.svg",
      "js": {
        "addthis": ""
      },
      "script": "addthis\\.com/js/",
      "website": "http://www.addthis.com"
    },
    "AddToAny": {
      "cats": [
        5
      ],
      "icon": "AddToAny.png",
      "js": {
        "a2apage_init": ""
      },
      "script": "addtoany\\.com/menu/page\\.js",
      "website": "http://www.addtoany.com"
    },
    "Adminer": {
      "cats": [
        3
      ],
      "html": [
        "Adminer</a> <span class=\"version\">([\\d.]+)</span>\\;version:\\1",
        "onclick=\"bodyClick\\(event\\);\" onload=\"verifyVersion\\('([\\d.]+)'\\);\">\\;version:\\1"
      ],
      "icon": "adminer.png",
      "implies": "PHP",
      "website": "http://www.adminer.org"
    },
    "Adnegah": {
      "cats": [
        36
      ],
      "headers": {
        "X-Advertising-By": "adnegah\\.net"
      },
      "html": "<iframe [^>]*src=\"[^\"]+adnegah\\.net",
      "icon": "adnegah.png",
      "script": "[^a-z]adnegah.*\\.js$",
      "website": "https://Adnegah.net"
    },
    "Adobe ColdFusion": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:adobe:coldfusion",
      "headers": {
        "Cookie": "CFTOKEN="
      },
      "html": "<!-- START headerTags\\.cfm",
      "icon": "Adobe ColdFusion.svg",
      "implies": "CFML",
      "js": {
        "_cfEmails": ""
      },
      "script": "/cfajax/",
      "url": "\\.cfm(?:$|\\?)",
      "website": "http://adobe.com/products/coldfusion-family.html"
    },
    "Adobe DTM": {
      "cats": [
        42
      ],
      "icon": "adobedmt.png",
      "js": {
        "_satellite": ""
      },
      "website": "https://marketing.adobe.com/resources/help/en_US/dtm/c_overview.html"
    },
    "Adobe Experience Manager": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:adobe:experience_manager",
      "html": [
        "<div class=\"[^\"]*parbase",
        "<div[^>]+data-component-path=\"[^\"+]jcr:",
        "<div class=\"[^\"]*aem-Grid"
      ],
      "icon": "Adobe Experience Manager.svg",
      "implies": "Java",
      "script": [
        "/etc/designs/",
        "/etc/clientlibs/",
        "/etc\\.clientlibs/"
      ],
      "website": "https://www.adobe.com/marketing/experience-manager.html"
    },
    "Adobe GoLive": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:adobe:golive",
      "icon": "Adobe GoLive.png",
      "meta": {
        "generator": "Adobe GoLive(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "http://www.adobe.com/products/golive"
    },
    "Adobe RoboHelp": {
      "cats": [
        4
      ],
      "cpe": "cpe:/a:adobe:robohelp",
      "icon": "Adobe RoboHelp.svg",
      "js": {
        "gbWhLang": "",
        "gbWhMsg": "",
        "gbWhProxy": "",
        "gbWhUtil": "",
        "gbWhVer": ""
      },
      "meta": {
        "generator": "^Adobe RoboHelp(?: ([\\d]+))?\\;version:\\1"
      },
      "script": "(?:wh(?:utils|ver|proxy|lang|topic|msg)|ehlpdhtm)\\.js",
      "website": "http://adobe.com/products/robohelp.html"
    },
    "Advanced Web Stats": {
      "cats": [
        10
      ],
      "html": "aws\\.src = [^<]+caphyon-analytics",
      "icon": "Advanced Web Stats.png",
      "implies": "Java",
      "website": "http://www.advancedwebstats.com"
    },
    "Advert Stream": {
      "cats": [
        36
      ],
      "icon": "Advert Stream.png",
      "js": {
        "advst_is_above_the_fold": ""
      },
      "script": "(?:ad\\.advertstream\\.com|adxcore\\.com)",
      "website": "http://www.advertstream.com"
    },
    "Adverticum": {
      "cats": [
        36
      ],
      "html": "<div (?:id=\"[a-zA-Z0-9_]*\" )?class=\"goAdverticum\"",
      "icon": "Adverticum.svg",
      "script": "(?:ad\\.)?adverticum\\.net/g3\\.js",
      "website": "http://adverticum.net"
    },
    "Adyen": {
      "cats": [
        41
      ],
      "icon": "Adyen.svg",
      "js": {
        "adyen.encrypt.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://www.adyen.com"
    },
    "Adzerk": {
      "cats": [
        36
      ],
      "html": "<iframe [^>]*src=\"[^\"]+adzerk\\.net",
      "icon": "Adzerk.png",
      "js": {
        "ados": "",
        "adosResults": ""
      },
      "script": "adzerk\\.net/ados\\.js",
      "website": "http://adzerk.com"
    },
    "Aegea": {
      "cats": [
        11
      ],
      "headers": {
        "X-Powered-By": "^E2 Aegea v(\\d+)$\\;version:\\1"
      },
      "icon": "Aegea.png",
      "implies": [
        "PHP",
        "jQuery"
      ],
      "website": "http://blogengine.ru"
    },
    "Afosto": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "Afosto SaaS BV"
      },
      "icon": "Afosto.svg",
      "website": "http://afosto.com"
    },
    "AfterBuy": {
      "cats": [
        6
      ],
      "html": [
        "<dd>This OnlineStore is brought to you by ViA-Online GmbH Afterbuy\\. Information and contribution at https://www\\.afterbuy\\.de</dd>"
      ],
      "icon": "after-buy.png",
      "script": "shop-static\\.afterbuy\\.de",
      "website": "http://www.afterbuy.de"
    },
    "Ahoy": {
      "cats": [
        10
      ],
      "cookies": {
        "ahoy_track": "",
        "ahoy_visit": "",
        "ahoy_visitor": ""
      },
      "js": {
        "ahoy": ""
      },
      "website": "https://github.com/ankane/ahoy"
    },
    "Aircall": {
      "cats": [
        52
      ],
      "icon": "aircall.png",
      "script": "^https?://cdn\\.aircall\\.io/",
      "website": "http://aircall.io"
    },
    "Airee": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^Airee"
      },
      "icon": "Airee.png",
      "website": "http://xn--80aqc2a.xn--p1ai"
    },
    "Airform": {
      "cats": [
        61
      ],
      "html": [
        "<form[^>]+?action=\"[^\"]*airform\\.io[^>]+?>"
      ],
      "icon": "Airform.svg",
      "website": "https://airform.io"
    },
    "Akamai": {
      "cats": [
        31
      ],
      "headers": {
        "X-Akamai-Transformed": ""
      },
      "icon": "akamai.svg",
      "website": "http://akamai.com"
    },
    "Akaunting": {
      "cats": [
        55
      ],
      "headers": {
        "X-Akaunting": "^Free Accounting Software$"
      },
      "html": [
        "<link[^>]+akaunting-green\\.css",
        "Powered By Akaunting: <a [^>]*href=\"https?://(?:www\\.)?akaunting\\.com[^>]+>"
      ],
      "icon": "akaunting.svg",
      "implies": "Laravel",
      "website": "https://akaunting.com"
    },
    "Akka HTTP": {
      "cats": [
        18,
        22
      ],
      "cpe": "cpe:/a:lightbend:akka_http",
      "headers": {
        "Server": "akka-http(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "akka-http.png",
      "website": "http://akka.io"
    },
    "Algolia": {
      "cats": [
        29
      ],
      "icon": "Algolia.svg",
      "js": {
        "AlgoliaSearch": "",
        "algoliasearch.version": "^(.+)$\\;version:\\1"
      },
      "website": "http://www.algolia.com"
    },
    "All in One SEO Pack": {
      "cats": [
        54
      ],
      "cpe": "cpe:/a:semperfiwebdesign:all_in_one_seo_pack",
      "html": "<!-- All in One SEO Pack ([\\d.]+) \\;version:\\1",
      "icon": "all-in-One-SEO-Pack.png",
      "implies": "WordPress",
      "website": "https://wordpress.org/plugins/all-in-one-seo-pack/"
    },
    "Allegro RomPager": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Allegro-Software-RomPager(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Allegro RomPager.png",
      "website": "http://allegrosoft.com/embedded-web-server-s2"
    },
    "AlloyUI": {
      "cats": [
        12
      ],
      "icon": "AlloyUI.png",
      "implies": [
        "Bootstrap",
        "YUI"
      ],
      "js": {
        "AUI": ""
      },
      "script": "^https?://cdn\\.alloyui\\.com/",
      "website": "http://www.alloyui.com"
    },
    "Alpine.js": {
      "cats": [
        12
      ],
      "html": "<[^>]+[^\\w-]x-data[^\\w-][^<]+\\;confidence:75",
      "icon": "Alpine.js.png",
      "js": {
        "Alpine.version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "/alpine(?:\\.min)?\\.js"
      ],
      "website": "https://github.com/alpinejs/alpine"
    },
    "Amaya": {
      "cats": [
        20
      ],
      "icon": "Amaya.png",
      "meta": {
        "generator": "Amaya(?: V?([\\d.]+[a-z]))?\\;version:\\1"
      },
      "website": "http://www.w3.org/Amaya"
    },
    "Amazon ALB": {
      "cats": [
        65
      ],
      "cookies": {
        "AWSALB": "",
        "AWSALBCORS": ""
      },
      "icon": "aws-elb.png",
      "implies": "Amazon Web Services",
      "website": "https://aws.amazon.com/elasticloadbalancing/"
    },
    "Amazon Cloudfront": {
      "cats": [
        31
      ],
      "headers": {
        "Via": "\\(CloudFront\\)$",
        "X-Amz-Cf-Id": ""
      },
      "icon": "Amazon-Cloudfront.svg",
      "implies": "Amazon Web Services",
      "website": "http://aws.amazon.com/cloudfront/"
    },
    "Amazon EC2": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "\\(Amazon\\)"
      },
      "icon": "aws-ec2.svg",
      "implies": "Amazon Web Services",
      "website": "http://aws.amazon.com/ec2/"
    },
    "Amazon ECS": {
      "cats": [
        63
      ],
      "headers": {
        "Server": "^ECS"
      },
      "icon": "aws.svg",
      "implies": [
        "Amazon Web Services",
        "Docker"
      ],
      "website": "https://aws.amazon.com/elasticloadbalancing/"
    },
    "Amazon ELB": {
      "cats": [
        65
      ],
      "cookies": {
        "AWSELB": ""
      },
      "icon": "aws-elb.png",
      "implies": "Amazon Web Services",
      "website": "https://aws.amazon.com/elasticloadbalancing/"
    },
    "Amazon S3": {
      "cats": [
        19
      ],
      "headers": {
        "server": "^AmazonS3$"
      },
      "icon": "aws-s3.svg",
      "implies": "Amazon Web Services",
      "website": "http://aws.amazon.com/s3/"
    },
    "Amazon Web Services": {
      "cats": [
        62
      ],
      "icon": "aws.svg",
      "website": "https://aws.amazon.com/"
    },
    "Amber": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "X-Powered-By": "^Amber$"
      },
      "icon": "amber.png",
      "website": "https://amberframework.org"
    },
    "Ametys": {
      "cats": [
        1
      ],
      "icon": "Ametys.png",
      "implies": "Java",
      "meta": {
        "generator": "(?:Ametys|Anyware Technologies)"
      },
      "script": "ametys\\.js",
      "website": "http://ametys.org"
    },
    "Amiro.CMS": {
      "cats": [
        1
      ],
      "icon": "Amiro.CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "Amiro"
      },
      "website": "http://amirocms.com"
    },
    "Amplitude": {
      "cats": [
        10
      ],
      "icon": "amplitude.png",
      "script": [
        "cdn\\.amplitude\\.com"
      ],
      "website": "https://amplitude.com/"
    },
    "Analysys Ark": {
      "cats": [
        10
      ],
      "cookies": {
        "ARK_ID": ""
      },
      "icon": "Analysys Ark.svg",
      "js": {
        "AnalysysAgent": ""
      },
      "script": "AnalysysFangzhou_JS_SDK\\.min\\.js\\?v=([\\d.]+)\\;version:\\1",
      "website": "https://ark.analysys.cn"
    },
    "Anetwork": {
      "cats": [
        36
      ],
      "icon": "Anetwork.png",
      "script": "static-cdn\\.anetwork\\.ir/",
      "website": "https://www.anetwork.ir"
    },
    "Angular": {
      "cats": [
        12
      ],
      "excludes": [
        "AngularDart",
        "AngularJS"
      ],
      "html": "<[^>]+ ng-version=\"([\\d.]+)\"\\;version:\\1",
      "icon": "Angular.svg",
      "js": {
        "ng.coreTokens": "",
        "ng.probe": ""
      },
      "website": "https://angular.io"
    },
    "Angular Material": {
      "cats": [
        66
      ],
      "icon": "AngularJS.svg",
      "implies": "AngularJS",
      "js": {
        "ngMaterial": ""
      },
      "script": "/([\\d.rc-]+)?/angular-material(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://material.angularjs.org"
    },
    "AngularDart": {
      "cats": [
        18
      ],
      "excludes": [
        "Angular",
        "AngularJS"
      ],
      "icon": "AngularDart.svg",
      "implies": "Dart",
      "js": {
        "ngTestabilityRegistries": ""
      },
      "website": "https://webdev.dartlang.org/angular/"
    },
    "AngularJS": {
      "cats": [
        12
      ],
      "excludes": [
        "Angular",
        "AngularDart"
      ],
      "html": [
        "<(?:div|html)[^>]+ng-app=",
        "<ng-app"
      ],
      "icon": "AngularJS.svg",
      "js": {
        "angular": "",
        "angular.version.full": "^(.+)$\\;version:\\1"
      },
      "script": [
        "angular[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "/([\\d.]+(?:-?rc[.\\d]*)*)/angular(?:\\.min)?\\.js\\;version:\\1",
        "angular.*\\.js"
      ],
      "website": "https://angularjs.org"
    },
    "Ant Design": {
      "cats": [
        12
      ],
      "html": [
        "<[^>]*class=\"ant-(?:btn|col|row|layout|breadcrumb|menu|pagination|steps|select|cascader|checkbox|calendar|form|input-number|input|mention|rate|radio|slider|switch|tree-select|time-picker|transfer|upload|avatar|badge|card|carousel|collapse|list|popover|tooltip|table|tabs|tag|timeline|tree|alert|modal|message|notification|progress|popconfirm|spin|anchor|back-top|divider|drawer)",
        "<i class=\"anticon anticon-"
      ],
      "icon": "Ant Design.svg",
      "js": {
        "antd": ""
      },
      "website": "https://ant.design"
    },
    "Apache": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:apache:http_server",
      "headers": {
        "Server": "(?:Apache(?:$|/([\\d.]+)|[^/-])|(?:^|\\b)HTTPD)\\;version:\\1"
      },
      "icon": "Apache.svg",
      "website": "http://apache.org"
    },
    "Apache JSPWiki": {
      "cats": [
        8
      ],
      "cpe": "cpe:/a:apache:jspwiki",
      "html": "<html[^>]* xmlns:jspwiki=",
      "icon": "Apache JSPWiki.png",
      "implies": "Apache Tomcat",
      "script": "jspwiki",
      "url": "wiki\\.jsp",
      "website": "http://jspwiki.org"
    },
    "Apache Tomcat": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:apache:tomcat",
      "headers": {
        "Server": "^Apache-Coyote(?:/([\\d.]+))?\\;version:\\1",
        "X-Powered-By": "\\bTomcat\\b(?:-([\\d.]+))?\\;version:\\1"
      },
      "icon": "Apache Tomcat.svg",
      "implies": "Java",
      "website": "http://tomcat.apache.org"
    },
    "Apache Traffic Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:apache:traffic_server",
      "headers": {
        "Server": "ATS/?([\\d.]+)?\\;version:\\1"
      },
      "icon": "Apache Traffic Server.png",
      "website": "http://trafficserver.apache.org/"
    },
    "Apache Wicket": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:apache:wicket",
      "icon": "Apache Wicket.svg",
      "implies": "Java",
      "js": {
        "Wicket": ""
      },
      "website": "http://wicket.apache.org"
    },
    "ApexPages": {
      "cats": [
        51
      ],
      "headers": {
        "X-Powered-By": "Salesforce\\.com ApexPages"
      },
      "icon": "ApexPages.png",
      "implies": "Salesforce",
      "website": "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_intro.htm"
    },
    "Apigee": {
      "cats": [
        4
      ],
      "html": "<script>[^>]{0,50}script src=[^>]/profiles/apigee",
      "icon": "apigee.svg",
      "script": "/profiles/apigee",
      "website": "https://cloud.google.com/apigee/"
    },
    "Apollo": {
      "cats": [
        59
      ],
      "icon": "Apollo.svg",
      "js": {
        "__APOLLO_CLIENT__": "",
        "__APOLLO_CLIENT__.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://www.apollographql.com"
    },
    "ApostropheCMS": {
      "cats": [
        1
      ],
      "html": "<[^>]+data-apos-refreshable[^>]",
      "icon": "apostrophecms.svg",
      "implies": "Node.js",
      "website": "http://apostrophecms.org"
    },
    "AppDynamics": {
      "cats": [
        10
      ],
      "icon": "AppDynamics.png",
      "script": "adrum\\.js|adrum\\.([0-9].*)\\.js\\;version:\\1",
      "website": "https://appdynamics.com"
    },
    "AppNexus": {
      "cats": [
        36
      ],
      "html": "<(?:iframe|img)[^>]+adnxs\\.(?:net|com)",
      "icon": "AppNexus.svg",
      "script": "adnxs\\.(?:net|com)",
      "website": "http://appnexus.com"
    },
    "Arastta": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:arastta:ecommerce",
      "excludes": "OpenCart",
      "headers": {
        "Arastta": "^(.+)$\\;version:\\1",
        "X-Arastta": ""
      },
      "html": "Powered by <a [^>]*href=\"https?://(?:www\\.)?arastta\\.org[^>]+>Arastta",
      "icon": "Arastta.svg",
      "implies": "PHP",
      "script": "arastta\\.js",
      "website": "http://arastta.org"
    },
    "Arc Publishing": {
      "cats": [
        1
      ],
      "html": "<div [^>]*id=\"pb-root\"",
      "icon": "Arc-Publishing.svg",
      "js": {
        "Fusion.arcSite": ""
      },
      "website": "https://www.arcpublishing.com/"
    },
    "ArcGIS API for JavaScript": {
      "cats": [
        35
      ],
      "icon": "arcgis_icon.png",
      "script": [
        "js\\.arcgis\\.com",
        "basemaps\\.arcgis\\.com"
      ],
      "website": "https://developers.arcgis.com/javascript/"
    },
    "Artifactory": {
      "cats": [
        47
      ],
      "cpe": "cpe:/a:jfrog:artifactory",
      "html": [
        "<span class=\"version\">Artifactory(?: Pro)?(?: Power Pack)?(?: ([\\d.]+))?\\;version:\\1"
      ],
      "icon": "Artifactory.svg",
      "js": {
        "ArtifactoryUpdates": ""
      },
      "script": [
        "wicket/resource/org\\.artifactory\\."
      ],
      "website": "http://jfrog.com/open-source/#os-arti"
    },
    "Artifactory Web Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:jfrog:artifactory",
      "headers": {
        "Server": "Artifactory(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Artifactory.svg",
      "implies": "Artifactory",
      "website": "http://jfrog.com/open-source/#os-arti"
    },
    "ArvanCloud": {
      "cats": [
        31
      ],
      "headers": {
        "AR-PoweredBy": "Arvan Cloud \\(arvancloud\\.com\\)"
      },
      "icon": "ArvanCloud.png",
      "js": {
        "ArvanCloud": ""
      },
      "website": "http://www.ArvanCloud.com"
    },
    "AsciiDoc": {
      "cats": [
        1,
        20,
        27
      ],
      "icon": "AsciiDoc.png",
      "js": {
        "asciidoc": ""
      },
      "meta": {
        "generator": "^AsciiDoc ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.methods.co.nz/asciidoc"
    },
    "Asciinema": {
      "cats": [
        14
      ],
      "html": "<asciinema-player",
      "icon": "asciinema.png",
      "js": {
        "asciinema": ""
      },
      "script": "asciinema\\.org/",
      "website": "https://asciinema.org/"
    },
    "Atlassian Bitbucket": {
      "cats": [
        47
      ],
      "cpe": "cpe:/a:atlassian:bitbucket",
      "html": "<li>Atlassian Bitbucket <span title=\"[a-z0-9]+\" id=\"product-version\" data-commitid=\"[a-z0-9]+\" data-system-build-number=\"[a-z0-9]+\"> v([\\d.]+)<\\;version:\\1",
      "icon": "Atlassian Bitbucket.svg",
      "implies": "Python",
      "js": {
        "bitbucket": ""
      },
      "meta": {
        "application-name": "Bitbucket"
      },
      "website": "http://www.atlassian.com/software/bitbucket/overview/"
    },
    "Atlassian Confluence": {
      "cats": [
        8
      ],
      "cpe": "cpe:/a:atlassian:confluence",
      "headers": {
        "X-Confluence-Request-Time": ""
      },
      "html": "Powered by <a href=[^>]+atlassian\\.com/software/confluence(?:[^>]+>Atlassian Confluence</a> ([\\d.]+))?\\;version:\\1",
      "icon": "Atlassian Confluence.svg",
      "implies": "Java",
      "meta": {
        "confluence-request-time": ""
      },
      "website": "http://www.atlassian.com/software/confluence/overview/team-collaboration-software"
    },
    "Atlassian FishEye": {
      "cats": [
        47
      ],
      "cookies": {
        "FESESSIONID": ""
      },
      "cpe": "cpe:/a:atlassian:fisheye",
      "html": "<title>(?:Log in to )?FishEye (?:and Crucible )?([\\d.]+)?</title>\\;version:\\1",
      "icon": "Atlassian FishEye.svg",
      "website": "http://www.atlassian.com/software/fisheye/overview/"
    },
    "Atlassian Jira": {
      "cats": [
        13
      ],
      "cpe": "cpe:/a:atlassian:jira",
      "html": "Powered by\\s+<a href=[^>]+atlassian\\.com/(?:software/jira|jira-bug-tracking/)[^>]+>Atlassian\\s+JIRA(?:[^v]*v(?:ersion: )?(\\d+\\.\\d+(?:\\.\\d+)?))?\\;version:\\1",
      "icon": "Atlassian Jira.svg",
      "implies": "Java",
      "js": {
        "jira": ""
      },
      "meta": {
        "ajs-version-number": "^(.+)$\\;version:\\1",
        "application-name": "JIRA"
      },
      "website": "http://www.atlassian.com/software/jira/overview/"
    },
    "Atlassian Jira Issue Collector": {
      "cats": [
        13,
        47
      ],
      "icon": "Atlassian Jira.svg",
      "script": [
        "jira-issue-collector-plugin",
        "atlassian\\.jira\\.collector\\.plugin"
      ],
      "website": "http://www.atlassian.com/software/jira/overview/"
    },
    "Atlassian Statuspage": {
      "cats": [
        13,
        62
      ],
      "headers": {
        "X-StatusPage-Skip-Logging": "",
        "X-StatusPage-Version": ""
      },
      "html": "<a[^>]*href=\"https?://(?:www\\.)?statuspage\\.io/powered-by[^>]+>",
      "icon": "Atlassian Statuspage.svg",
      "website": "https://www.statuspage.io/"
    },
    "Aurelia": {
      "cats": [
        12
      ],
      "html": [
        "<[^>]+aurelia-app=[^>]",
        "<[^>]+data-main=[^>]aurelia-bootstrapper",
        "<[^>]+au-target-id=[^>]\\d"
      ],
      "icon": "Aurelia.svg",
      "script": [
        "aurelia(?:\\.min)?\\.js"
      ],
      "website": "http://aurelia.io"
    },
    "Automattic": {
      "cats": [
        62
      ],
      "headers": {
        "X-Hacker": "(?:automattic\\.com/jobs|wpvip\\.com/careers)"
      },
      "icon": "automattic.png",
      "implies": "WordPress",
      "website": "https://automattic.com/"
    },
    "Avangate": {
      "cats": [
        6
      ],
      "html": "<link[^>]* href=\"https?://edge\\.avangate\\.net/",
      "icon": "Avangate.svg",
      "js": {
        "__avng8_": "",
        "avng8_": ""
      },
      "script": "^https?://edge\\.avangate\\.net/",
      "website": "http://avangate.com"
    },
    "Avasize": {
      "cats": [
        5
      ],
      "icon": "Avasize.png",
      "script": "^https?://cdn\\.avasize\\.com/",
      "website": "https://www.avasize.com"
    },
    "Awesomplete": {
      "cats": [
        29
      ],
      "html": "<link[^>]+href=\"[^>]*awesomplete(?:\\.min)?\\.css",
      "js": {
        "awesomplete": ""
      },
      "script": "/awesomplete\\.js(?:$|\\?)",
      "website": "https://leaverou.github.io/awesomplete/"
    },
    "Azure": {
      "cats": [
        62
      ],
      "cookies": {
        "ARRAffinity": "",
        "TiPMix": ""
      },
      "headers": {
        "azure-regionname": "",
        "azure-sitename": "",
        "azure-slotname": "",
        "azure-version": ""
      },
      "icon": "azure.svg",
      "website": "https://azure.microsoft.com"
    },
    "Azure CDN": {
      "cats": [
        31
      ],
      "headers": {
        "X-EC-Debug": "",
        "server": "^(?:ECAcc|ECS|ECD)"
      },
      "icon": "azure.svg",
      "website": "https://azure.microsoft.com/en-us/services/cdn/"
    },
    "BEM": {
      "cats": [
        12
      ],
      "html": "<[^>]+data-bem",
      "icon": "BEM.png",
      "website": "http://en.bem.info"
    },
    "BIGACE": {
      "cats": [
        1
      ],
      "html": "(?:Powered by <a href=\"[^>]+BIGACE|<!--\\s+Site is running BIGACE)",
      "icon": "BIGACE.png",
      "implies": "PHP",
      "meta": {
        "generator": "BIGACE ([\\d.]+)\\;version:\\1"
      },
      "website": "http://bigace.de"
    },
    "BOOM": {
      "cats": [
        1
      ],
      "headers": {
        "X-Supplied-By": "MANA"
      },
      "icon": "boom.svg",
      "implies": "WordPress",
      "meta": {
        "generator": "^boom site builder$"
      },
      "website": "http://manaandisheh.com"
    },
    "Babel": {
      "cats": [
        19
      ],
      "icon": "Babel.svg",
      "js": {
        "_babelPolyfill": ""
      },
      "website": "https://babeljs.io"
    },
    "Bablic": {
      "cats": [
        3,
        9
      ],
      "icon": "bablic.png",
      "js": {
        "bablic": ""
      },
      "website": "https://www.bablic.com/"
    },
    "Backbone.js": {
      "cats": [
        12
      ],
      "icon": "Backbone.js.png",
      "implies": "Underscore.js",
      "js": {
        "Backbone": "",
        "Backbone.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "backbone.*\\.js",
      "website": "http://backbonejs.org"
    },
    "Backdrop": {
      "cats": [
        1
      ],
      "excludes": "Drupal",
      "headers": {
        "X-Backdrop-Cache": "",
        "X-Generator": "^Backdrop CMS(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "icon": "Backdrop.png",
      "implies": "PHP",
      "js": {
        "Backdrop": ""
      },
      "meta": {
        "generator": "^Backdrop CMS(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "https://backdropcms.org"
    },
    "Baidu Analytics (百度统计)": {
      "cats": [
        10
      ],
      "icon": "Baidu Tongji.png",
      "script": "hm\\.baidu\\.com/hm\\.js",
      "website": "https://tongji.baidu.com/"
    },
    "Banshee": {
      "cats": [
        1,
        18
      ],
      "html": "Built upon the <a href=\"[^>]+banshee-php\\.org/\">[a-z]+</a>(?:v([\\d.]+))?\\;version:\\1",
      "icon": "Banshee.png",
      "implies": "PHP",
      "meta": {
        "generator": "Banshee PHP"
      },
      "website": "http://www.banshee-php.org"
    },
    "BaseHTTP": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "BaseHTTP\\/?([\\d\\.]+)?\\;version:\\1"
      },
      "icon": "BaseHTTP.png",
      "implies": "Python",
      "website": "http://docs.python.org/2/library/basehttpserver.html"
    },
    "Big Cartel": {
      "cats": [
        6
      ],
      "icon": "bigcartel.png",
      "meta": {
        "generator": "Big Cartel"
      },
      "website": "https://www.bigcartel.com"
    },
    "BigDump": {
      "cats": [
        3
      ],
      "html": "<!-- <h1>BigDump: Staggered MySQL Dump Importer ver\\. ([\\d.b]+)\\;version:\\1",
      "implies": [
        "MySQL",
        "PHP"
      ],
      "website": "http://www.ozerov.de/bigdump.php"
    },
    "Bigcommerce": {
      "cats": [
        6
      ],
      "html": "<link href=[^>]+cdn\\d+\\.bigcommerce\\.com/",
      "icon": "Bigcommerce.png",
      "script": "cdn\\d+\\.bigcommerce\\.com/",
      "url": "mybigcommerce\\.com",
      "website": "http://www.bigcommerce.com"
    },
    "Bigware": {
      "cats": [
        6
      ],
      "cookies": {
        "bigWAdminID": "",
        "bigwareCsid": ""
      },
      "cpe": "cpe:/a:bigware:bigware_shop",
      "html": "(?:Diese <a href=[^>]+bigware\\.de|<a href=[^>]+/main_bigware_\\d+\\.php)",
      "icon": "Bigware.png",
      "implies": "PHP",
      "url": "(?:\\?|&)bigWAdminID=",
      "website": "http://bigware.de"
    },
    "BittAds": {
      "cats": [
        36
      ],
      "icon": "BittAds.png",
      "js": {
        "bitt": ""
      },
      "script": "bittads\\.com/js/bitt\\.js$",
      "website": "http://bittads.com"
    },
    "Bizweb": {
      "cats": [
        6
      ],
      "icon": "bizweb.png",
      "js": {
        "Bizweb": ""
      },
      "website": "https://www.bizweb.vn"
    },
    "Blade": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "X-Powered-By": "blade-([\\w.]+)?\\;version:\\1"
      },
      "icon": "Blade.png",
      "implies": "Java",
      "website": "https://lets-blade.com"
    },
    "Blazor": {
      "cats": [
        18
      ],
      "icon": "Blazor.png",
      "implies": "Microsoft ASP.NET",
      "script": [
        "blazor\\.server\\.js",
        "blazor\\.host\\.min\\.js",
        "blazor\\.webassembly\\.js"
      ],
      "website": "https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor"
    },
    "Blessing Skin": {
      "cats": [
        7
      ],
      "icon": "Blessing Skin.png",
      "implies": "Laravel",
      "js": {
        "blessing.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://github.com/bs-community/blessing-skin-server"
    },
    "Blesta": {
      "cats": [
        6
      ],
      "cookies": {
        "blesta_sid": ""
      },
      "icon": "Blesta.png",
      "website": "http://www.blesta.com"
    },
    "Blip.tv": {
      "cats": [
        14
      ],
      "html": "<(?:param|embed|iframe)[^>]+blip\\.tv/play",
      "icon": "Blip.tv.png",
      "website": "http://blip.tv"
    },
    "Blogger": {
      "cats": [
        11
      ],
      "icon": "Blogger.png",
      "implies": "Python",
      "meta": {
        "generator": "^Blogger$"
      },
      "url": "^https?://[^/]+\\.blogspot\\.com",
      "website": "http://www.blogger.com"
    },
    "Bloomreach": {
      "cats": [
        1
      ],
      "html": "<[^>]+/binaries/(?:[^/]+/)*content/gallery/",
      "icon": "Bloomreach.png",
      "website": "https://developers.bloomreach.com"
    },
    "Bluefish": {
      "cats": [
        20
      ],
      "icon": "Bluefish.png",
      "meta": {
        "generator": "Bluefish(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "http://sourceforge.net/projects/bluefish"
    },
    "Boa": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:boa:boa",
      "headers": {
        "Server": "Boa\\/?([\\d\\.a-z]+)?\\;version:\\1"
      },
      "website": "http://www.boa.org"
    },
    "Boba.js": {
      "cats": [
        59
      ],
      "implies": "Google Analytics",
      "script": "boba(?:\\.min)?\\.js",
      "website": "http://boba.space150.com"
    },
    "Bokeh": {
      "cats": [
        25
      ],
      "icon": "bokeh.png",
      "implies": "Python",
      "js": {
        "Bokeh": "",
        "Bokeh.version": "^(.+)$\\;version:\\1"
      },
      "script": "bokeh.*\\.js",
      "website": "https://bokeh.org"
    },
    "Bold Chat": {
      "cats": [
        52
      ],
      "icon": "BoldChat.png",
      "script": "^https?://vmss\\.boldchat\\.com/aid/\\d{18}/bc\\.vms4/vms\\.js",
      "website": "https://www.boldchat.com/"
    },
    "BoldGrid": {
      "cats": [
        1,
        11
      ],
      "html": [
        "<link rel=[\"']stylesheet[\"'] [^>]+boldgrid",
        "<link rel=[\"']stylesheet[\"'] [^>]+post-and-page-builder",
        "<link[^>]+s\\d+\\.boldgrid\\.com"
      ],
      "implies": "WordPress",
      "script": "/wp-content/plugins/post-and-page-builder",
      "website": "https://boldgrid.com"
    },
    "Bolt": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:bolt:bolt",
      "icon": "Bolt.png",
      "implies": "PHP",
      "meta": {
        "generator": "Bolt"
      },
      "website": "http://bolt.cm"
    },
    "Bonfire": {
      "cats": [
        18
      ],
      "cookies": {
        "bf_session": ""
      },
      "html": "Powered by <a[^>]+href=\"https?://(?:www\\.)?cibonfire\\.com[^>]*>Bonfire v([^<]+)\\;version:\\1",
      "icon": "Bonfire.png",
      "implies": "CodeIgniter",
      "website": "http://cibonfire.com"
    },
    "Bootstrap": {
      "cats": [
        66
      ],
      "cpe": "cpe:/a:getbootstrap:bootstrap",
      "html": [
        "<style>/\\*!\\* Bootstrap v(\\d\\.\\d\\.\\d)\\;version:\\1",
        "<link[^>]+?href=[^\"]/css/([\\d.]+)/bootstrap\\.(?:min\\.)?css\\;version:\\1",
        "<link[^>]+?href=\"[^\"]*bootstrap(?:\\.min)?\\.css",
        "<div[^>]+class=\"[^\"]*glyphicon glyphicon-"
      ],
      "icon": "Bootstrap.png",
      "js": {
        "bootstrap.Alert.VERSION": "^(.+)$\\;version:\\1",
        "jQuery.fn.tooltip.Constructor.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": [
        "twitter\\.github\\.com/bootstrap",
        "bootstrap[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "(?:/([\\d.]+))?(?:/js)?/bootstrap(?:\\.min)?\\.js\\;version:\\1"
      ],
      "website": "https://getbootstrap.com"
    },
    "Bootstrap Table": {
      "cats": [
        59
      ],
      "html": "<link[^>]+href=\"[^>]*bootstrap-table(?:\\.min)?\\.css",
      "icon": "Bootstrap Table.svg",
      "implies": [
        "Bootstrap",
        "jQuery"
      ],
      "script": "bootstrap-table(?:\\.min)?\\.js",
      "website": "http://bootstrap-table.wenzhixin.net.cn/"
    },
    "Botble CMS": {
      "cats": [
        1,
        6
      ],
      "cookies": {
        "botble_session": ""
      },
      "headers": {
        "CMS-Version": "^(.+)$\\;version:\\1\\;confidence:0"
      },
      "icon": "Botble-CMS.png",
      "implies": "Laravel",
      "website": "https://botble.com"
    },
    "Bounce Exchange": {
      "cats": [
        32
      ],
      "icon": "Bounce Exchange.svg",
      "js": {
        "bouncex": ""
      },
      "script": "^https?://tag\\.bounceexchange\\.com/",
      "website": "http://www.bounceexchange.com"
    },
    "Braintree": {
      "cats": [
        41
      ],
      "icon": "Braintree.svg",
      "js": {
        "Braintree": "",
        "Braintree.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://www.braintreepayments.com"
    },
    "Brightspot": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "^Brightspot$"
      },
      "icon": "Brightspot.svg",
      "implies": "Java",
      "website": "https://www.brightspot.com"
    },
    "BrowserCMS": {
      "cats": [
        1
      ],
      "icon": "BrowserCMS.png",
      "implies": "Ruby",
      "meta": {
        "generator": "BrowserCMS ([\\d.]+)\\;version:\\1"
      },
      "website": "http://browsercms.org"
    },
    "Bubble": {
      "cats": [
        1,
        18
      ],
      "headers": {
        "x-bubble-capacity-limit": "",
        "x-bubble-capacity-used": "",
        "x-bubble-perf": ""
      },
      "icon": "bubble.png",
      "implies": "Node.js",
      "js": {
        "_bubble_page_load_data": "",
        "bubble_environment": "",
        "bubble_hostname_modifier": "",
        "bubble_version": ""
      },
      "website": "http://bubble.is"
    },
    "BugSnag": {
      "cats": [
        10
      ],
      "icon": "BugSnag.png",
      "js": {
        "Bugsnag": "",
        "bugsnag": "",
        "bugsnagClient": ""
      },
      "script": "/bugsnag.*\\.js",
      "website": "http://bugsnag.com"
    },
    "Bugzilla": {
      "cats": [
        13
      ],
      "cookies": {
        "Bugzilla_login_request_cookie": ""
      },
      "cpe": "cpe:/a:mozilla:bugzilla",
      "html": [
        "href=\"enter_bug\\.cgi\">",
        "<main id=\"bugzilla-body\"",
        "<a href=\"https?://www\\.bugzilla\\.org/docs/([0-9.]+)/[^>]+>Help<\\;version:\\1",
        "<span id=\"information\" class=\"header_addl_info\">version ([\\d.]+)<\\;version:\\1"
      ],
      "icon": "Bugzilla.png",
      "implies": "Perl",
      "js": {
        "BUGZILLA": ""
      },
      "meta": {
        "generator": "Bugzilla ?([\\d.]+)?\\;version:\\1"
      },
      "website": "http://www.bugzilla.org"
    },
    "Bulma": {
      "cats": [
        66
      ],
      "html": "<link[^>]+?href=\"[^\"]+bulma(?:\\.min)?\\.css",
      "icon": "Bulma.png",
      "website": "http://bulma.io"
    },
    "Burning Board": {
      "cats": [
        2
      ],
      "html": "<a href=\"[^>]+woltlab\\.com[^<]+<strong>Burning Board",
      "icon": "Burning Board.png",
      "implies": [
        "PHP",
        "Woltlab Community Framework"
      ],
      "website": "http://www.woltlab.com"
    },
    "Business Catalyst": {
      "cats": [
        1
      ],
      "html": "<!-- BC_OBNW -->",
      "icon": "Business Catalyst.png",
      "script": "CatalystScripts",
      "website": "http://businesscatalyst.com"
    },
    "BuySellAds": {
      "cats": [
        36
      ],
      "icon": "BuySellAds.png",
      "js": {
        "_bsa": "",
        "_bsaPRO": "",
        "_bsap": "",
        "_bsap_serving_callback": ""
      },
      "script": "^https?://s\\d\\.buysellads\\.com/",
      "website": "http://buysellads.com"
    },
    "CCV Shop": {
      "cats": [
        6
      ],
      "icon": "ccvshop.png",
      "script": "/website/JavaScript/Vertoshop\\.js",
      "website": "https://ccvshop.be"
    },
    "CDN77": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^CDN77-Turbo$"
      },
      "icon": "CDN77.png",
      "website": "https://www.cdn77.com"
    },
    "CFML": {
      "cats": [
        27
      ],
      "icon": "CFML.png",
      "website": "http://adobe.com/products/coldfusion-family.html"
    },
    "CKEditor": {
      "cats": [
        24
      ],
      "cpe": "cpe:/a:ckeditor:ckeditor",
      "icon": "CKEditor.png",
      "js": {
        "CKEDITOR": "",
        "CKEDITOR.version": "^(.+)$\\;version:\\1",
        "CKEDITOR_BASEPATH": ""
      },
      "website": "http://ckeditor.com"
    },
    "CMS Made Simple": {
      "cats": [
        1
      ],
      "cookies": {
        "CMSSESSID": ""
      },
      "cpe": "cpe:/a:cmsmadesimple:cms_made_simple",
      "icon": "CMS Made Simple.png",
      "implies": "PHP",
      "meta": {
        "generator": "CMS Made Simple"
      },
      "website": "http://cmsmadesimple.org"
    },
    "CMSimple": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:cmsimple:cmsimple",
      "implies": "PHP",
      "meta": {
        "generator": "CMSimple( [\\d.]+)?\\;version:\\1"
      },
      "website": "http://www.cmsimple.org/en"
    },
    "CNZZ": {
      "cats": [
        10
      ],
      "icon": "cnzz.png",
      "js": {
        "cnzz_protocol": "\\;confidence:99"
      },
      "website": "https://web.umeng.com/"
    },
    "CPG Dragonfly": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "^Dragonfly CMS"
      },
      "icon": "CPG Dragonfly.png",
      "implies": "PHP",
      "meta": {
        "generator": "CPG Dragonfly"
      },
      "website": "http://dragonflycms.org"
    },
    "CS Cart": {
      "cats": [
        6
      ],
      "html": [
        "&nbsp;Powered by (?:<a href=[^>]+cs-cart\\.com|CS-Cart)",
        "\\.cm-noscript[^>]+</style>"
      ],
      "icon": "CS Cart.png",
      "implies": "PHP",
      "js": {
        "fn_compare_strings": ""
      },
      "website": "http://www.cs-cart.com"
    },
    "CacheFly": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^CFS ",
        "X-CF1": "",
        "X-CF2": ""
      },
      "icon": "CacheFly.png",
      "website": "http://www.cachefly.com"
    },
    "Caddy": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Caddy$"
      },
      "icon": "caddy.svg",
      "implies": "Go",
      "website": "http://caddyserver.com"
    },
    "Cafe24": {
      "cats": [
        6
      ],
      "icon": "Cafe24.png",
      "js": {
        "EC_GLOBAL_DATETIME": "",
        "EC_GLOBAL_INFO": "",
        "EC_ROOT_DOMAIN": ""
      },
      "website": "https://www.cafe24.com"
    },
    "CakePHP": {
      "cats": [
        18
      ],
      "cookies": {
        "cakephp": ""
      },
      "cpe": "cpe:/a:cakephp:cakephp",
      "icon": "CakePHP.png",
      "implies": "PHP",
      "meta": {
        "application-name": "CakePHP"
      },
      "website": "http://cakephp.org"
    },
    "Captch Me": {
      "cats": [
        16,
        36
      ],
      "icon": "Captch Me.svg",
      "js": {
        "Captchme": ""
      },
      "script": "^https?://api\\.captchme\\.net/",
      "website": "http://captchme.com"
    },
    "Carbon Ads": {
      "cats": [
        36
      ],
      "html": "<[a-z]+ [^>]*id=\"carbonads-container\"",
      "icon": "Carbon Ads.png",
      "js": {
        "_carbonads": ""
      },
      "script": "carbonads\\.com",
      "website": "http://carbonads.net"
    },
    "Cargo": {
      "cats": [
        1
      ],
      "html": "<link [^>]+Cargo feed",
      "icon": "Cargo.png",
      "implies": "PHP",
      "meta": {
        "cargo_title": ""
      },
      "script": "/cargo\\.",
      "website": "http://cargocollective.com"
    },
    "Catberry.js": {
      "cats": [
        12,
        18
      ],
      "headers": {
        "X-Powered-By": "Catberry"
      },
      "icon": "Catberry.js.png",
      "implies": "Node.js",
      "js": {
        "catberry": "",
        "catberry.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://catberry.github.io/"
    },
    "Cecil": {
      "cats": [
        57
      ],
      "icon": "Cecil.png",
      "meta": {
        "generator": "^Cecil(?: ([0-9.]+))?$\\;version:\\1"
      },
      "website": "https://cecil.app"
    },
    "CentOS": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:centos:centos",
      "headers": {
        "Server": "CentOS",
        "X-Powered-By": "CentOS"
      },
      "icon": "CentOS.png",
      "website": "http://centos.org"
    },
    "Ceres": {
      "cats": [
        6
      ],
      "headers": {
        "X-Plenty-Shop": "Ceres"
      },
      "icon": "Ceres.svg",
      "website": "https://www.plentymarkets.com/"
    },
    "Chamilo": {
      "cats": [
        21
      ],
      "cpe": "cpe:/a:chamilo:chamilo_lms",
      "headers": {
        "X-Powered-By": "Chamilo ([\\d.]+)\\;version:\\1"
      },
      "html": "\">Chamilo ([\\d.]+)</a>\\;version:\\1",
      "icon": "Chamilo.png",
      "implies": "PHP",
      "meta": {
        "generator": "Chamilo ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.chamilo.org"
    },
    "Chart.js": {
      "cats": [
        25
      ],
      "icon": "Chart.js.svg",
      "js": {
        "Chart": "\\;confidence:50",
        "Chart.defaults.doughnut": "",
        "chart.ctx.bezierCurveTo": ""
      },
      "script": [
        "/Chart(?:\\.bundle)?(?:\\.min)?\\.js\\;confidence:75",
        "chartjs\\.org/dist/([\\d.]+(?:-[^/]+)?|master|latest)/Chart.*\\.js\\;version:\\1",
        "cdnjs\\.cloudflare\\.com/ajax/libs/Chart\\.js/([\\d.]+(?:-[^/]+)?)/Chart.*\\.js\\;version:\\1",
        "cdn\\.jsdelivr\\.net/(?:npm|gh/chartjs)/chart\\.js@([\\d.]+(?:-[^/]+)?|latest)/dist/Chart.*\\.js\\;version:\\1"
      ],
      "website": "https://www.chartjs.org"
    },
    "Chartbeat": {
      "cats": [
        10
      ],
      "icon": "Chartbeat.png",
      "js": {
        "_sf_async_config": "",
        "_sf_endpt": ""
      },
      "script": "chartbeat\\.js",
      "website": "http://chartbeat.com"
    },
    "Cherokee": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:cherokee-project:cherokee",
      "headers": {
        "Server": "^Cherokee(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Cherokee.png",
      "website": "http://www.cherokee-project.com"
    },
    "CherryPy": {
      "cats": [
        18,
        22
      ],
      "cpe": "cpe:/a:cherrypy:cherrypy",
      "headers": {
        "Server": "CherryPy\\/?([\\d\\.]+)?\\;version:\\1"
      },
      "icon": "CherryPy.png",
      "implies": "Python",
      "website": "http://www.cherrypy.org"
    },
    "Chevereto": {
      "cats": [
        7
      ],
      "html": "Powered by <a href=\"https?://chevereto\\.com\">",
      "icon": "chevereto.png",
      "implies": "PHP",
      "meta": {
        "generator": "^Chevereto ?([0-9.]+)?$\\;version:\\1"
      },
      "script": "/chevereto\\.js",
      "website": "https://chevereto.com/"
    },
    "Chitika": {
      "cats": [
        36
      ],
      "icon": "Chitika.png",
      "js": {
        "ch_client": "",
        "ch_color_site_link": ""
      },
      "script": "scripts\\.chitika\\.net/",
      "website": "http://chitika.com"
    },
    "Chorus": {
      "cats": [
        1
      ],
      "html": "<meta data-chorus-version=",
      "icon": "Chorus.png",
      "website": "https://getchorus.voxmedia.com/"
    },
    "Ckan": {
      "cats": [
        1
      ],
      "headers": {
        "Access-Control-Allow-Headers": "X-CKAN-API-KEY",
        "Link": "<http://ckan\\.org/>; rel=shortlink"
      },
      "icon": "Ckan.png",
      "implies": [
        "Python",
        "Solr",
        "Java",
        "PostgreSQL"
      ],
      "meta": {
        "generator": "^ckan ?([0-9.]+)$\\;version:\\1"
      },
      "website": "http://ckan.org/"
    },
    "Clarity": {
      "cats": [
        66
      ],
      "html": [
        "<clr-main-container",
        "<link [^>]*href=\"[^\"]*clr-ui(?:\\.min)?\\.css"
      ],
      "icon": "clarity.svg",
      "implies": "Angular",
      "js": {
        "ClarityIcons": ""
      },
      "script": "clr-angular(?:\\.umd)?(?:\\.min)?\\.js",
      "website": "https://clarity.design/"
    },
    "ClickFunnels": {
      "cats": [
        32
      ],
      "html": "<meta property=\"cf:app_domain\" content=\"app\\.clickfunnels\\.com\"",
      "icon": "ClickFunnels.png",
      "website": "https://www.clickfunnels.com"
    },
    "ClickHeat": {
      "cats": [
        10
      ],
      "icon": "ClickHeat.png",
      "implies": "PHP",
      "js": {
        "clickHeatServer": ""
      },
      "script": "clickheat.*\\.js",
      "website": "http://www.labsmedia.com/clickheat/index.html"
    },
    "ClickTale": {
      "cats": [
        10
      ],
      "icon": "ClickTale.png",
      "js": {
        "clickTaleStartEventSignal": ""
      },
      "website": "http://www.clicktale.com"
    },
    "Clicky": {
      "cats": [
        10
      ],
      "icon": "Clicky.png",
      "js": {
        "clicky": ""
      },
      "script": "static\\.getclicky\\.com",
      "website": "http://getclicky.com"
    },
    "Clientexec": {
      "cats": [
        6
      ],
      "html": "clientexec\\.[^>]*\\s?=\\s?[^>]*;",
      "icon": "Clientexec.png",
      "website": "http://www.clientexec.com"
    },
    "Clipboard.js": {
      "cats": [
        19
      ],
      "icon": "Clipboard.js.svg",
      "script": "clipboard(?:-([\\d.]+))?(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://clipboardjs.com/"
    },
    "CloudCart": {
      "cats": [
        6
      ],
      "icon": "cloudcart.svg",
      "meta": {
        "author": "^CloudCart LLC$"
      },
      "script": "/cloudcart-(?:assets|storage)/",
      "website": "http://cloudcart.com"
    },
    "CloudSuite": {
      "cats": [
        6
      ],
      "cookies": {
        "cs_secure_session": ""
      },
      "icon": "CloudSuite.svg",
      "website": "https://cloudsuite.com"
    },
    "Cloudera": {
      "cats": [
        34
      ],
      "headers": {
        "Server": "cloudera"
      },
      "icon": "Cloudera.png",
      "website": "http://www.cloudera.com"
    },
    "Cloudflare": {
      "cats": [
        31
      ],
      "cookies": {
        "__cfduid": ""
      },
      "headers": {
        "Server": "^cloudflare$",
        "cf-cache-status": "",
        "cf-ray": ""
      },
      "icon": "CloudFlare.svg",
      "js": {
        "CloudFlare": ""
      },
      "website": "http://www.cloudflare.com"
    },
    "Coaster CMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:web-feet:coaster_cms",
      "icon": "coaster-cms.png",
      "implies": "Laravel",
      "meta": {
        "generator": "^Coaster CMS v([\\d.]+)$\\;version:\\1"
      },
      "website": "https://www.coastercms.org"
    },
    "CodeIgniter": {
      "cats": [
        18
      ],
      "cookies": {
        "ci_csrf_token": "^(.+)$\\;version:\\1?2+:",
        "ci_session": "",
        "exp_last_activity": "",
        "exp_tracker": ""
      },
      "cpe": "cpe:/a:codeigniter:codeigniter",
      "html": "<input[^>]+name=\"ci_csrf_token\"\\;version:2+",
      "icon": "CodeIgniter.png",
      "implies": "PHP",
      "website": "http://codeigniter.com"
    },
    "CodeMirror": {
      "cats": [
        19
      ],
      "icon": "CodeMirror.png",
      "js": {
        "CodeMirror": "",
        "CodeMirror.version": "^(.+)$\\;version:\\1"
      },
      "website": "http://codemirror.net"
    },
    "CoinHive": {
      "cats": [
        56
      ],
      "icon": "CoinHive.svg",
      "js": {
        "CoinHive": ""
      },
      "script": [
        "\\/(?:coinhive|(authedmine))(?:\\.min)?\\.js\\;version:\\1?opt-in:",
        "coinhive\\.com/lib"
      ],
      "url": "https?://cnhv\\.co/",
      "website": "https://coinhive.com"
    },
    "CoinHive Captcha": {
      "cats": [
        16,
        56
      ],
      "html": "(?:<div[^>]+class=\"coinhive-captcha[^>]+data-key|<div[^>]+data-key[^>]+class=\"coinhive-captcha)",
      "icon": "CoinHive.svg",
      "script": "https?://authedmine\\.com/(?:lib/captcha|captcha)",
      "website": "https://coinhive.com"
    },
    "Coinhave": {
      "cats": [
        56
      ],
      "icon": "coinhave.png",
      "script": "https?://coin-have\\.com/c/[0-9a-zA-Z]{4}\\.js",
      "website": "https://coin-have.com/"
    },
    "Coinimp": {
      "cats": [
        56
      ],
      "icon": "coinimp.png",
      "js": {
        "Client.Anonymous": "\\;confidence:50"
      },
      "script": "https?://www\\.hashing\\.win/scripts/min\\.js",
      "website": "https://www.coinimp.com"
    },
    "ColorMeShop": {
      "cats": [
        6
      ],
      "icon": "colormeshop.png",
      "js": {
        "Colorme": ""
      },
      "website": "https://shop-pro.jp"
    },
    "Comandia": {
      "cats": [
        6
      ],
      "html": "<link[^>]+=['\"]//cdn\\.mycomandia\\.com",
      "icon": "Comandia.svg",
      "js": {
        "Comandia": ""
      },
      "website": "http://comandia.com"
    },
    "Combeenation": {
      "cats": [
        6
      ],
      "html": "<iframe[^>]+src=\"[^>]+portal\\.combeenation\\.com",
      "icon": "Combeenation.png",
      "website": "https://www.combeenation.com"
    },
    "Commerce Server": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:microsoft:commerce_server",
      "headers": {
        "COMMERCE-SERVER-SOFTWARE": ""
      },
      "icon": "Commerce Server.png",
      "implies": "Microsoft ASP.NET",
      "website": "http://commerceserver.net"
    },
    "CompaqHTTPServer": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:hp:compaqhttpserver",
      "headers": {
        "Server": "CompaqHTTPServer\\/?([\\d\\.]+)?\\;version:\\1"
      },
      "icon": "HP.svg",
      "website": "http://www.hp.com"
    },
    "Concrete5": {
      "cats": [
        1
      ],
      "cookies": {
        "CONCRETE5": ""
      },
      "cpe": "cpe:/a:concrete5:concrete5",
      "icon": "Concrete5.png",
      "implies": "PHP",
      "js": {
        "CCM_IMAGE_PATH": ""
      },
      "meta": {
        "generator": "^concrete5 - ([\\d.]+)$\\;version:\\1"
      },
      "script": "/concrete/js/",
      "website": "https://concrete5.org"
    },
    "Contao": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:contao:contao_cms",
      "html": [
        "<!--[^>]+powered by (?:TYPOlight|Contao)[^>]*-->",
        "<link[^>]+(?:typolight|contao)\\.css"
      ],
      "icon": "Contao.png",
      "implies": "PHP",
      "meta": {
        "generator": "^Contao Open Source CMS$"
      },
      "website": "http://contao.org"
    },
    "Contenido": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:contenido:contendio",
      "icon": "Contenido.png",
      "implies": "PHP",
      "meta": {
        "generator": "Contenido ([\\d.]+)\\;version:\\1"
      },
      "website": "http://contenido.org/en"
    },
    "Contensis": {
      "cats": [
        1
      ],
      "icon": "Contensis.png",
      "implies": [
        "Java",
        "CFML"
      ],
      "meta": {
        "generator": "Contensis CMS Version ([\\d.]+)\\;version:\\1"
      },
      "website": "https://zengenti.com/en-gb/products/contensis"
    },
    "ContentBox": {
      "cats": [
        1,
        11
      ],
      "icon": "ContentBox.png",
      "implies": "Adobe ColdFusion",
      "meta": {
        "generator": "ContentBox powered by ColdBox"
      },
      "website": "http://www.gocontentbox.org"
    },
    "Contentful": {
      "cats": [
        1
      ],
      "html": "<[^>]+(?:https?:)?//(?:assets|downloads|images|videos)\\.(?:ct?fassets\\.net|contentful\\.com)",
      "icon": "Contentful.svg",
      "website": "http://www.contentful.com"
    },
    "ConversionLab": {
      "cats": [
        10
      ],
      "icon": "ConversionLab.png",
      "script": "conversionlab\\.trackset\\.com/track/tsend\\.js",
      "website": "http://www.trackset.it/conversionlab"
    },
    "Coppermine": {
      "cats": [
        7
      ],
      "cpe": "cpe:/a:coppermine-gallery:coppermine_photo_gallery",
      "html": "<!--Coppermine Photo Gallery ([\\d.]+)\\;version:\\1",
      "icon": "Coppermine.png",
      "implies": "PHP",
      "website": "http://coppermine-gallery.net"
    },
    "Cosmoshop": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:cosmoshop:cosmoshop",
      "icon": "Cosmoshop.png",
      "script": "cosmoshop_functions\\.js",
      "website": "http://cosmoshop.de"
    },
    "Cotonti": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:cotonti:cotonti_siena",
      "icon": "Cotonti.png",
      "implies": "PHP",
      "meta": {
        "generator": "Cotonti"
      },
      "website": "http://www.cotonti.com"
    },
    "CouchDB": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:apache:couchdb",
      "headers": {
        "Server": "CouchDB/([\\d.]+)\\;version:\\1"
      },
      "icon": "CouchDB.png",
      "website": "http://couchdb.apache.org"
    },
    "Countly": {
      "cats": [
        10
      ],
      "icon": "Countly.png",
      "js": {
        "Countly": ""
      },
      "website": "https://count.ly"
    },
    "Cowboy": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Cowboy$"
      },
      "icon": "Cowboy.png",
      "implies": "Erlang",
      "website": "http://ninenines.eu"
    },
    "CppCMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "^CppCMS/([\\d.]+)$\\;version:\\1"
      },
      "icon": "CppCMS.png",
      "website": "http://cppcms.com"
    },
    "Craft CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "CraftSessionId": ""
      },
      "cpe": "cpe:/a:craftcms:craft_cms",
      "headers": {
        "X-Powered-By": "\\bCraft CMS\\b"
      },
      "icon": "Craft CMS.svg",
      "implies": "Yii",
      "website": "https://craftcms.com"
    },
    "Craft Commerce": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "\\bCraft Commerce\\b"
      },
      "icon": "Craft CMS.svg",
      "implies": "Craft CMS",
      "website": "https://craftcommerce.com"
    },
    "Crazy Egg": {
      "cats": [
        10
      ],
      "icon": "Crazy Egg.png",
      "js": {
        "CE2": ""
      },
      "script": "script\\.crazyegg\\.com/pages/scripts/\\d+/\\d+\\.js",
      "website": "http://crazyegg.com"
    },
    "Criteo": {
      "cats": [
        36
      ],
      "icon": "Criteo.svg",
      "js": {
        "Criteo": "",
        "criteo_pubtag": "",
        "criteo_q": ""
      },
      "script": [
        "//(?:cas\\.criteo\\.com|(?:[^/]\\.)?criteo\\.net)/",
        "//static\\.criteo\\.net/js/ld/ld\\.js"
      ],
      "website": "http://criteo.com"
    },
    "Cross Pixel": {
      "cats": [
        10
      ],
      "icon": "Cross Pixel.png",
      "js": {
        "cp_C4w1ldN2d9PmVrkN": ""
      },
      "script": "tag\\.crsspxl\\.com/s1\\.js",
      "website": "http://datadesk.crsspxl.com"
    },
    "CrossBox": {
      "cats": [
        30
      ],
      "headers": {
        "server": "CBX-WS"
      },
      "icon": "CrossBox.png",
      "website": "https://crossbox.io"
    },
    "Crypto-Loot": {
      "cats": [
        56
      ],
      "icon": "Crypto-Loot.png",
      "js": {
        "CRLT.CONFIG.ASMJS_NAME": "",
        "CryptoLoot": ""
      },
      "script": [
        "^/crypto-loot\\.com/lib/",
        "^/webmine\\.pro/",
        "^/cryptoloot\\.pro/",
        "/crlt\\.js\\;confidence:75"
      ],
      "website": "https://crypto-loot.com/"
    },
    "CubeCart": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:cubecart:cubecart",
      "html": "(?:Powered by <a href=[^>]+cubecart\\.com|<p[^>]+>Powered by CubeCart)",
      "icon": "CubeCart.png",
      "implies": "PHP",
      "meta": {
        "generator": "cubecart"
      },
      "website": "http://www.cubecart.com"
    },
    "Cufon": {
      "cats": [
        17
      ],
      "icon": "Cufon.png",
      "js": {
        "Cufon": ""
      },
      "script": "cufon-yui\\.js",
      "website": "http://cufon.shoqolate.com"
    },
    "D3": {
      "cats": [
        25
      ],
      "cpe": "cpe:/a:d3.js_project:d3.js",
      "icon": "D3.png",
      "js": {
        "d3.version": "^(.+)$\\;version:\\1"
      },
      "script": "/d3(?:\\. v\\d+)?(?:\\.min)?\\.js",
      "website": "http://d3js.org"
    },
    "DERAK.CLOUD": {
      "cats": [
        31
      ],
      "cookies": {
        "__derak_auth": "",
        "__derak_user": ""
      },
      "headers": {
        "Derak-Umbrage": "",
        "Server": "^DERAK\\.CLOUD$"
      },
      "icon": "DerakCloud.png",
      "js": {
        "derakCloud.init": ""
      },
      "website": "https://derak.cloud"
    },
    "DHTMLX": {
      "cats": [
        59
      ],
      "icon": "DHTMLX.png",
      "script": "dhtmlxcommon\\.js",
      "website": "http://dhtmlx.com"
    },
    "DM Polopoly": {
      "cats": [
        1
      ],
      "html": "<(?:link [^>]*href|img [^>]*src)=\"/polopoly_fs/",
      "icon": "DM Polopoly.png",
      "implies": "Java",
      "website": "http://www.atex.com/products/dm-polopoly"
    },
    "DNN": {
      "cats": [
        1
      ],
      "cookies": {
        "DotNetNukeAnonymous": ""
      },
      "cpe": "cpe:/a:dnnsoftware:dotnetnuke",
      "headers": {
        "Cookie": "dnn_IsMobile=",
        "DNNOutputCache": "",
        "X-Compressed-By": "DotNetNuke"
      },
      "html": [
        "<!-- by DotNetNuke Corporation",
        "<!-- DNN Platform"
      ],
      "icon": "DNN.png",
      "implies": "Microsoft ASP.NET",
      "js": {
        "DotNetNuke": "",
        "dnn.apiversion": "^(.+)$\\;version:\\1"
      },
      "meta": {
        "generator": "DotNetNuke"
      },
      "script": [
        "/js/dnncore\\.js",
        "/js/dnn\\.js"
      ],
      "website": "http://dnnsoftware.com"
    },
    "DTG": {
      "cats": [
        1
      ],
      "html": [
        "<a[^>]+Site Powered by DTG"
      ],
      "icon": "DTG.png",
      "implies": "Mono.net",
      "website": "https://www.dtg.nl"
    },
    "Dancer": {
      "cats": [
        18
      ],
      "headers": {
        "Server": "Perl Dancer ([\\d.]+)\\;version:\\1",
        "X-Powered-By": "Perl Dancer ([\\d.]+)\\;version:\\1"
      },
      "icon": "Dancer.png",
      "implies": "Perl",
      "website": "http://perldancer.org"
    },
    "Danneo CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "CMS Danneo ([\\d.]+)\\;version:\\1"
      },
      "icon": "Danneo CMS.png",
      "implies": [
        "Apache",
        "PHP"
      ],
      "meta": {
        "generator": "Danneo CMS ([\\d.]+)\\;version:\\1"
      },
      "website": "http://danneo.com"
    },
    "Dart": {
      "cats": [
        27
      ],
      "excludes": [
        "Angular",
        "AngularJS"
      ],
      "html": "/(?:<script)[^>]+(?:type=\"application/dart\")/",
      "icon": "Dart.svg",
      "implies": "AngularDart",
      "js": {
        "___dart__$dart_dartObject_ZxYxX_0_": "",
        "___dart_dispatch_record_ZxYxX_0_": ""
      },
      "script": [
        "/(?:\\.)?(?:dart)(?:\\.js)?/",
        "packages/browser/dart\\.js"
      ],
      "website": "https://www.dartlang.org"
    },
    "Darwin": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Darwin",
        "X-Powered-By": "Darwin"
      },
      "icon": "Apple.svg",
      "website": "https://opensource.apple.com"
    },
    "DataLife Engine": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:dleviet:datalife_engine",
      "icon": "DataLife Engine.png",
      "implies": [
        "PHP",
        "Apache"
      ],
      "js": {
        "dle_root": ""
      },
      "meta": {
        "generator": "DataLife Engine"
      },
      "website": "https://dle-news.ru"
    },
    "DataTables": {
      "cats": [
        59
      ],
      "icon": "DataTables.png",
      "implies": "jQuery",
      "script": "dataTables.*\\.js",
      "website": "http://datatables.net"
    },
    "Datadome": {
      "cats": [
        19
      ],
      "cookies": {
        "datadome": ""
      },
      "headers": {
        "Server": "^DataDome$",
        "X-DataDome": "",
        "X-DataDome-CID": ""
      },
      "icon": "datadome.png",
      "script": "^https://ct\\.datadome\\.co/[a-z]\\.js$",
      "website": "https://datadome.co/"
    },
    "DatoCMS": {
      "cats": [
        1
      ],
      "html": "<[^>]+https://www\\.datocms-assets\\.com",
      "icon": "datocms.svg",
      "website": "https://www.datocms.com"
    },
    "Day.js": {
      "cats": [
        59
      ],
      "icon": "Day.js.svg",
      "js": {
        "dayjs": ""
      },
      "website": "https://github.com/iamkun/dayjs"
    },
    "Debian": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:debian:debian_linux",
      "headers": {
        "Server": "Debian",
        "X-Powered-By": "(?:Debian|dotdeb|(potato|woody|sarge|etch|lenny|squeeze|wheezy|jessie|stretch|buster|sid))\\;version:\\1"
      },
      "icon": "Debian.png",
      "website": "https://debian.org"
    },
    "DedeCMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:dedecms:dedecms",
      "icon": "DedeCMS.png",
      "implies": "PHP",
      "js": {
        "DedeContainer": ""
      },
      "script": "dedeajax",
      "website": "http://dedecms.com"
    },
    "DirectAdmin": {
      "cats": [
        9
      ],
      "cpe": "cpe:/a:directadmin:directadmin",
      "headers": {
        "Server": "DirectAdmin Daemon v([\\d.]+)\\;version:\\1"
      },
      "html": "<a[^>]+>DirectAdmin</a> Web Control Panel",
      "icon": "DirectAdmin.png",
      "implies": [
        "PHP",
        "Apache"
      ],
      "website": "https://www.directadmin.com"
    },
    "Discourse": {
      "cats": [
        2
      ],
      "icon": "Discourse.png",
      "implies": "Ruby on Rails",
      "js": {
        "Discourse": ""
      },
      "meta": {
        "generator": "Discourse(?: ?/?([\\d.]+\\d))?\\;version:\\1"
      },
      "website": "https://discourse.org"
    },
    "Discuz! X": {
      "cats": [
        2
      ],
      "icon": "Discuz X.png",
      "implies": "PHP",
      "js": {
        "DISCUZCODE": "",
        "discuzVersion": "^(.+)$\\;version:\\1",
        "discuz_uid": ""
      },
      "meta": {
        "generator": "Discuz! X([\\d\\.]+)?\\;version:\\1"
      },
      "website": "http://www.discuz.net"
    },
    "Disqus": {
      "cats": [
        15
      ],
      "cpe": "cpe:/a:disqus:disqus_comment_system",
      "html": "<div[^>]+id=\"disqus_thread\"",
      "icon": "Disqus.svg",
      "js": {
        "DISQUS": "",
        "disqus_shortname": "",
        "disqus_url": ""
      },
      "script": "disqus_url",
      "website": "https://disqus.com"
    },
    "Django": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:djangoproject:django",
      "html": "(?:powered by <a[^>]+>Django ?([\\d.]+)?<\\/a>|<input[^>]*name=[\"']csrfmiddlewaretoken[\"'][^>]*>)\\;version:\\1",
      "icon": "Django.png",
      "implies": "Python",
      "js": {
        "__admin_media_prefix__": "",
        "django": ""
      },
      "website": "https://djangoproject.com"
    },
    "Docker": {
      "cats": [
        60
      ],
      "cpe": "cpe:/a:docker:engine",
      "html": "<!-- This comment is expected by the docker HEALTHCHECK  -->",
      "icon": "Docker.svg",
      "website": "https://www.docker.com/"
    },
    "Docusaurus": {
      "cats": [
        4
      ],
      "icon": "docusaurus.svg",
      "implies": [
        "React",
        "webpack"
      ],
      "js": {
        "search.indexName": ""
      },
      "meta": {
        "generator": "^Docusaurus$"
      },
      "website": "https://docusaurus.io/"
    },
    "Dojo": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:dojotoolkit:dojo",
      "icon": "Dojo.png",
      "js": {
        "dojo": "",
        "dojo.version.major": "^(.+)$\\;version:\\1"
      },
      "script": "([\\d.]+)/dojo/dojo(?:\\.xd)?\\.js\\;version:\\1",
      "website": "https://dojotoolkit.org"
    },
    "Dokeos": {
      "cats": [
        21
      ],
      "headers": {
        "X-Powered-By": "Dokeos"
      },
      "html": "(?:Portal <a[^>]+>Dokeos|@import \"[^\"]+dokeos_blue)",
      "icon": "Dokeos.png",
      "implies": [
        "PHP",
        "Xajax",
        "jQuery",
        "CKEditor"
      ],
      "meta": {
        "generator": "Dokeos"
      },
      "website": "https://dokeos.com"
    },
    "DokuWiki": {
      "cats": [
        8
      ],
      "cookies": {
        "DokuWiki": ""
      },
      "cpe": "cpe:/a:dokuwiki:dokuwiki",
      "html": [
        "<div[^>]+id=\"dokuwiki__>",
        "<a[^>]+href=\"#dokuwiki__"
      ],
      "icon": "DokuWiki.png",
      "implies": "PHP",
      "meta": {
        "generator": "^DokuWiki( Release [\\d-]+)?\\;version:\\1"
      },
      "website": "https://www.dokuwiki.org"
    },
    "Dotclear": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:dotclear:dotclear",
      "headers": {
        "X-Dotclear-Static-Cache": ""
      },
      "icon": "Dotclear.png",
      "implies": "PHP",
      "website": "http://dotclear.org"
    },
    "DoubleClick Ad Exchange (AdX)": {
      "cats": [
        36
      ],
      "icon": "DoubleClick.svg",
      "script": [
        "googlesyndication\\.com/pagead/show_ads\\.js",
        "tpc\\.googlesyndication\\.com/safeframe",
        "googlesyndication\\.com.*abg\\.js"
      ],
      "website": "http://www.doubleclickbygoogle.com/solutions/digital-marketing/ad-exchange/"
    },
    "DoubleClick Campaign Manager (DCM)": {
      "cats": [
        36
      ],
      "icon": "DoubleClick.svg",
      "script": "2mdn\\.net",
      "website": "http://www.doubleclickbygoogle.com/solutions/digital-marketing/campaign-manager/"
    },
    "DoubleClick Floodlight": {
      "cats": [
        36
      ],
      "icon": "DoubleClick.svg",
      "script": "https?://fls\\.doubleclick\\.net",
      "website": "http://support.google.com/ds/answer/6029713?hl=en"
    },
    "DoubleClick for Publishers (DFP)": {
      "cats": [
        36
      ],
      "icon": "DoubleClick.svg",
      "script": "googletagservices\\.com/tag/js/gpt(?:_mobile)?\\.js",
      "website": "http://www.google.com/dfp"
    },
    "DovetailWRP": {
      "cats": [
        1
      ],
      "html": "<link[^>]* href=\"\\/DovetailWRP\\/",
      "icon": "DovetailWRP.png",
      "implies": "Microsoft ASP.NET",
      "script": "\\/DovetailWRP\\/",
      "website": "http://www.dovetailinternet.com"
    },
    "Doxygen": {
      "cats": [
        4
      ],
      "cpe": "cpe:/a:doxygen:doxygen",
      "html": "(?:<!-- Generated by Doxygen ([\\d.]+)|<link[^>]+doxygen\\.css)\\;version:\\1",
      "icon": "Doxygen.png",
      "meta": {
        "generator": "Doxygen ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.doxygen.nl/"
    },
    "DreamWeaver": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:adobe:dreamweaver",
      "html": "<!--[^>]*(?:InstanceBeginEditable|Dreamweaver([^>]+)target|DWLayoutDefaultTable)\\;version:\\1",
      "icon": "DreamWeaver.png",
      "js": {
        "MM_preloadImages": "",
        "MM_showHideLayers": "",
        "MM_showMenu": ""
      },
      "website": "https://www.adobe.com/products/dreamweaver.html"
    },
    "Drupal": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:drupal:drupal",
      "headers": {
        "Expires": "19 Nov 1978",
        "X-Drupal-Cache": "",
        "X-Generator": "^Drupal(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "html": "<(?:link|style)[^>]+\"/sites/(?:default|all)/(?:themes|modules)/",
      "icon": "Drupal.svg",
      "implies": "PHP",
      "js": {
        "Drupal": ""
      },
      "meta": {
        "generator": "^Drupal(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "script": "drupal\\.js",
      "website": "https://drupal.org"
    },
    "Drupal Commerce": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:commerceguys:commerce",
      "html": "<[^>]+(?:id=\"block[_-]commerce[_-]cart[_-]cart|class=\"commerce[_-]product[_-]field)",
      "icon": "Drupal Commerce.png",
      "implies": "Drupal",
      "website": "http://drupalcommerce.org"
    },
    "Duda": {
      "cats": [
        1
      ],
      "html": "<div[^>]*id=\"P6iryBW0Wu\"",
      "icon": "duda.png",
      "js": {
        "SystemID": "^.*DIRECT.*$",
        "version": "^(.*)$\\;version:\\1\\;confidence:0"
      },
      "website": "https://www.duda.co/website-builder"
    },
    "Dynamicweb": {
      "cats": [
        1,
        6,
        10
      ],
      "cookies": {
        "Dynamicweb": ""
      },
      "icon": "Dynamicweb.png",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "Dynamicweb ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.dynamicweb.dk"
    },
    "Dynatrace": {
      "cats": [
        10
      ],
      "headers": {
        "X-dynaTrace-JS-Agent": ""
      },
      "icon": "Dynatrace.png",
      "script": "dtagent.*\\.js",
      "website": "http://dynatrace.com"
    },
    "EC-CUBE": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:lockon:ec-cube",
      "icon": "ec-cube.png",
      "implies": "PHP",
      "script": [
        "eccube\\.js",
        "win_op\\.js"
      ],
      "website": "http://www.ec-cube.net"
    },
    "EKM": {
      "cats": [
        6
      ],
      "cookies": {
        "ekmpowershop": ""
      },
      "icon": "EKM.png",
      "js": {
        "_ekmpinpoint": ""
      },
      "website": "https://www.ekm.com"
    },
    "ELOG": {
      "cats": [
        19
      ],
      "html": "<title>ELOG Logbook Selection</title>",
      "icon": "ELOG.png",
      "website": "http://midas.psi.ch/elog"
    },
    "ELOG HTTP": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "ELOG HTTP ?([\\d.-]+)?\\;version:\\1"
      },
      "icon": "ELOG.png",
      "implies": "ELOG",
      "website": "http://midas.psi.ch/elog"
    },
    "EPages": {
      "cats": [
        6
      ],
      "headers": {
        "X-epages-RequestId": ""
      },
      "icon": "epages.png",
      "js": {
        "epages": ""
      },
      "website": "http://www.epages.com/"
    },
    "EPiServer": {
      "cats": [
        1
      ],
      "cookies": {
        "EPiServer": "",
        "EPiTrace": ""
      },
      "cpe": "cpe:/a:episerver:episerver",
      "icon": "EPiServer.png",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "EPiServer"
      },
      "website": "http://episerver.com"
    },
    "EPrints": {
      "cats": [
        19
      ],
      "icon": "EPrints.png",
      "implies": "Perl",
      "js": {
        "EPJS_menu_template": "",
        "EPrints": ""
      },
      "meta": {
        "generator": "EPrints ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.eprints.org"
    },
    "EasyEngine": {
      "cats": [
        47,
        9
      ],
      "headers": {
        "x-powered-by": "^EasyEngine (.*)$\\;version:\\1"
      },
      "icon": "EasyEngine.png",
      "implies": "Docker",
      "website": "https://easyengine.io"
    },
    "Ecwid": {
      "cats": [
        6
      ],
      "icon": "ecwid.svg",
      "js": {
        "Ecwid": "",
        "EcwidCart": ""
      },
      "script": [
        "https://app\\.multiscreenstore\\.com/script\\.js",
        "https://app\\.ecwid\\.com/script\\.js"
      ],
      "website": "https://www.ecwid.com/"
    },
    "EdgeCast": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^ECD\\s\\(\\S+\\)"
      },
      "icon": "EdgeCast.png",
      "url": "https?://(?:[^/]+\\.)?edgecastcdn\\.net/",
      "website": "http://www.edgecast.com"
    },
    "Elcodi": {
      "cats": [
        6
      ],
      "headers": {
        "X-Elcodi": ""
      },
      "icon": "Elcodi.png",
      "implies": [
        "PHP",
        "Symfony"
      ],
      "website": "http://elcodi.io"
    },
    "Eleanor CMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:eleanor-cms:eleanor_cms",
      "icon": "Eleanor CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "Eleanor"
      },
      "website": "http://eleanor-cms.ru"
    },
    "Element UI": {
      "cats": [
        12
      ],
      "html": [
        "<(?:div|button) class=\"el-(?:table-column|table-filter|popper|pagination|pager|select-group|form|form-item|color-predefine|color-hue-slider|color-svpanel|color-alpha-slider|color-dropdown|color-picker|badge|tree|tree-node|select|message|dialog|checkbox|checkbox-button|checkbox-group|container|steps|carousel|menu|menu-item|submenu|menu-item-group|button|button-group|card|table|select-dropdown|row|tabs|notification|radio|progress|progress-bar|tag|popover|tooltip|cascader|cascader-menus|cascader-menu|time-spinner|spinner|spinner-inner|transfer|transfer-panel|rate|slider|dropdown|dropdown-menu|textarea|input|input-group|popup-parent|radio-group|main|breadcrumb|time-range-picker|date-range-picker|year-table|date-editor|range-editor|time-spinner|date-picker|time-panel|date-table|month-table|picker-panel|collapse|collapse-item|alert|select-dropdown|select-dropdown__empty|select-dropdown__wrap|select-dropdown__list|scrollbar|switch|carousel|upload|upload-dragger|upload-list|upload-cover|aside|input-number|header|message-box|footer|radio-button|step|autocomplete|autocomplete-suggestion|loading-parent|loading-mask|loading-spinner|)"
      ],
      "icon": "ElementUI.svg",
      "implies": "Vue.js",
      "website": "https://element.eleme.io/"
    },
    "Elementor": {
      "cats": [
        51
      ],
      "html": [
        "<div class=(?:\"|')[^\"']*elementor",
        "<section class=(?:\"|')[^\"']*elementor",
        "<link [^>]*href=(?:\"|')[^\"']*elementor/assets",
        "<link [^>]*href=(?:\"|')[^\"']*uploads/elementor/css"
      ],
      "icon": "Elementor.png",
      "implies": "WordPress",
      "js": {
        "elementorFrontend.getElements": ""
      },
      "script": "elementor/assets/js/[^/]+\\.js\\?ver=([\\d.]+)$\\;version:\\1",
      "website": "https://elementor.com"
    },
    "Elm": {
      "cats": [
        27,
        12
      ],
      "icon": "elm.svg",
      "js": {
        "Elm.Main.embed": "\\;version:0.18",
        "Elm.Main.init": "\\;version:0.19"
      },
      "website": "https://elm-lang.org/"
    },
    "Elm-ui": {
      "cats": [
        66
      ],
      "html": "<style>[\\s\\S]*\\.explain > \\.s[\\s\\S]*\\.explain > \\.ctr > \\.s",
      "icon": "elm.svg",
      "implies": "Elm",
      "website": "https://github.com/mdgriffith/elm-ui"
    },
    "Eloqua": {
      "cats": [
        32
      ],
      "icon": "Oracle.png",
      "js": {
        "elqCurESite": "",
        "elqLoad": "",
        "elqSiteID": "",
        "elq_global": ""
      },
      "script": "elqCfg\\.js",
      "website": "http://eloqua.com"
    },
    "EmbedThis Appweb": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:embedthis:appweb",
      "headers": {
        "Server": "Mbedthis-Appweb(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Embedthis.png",
      "website": "http://embedthis.com/appweb"
    },
    "Ember.js": {
      "cats": [
        12
      ],
      "cpe": "cpe:/a:emberjs:ember.js",
      "icon": "Ember.js.png",
      "implies": "Handlebars",
      "js": {
        "Ember": "",
        "Ember.VERSION": "^(.+)$\\;version:\\1"
      },
      "website": "http://emberjs.com"
    },
    "Ensighten": {
      "cats": [
        42
      ],
      "icon": "ensighten.png",
      "script": "//nexus\\.ensighten\\.com/",
      "website": "https://success.ensighten.com/hc/en-us"
    },
    "Envoy": {
      "cats": [
        64
      ],
      "cpe": "cpe:/a:envoyproxy:envoy",
      "headers": {
        "Server": "^envoy$",
        "x-envoy-upstream-service-time": ""
      },
      "icon": "Envoy.png",
      "website": "https://www.envoyproxy.io/"
    },
    "Enyo": {
      "cats": [
        12,
        26
      ],
      "icon": "Enyo.png",
      "js": {
        "enyo": ""
      },
      "script": "enyo\\.js",
      "website": "http://enyojs.com"
    },
    "Epoch": {
      "cats": [
        25
      ],
      "html": "<link[^>]+?href=\"[^\"]+epoch(?:\\.min)?\\.css",
      "implies": "D3",
      "script": "epoch(?:\\.min)?\\.js",
      "website": "https://fastly.github.io/epoch"
    },
    "Epom": {
      "cats": [
        36
      ],
      "icon": "Epom.png",
      "js": {
        "epomCustomParams": ""
      },
      "url": "^https?://(?:[^/]+\\.)?ad(?:op)?shost1\\.com/",
      "website": "http://epom.com"
    },
    "Erlang": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:erlang:erlang%2fotp",
      "headers": {
        "Server": "Erlang( OTP/(?:[\\d.ABR-]+))?\\;version:\\1"
      },
      "icon": "Erlang.png",
      "website": "http://www.erlang.org"
    },
    "Essential JS 2": {
      "cats": [
        12,
        59
      ],
      "html": "<[^>]+ class ?= ?\"(?:e-control|[^\"]+ e-control)(?: )[^\"]* e-lib\\b",
      "icon": "syncfusion.svg",
      "website": "https://www.syncfusion.com/javascript-ui-controls"
    },
    "Etherpad": {
      "cats": [
        24
      ],
      "cpe": "cpe:/a:etherpad:etherpad",
      "headers": {
        "Server": "^Etherpad"
      },
      "icon": "etherpad.png",
      "implies": "Node.js",
      "js": {
        "padeditbar": "",
        "padimpexp": ""
      },
      "script": [
        "/ep_etherpad-lite/"
      ],
      "website": "https://etherpad.org"
    },
    "Exhibit": {
      "cats": [
        25
      ],
      "icon": "Exhibit.png",
      "js": {
        "Exhibit": "",
        "Exhibit.version": "^(.+)$\\;version:\\1"
      },
      "script": "exhibit.*\\.js",
      "website": "http://simile-widgets.org/exhibit/"
    },
    "ExpertRec": {
      "cats": [
        29
      ],
      "icon": "ExpertRec.png",
      "script": "cse\\.expertrec\\.com/api/js/ci_common\\.js\\?id=.*$",
      "website": "https://expertrec.com"
    },
    "Express": {
      "cats": [
        18,
        22
      ],
      "cpe": "cpe:/a:expressjs:express",
      "headers": {
        "X-Powered-By": "^Express$"
      },
      "icon": "Express.png",
      "implies": "Node.js",
      "website": "http://expressjs.com"
    },
    "ExpressionEngine": {
      "cats": [
        1
      ],
      "cookies": {
        "exp_csrf_token": "",
        "exp_last_activity": "",
        "exp_tracker": ""
      },
      "cpe": "cpe:/a:ellislab:expressionengine",
      "icon": "ExpressionEngine.png",
      "implies": "PHP",
      "website": "http://expressionengine.com"
    },
    "ExtJS": {
      "cats": [
        12
      ],
      "icon": "ExtJS.png",
      "js": {
        "Ext": "",
        "Ext.version": "^(.+)$\\;version:\\1",
        "Ext.versions.extjs.version": "^(.+)$\\;version:\\1"
      },
      "script": "ext-base\\.js",
      "website": "https://www.sencha.com"
    },
    "F5 BigIP": {
      "cats": [
        64
      ],
      "cookies": {
        "F5_HT_shrinked": "",
        "F5_ST": "",
        "F5_fullWT": "",
        "LastMRH_Session": "",
        "MRHSHint": "",
        "MRHSequence": "",
        "MRHSession": "",
        "TIN": ""
      },
      "headers": {
        "server": "^big-?ip$"
      },
      "icon": "F5.png",
      "website": "https://www.f5.com/products/big-ip-services"
    },
    "FAST ESP": {
      "cats": [
        29
      ],
      "html": "<form[^>]+id=\"fastsearch\"",
      "icon": "FAST ESP.png",
      "website": "http://microsoft.com/enterprisesearch"
    },
    "FAST Search for SharePoint": {
      "cats": [
        29
      ],
      "html": "<input[^>]+ name=\"ParametricSearch",
      "icon": "FAST Search for SharePoint.png",
      "implies": [
        "Microsoft SharePoint",
        "Microsoft ASP.NET"
      ],
      "url": "Pages/SearchResults\\.aspx\\?k=",
      "website": "http://sharepoint.microsoft.com/en-us/product/capabilities/search/Pages/Fast-Search.aspx"
    },
    "Facebook": {
      "cats": [
        5
      ],
      "icon": "Facebook.svg",
      "script": "//connect\\.facebook\\.net/[^/]*/[a-z]*\\.js",
      "website": "http://facebook.com"
    },
    "Fact Finder": {
      "cats": [
        29
      ],
      "html": "<!-- Factfinder",
      "icon": "Fact Finder.png",
      "script": "Suggest\\.ff",
      "url": "(?:/ViewParametricSearch|ffsuggest\\.[a-z]htm)",
      "website": "http://fact-finder.com"
    },
    "FancyBox": {
      "cats": [
        59
      ],
      "icon": "FancyBox.png",
      "implies": "jQuery",
      "js": {
        "$.fancybox.version": "^(.+)$\\;version:\\1"
      },
      "script": "jquery\\.fancybox(?:\\.pack|\\.min)?\\.js(?:\\?v=([\\d.]+))?$\\;version:\\1",
      "website": "http://fancyapps.com/fancybox"
    },
    "FaraPy": {
      "cats": [
        1
      ],
      "html": "<!-- Powered by FaraPy.",
      "icon": "FaraPy.png",
      "website": "https://faral.tech"
    },
    "Fastcommerce": {
      "cats": [
        6
      ],
      "icon": "Fastcommerce.png",
      "meta": {
        "generator": "^Fastcommerce"
      },
      "website": "https://www.fastcommerce.com.br"
    },
    "Fastly": {
      "cats": [
        31
      ],
      "headers": {
        "Fastly-Debug-Digest": "",
        "Vary": "Fastly-SSL",
        "X-Fastly-Request-ID": "",
        "x-via-fastly:": ""
      },
      "icon": "Fastly.svg",
      "website": "https://www.fastly.com"
    },
    "Fastspring": {
      "cats": [
        6
      ],
      "html": [
        "<a [^>]*href=\"https?://sites\\.fastspring\\.com",
        "<form [^>]*action=\"https?://sites\\.fastspring\\.com"
      ],
      "icon": "fastspring.png",
      "website": "https://fastspring.com"
    },
    "Fat-Free Framework": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "^Fat-Free Framework$"
      },
      "icon": "Fat-Free Framework.png",
      "implies": "PHP",
      "website": "http://fatfreeframework.com"
    },
    "Fbits": {
      "cats": [
        6
      ],
      "icon": "Fbits.png",
      "js": {
        "fbits": ""
      },
      "website": "https://www.traycorp.com.br"
    },
    "Fedora": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:fedoraproject:fedora",
      "headers": {
        "Server": "Fedora"
      },
      "icon": "Fedora.png",
      "website": "http://fedoraproject.org"
    },
    "Fingerprintjs": {
      "cats": [
        59
      ],
      "js": {
        "Fingerprint": "(\\d)?$\\;version:\\1",
        "Fingerprint2": "",
        "Fingerprint2.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "fingerprint(\\d)?(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://valve.github.io/fingerprintjs2/"
    },
    "Firebase": {
      "cats": [
        34
      ],
      "icon": "Firebase.png",
      "js": {
        "firebase.SDK_VERSION": "([\\d.]+)$\\;version:\\1"
      },
      "script": "/(?:([\\d.]+)/)?firebase(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://firebase.com"
    },
    "Fireblade": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "fbs"
      },
      "icon": "Fireblade.png",
      "website": "http://fireblade.com"
    },
    "Flarum": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:flarum:flarum",
      "html": "<div id=\"flarum-loading\"",
      "icon": "flarum.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "app.cache.discussionList": "",
        "app.forum.freshness": ""
      },
      "website": "http://flarum.org/"
    },
    "Flask": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "Server": "Werkzeug/?([\\d\\.]+)?\\;version:\\1"
      },
      "icon": "Flask.png",
      "implies": "Python",
      "website": "http://flask.pocoo.org"
    },
    "Flat UI": {
      "cats": [
        66
      ],
      "html": "<link[^>]* href=[^>]+flat-ui(?:\\.min)?\\.css",
      "icon": "Flat UI.png",
      "implies": "Bootstrap",
      "website": "https://designmodo.github.io/Flat-UI/"
    },
    "FlexCMP": {
      "cats": [
        1
      ],
      "headers": {
        "X-Flex-Lang": "",
        "X-Powered-By": "FlexCMP.+\\[v\\. ([\\d.]+)\\;version:\\1"
      },
      "html": "<!--[^>]+FlexCMP[^>v]+v\\. ([\\d.]+)\\;version:\\1",
      "icon": "FlexCMP.png",
      "meta": {
        "generator": "^FlexCMP"
      },
      "website": "http://www.flexcmp.com/cms/home"
    },
    "FlexSlider": {
      "cats": [
        5
      ],
      "icon": "FlexSlider.png",
      "implies": "jQuery",
      "script": [
        "jquery\\.flexslider(?:\\.min)?\\.js$"
      ],
      "website": "https://woocommerce.com/flexslider/"
    },
    "Flickity": {
      "cats": [
        59
      ],
      "js": {
        "Flickity": ""
      },
      "script": "/flickity(?:\\.pkgd)?(?:\\.min)?\\.js",
      "website": "https://flickity.metafizzy.co/"
    },
    "FluxBB": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:fluxbb:fluxbb",
      "html": "<p id=\"poweredby\">[^<]+<a href=\"https?://fluxbb\\.org/\">",
      "icon": "FluxBB.png",
      "implies": "PHP",
      "website": "https://fluxbb.org"
    },
    "Flyspray": {
      "cats": [
        13
      ],
      "cookies": {
        "flyspray_project": ""
      },
      "html": "(?:<a[^>]+>Powered by Flyspray|<map id=\"projectsearchform)",
      "icon": "Flyspray.png",
      "implies": "PHP",
      "website": "http://flyspray.org"
    },
    "Flywheel": {
      "cats": [
        62
      ],
      "headers": {
        "x-fw-hash": "",
        "x-fw-serve": "",
        "x-fw-server": "^Flywheel(?:/([\\d.]+))?\\;version:\\1",
        "x-fw-static": "",
        "x-fw-type": ""
      },
      "icon": "flywheel.svg",
      "implies": "WordPress",
      "website": "https://getflywheel.com"
    },
    "Font Awesome": {
      "cats": [
        17
      ],
      "html": [
        "<link[^>]* href=[^>]+(?:([\\d.]+)/)?(?:css/)?font-awesome(?:\\.min)?\\.css\\;version:\\1",
        "<link[^>]* href=[^>]*?(?:F|f)o(?:n|r)t-?(?:A|a)wesome(?:[^>]*?([0-9a-fA-F]{7,40}|[\\d]+(?:.[\\d]+(?:.[\\d]+)?)?)|)\\;version:\\1"
      ],
      "icon": "font-awesome.svg",
      "script": "(?:F|f)o(?:n|r)t-?(?:A|a)wesome(?:.*?([0-9a-fA-F]{7,40}|[\\d]+(?:.[\\d]+(?:.[\\d]+)?)?)|)\\;version:\\1",
      "website": "https://fontawesome.com/"
    },
    "Fork CMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:fork-cms:fork_cms",
      "icon": "ForkCMS.png",
      "implies": "Symfony",
      "meta": {
        "generator": "^Fork CMS$"
      },
      "website": "http://www.fork-cms.com/"
    },
    "Fortune3": {
      "cats": [
        6
      ],
      "html": "(?:<link [^>]*href=\"[^\\/]*\\/\\/www\\.fortune3\\.com\\/[^\"]*siterate\\/rate\\.css|Powered by <a [^>]*href=\"[^\"]+fortune3\\.com)",
      "icon": "Fortune3.png",
      "script": "cartjs\\.php\\?(?:.*&)?s=[^&]*myfortune3cart\\.com",
      "website": "http://fortune3.com"
    },
    "Foswiki": {
      "cats": [
        8
      ],
      "cookies": {
        "FOSWIKISTRIKEONE": "",
        "SFOSWIKISID": ""
      },
      "cpe": "cpe:/a:foswiki:foswiki",
      "headers": {
        "X-Foswikiaction": "",
        "X-Foswikiuri": ""
      },
      "html": [
        "<div class=\"foswiki(?:Copyright|Page|Main)\">"
      ],
      "icon": "foswiki.png",
      "implies": "Perl",
      "js": {
        "foswiki": ""
      },
      "meta": {
        "foswiki.SERVERTIME": "",
        "foswiki.WIKINAME": ""
      },
      "website": "http://foswiki.org"
    },
    "FreeBSD": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:freebsd:freebsd",
      "headers": {
        "Server": "FreeBSD(?: ([\\d.]+))?\\;version:\\1"
      },
      "icon": "FreeBSD.png",
      "website": "http://freebsd.org"
    },
    "FreeTextBox": {
      "cats": [
        24
      ],
      "html": "/<!--\\s*\\*\\s*FreeTextBox v\\d+ \\(([.\\d]+)(?:(?:\\.|\\n)+?<!--\\s*\\*\\s*License Type: (Distribution|Professional)License)?/i\\;version:\\1 \\2",
      "icon": "FreeTextBox.png",
      "implies": "Microsoft ASP.NET",
      "js": {
        "FTB_API": "",
        "FTB_AddEvent": ""
      },
      "website": "http://freetextbox.com"
    },
    "Freespee": {
      "cats": [
        10
      ],
      "icon": "Freespee.svg",
      "script": "analytics\\.freespee\\.com/js/external/fs\\.(?:min\\.)?js",
      "website": "https://www.freespee.com"
    },
    "Freshchat": {
      "cats": [
        52
      ],
      "icon": "freshchat.png",
      "script": "wchat\\.freshchat\\.com/js/widget\\.js",
      "website": "https://www.freshworks.com/live-chat-software/"
    },
    "Freshmarketer": {
      "cats": [
        10
      ],
      "icon": "freshmarketer.png",
      "script": "cdn\\.freshmarketer\\.com",
      "website": "https://www.freshworks.com/marketing-automation/conversion-rate-optimization/"
    },
    "Froala Editor": {
      "cats": [
        24
      ],
      "html": "<[^>]+class=\"[^\"]*(?:fr-view|fr-box)",
      "icon": "Froala.svg",
      "implies": [
        "jQuery",
        "Font Awesome"
      ],
      "website": "http://froala.com/wysiwyg-editor"
    },
    "FrontPage": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:microsoft:frontpage",
      "icon": "FrontPage.png",
      "meta": {
        "ProgId": "^FrontPage\\.",
        "generator": "Microsoft FrontPage(?:\\s((?:Express )?[\\d.]+))?\\;version:\\1"
      },
      "website": "http://office.microsoft.com/frontpage"
    },
    "Fusion Ads": {
      "cats": [
        36
      ],
      "icon": "Fusion Ads.png",
      "js": {
        "_fusion": ""
      },
      "script": "^[^\\/]*//[ac]dn\\.fusionads\\.net/(?:api/([\\d.]+)/)?\\;version:\\1",
      "website": "http://fusionads.net"
    },
    "Future Shop": {
      "cats": [
        6
      ],
      "icon": "futureshop.png",
      "script": "future-shop.*\\.js",
      "website": "https://www.future-shop.jp"
    },
    "G-WAN": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "G-WAN"
      },
      "icon": "G-WAN.png",
      "website": "http://gwan.com"
    },
    "GOV.UK Frontend": {
      "cats": [
        66,
        19
      ],
      "html": [
        "<body[^>]+govuk-template__body",
        "<a[^>]+govuk-link"
      ],
      "icon": "govuk.png",
      "website": "https://design-system.service.gov.uk/"
    },
    "GSAP": {
      "cats": [
        12
      ],
      "icon": "TweenMax.png",
      "js": {
        "TweenMax": "",
        "gsapVersions": ""
      },
      "script": "TweenMax(?:\\.min)?\\.js",
      "website": "https://greensock.com/gsap"
    },
    "GX WebManager": {
      "cats": [
        1
      ],
      "html": "<!--\\s+Powered by GX",
      "icon": "GX WebManager.png",
      "meta": {
        "generator": "GX WebManager(?: ([\\d.]+))?\\;version:\\1"
      },
      "website": "http://www.gxsoftware.com/en/products/web-content-management.htm"
    },
    "Gallery": {
      "cats": [
        7
      ],
      "html": [
        "<div id=\"gsNavBar\" class=\"gcBorder1\">",
        "<a href=\"http://gallery\\.sourceforge\\.net\"><img[^>]+Powered by Gallery\\s*(?:(?:v|Version)\\s*([0-9.]+))?\\;version:\\1"
      ],
      "icon": "Gallery.png",
      "js": {
        "$.fn.gallery_valign": "",
        "galleryAuthToken": ""
      },
      "website": "http://galleryproject.org/"
    },
    "Gambio": {
      "cats": [
        6
      ],
      "html": "(?:<link[^>]* href=\"templates/gambio/|<a[^>]content\\.php\\?coID=\\d|<!-- gambio eof -->|<!--[\\s=]+Shopsoftware by Gambio GmbH \\(c\\))",
      "icon": "Gambio.png",
      "implies": "PHP",
      "js": {
        "gambio": ""
      },
      "script": "gm_javascript\\.js\\.php",
      "website": "http://gambio.de"
    },
    "Gatsby": {
      "cats": [
        57,
        12
      ],
      "html": [
        "<div id=\"___gatsby\">",
        "<style id=\"gatsby-inlined-css\">"
      ],
      "icon": "Gatsby.svg",
      "implies": [
        "React",
        "webpack"
      ],
      "meta": {
        "generator": "^Gatsby(?: ([0-9.]+))?$\\;version:\\1"
      },
      "website": "https://www.gatsbyjs.org/"
    },
    "Gauges": {
      "cats": [
        10
      ],
      "cookies": {
        "_gauges_": ""
      },
      "icon": "Gauges.png",
      "js": {
        "_gauges": ""
      },
      "website": "https://get.gaug.es"
    },
    "Gemius": {
      "cats": [
        10
      ],
      "html": "<a [^>]*onclick=\"gemius_hit",
      "icon": "Gemius.png",
      "js": {
        "gemius_hit": "",
        "gemius_init": "",
        "gemius_pending": "",
        "pp_gemius_hit": ""
      },
      "script": [
        "hit\\.gemius\\.pl/xgemius\\.js",
        "hit\\.gemius\\.pl\\;confidence:80",
        "xgemius\\.js\\;confidence:30"
      ],
      "website": "https://www.gemius.com"
    },
    "GeneXus": {
      "cats": [
        27
      ],
      "html": [
        "<link[^>]+?id=\"gxtheme_css_reference\""
      ],
      "icon": "GeneXus.png",
      "js": {
        "gx.gxVersion": "^(.+)-.*$\\;version:\\1"
      },
      "script": [
        "/static/gxgral\\.js",
        "/static/gxtimezone\\.js"
      ],
      "website": "https://www.genexus.com/"
    },
    "Gentoo": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:gentoo:linux",
      "headers": {
        "X-Powered-By": "gentoo"
      },
      "icon": "Gentoo.png",
      "website": "http://www.gentoo.org"
    },
    "Gerrit": {
      "cats": [
        47
      ],
      "html": [
        ">Gerrit Code Review</a>\\s*\"\\s*\\(([0-9.]+)\\)\\;version:\\1",
        "<(?:div|style) id=\"gerrit_"
      ],
      "icon": "gerrit.svg",
      "implies": [
        "Java",
        "git"
      ],
      "js": {
        "Gerrit": "",
        "gerrit_ui": ""
      },
      "meta": {
        "title": "^Gerrit Code Review$"
      },
      "script": "^gerrit_ui/gerrit_ui",
      "website": "http://www.gerritcodereview.com"
    },
    "Get Satisfaction": {
      "cats": [
        13
      ],
      "icon": "Get Satisfaction.png",
      "js": {
        "GSFN": ""
      },
      "website": "https://getsatisfaction.com/corp/"
    },
    "GetSimple CMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:get-simple:getsimple_cms",
      "icon": "GetSimple CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "GetSimple"
      },
      "website": "http://get-simple.info"
    },
    "Ghost": {
      "cats": [
        11
      ],
      "headers": {
        "X-Ghost-Cache-Status": ""
      },
      "icon": "Ghost.png",
      "implies": "Node.js",
      "meta": {
        "generator": "Ghost(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "http://ghost.org"
    },
    "GitBook": {
      "cats": [
        4
      ],
      "icon": "GitBook.png",
      "meta": {
        "generator": "GitBook(?:\\.([\\d.]+))?\\;version:\\1"
      },
      "url": "^https?://[^/]+\\.gitbook\\.com/",
      "website": "https://www.gitbook.com"
    },
    "GitHub Pages": {
      "cats": [
        62
      ],
      "headers": {
        "Server": "^GitHub\\.com$",
        "X-GitHub-Request-Id": ""
      },
      "icon": "GitHub.svg",
      "implies": "Ruby on Rails",
      "url": "^https?://[^/]+\\.github\\.io",
      "website": "https://pages.github.com/"
    },
    "GitLab": {
      "cats": [
        13,
        47
      ],
      "cookies": {
        "_gitlab_session": ""
      },
      "html": [
        "<meta content=\"https?://[^/]+/assets/gitlab_logo-",
        "<header class=\"navbar navbar-fixed-top navbar-gitlab with-horizontal-nav\">"
      ],
      "icon": "GitLab.svg",
      "implies": [
        "Ruby on Rails",
        "Vue.js"
      ],
      "js": {
        "GitLab": "",
        "gl.dashboardOptions": ""
      },
      "meta": {
        "og:site_name": "^GitLab$"
      },
      "website": "https://about.gitlab.com"
    },
    "GitLab CI": {
      "cats": [
        44,
        47
      ],
      "icon": "GitLab CI.png",
      "implies": "Ruby on Rails",
      "meta": {
        "description": "GitLab Continuous Integration"
      },
      "website": "http://about.gitlab.com/gitlab-ci"
    },
    "Gitea": {
      "cats": [
        47
      ],
      "cookies": {
        "i_like_gitea": ""
      },
      "cpe": "cpe:/a:gitea:gitea",
      "html": [
        "<div class=\"ui left\">\\n\\s+© Gitea Version: ([\\d.]+)\\;version:\\1"
      ],
      "icon": "gitea.svg",
      "meta": {
        "keywords": "^go,git,self-hosted,gitea$"
      },
      "website": "https://gitea.io"
    },
    "Gitiles": {
      "cats": [
        47
      ],
      "html": "Powered by <a href=\"https://gerrit\\.googlesource\\.com/gitiles/\">Gitiles<",
      "implies": [
        "Java",
        "git"
      ],
      "website": "http://gerrit.googlesource.com/gitiles/"
    },
    "GlassFish": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:oracle:glassfish_server",
      "headers": {
        "Server": "GlassFish(?: Server)?(?: Open Source Edition)?(?: ?/?([\\d.]+))?\\;version:\\1"
      },
      "icon": "GlassFish.png",
      "implies": "Java",
      "website": "http://glassfish.java.net"
    },
    "Glyphicons": {
      "cats": [
        17
      ],
      "html": "(?:<link[^>]* href=[^>]+glyphicons(?:\\.min)?\\.css|<img[^>]* src=[^>]+glyphicons)",
      "icon": "Glyphicons.png",
      "website": "http://glyphicons.com"
    },
    "Go": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:golang:go",
      "icon": "Go.svg",
      "website": "https://golang.org"
    },
    "GoAhead": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:embedthis:goahead",
      "headers": {
        "Server": "GoAhead"
      },
      "icon": "GoAhead.png",
      "website": "http://embedthis.com/products/goahead/index.html"
    },
    "GoCache": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^gocache$",
        "X-GoCache-CacheStatus": ""
      },
      "icon": "GoCache.png",
      "website": "https://www.gocache.com.br/"
    },
    "GoDaddy Website Builder": {
      "cats": [
        1
      ],
      "cookies": {
        "dps_site_id": ""
      },
      "icon": "godaddy.svg",
      "meta": {
        "generator": "Go Daddy Website Builder (.+)\\;version:\\1"
      },
      "website": "https://www.godaddy.com/websites/website-builder"
    },
    "GoJS": {
      "cats": [
        25
      ],
      "icon": "GoJS.png",
      "js": {
        "go.GraphObject": "",
        "go.version": "(.*)\\;version:\\1"
      },
      "website": "https://gojs.net/"
    },
    "GoStats": {
      "cats": [
        10
      ],
      "icon": "GoStats.png",
      "js": {
        "_goStatsRun": "",
        "_go_track_src": "",
        "go_msie": ""
      },
      "website": "http://gostats.com/"
    },
    "Gogs": {
      "cats": [
        47
      ],
      "cookies": {
        "i_like_gogits": ""
      },
      "cpe": "cpe:/a:gogs:gogs",
      "html": [
        "<div class=\"ui left\">\\n\\s+© \\d{4} Gogs Version: ([\\d.]+) Page:\\;version:\\1",
        "<button class=\"ui basic clone button\" id=\"repo-clone-ssh\" data-link=\"gogs@"
      ],
      "icon": "gogs.png",
      "meta": {
        "keywords": "go, git, self-hosted, gogs"
      },
      "script": "js/gogs\\.js",
      "website": "http://gogs.io"
    },
    "Google AdSense": {
      "cats": [
        36
      ],
      "icon": "Google AdSense.svg",
      "js": {
        "Goog_AdSense_": "",
        "__google_ad_urls": "",
        "google_ad_": ""
      },
      "script": [
        "googlesyndication\\.com/",
        "ad\\.ca\\.doubleclick\\.net",
        "2mdn\\.net",
        "ad\\.ca\\.doubleclick\\.net"
      ],
      "website": "https://www.google.fr/adsense/start/"
    },
    "Google Analytics": {
      "cats": [
        10
      ],
      "cookies": {
        "__utma": "",
        "_ga": "",
        "_gat": ""
      },
      "html": "<amp-analytics [^>]*type=[\"']googleanalytics[\"']",
      "icon": "Google Analytics.svg",
      "js": {
        "GoogleAnalyticsObject": "",
        "gaGlobal": ""
      },
      "script": "google-analytics\\.com\\/(?:ga|urchin|analytics)\\.js",
      "website": "http://google.com/analytics"
    },
    "Google Analytics Enhanced eCommerce": {
      "cats": [
        10
      ],
      "icon": "Google Analytics.svg",
      "implies": "Google Analytics",
      "js": {
        "gaplugins.EC": ""
      },
      "script": "google-analytics\\.com\\/plugins\\/ua\\/(?:ec|ecommerce)\\.js",
      "website": "https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce"
    },
    "Google App Engine": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Google Frontend"
      },
      "icon": "Google App Engine.png",
      "website": "http://code.google.com/appengine"
    },
    "Google Charts": {
      "cats": [
        25
      ],
      "icon": "Google Charts.png",
      "js": {
        "__googleVisualizationAbstractRendererElementsCount__": "",
        "__gvizguard__": ""
      },
      "website": "http://developers.google.com/chart/"
    },
    "Google Cloud": {
      "cats": [
        31
      ],
      "cpe": "cpe:/a:google:cloud_platform",
      "headers": {
        "Via": "^1\\.1 google$"
      },
      "icon": "google_cloud.svg",
      "website": "https://cloud.google.com"
    },
    "Google Code Prettify": {
      "cats": [
        19
      ],
      "icon": "Google.svg",
      "js": {
        "prettyPrint": ""
      },
      "website": "http://code.google.com/p/google-code-prettify"
    },
    "Google Font API": {
      "cats": [
        17
      ],
      "html": "<link[^>]* href=[^>]+fonts\\.(?:googleapis|google)\\.com",
      "icon": "Google Font API.png",
      "js": {
        "WebFonts": ""
      },
      "script": "googleapis\\.com/.+webfont",
      "website": "http://google.com/fonts"
    },
    "Google Maps": {
      "cats": [
        35
      ],
      "icon": "Google Maps.png",
      "script": [
        "(?:maps\\.google\\.com/maps\\?file=api(?:&v=([\\d.]+))?|maps\\.google\\.com/maps/api/staticmap)\\;version:API v\\1",
        "//maps\\.googleapis\\.com/maps/api/js"
      ],
      "website": "http://maps.google.com"
    },
    "Google PageSpeed": {
      "cats": [
        23,
        33
      ],
      "headers": {
        "X-Mod-Pagespeed": "([\\d.]+)\\;version:\\1",
        "X-Page-Speed": "(.+)\\;version:\\1"
      },
      "icon": "Google PageSpeed.png",
      "website": "http://developers.google.com/speed/pagespeed/mod"
    },
    "Google Plus": {
      "cats": [
        5
      ],
      "icon": "Google Plus.svg",
      "script": "apis\\.google\\.com/js/[a-z]*\\.js",
      "website": "http://plus.google.com"
    },
    "Google Sites": {
      "cats": [
        1
      ],
      "icon": "Google Sites.png",
      "url": "^https?://sites\\.google\\.com",
      "website": "http://sites.google.com"
    },
    "Google Tag Manager": {
      "cats": [
        42
      ],
      "html": [
        "googletagmanager\\.com/ns\\.html[^>]+></iframe>",
        "<!-- (?:End )?Google Tag Manager -->"
      ],
      "icon": "Google Tag Manager.png",
      "js": {
        "google_tag_manager": "",
        "googletag": ""
      },
      "website": "http://www.google.com/tagmanager"
    },
    "Google Wallet": {
      "cats": [
        41
      ],
      "icon": "Google Wallet.png",
      "script": [
        "checkout\\.google\\.com",
        "wallet\\.google\\.com"
      ],
      "website": "http://wallet.google.com"
    },
    "Google Web Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:google:web_server",
      "headers": {
        "Server": "gws"
      },
      "icon": "Google.svg",
      "website": "http://en.wikipedia.org/wiki/Google_Web_Server"
    },
    "Google Web Toolkit": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:google:web_toolkit",
      "icon": "Google Web Toolkit.png",
      "implies": "Java",
      "js": {
        "__gwt_": "",
        "__gwt_activeModules": "",
        "__gwt_getMetaProperty": "",
        "__gwt_isKnownPropertyValue": "",
        "__gwt_stylesLoaded": "",
        "__gwtlistener": ""
      },
      "meta": {
        "gwt:property": ""
      },
      "website": "http://developers.google.com/web-toolkit"
    },
    "Graffiti CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "graffitibot": ""
      },
      "icon": "Graffiti CMS.png",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "Graffiti CMS ([^\"]+)\\;version:\\1"
      },
      "script": "/graffiti\\.js",
      "website": "http://graffiticms.codeplex.com"
    },
    "GrandNode": {
      "cats": [
        6
      ],
      "cookies": {
        "Grand.customer": ""
      },
      "html": "(?:<!--GrandNode |<a[^>]+grandnode - Powered by |Powered by: <a[^>]+nopcommerce)",
      "icon": "GrandNode.svg",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "grandnode"
      },
      "website": "https://grandnode.com"
    },
    "Grav": {
      "cats": [
        1
      ],
      "icon": "Grav.png",
      "implies": "PHP",
      "meta": {
        "generator": "GravCMS(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "http://getgrav.org"
    },
    "Gravatar": {
      "cats": [
        19
      ],
      "html": "<[^>]+gravatar\\.com/avatar/",
      "icon": "Gravatar.png",
      "js": {
        "Gravatar": ""
      },
      "website": "http://gravatar.com"
    },
    "Gravity Forms": {
      "cats": [
        19
      ],
      "html": [
        "<div class=(?:\"|')[^>]*gform_wrapper",
        "<div class=(?:\"|')[^>]*gform_body",
        "<ul [^>]*class=(?:\"|')[^>]*gform_fields",
        "<link [^>]*href=(?:\"|')[^>]*wp-content/plugins/gravityforms/css/"
      ],
      "icon": "gravityforms.svg",
      "implies": "WordPress",
      "script": "/wp-content/plugins/gravityforms/js/[^/]+\\.js\\?ver=([\\d.]+)$\\;version:\\1",
      "website": "http://gravityforms.com"
    },
    "Green Valley CMS": {
      "cats": [
        1
      ],
      "html": "<img[^>]+/dsresource\\?objectid=",
      "icon": "Green Valley CMS.png",
      "implies": "Apache Tomcat",
      "meta": {
        "DC.identifier": "/content\\.jsp\\?objectid="
      },
      "website": "http://www.greenvalley.nl/Public/Producten/Content_Management/CMS"
    },
    "Gridsome": {
      "cats": [
        57
      ],
      "icon": "Gridsome.svg",
      "implies": "Vue.js",
      "meta": {
        "generator": "^Gridsome v([\\d.]+)$\\;version:\\1"
      },
      "website": "https://gridsome.org"
    },
    "GrowingIO": {
      "cats": [
        10
      ],
      "cookies": {
        "gr_user_id": "",
        "grwng_uid": ""
      },
      "icon": "GrowingIO.png",
      "script": "assets\\.growingio\\.com/([\\d.]+)/gio\\.js\\;version:\\1",
      "website": "https://www.growingio.com/"
    },
    "HERE": {
      "cats": [
        35
      ],
      "icon": "HERE.png",
      "script": "https?://js\\.cit\\.api\\.here\\.com/se/([\\d.]+)\\/\\;version:\\1",
      "website": "http://developer.here.com"
    },
    "HHVM": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:facebook:hhvm",
      "headers": {
        "X-Powered-By": "HHVM/?([\\d.]+)?\\;version:\\1"
      },
      "icon": "HHVM.png",
      "implies": "PHP\\;confidence:75",
      "website": "http://hhvm.com"
    },
    "HP ChaiServer": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "HP-Chai(?:Server|SOE)(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "HP.svg",
      "website": "http://hp.com"
    },
    "HP Compact Server": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "HP_Compact_Server(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "HP.svg",
      "website": "http://hp.com"
    },
    "HP iLO": {
      "cats": [
        22,
        46
      ],
      "headers": {
        "Server": "HP-iLO-Server(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "HP.svg",
      "website": "http://hp.com"
    },
    "HTTP/2": {
      "cats": [
        19
      ],
      "excludes": "SPDY",
      "headers": {
        "X-Firefox-Spdy": "h2"
      },
      "icon": "http2.png",
      "website": "https://http2.github.io"
    },
    "Haddock": {
      "cats": [
        4
      ],
      "html": "<p>Produced by <a href=\"http://www\\.haskell\\.org/haddock/\">Haddock</a> version ([0-9.]+)</p>\\;version:\\1",
      "script": "haddock-util\\.js",
      "website": "http://www.haskell.org/haddock/"
    },
    "Halo": {
      "cats": [
        1,
        11
      ],
      "icon": "Halo.svg",
      "implies": "Java",
      "meta": {
        "generator": "Halo ([\\d.]+)?\\;version:\\1"
      },
      "website": "https://halo.run"
    },
    "Hammer.js": {
      "cats": [
        59
      ],
      "icon": "Hammer.js.png",
      "js": {
        "Ha.VERSION": "^(.+)$\\;version:\\1",
        "Hammer": "",
        "Hammer.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "hammer(?:\\.min)?\\.js",
      "website": "https://hammerjs.github.io"
    },
    "Handlebars": {
      "cats": [
        12
      ],
      "html": "<[^>]*type=[^>]text\\/x-handlebars-template",
      "icon": "Handlebars.png",
      "js": {
        "Handlebars": "",
        "Handlebars.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "handlebars(?:\\.runtime)?(?:-v([\\d.]+?))?(?:\\.min)?\\.js\\;version:\\1",
      "website": "http://handlebarsjs.com"
    },
    "Haravan": {
      "cats": [
        6
      ],
      "icon": "Haravan.png",
      "js": {
        "Haravan": ""
      },
      "script": "haravan.*\\.js",
      "website": "https://www.haravan.com"
    },
    "Haskell": {
      "cats": [
        27
      ],
      "icon": "Haskell.png",
      "website": "http://wiki.haskell.org/Haskell"
    },
    "HeadJS": {
      "cats": [
        59
      ],
      "html": "<[^>]*data-headjs-load",
      "icon": "HeadJS.png",
      "js": {
        "head.browser.name": ""
      },
      "script": "head\\.(?:core|load)(?:\\.min)?\\.js",
      "website": "http://headjs.com"
    },
    "Heap": {
      "cats": [
        10
      ],
      "icon": "Heap.png",
      "js": {
        "heap": ""
      },
      "script": "heap-\\d+\\.js",
      "website": "http://heapanalytics.com"
    },
    "Hello Bar": {
      "cats": [
        5
      ],
      "icon": "Hello Bar.png",
      "js": {
        "HelloBar": ""
      },
      "script": "hellobar\\.js",
      "website": "http://hellobar.com"
    },
    "Heroku": {
      "cats": [
        62
      ],
      "headers": {
        "Via": "/[\\d.-]+ vegur$"
      },
      "icon": "heroku.svg",
      "implies": [
        "Amazon Web Services"
      ],
      "website": "https://www.heroku.com/"
    },
    "Hexo": {
      "cats": [
        57
      ],
      "html": [
        "Powered by <a href=\"https?://hexo\\.io/?\"[^>]*>Hexo</"
      ],
      "icon": "Hexo.png",
      "meta": {
        "generator": "Hexo(?: v?([\\d.]+))?\\;version:\\1"
      },
      "website": "https://hexo.io"
    },
    "Hiawatha": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Hiawatha v([\\d.]+)\\;version:\\1"
      },
      "icon": "Hiawatha.png",
      "website": "http://hiawatha-webserver.org"
    },
    "Highcharts": {
      "cats": [
        25
      ],
      "html": "<svg[^>]*><desc>Created with Highcharts ([\\d.]*)\\;version:\\1",
      "icon": "Highcharts.png",
      "js": {
        "Highcharts": "",
        "Highcharts.version": "^(.+)$\\;version:\\1"
      },
      "script": "highcharts.*\\.js",
      "website": "https://www.highcharts.com"
    },
    "Highlight.js": {
      "cats": [
        19
      ],
      "icon": "Highlight.js.png",
      "js": {
        "hljs.highlightBlock": "",
        "hljs.listLanguages": ""
      },
      "script": "/(?:([\\d.])+/)?highlight(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://highlightjs.org/"
    },
    "Highstock": {
      "cats": [
        25
      ],
      "html": "<svg[^>]*><desc>Created with Highstock ([\\d.]*)\\;version:\\1",
      "icon": "Highcharts.png",
      "script": "highstock[.-]?([\\d\\.]*\\d).*\\.js\\;version:\\1",
      "website": "http://highcharts.com/products/highstock"
    },
    "Hinza Advanced CMS": {
      "cats": [
        1,
        6
      ],
      "icon": "hinza_advanced_cms.svg",
      "implies": "Laravel",
      "meta": {
        "generator": "hinzacms"
      },
      "website": "http://hinzaco.com"
    },
    "Hogan.js": {
      "cats": [
        12
      ],
      "icon": "Hogan.js.png",
      "js": {
        "Hogan": ""
      },
      "script": [
        "hogan-[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "([\\d.]+)/hogan(?:\\.min)?\\.js\\;version:\\1"
      ],
      "website": "https://twitter.github.io/hogan.js/"
    },
    "Hotaru CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "hotaru_mobile": ""
      },
      "icon": "Hotaru CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "Hotaru CMS"
      },
      "website": "http://hotarucms.org"
    },
    "Hotjar": {
      "cats": [
        10
      ],
      "icon": "Hotjar.png",
      "js": {
        "HotLeadfactory": "",
        "HotleadController": "",
        "hj.apiUrlBase": ""
      },
      "script": "//static\\.hotjar\\.com/c/hotjar-",
      "website": "https://www.hotjar.com"
    },
    "HubSpot": {
      "cats": [
        32
      ],
      "html": "<!-- Start of Async HubSpot",
      "icon": "HubSpot.png",
      "js": {
        "_hsq": "",
        "hubspot": ""
      },
      "website": "https://www.hubspot.com"
    },
    "Hugo": {
      "cats": [
        57
      ],
      "html": "powered by <a [^>]*href=\"http://hugo\\.spf13\\.com",
      "icon": "Hugo.png",
      "meta": {
        "generator": "Hugo ([\\d.]+)?\\;version:\\1"
      },
      "website": "http://gohugo.io"
    },
    "IBM Coremetrics": {
      "cats": [
        10
      ],
      "icon": "IBM.svg",
      "script": "cmdatatagutils\\.js",
      "website": "http://ibm.com/software/marketing-solutions/coremetrics"
    },
    "IBM DataPower": {
      "cats": [
        64
      ],
      "cpe": "cpe:/a:ibm:datapower_gateway",
      "headers": {
        "X-Backside-Transport": "",
        "X-Global-Transaction-ID": ""
      },
      "icon": "DataPower.png",
      "website": "https://www.ibm.com/products/datapower-gateway"
    },
    "IBM HTTP Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:ibm:http_server",
      "headers": {
        "Server": "IBM_HTTP_Server(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "IBM.svg",
      "website": "http://ibm.com/software/webservers/httpservers"
    },
    "IBM WebSphere Commerce": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:ibm:websphere_commerce_suite",
      "html": "href=\"(?:\\/|[^>]+)webapp\\/wcs\\/",
      "icon": "IBM.svg",
      "implies": "Java",
      "url": "/wcs/",
      "website": "http://ibm.com/software/genservers/commerceproductline"
    },
    "IBM WebSphere Portal": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:ibm:websphere_portal",
      "headers": {
        "IBM-Web2-Location": "",
        "Itx-Generated-Timestamp": ""
      },
      "icon": "IBM.svg",
      "implies": "Java",
      "url": "/wps/",
      "website": "http://ibm.com/software/websphere/portal"
    },
    "IIS": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:microsoft:internet_information_server",
      "headers": {
        "Server": "^(?:Microsoft-)?IIS(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "IIS.png",
      "implies": "Windows Server",
      "website": "http://www.iis.net"
    },
    "INFOnline": {
      "cats": [
        10
      ],
      "icon": "INFOnline.png",
      "js": {
        "iam_data": "",
        "szmvars": ""
      },
      "script": "^https?://(?:[^/]+\\.)?i(?:oam|v)wbox\\.de/",
      "website": "https://www.infonline.de"
    },
    "INTI": {
      "cats": [
        6,
        53
      ],
      "icon": "byINTI.svg",
      "url": "\\.byinti\\.com",
      "website": "https://byinti.com"
    },
    "IPB": {
      "cats": [
        2
      ],
      "cookies": {
        "ipbWWLmodpids": "",
        "ipbWWLsession_id": ""
      },
      "html": "<link[^>]+ipb_[^>]+\\.css",
      "icon": "IPB.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "IPBoard": "",
        "ipb_var": "",
        "ipsSettings": ""
      },
      "script": "jscripts/ips_",
      "website": "https://invisioncommunity.com/"
    },
    "Ideasoft": {
      "cats": [
        6
      ],
      "icon": "Ideasoft.png",
      "script": [
        "\\.myideasoft\\.com/"
      ],
      "website": "https://www.ideasoft.com"
    },
    "IdoSell Shop": {
      "cats": [
        6
      ],
      "icon": "idosellshop.png",
      "js": {
        "IAI_Ajax": ""
      },
      "website": "https://www.idosell.com"
    },
    "Immutable.js": {
      "cats": [
        59
      ],
      "icon": "Immutable.js.png",
      "js": {
        "Immutable": "",
        "Immutable.version": "^(.+)$\\;version:\\1"
      },
      "script": "^immutable\\.(?:min\\.)?js$",
      "website": "https://facebook.github.io/immutable-js/"
    },
    "ImpressCMS": {
      "cats": [
        1
      ],
      "cookies": {
        "ICMSSession": "",
        "ImpressCMS": ""
      },
      "cpe": "cpe:/a:impresscms:impresscms",
      "icon": "ImpressCMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "ImpressCMS"
      },
      "script": "include/linkexternal\\.js",
      "website": "http://www.impresscms.org"
    },
    "ImpressPages": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:impresspages:impresspages_cms",
      "icon": "ImpressPages.png",
      "implies": "PHP",
      "meta": {
        "generator": "ImpressPages(?: CMS)?( [\\d.]*)?\\;version:\\1"
      },
      "website": "http://impresspages.org"
    },
    "Incapsula": {
      "cats": [
        31
      ],
      "headers": {
        "X-CDN": "Incapsula"
      },
      "icon": "Incapsula.png",
      "website": "http://www.incapsula.com"
    },
    "Includable": {
      "cats": [
        18
      ],
      "headers": {
        "X-Includable-Version": ""
      },
      "icon": "Includable.svg",
      "website": "http://includable.com"
    },
    "Indexhibit": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:indexhibit:indexhibit",
      "html": "<(?:link|a href) [^>]+ndxz-studio",
      "implies": [
        "PHP",
        "Apache",
        "Exhibit"
      ],
      "meta": {
        "generator": "Indexhibit"
      },
      "website": "http://www.indexhibit.org"
    },
    "Indico": {
      "cats": [
        1
      ],
      "cookies": {
        "MAKACSESSION": ""
      },
      "html": "Powered by\\s+(?:CERN )?<a href=\"http://(?:cdsware\\.cern\\.ch/indico/|indico-software\\.org|cern\\.ch/indico)\">(?:CDS )?Indico( [\\d\\.]+)?\\;version:\\1",
      "icon": "Indico.png",
      "website": "http://indico-software.org"
    },
    "Indy": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Indy(?:/([\\d.]+))?\\;version:\\1"
      },
      "website": "http://indyproject.org"
    },
    "InfernoJS": {
      "cats": [
        12
      ],
      "icon": "InfernoJS.png",
      "js": {
        "Inferno": "",
        "Inferno.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://infernojs.org"
    },
    "Infusionsoft": {
      "cats": [
        32
      ],
      "cpe": "cpe:/a:infusionsoft_project:infusionsoft",
      "html": [
        "<input [^>]*name=\"infusionsoft_version\" [^>]*value=\"([^>]*)\" [^>]*\\/>\\;version:\\1",
        "<input [^>]*value=\"([^>]*)\" [^>]*name=\"infusionsoft_version\" [^>]*\\/>\\;version:\\1"
      ],
      "icon": "infusionsoft.svg",
      "website": "http://infusionsoft.com"
    },
    "Inspectlet": {
      "cats": [
        10
      ],
      "html": [
        "<!-- (?:Begin|End) Inspectlet Embed Code -->"
      ],
      "icon": "inspectlet.png",
      "js": {
        "__insp": "",
        "__inspld": ""
      },
      "script": [
        "cdn\\.inspectlet\\.com"
      ],
      "website": "https://www.inspectlet.com/"
    },
    "Instabot": {
      "cats": [
        5,
        10,
        32,
        52,
        58
      ],
      "icon": "Instabot.png",
      "js": {
        "Instabot": ""
      },
      "script": "/rokoInstabot\\.js",
      "website": "https://instabot.io/"
    },
    "InstantCMS": {
      "cats": [
        1
      ],
      "cookies": {
        "InstantCMS[logdate]": ""
      },
      "cpe": "cpe:/a:instantcms:instantcms",
      "icon": "InstantCMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "InstantCMS"
      },
      "website": "http://www.instantcms.ru"
    },
    "Intel Active Management Technology": {
      "cats": [
        22,
        46
      ],
      "cpe": "cpe:/a:intel:active_management_technology",
      "headers": {
        "Server": "Intel\\(R\\) Active Management Technology(?: ([\\d.]+))?\\;version:\\1"
      },
      "icon": "Intel Active Management Technology.png",
      "website": "http://intel.com"
    },
    "IntenseDebate": {
      "cats": [
        15
      ],
      "icon": "IntenseDebate.png",
      "script": "intensedebate\\.com",
      "website": "http://intensedebate.com"
    },
    "Intercom": {
      "cats": [
        10
      ],
      "icon": "Intercom.svg",
      "js": {
        "Intercom": ""
      },
      "script": "(?:api\\.intercom\\.io/api|static\\.intercomcdn\\.com/intercom\\.v1)",
      "website": "https://www.intercom.com"
    },
    "Intershop": {
      "cats": [
        6
      ],
      "html": "<ish-root",
      "icon": "Intershop.png",
      "script": "(?:is-bin|INTERSHOP)",
      "website": "http://intershop.com"
    },
    "Invenio": {
      "cats": [
        50
      ],
      "cookies": {
        "INVENIOSESSION": ""
      },
      "html": "(?:Powered by|System)\\s+(?:CERN )?<a (?:class=\"footer\" )?href=\"http://(?:cdsware\\.cern\\.ch(?:/invenio)?|invenio-software\\.org|cern\\.ch/invenio)(?:/)?\">(?:CDS )?Invenio</a>\\s*v?([\\d\\.]+)?\\;version:\\1",
      "icon": "Invenio.png",
      "website": "http://invenio-software.org"
    },
    "Ionic": {
      "cats": [
        18
      ],
      "icon": "ionic.png",
      "js": {
        "Ionic.config": "",
        "Ionic.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://ionicframework.com"
    },
    "Ionicons": {
      "cats": [
        17
      ],
      "html": "<link[^>]* href=[^>]+ionicons(?:\\.min)?\\.css",
      "icon": "Ionicons.png",
      "website": "http://ionicons.com"
    },
    "Irroba": {
      "cats": [
        6
      ],
      "html": "<a[^>]*href=\"https://www\\.irroba\\.com\\.br",
      "icon": "irroba.svg",
      "website": "https://www.irroba.com.br/"
    },
    "J2Store": {
      "cats": [
        6
      ],
      "icon": "j2store.png",
      "implies": "Joomla",
      "js": {
        "j2storeURL": ""
      },
      "website": "https://www.j2store.org/"
    },
    "JAlbum": {
      "cats": [
        7
      ],
      "icon": "JAlbum.png",
      "implies": "Java",
      "meta": {
        "generator": "JAlbum( [\\d.]+)?\\;version:\\1"
      },
      "website": "http://jalbum.net/en"
    },
    "JBoss Application Server": {
      "cats": [
        22
      ],
      "headers": {
        "X-Powered-By": "JBoss(?:-([\\d.]+))?\\;version:\\1"
      },
      "icon": "JBoss Application Server.png",
      "website": "http://jboss.org/jbossas.html"
    },
    "JBoss Web": {
      "cats": [
        22
      ],
      "excludes": "Apache Tomcat",
      "headers": {
        "X-Powered-By": "JBossWeb(?:-([\\d.]+))?\\;version:\\1"
      },
      "icon": "JBoss Web.png",
      "implies": "JBoss Application Server",
      "website": "http://jboss.org/jbossweb"
    },
    "JET Enterprise": {
      "cats": [
        6
      ],
      "headers": {
        "powered": "jet-enterprise"
      },
      "icon": "JET Enterprise.svg",
      "website": "http://www.jetecommerce.com.br/"
    },
    "JS Charts": {
      "cats": [
        25
      ],
      "icon": "JS Charts.png",
      "js": {
        "JSChart": ""
      },
      "script": "jscharts.*\\.js",
      "website": "http://www.jscharts.com"
    },
    "JSEcoin": {
      "cats": [
        56
      ],
      "icon": "JSEcoin.png",
      "js": {
        "jseMine": ""
      },
      "script": "^(?:https):?//load\\.jsecoin\\.com/load/",
      "website": "https://jsecoin.com/"
    },
    "JTL Shop": {
      "cats": [
        6
      ],
      "cookies": {
        "JTLSHOP": ""
      },
      "html": "(?:<input[^>]+name=\"JTLSHOP|<a href=\"jtl\\.php)",
      "icon": "JTL Shop.png",
      "website": "http://www.jtl-software.de/produkte/jtl-shop3"
    },
    "Jahia DX": {
      "cats": [
        1,
        47
      ],
      "html": "<script id=\"staticAssetAggregatedJavascrip",
      "icon": "JahiaDX.svg",
      "website": "http://www.jahia.com/dx"
    },
    "Jalios": {
      "cats": [
        1
      ],
      "icon": "Jalios.png",
      "meta": {
        "generator": "Jalios"
      },
      "website": "http://www.jalios.com"
    },
    "Java": {
      "cats": [
        27
      ],
      "cookies": {
        "JSESSIONID": ""
      },
      "icon": "Java.png",
      "website": "http://java.com"
    },
    "Java Servlet": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "Servlet(?:\\.([\\d.]+))?\\;version:\\1"
      },
      "icon": "Java.png",
      "implies": "Java",
      "website": "http://www.oracle.com/technetwork/java/index-jsp-135475.html"
    },
    "JavaScript Infovis Toolkit": {
      "cats": [
        25
      ],
      "icon": "JavaScript Infovis Toolkit.png",
      "js": {
        "$jit": "",
        "$jit.version": "^(.+)$\\;version:\\1"
      },
      "script": "jit(?:-yc)?\\.js",
      "website": "https://philogb.github.io/jit/"
    },
    "JavaServer Faces": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "JSF(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "JavaServer Faces.png",
      "implies": "Java",
      "website": "http://javaserverfaces.java.net"
    },
    "JavaServer Pages": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "JSP(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Java.png",
      "implies": "Java",
      "website": "http://www.oracle.com/technetwork/java/javaee/jsp/index.html"
    },
    "Javadoc": {
      "cats": [
        4
      ],
      "html": "<!-- Generated by javadoc -->",
      "icon": "Java.png",
      "website": "https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html"
    },
    "Jekyll": {
      "cats": [
        57
      ],
      "cpe": "cpe:/a:jekyllrb:jekyll",
      "html": [
        "Powered by <a href=\"https?://jekyllrb\\.com\"[^>]*>Jekyll</",
        "<!-- Created with Jekyll Now -",
        "<!-- Begin Jekyll SEO tag"
      ],
      "icon": "Jekyll.png",
      "meta": {
        "generator": "Jekyll (v[\\d.]+)?\\;version:\\1"
      },
      "website": "http://jekyllrb.com"
    },
    "Jenkins": {
      "cats": [
        44
      ],
      "headers": {
        "X-Jenkins": "([\\d.]+)\\;version:\\1"
      },
      "html": "<span class=\"jenkins_ver\"><a href=\"https://jenkins\\.io/\">Jenkins ver\\. ([\\d.]+)\\;version:\\1",
      "icon": "Jenkins.png",
      "implies": "Java",
      "js": {
        "jenkinsCIGlobal": "",
        "jenkinsRules": ""
      },
      "website": "https://jenkins.io/"
    },
    "Jetshop": {
      "cats": [
        6
      ],
      "html": "<(?:div|aside) id=\"jetshop-branding\">",
      "icon": "Jetshop.png",
      "js": {
        "JetshopData": ""
      },
      "website": "http://jetshop.se"
    },
    "Jetty": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Jetty(?:\\(([\\d\\.]*\\d+))?\\;version:\\1"
      },
      "icon": "Jetty.png",
      "implies": "Java",
      "website": "http://www.eclipse.org/jetty"
    },
    "Jimdo": {
      "cats": [
        1
      ],
      "headers": {
        "X-Jimdo-Instance": "",
        "X-Jimdo-Wid": ""
      },
      "icon": "jimdo.png",
      "url": "\\.jimdo\\.com/",
      "website": "https://www.jimdo.com"
    },
    "Jirafe": {
      "cats": [
        10,
        32
      ],
      "icon": "Jirafe.png",
      "js": {
        "jirafe": ""
      },
      "script": "/jirafe\\.js",
      "website": "https://docs.jirafe.com"
    },
    "Jitsi": {
      "cats": [
        52
      ],
      "icon": "Jitsi.png",
      "script": "lib-jitsi-meet.*\\.js",
      "website": "https://jitsi.org"
    },
    "Jive": {
      "cats": [
        19
      ],
      "headers": {
        "X-JIVE-USER-ID": "",
        "X-JSL": "",
        "X-Jive-Flow-Id": "",
        "X-Jive-Request-Id": "",
        "x-jive-chrome-wrapped": ""
      },
      "icon": "Jive.png",
      "website": "http://www.jivesoftware.com"
    },
    "JobberBase": {
      "cats": [
        19
      ],
      "icon": "JobberBase.png",
      "implies": "PHP",
      "js": {
        "Jobber": ""
      },
      "meta": {
        "generator": "Jobberbase"
      },
      "website": "http://www.jobberbase.com"
    },
    "Joomla": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:joomla:joomla",
      "headers": {
        "X-Content-Encoded-By": "Joomla! ([\\d.]+)\\;version:\\1"
      },
      "html": "(?:<div[^>]+id=\"wrapper_r\"|<(?:link|script)[^>]+(?:feed|components)/com_|<table[^>]+class=\"pill)\\;confidence:50",
      "icon": "Joomla.svg",
      "implies": "PHP",
      "js": {
        "Joomla": "",
        "jcomments": ""
      },
      "meta": {
        "generator": "Joomla!(?: ([\\d.]+))?\\;version:\\1"
      },
      "url": "option=com_",
      "website": "https://www.joomla.org"
    },
    "K2": {
      "cats": [
        19
      ],
      "html": "<!--(?: JoomlaWorks \"K2\"| Start K2)",
      "icon": "K2.png",
      "implies": "Joomla",
      "js": {
        "K2RatingURL": ""
      },
      "website": "https://getk2.org"
    },
    "KISSmetrics": {
      "cats": [
        10
      ],
      "icon": "KISSmetrics.png",
      "js": {
        "KM_COOKIE_DOMAIN": ""
      },
      "website": "https://www.kissmetrics.com"
    },
    "Kajabi": {
      "cats": [
        6
      ],
      "cookies": {
        "_kjb_session": ""
      },
      "icon": "Kajabi.svg",
      "js": {
        "Kajabi": ""
      },
      "website": "https://newkajabi.com"
    },
    "Kampyle": {
      "cats": [
        10,
        13
      ],
      "cookies": {
        "k_visit": ""
      },
      "icon": "Kampyle.png",
      "js": {
        "KAMPYLE_COMMON": "",
        "k_track": "",
        "kampyle": ""
      },
      "script": "cf\\.kampyle\\.com/k_button\\.js",
      "website": "http://www.kampyle.com"
    },
    "Kamva": {
      "cats": [
        6
      ],
      "icon": "Kamva.svg",
      "js": {
        "Kamva": ""
      },
      "meta": {
        "generator": "[CK]amva"
      },
      "script": "cdn\\.mykamva\\.ir",
      "website": "https://kamva.ir"
    },
    "Kemal": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "X-Powered-By": "Kemal"
      },
      "icon": "kemalcr.png",
      "website": "http://kemalcr.com"
    },
    "Kendo UI": {
      "cats": [
        66
      ],
      "html": "<link[^>]*\\s+href=[^>]*styles/kendo\\.common(?:\\.min)?\\.css[^>]*/>",
      "icon": "Kendo UI.png",
      "implies": "jQuery",
      "js": {
        "kendo": "",
        "kendo.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://www.telerik.com/kendo-ui"
    },
    "Kentico CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "CMSPreferredCulture": ""
      },
      "cpe": "cpe:/a:kentico:kentico_cms",
      "icon": "Kentico CMS.png",
      "meta": {
        "generator": "Kentico CMS ([\\d.R]+ \\(build [\\d.]+\\))\\;version:\\1"
      },
      "website": "http://www.kentico.com"
    },
    "Kestrel": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Kestrel"
      },
      "icon": "kestrel.svg",
      "implies": "Microsoft ASP.NET",
      "website": "https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel"
    },
    "KeyCDN": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^keycdn-engine$"
      },
      "icon": "KeyCDN.png",
      "website": "http://www.keycdn.com"
    },
    "Kibana": {
      "cats": [
        29,
        25
      ],
      "cpe": "cpe:/a:elasticsearch:kibana",
      "headers": {
        "kbn-name": "kibana",
        "kbn-version": "^([\\d.]+)$\\;version:\\1"
      },
      "html": "<title>Kibana</title>",
      "icon": "kibana.svg",
      "implies": "Node.js",
      "url": "kibana#/dashboard/",
      "website": "http://www.elastic.co/products/kibana"
    },
    "KineticJS": {
      "cats": [
        25
      ],
      "icon": "KineticJS.png",
      "js": {
        "Kinetic": "",
        "Kinetic.version": "^(.+)$\\;version:\\1"
      },
      "script": "kinetic(?:-v?([\\d.]+))?(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://github.com/ericdrowell/KineticJS/"
    },
    "Kinsta": {
      "cats": [
        62
      ],
      "headers": {
        "x-kinsta-cache": ""
      },
      "icon": "kinsta.svg",
      "implies": "WordPress",
      "website": "https://kinsta.com"
    },
    "Klarna Checkout": {
      "cats": [
        41,
        6,
        5
      ],
      "icon": "Klarna.svg",
      "js": {
        "_klarnaCheckout": ""
      },
      "website": "https://www.klarna.com/international/"
    },
    "Knockout.js": {
      "cats": [
        12
      ],
      "icon": "Knockout.js.png",
      "js": {
        "ko.version": "^(.+)$\\;version:\\1"
      },
      "website": "http://knockoutjs.com"
    },
    "Koa": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "X-Powered-By": "^koa$"
      },
      "icon": "Koa.png",
      "implies": "Node.js",
      "website": "http://koajs.com"
    },
    "Koala Framework": {
      "cats": [
        1,
        18
      ],
      "html": "<!--[^>]+This website is powered by Koala Web Framework CMS",
      "icon": "Koala Framework.png",
      "implies": "PHP",
      "meta": {
        "generator": "^Koala Web Framework CMS"
      },
      "website": "http://koala-framework.org"
    },
    "KobiMaster": {
      "cats": [
        6
      ],
      "icon": "Kobimaster.png",
      "implies": "Microsoft ASP.NET",
      "js": {
        "kmGetSession": "",
        "kmPageInfo": ""
      },
      "website": "https://www.kobimaster.com.tr"
    },
    "Koha": {
      "cats": [
        50
      ],
      "cpe": "cpe:/a:koha:koha",
      "html": [
        "<input name=\"koha_login_context\" value=\"intranet\" type=\"hidden\">",
        "<a href=\"/cgi-bin/koha/"
      ],
      "icon": "koha.png",
      "implies": "Perl",
      "js": {
        "KOHA": ""
      },
      "meta": {
        "generator": "^Koha ([\\d.]+)$\\;version:\\1"
      },
      "website": "https://koha-community.org/"
    },
    "Kohana": {
      "cats": [
        18
      ],
      "cookies": {
        "kohanasession": ""
      },
      "cpe": "cpe:/a:kohanaframework:kohana",
      "headers": {
        "X-Powered-By": "Kohana Framework ([\\d.]+)\\;version:\\1"
      },
      "icon": "Kohana.png",
      "implies": "PHP",
      "website": "http://kohanaframework.org"
    },
    "Koken": {
      "cats": [
        1
      ],
      "cookies": {
        "koken_referrer": ""
      },
      "html": [
        "<html lang=\"en\" class=\"k-source-essays k-lens-essays\">",
        "<!--\\s+KOKEN DEBUGGING"
      ],
      "icon": "Koken.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "meta": {
        "generator": "Koken ([\\d.]+)\\;version:\\1"
      },
      "script": "koken(?:\\.js\\?([\\d.]+)|/storage)\\;version:\\1",
      "website": "http://koken.me"
    },
    "Kolibri CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "Kolibri"
      },
      "meta": {
        "generator": "Kolibri"
      },
      "website": "http://alias.io"
    },
    "Komodo CMS": {
      "cats": [
        1
      ],
      "icon": "Komodo CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "^Komodo CMS"
      },
      "website": "http://www.komodocms.com"
    },
    "Koobi": {
      "cats": [
        1
      ],
      "html": "<!--[^K>-]+Koobi ([a-z\\d.]+)\\;version:\\1",
      "icon": "Koobi.png",
      "meta": {
        "generator": "Koobi"
      },
      "website": "http://dream4.de/cms"
    },
    "Kooboo CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-KoobooCMS-Version": "^(.+)$\\;version:\\1"
      },
      "icon": "Kooboo CMS.png",
      "implies": "Microsoft ASP.NET",
      "script": "/Kooboo",
      "website": "http://kooboo.com"
    },
    "Kotisivukone": {
      "cats": [
        1
      ],
      "icon": "Kotisivukone.png",
      "script": "kotisivukone(?:\\.min)?\\.js",
      "website": "http://www.kotisivukone.fi"
    },
    "Kubernetes Dashboard": {
      "cats": [
        47
      ],
      "cpe": "cpe:/a:kubernetes:kubernetes",
      "html": "<html ng-app=\"kubernetesDashboard\">",
      "icon": "Kubernetes.svg",
      "website": "https://kubernetes.io/"
    },
    "LEPTON": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:lepton-cms:lepton",
      "icon": "LEPTON.png",
      "implies": "PHP",
      "meta": {
        "generator": "LEPTON"
      },
      "website": "http://www.lepton-cms.org"
    },
    "LOU": {
      "cats": [
        58
      ],
      "icon": "LOU.png",
      "script": "cdn\\.louassist\\.com*",
      "website": "https://www.louassist.com"
    },
    "Lagoon": {
      "cats": [
        62
      ],
      "headers": {
        "X-LAGOON": "",
        "x-lagoon": ""
      },
      "icon": "Lagoon.png",
      "website": "https://www.amazee.io/hosting"
    },
    "Laravel": {
      "cats": [
        18
      ],
      "cookies": {
        "laravel_session": ""
      },
      "cpe": "cpe:/a:laravel:laravel",
      "icon": "Laravel.svg",
      "implies": "PHP",
      "js": {
        "Laravel": ""
      },
      "website": "https://laravel.com"
    },
    "Laterpay": {
      "cats": [
        41
      ],
      "icon": "laterpay.png",
      "meta": {
        "laterpay:connector:callbacks:on_user_has_access": "deobfuscateText"
      },
      "script": "https?://connectormwi\\.laterpay\\.net/([0-9.]+)[a-zA-z-]*/live/[\\w-]+\\.js\\;version:\\1",
      "website": "https://www.laterpay.net/"
    },
    "Leaflet": {
      "cats": [
        35
      ],
      "icon": "Leaflet.png",
      "js": {
        "L.DistanceGrid": "",
        "L.PosAnimation": "",
        "L.version": "^(.+)$\\;version:\\1\\;confidence:0"
      },
      "script": "leaflet.*\\.js",
      "website": "http://leafletjs.com"
    },
    "Less": {
      "cats": [
        19
      ],
      "html": "<link[^>]+ rel=\"stylesheet/less\"",
      "icon": "Less.png",
      "website": "http://lesscss.org"
    },
    "Liferay": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:liferay:liferay_portal",
      "headers": {
        "Liferay-Portal": "[a-z\\s]+([\\d.]+)\\;version:\\1"
      },
      "icon": "Liferay.svg",
      "js": {
        "Liferay": ""
      },
      "website": "https://www.liferay.com"
    },
    "Lift": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:liftweb:lift",
      "headers": {
        "X-Lift-Version": "(.+)\\;version:\\1"
      },
      "icon": "Lift.png",
      "implies": "Scala",
      "website": "http://liftweb.net"
    },
    "LightMon Engine": {
      "cats": [
        1
      ],
      "cookies": {
        "lm_online": ""
      },
      "html": "<!-- Lightmon Engine Copyright Lightmon",
      "icon": "LightMon Engine.png",
      "implies": "PHP",
      "meta": {
        "generator": "LightMon Engine"
      },
      "website": "http://lightmon.ru"
    },
    "Lightbox": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:lightbox_photo_gallery_project:lightbox_photo_gallery",
      "html": "<link [^>]*href=\"[^\"]+lightbox(?:\\.min)?\\.css",
      "icon": "Lightbox.png",
      "script": "lightbox.*\\.js",
      "website": "http://lokeshdhakar.com/projects/lightbox2/"
    },
    "Lightspeed eCom": {
      "cats": [
        6
      ],
      "html": "<!-- \\[START\\] 'blocks/head\\.rain' -->",
      "icon": "Lightspeed.svg",
      "script": "http://assets\\.webshopapp\\.com",
      "url": "seoshop.webshopapp.com",
      "website": "http://www.lightspeedhq.com/products/ecommerce/"
    },
    "LinkSmart": {
      "cats": [
        36
      ],
      "icon": "LinkSmart.png",
      "js": {
        "LS_JSON": "",
        "LinkSmart": "",
        "_mb_site_guid": ""
      },
      "script": "^https?://cdn\\.linksmart\\.com/linksmart_([\\d.]+?)(?:\\.min)?\\.js\\;version:\\1",
      "website": "http://linksmart.com"
    },
    "Linkedin": {
      "cats": [
        5
      ],
      "icon": "Linkedin.svg",
      "script": "//platform\\.linkedin\\.com/in\\.js",
      "website": "http://linkedin.com"
    },
    "Liquid Web": {
      "cats": [
        62
      ],
      "headers": {
        "x-lw-cache": ""
      },
      "icon": "liquidweb.svg",
      "website": "https://www.liquidweb.com"
    },
    "List.js": {
      "cats": [
        59
      ],
      "icon": "List.js.png",
      "js": {
        "List": ""
      },
      "script": "^list\\.(?:min\\.)?js$",
      "website": "http://listjs.com"
    },
    "LiteSpeed": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:litespeedtech:litespeed_web_server",
      "headers": {
        "Server": "^LiteSpeed$"
      },
      "icon": "LiteSpeed.svg",
      "website": "http://litespeedtech.com"
    },
    "Litespeed Cache": {
      "cats": [
        23
      ],
      "headers": {
        "x-litespeed-cache": ""
      },
      "icon": "litespeed-cache.png",
      "implies": "WordPress",
      "website": "https://wordpress.org/plugins/litespeed-cache/"
    },
    "Lithium": {
      "cats": [
        1
      ],
      "cookies": {
        "LithiumVisitor": ""
      },
      "html": " <a [^>]+Powered by Lithium",
      "icon": "Lithium.png",
      "implies": "PHP",
      "js": {
        "LITHIUM": ""
      },
      "website": "https://www.lithium.com"
    },
    "Live Story": {
      "cats": [
        1
      ],
      "icon": "LiveStory.png",
      "js": {
        "LSHelpers": "",
        "LiveStory": ""
      },
      "website": "https://www.livestory.nyc/"
    },
    "LiveAgent": {
      "cats": [
        52
      ],
      "icon": "LiveAgent.png",
      "js": {
        "LiveAgent": ""
      },
      "website": "https://www.ladesk.com"
    },
    "LiveChat": {
      "cats": [
        52
      ],
      "icon": "LiveChat.png",
      "script": "cdn\\.livechatinc\\.com/.*tracking\\.js",
      "website": "http://livechatinc.com"
    },
    "LiveHelp": {
      "cats": [
        52,
        53
      ],
      "icon": "LiveHelp.png",
      "js": {
        "LHready": ""
      },
      "website": "http://www.livehelp.it"
    },
    "LiveJournal": {
      "cats": [
        11
      ],
      "icon": "LiveJournal.png",
      "url": "\\.livejournal\\.com",
      "website": "http://www.livejournal.com"
    },
    "LivePerson": {
      "cats": [
        52
      ],
      "icon": "LivePerson.png",
      "script": "^https?://lptag\\.liveperson\\.net/tag/tag\\.js",
      "website": "https://www.liveperson.com/"
    },
    "LiveStreet CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "LiveStreet CMS"
      },
      "icon": "LiveStreet CMS.png",
      "implies": "PHP",
      "js": {
        "LIVESTREET_SECURITY_KEY": ""
      },
      "website": "http://livestreetcms.com"
    },
    "Livefyre": {
      "cats": [
        15
      ],
      "html": "<[^>]+(?:id|class)=\"livefyre",
      "icon": "Livefyre.png",
      "js": {
        "FyreLoader": "",
        "L.version": "^(.+)$\\;confidence:0\\;version:\\1",
        "LF.CommentCount": "",
        "fyre": ""
      },
      "script": "livefyre_init\\.js",
      "website": "http://livefyre.com"
    },
    "Liveinternet": {
      "cats": [
        10
      ],
      "html": [
        "<script[^<>]*>[^]{0,128}?src\\s*=\\s*['\"]//counter\\.yadro\\.ru/hit(?:;\\S+)?\\?(?:t\\d+\\.\\d+;)?r",
        "<!--LiveInternet counter-->",
        "<!--/LiveInternet-->",
        "<a href=\"http://www\\.liveinternet\\.ru/click\""
      ],
      "icon": "Liveinternet.png",
      "script": "/js/al/common\\.js\\?[0-9_]+",
      "website": "http://liveinternet.ru/rating/"
    },
    "Livewire": {
      "cats": [
        18,
        19
      ],
      "html": "<[^>]+wire:",
      "icon": "Livewire.png",
      "implies": "Laravel",
      "js": {
        "livewire": ""
      },
      "script": "livewire(?:\\.min)?\\.js",
      "website": "https://laravel-livewire.com"
    },
    "LocalFocus": {
      "cats": [
        61
      ],
      "html": "<iframe[^>]+localfocus",
      "icon": "LocalFocus.png",
      "implies": [
        "Angular",
        "D3"
      ],
      "website": "https://www.localfocus.nl/en/"
    },
    "Locomotive": {
      "cats": [
        1
      ],
      "html": "<link[^>]*/sites/[a-z\\d]{24}/theme/stylesheets",
      "icon": "Locomotive.png",
      "implies": [
        "Ruby on Rails",
        "MongoDB"
      ],
      "website": "http://www.locomotivecms.com"
    },
    "Lodash": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:lodash:lodash",
      "excludes": "Underscore.js",
      "icon": "Lo-dash.png",
      "js": {
        "_.VERSION": "^(.+)$\\;confidence:0\\;version:\\1",
        "_.differenceBy": "",
        "_.templateSettings.imports._.templateSettings.imports._.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "lodash.*\\.js",
      "website": "http://www.lodash.com"
    },
    "Logitech Media Server": {
      "cats": [
        22,
        38
      ],
      "headers": {
        "Server": "Logitech Media Server(?: \\(([\\d\\.]+))?\\;version:\\1"
      },
      "icon": "Logitech Media Server.png",
      "website": "http://www.mysqueezebox.com"
    },
    "Loja Integrada": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "vtex-integrated-store"
      },
      "icon": "Loja Integrada.png",
      "js": {
        "window.LOJA_ID": ""
      },
      "website": "https://lojaintegrada.com.br/"
    },
    "Lotus Domino": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:ibm:lotus_domino",
      "headers": {
        "Server": "Lotus-Domino"
      },
      "icon": "Lotus Domino.png",
      "implies": "Java",
      "website": "http://www-01.ibm.com/software/lotus/products/domino"
    },
    "Lua": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:lua:lua",
      "headers": {
        "X-Powered-By": "\\bLua(?: ([\\d.]+))?\\;version:\\1"
      },
      "icon": "Lua.png",
      "website": "http://www.lua.org"
    },
    "Lucene": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:apache:lucene",
      "icon": "Lucene.png",
      "implies": "Java",
      "website": "http://lucene.apache.org/core/"
    },
    "Luigi’s Box": {
      "cats": [
        10,
        29
      ],
      "icon": "Luigisbox.svg",
      "js": {
        "Luigis": ""
      },
      "website": "https://www.luigisbox.com"
    },
    "MODX": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:modx:modx_revolution",
      "headers": {
        "X-Powered-By": "^MODX"
      },
      "html": [
        "<a[^>]+>Powered by MODX</a>",
        "<(?:link|script)[^>]+assets/snippets/\\;confidence:20",
        "<form[^>]+id=\"ajaxSearch_form\\;confidence:20",
        "<input[^>]+id=\"ajaxSearch_input\\;confidence:20"
      ],
      "icon": "MODX.png",
      "implies": "PHP",
      "js": {
        "MODX": "",
        "MODX_MEDIA_PATH": ""
      },
      "meta": {
        "generator": "MODX[^\\d.]*([\\d.]+)?\\;version:\\1"
      },
      "website": "http://modx.com"
    },
    "MadAdsMedia": {
      "cats": [
        36
      ],
      "icon": "MadAdsMedia.png",
      "js": {
        "setMIframe": "",
        "setMRefURL": ""
      },
      "script": "^https?://(?:ads-by|pixel)\\.madadsmedia\\.com/",
      "website": "http://madadsmedia.com"
    },
    "Magento": {
      "cats": [
        6
      ],
      "cookies": {
        "frontend": "\\;confidence:50"
      },
      "cpe": "cpe:/a:magento:magento",
      "html": [
        "<script [^>]+data-requiremodule=\"mage/\\;version:2",
        "<script [^>]+data-requiremodule=\"Magento_\\;version:2",
        "<script type=\"text/x-magento-init\">"
      ],
      "icon": "Magento.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "Mage": "",
        "VarienForm": ""
      },
      "script": [
        "js/mage",
        "skin/frontend/(?:default|(enterprise))\\;version:\\1?Enterprise:Community",
        "static/_requirejs\\;confidence:50\\;version:2"
      ],
      "website": "https://magento.com"
    },
    "MailChimp": {
      "cats": [
        32
      ],
      "cpe": "cpe:/a:thinkshout:mailchimp",
      "html": [
        "<form [^>]*data-mailchimp-url",
        "<form [^>]*id=\"mc-embedded-subscribe-form\"",
        "<form [^>]*name=\"mc-embedded-subscribe-form\"",
        "<input [^>]*id=\"mc-email\"\\;confidence:20",
        "<!-- Begin MailChimp Signup Form -->"
      ],
      "icon": "mailchimp.svg",
      "script": [
        "s3\\.amazonaws\\.com/downloads\\.mailchimp\\.com/js/mc-validate\\.js",
        "cdn-images\\.mailchimp\\.com/[^>]*\\.css"
      ],
      "website": "http://mailchimp.com"
    },
    "MakeShopKorea": {
      "cats": [
        6
      ],
      "icon": "MakeShopKorea.png",
      "js": {
        "Makeshop": "",
        "MakeshopLogUniqueId": ""
      },
      "website": "https://www.makeshop.co.kr"
    },
    "Mambo": {
      "cats": [
        1
      ],
      "excludes": "Joomla",
      "icon": "Mambo.png",
      "meta": {
        "generator": "Mambo"
      },
      "website": "http://mambo-foundation.org"
    },
    "MantisBT": {
      "cats": [
        13
      ],
      "cpe": "cpe:/a:mantisbt:mantisbt",
      "html": "<img[^>]+ alt=\"Powered by Mantis Bugtracker",
      "icon": "MantisBT.png",
      "implies": "PHP",
      "website": "http://www.mantisbt.org"
    },
    "ManyContacts": {
      "cats": [
        5
      ],
      "icon": "ManyContacts.png",
      "script": "\\/assets\\/js\\/manycontacts\\.min\\.js",
      "website": "http://www.manycontacts.com"
    },
    "MariaDB": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:mariadb_project:mariadb",
      "icon": "mariadb.svg",
      "website": "https://mariadb.org"
    },
    "Marionette.js": {
      "cats": [
        12
      ],
      "icon": "Marionette.js.svg",
      "implies": [
        "Underscore.js",
        "Backbone.js"
      ],
      "js": {
        "Marionette": "",
        "Marionette.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "backbone\\.marionette.*\\.js",
      "website": "https://marionettejs.com"
    },
    "Marked": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:marked_project:marked",
      "icon": "marked.svg",
      "js": {
        "marked": ""
      },
      "script": "/marked(?:\\.min)?\\.js",
      "website": "https://marked.js.org"
    },
    "Marketo": {
      "cats": [
        32
      ],
      "icon": "Marketo.png",
      "js": {
        "Munchkin": ""
      },
      "script": "munchkin\\.marketo\\.net/munchkin\\.js",
      "website": "https://www.marketo.com"
    },
    "Material Design Lite": {
      "cats": [
        66
      ],
      "html": "<link[^>]* href=\"[^\"]*material(?:\\.[\\w]+-[\\w]+)?(?:\\.min)?\\.css",
      "icon": "Material Design Lite.png",
      "js": {
        "MaterialIconToggle": ""
      },
      "script": "(?:/([\\d.]+))?/material(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://getmdl.io"
    },
    "Materialize CSS": {
      "cats": [
        66
      ],
      "html": "<link[^>]* href=\"[^\"]*materialize(?:\\.min)?\\.css",
      "icon": "Materialize CSS.png",
      "script": "materialize(?:\\.min)?\\.js",
      "website": "http://materializecss.com"
    },
    "MathJax": {
      "cats": [
        25
      ],
      "icon": "MathJax.png",
      "js": {
        "MathJax": "",
        "MathJax.version": "^(.+)$\\;version:\\1"
      },
      "script": "([\\d.]+)?/mathjax\\.js\\;version:\\1",
      "website": "https://www.mathjax.org"
    },
    "Matomo": {
      "cats": [
        10
      ],
      "cookies": {
        "PIWIK_SESSID": ""
      },
      "cpe": "cpe:/a:matomo:matomo",
      "icon": "Matomo.png",
      "js": {
        "Matomo": "",
        "Piwik": "",
        "_paq": ""
      },
      "meta": {
        "apple-itunes-app": "app-id=737216887",
        "generator": "(?:Matomo|Piwik) - Open Source Web Analytics",
        "google-play-app": "app-id=org\\.piwik\\.mobile2"
      },
      "script": "piwik\\.js|piwik\\.php",
      "website": "https://matomo.org"
    },
    "Mattermost": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:jenkins:mattermost",
      "html": "<noscript> To use Mattermost, please enable JavaScript\\. </noscript>",
      "icon": "mattermost.png",
      "implies": [
        "Go",
        "React"
      ],
      "js": {
        "mm_config": "",
        "mm_current_user_id": "",
        "mm_license": "",
        "mm_user": ""
      },
      "website": "https://about.mattermost.com"
    },
    "Mautic": {
      "cats": [
        32
      ],
      "cpe": "cpe:/a:mautic:mautic",
      "icon": "mautic.svg",
      "js": {
        "MauticTrackingObject": ""
      },
      "script": "[^a-z]mtc.*\\.js",
      "website": "https://www.mautic.org/"
    },
    "MaxCDN": {
      "cats": [
        31
      ],
      "headers": {
        "Server": "^NetDNA",
        "X-CDN-Forward": "^maxcdn$"
      },
      "icon": "MaxCDN.png",
      "website": "http://www.maxcdn.com"
    },
    "MaxSite CMS": {
      "cats": [
        1
      ],
      "icon": "MaxSite CMS.png",
      "implies": "PHP",
      "meta": {
        "generator": "MaxSite CMS"
      },
      "website": "http://max-3000.com"
    },
    "MediaElement.js": {
      "cats": [
        14
      ],
      "icon": "MediaElement.js.png",
      "js": {
        "mejs": "",
        "mejs.version": "^(.+)$\\;version:\\1"
      },
      "website": "http://www.mediaelementjs.com"
    },
    "MediaWiki": {
      "cats": [
        8
      ],
      "cpe": "cpe:/a:mediawiki:mediawiki",
      "html": [
        "<body[^>]+class=\"mediawiki\"",
        "<(?:a|img)[^>]+>Powered by MediaWiki</a>",
        "<a[^>]+/Special:WhatLinksHere/"
      ],
      "icon": "MediaWiki.png",
      "implies": "PHP",
      "js": {
        "mw.util.toggleToc": ""
      },
      "meta": {
        "generator": "^MediaWiki ?(.+)$\\;version:\\1"
      },
      "website": "https://www.mediawiki.org"
    },
    "Medium": {
      "cats": [
        11
      ],
      "headers": {
        "X-Powered-By": "^Medium$"
      },
      "icon": "Medium.svg",
      "implies": "Node.js",
      "script": "medium\\.com",
      "url": "^https?://(?:www\\.)?medium\\.com",
      "website": "https://medium.com"
    },
    "Meebo": {
      "cats": [
        5
      ],
      "html": "(?:<iframe id=\"meebo-iframe\"|Meebo\\('domReady'\\))",
      "icon": "Meebo.png",
      "website": "http://www.meebo.com"
    },
    "Melis Platform": {
      "cats": [
        1,
        6,
        11,
        32
      ],
      "cpe": "cpe:/a:melisplatform:melisplatform",
      "html": [
        "<!-- Rendered with Melis CMS V2",
        "<!-- Rendered with Melis Platform"
      ],
      "icon": "melis-platform.svg",
      "implies": [
        "Apache",
        "PHP",
        "MySQL",
        "Symfony",
        "Laravel",
        "Zend"
      ],
      "meta": {
        "generator": "^Melis Platform\\.",
        "powered-by": "^Melis CMS\\."
      },
      "website": "https://www.melistechnology.com/"
    },
    "MemberStack": {
      "cats": [
        6,
        47
      ],
      "cookies": {
        "memberstack": ""
      },
      "icon": "MemberStack.png",
      "js": {
        "MemberStack": ""
      },
      "script": "memberstack\\.js",
      "url": "^https?//.+\\.memberstack\\.io",
      "website": "https://www.memberstack.io"
    },
    "Mermaid": {
      "cats": [
        25
      ],
      "html": "<div [^>]*class=[\"']mermaid[\"']>\\;confidence:90",
      "js": {
        "mermaid": ""
      },
      "script": "/mermaid(?:\\.min)?\\.js",
      "website": "https://mermaidjs.github.io/"
    },
    "Meteor": {
      "cats": [
        12,
        18
      ],
      "html": "<link[^>]+__meteor-css__",
      "icon": "Meteor.png",
      "implies": [
        "MongoDB",
        "Node.js"
      ],
      "js": {
        "Meteor": "",
        "Meteor.release": "^METEOR@([\\d.]+)\\;version:\\1"
      },
      "website": "https://www.meteor.com"
    },
    "Methode": {
      "cats": [
        1
      ],
      "html": "<!-- Methode uuid: \"[a-f\\d]+\" ?-->",
      "icon": "Methode.png",
      "meta": {
        "eomportal-id": "\\d+",
        "eomportal-instanceid": "\\d+",
        "eomportal-lastUpdate": "",
        "eomportal-loid": "[\\d.]+",
        "eomportal-uuid": "[a-f\\d]+"
      },
      "website": "https://www.eidosmedia.com/"
    },
    "Microsoft ASP.NET": {
      "cats": [
        18
      ],
      "cookies": {
        "ASP.NET_SessionId": "",
        "ASPSESSION": ""
      },
      "cpe": "cpe:/a:microsoft:asp.net",
      "headers": {
        "X-AspNet-Version": "(.+)\\;version:\\1",
        "X-Powered-By": "^ASP\\.NET"
      },
      "html": "<input[^>]+name=\"__VIEWSTATE",
      "icon": "Microsoft ASP.NET.png",
      "implies": "IIS\\;confidence:50",
      "url": "\\.aspx?(?:$|\\?)",
      "website": "https://www.asp.net"
    },
    "Microsoft Excel": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:microsoft:excel",
      "html": "(?:<html [^>]*xmlns:w=\"urn:schemas-microsoft-com:office:excel\"|<!--\\s*(?:START|END) OF OUTPUT FROM EXCEL PUBLISH AS WEB PAGE WIZARD\\s*-->|<div [^>]*x:publishsource=\"?Excel\"?)",
      "icon": "Microsoft Excel.svg",
      "meta": {
        "ProgId": "^Excel\\.",
        "generator": "Microsoft Excel( [\\d.]+)?\\;version:\\1"
      },
      "website": "https://office.microsoft.com/excel"
    },
    "Microsoft HTTPAPI": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Microsoft-HTTPAPI(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Microsoft.png",
      "website": "http://microsoft.com"
    },
    "Microsoft PowerPoint": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:microsoft:powerpoint",
      "html": "(?:<html [^>]*xmlns:w=\"urn:schemas-microsoft-com:office:powerpoint\"|<link rel=\"?Presentation-XML\"? href=\"?[^\"]+\\.xml\"?>|<o:PresentationFormat>[^<]+</o:PresentationFormat>[^!]+<o:Slides>\\d+</o:Slides>(?:[^!]+<o:Version>([\\d.]+)</o:Version>)?)\\;version:\\1",
      "icon": "Microsoft PowerPoint.svg",
      "meta": {
        "ProgId": "^PowerPoint\\.",
        "generator": "Microsoft PowerPoint ( [\\d.]+)?\\;version:\\1"
      },
      "website": "https://office.microsoft.com/powerpoint"
    },
    "Microsoft Publisher": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:microsoft:publisher",
      "html": "(?:<html [^>]*xmlns:w=\"urn:schemas-microsoft-com:office:publisher\"|<!--[if pub]><xml>)",
      "icon": "Microsoft Publisher.svg",
      "meta": {
        "ProgId": "^Publisher\\.",
        "generator": "Microsoft Publisher( [\\d.]+)?\\;version:\\1"
      },
      "website": "https://office.microsoft.com/publisher"
    },
    "Microsoft SharePoint": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:microsoft:sharepoint_server",
      "headers": {
        "MicrosoftSharePointTeamServices": "^(.+)$\\;version:\\1",
        "SPRequestGuid": "",
        "SharePointHealthScore": "",
        "X-SharePointHealthScore": ""
      },
      "icon": "Microsoft SharePoint.png",
      "js": {
        "SPDesignerProgID": "",
        "_spBodyOnLoadCalled": ""
      },
      "meta": {
        "generator": "Microsoft SharePoint"
      },
      "website": "https://sharepoint.microsoft.com"
    },
    "Microsoft Word": {
      "cats": [
        20
      ],
      "cpe": "cpe:/a:microsoft:word",
      "html": "(?:<html [^>]*xmlns:w=\"urn:schemas-microsoft-com:office:word\"|<w:WordDocument>|<div [^>]*class=\"?WordSection1[\" >]|<style[^>]*>[^>]*@page WordSection1)",
      "icon": "Microsoft Word.svg",
      "meta": {
        "ProgId": "^Word\\.",
        "generator": "Microsoft Word( [\\d.]+)?\\;version:\\1"
      },
      "website": "https://office.microsoft.com/word"
    },
    "Milligram": {
      "cats": [
        66
      ],
      "html": [
        "<link[^>]+?href=\"[^\"]+milligram(?:\\.min)?\\.css"
      ],
      "icon": "Milligram.png",
      "website": "https://milligram.io"
    },
    "Minero.cc": {
      "cats": [
        56
      ],
      "script": [
        "//minero\\.cc/lib/minero(?:-miner|-hidden)?\\.min\\.js"
      ],
      "website": "http://minero.cc/"
    },
    "MiniBB": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:minibb:minibb",
      "html": "<a href=\"[^\"]+minibb[^<]+</a>[^<]+\\n<!--End of copyright link",
      "icon": "MiniBB.png",
      "website": "http://www.minibb.com"
    },
    "MiniServ": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "MiniServ\\/?([\\d\\.]+)?\\;version:\\1"
      },
      "website": "http://sourceforge.net/projects/miniserv"
    },
    "Mint": {
      "cats": [
        10
      ],
      "icon": "Mint.png",
      "js": {
        "Mint": ""
      },
      "script": "mint/\\?js",
      "website": "https://haveamint.com"
    },
    "Miva": {
      "cats": [
        6
      ],
      "headers": {
        "content-disposition": "filename=(?:mvga\\.js|MivaEvents\\.js)"
      },
      "icon": "miva.png",
      "js": {
        "MivaVM_API": "",
        "MivaVM_Version": "^(.+)$\\;version:\\1",
        "mivaJS": "",
        "mivaJS.Page": "",
        "mivaJS.Product_Code": "",
        "mivaJS.Product_ID": "",
        "mivaJS.Screen": "",
        "mivaJS.Store_Code": ""
      },
      "script": "mvga\\.js",
      "website": "http://www.miva.com"
    },
    "Mixpanel": {
      "cats": [
        10
      ],
      "icon": "Mixpanel.png",
      "js": {
        "mixpanel": ""
      },
      "script": "api\\.mixpanel\\.com/track",
      "website": "https://mixpanel.com"
    },
    "MkDocs": {
      "cats": [
        4
      ],
      "icon": "mkdocs.png",
      "meta": {
        "generator": "^mkdocs-([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.mkdocs.org/"
    },
    "MobX": {
      "cats": [
        59
      ],
      "icon": "MobX.svg",
      "js": {
        "__mobxGlobal": "",
        "__mobxGlobals": "",
        "__mobxInstanceCount": ""
      },
      "script": "(?:/([\\d\\.]+))?/mobx(?:\\.[a-z]+){0,2}\\.js(?:$|\\?)\\;version:\\1",
      "website": "https://mobx.js.org"
    },
    "Mobify": {
      "cats": [
        26
      ],
      "icon": "Mobify.png",
      "js": {
        "Mobify": ""
      },
      "script": "//cdn\\.mobify\\.com/",
      "website": "https://www.mobify.com"
    },
    "Mobirise": {
      "cats": [
        51
      ],
      "html": [
        "<!-- Site made with Mobirise Website Builder v([\\d.]+)\\;version:\\1"
      ],
      "icon": "mobirise.png",
      "meta": {
        "generator": "^Mobirise v([\\d.]+)\\;version:\\1"
      },
      "website": "https://mobirise.com"
    },
    "MochiKit": {
      "cats": [
        59
      ],
      "icon": "MochiKit.png",
      "js": {
        "MochiKit": "",
        "MochiKit.MochiKit.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "MochiKit(?:\\.min)?\\.js",
      "website": "https://mochi.github.io/mochikit/"
    },
    "MochiWeb": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:mochiweb_project:mochiweb",
      "headers": {
        "Server": "MochiWeb(?:/([\\d.]+))?\\;version:\\1"
      },
      "website": "https://github.com/mochi/mochiweb"
    },
    "Modernizr": {
      "cats": [
        59
      ],
      "icon": "Modernizr.svg",
      "js": {
        "Modernizr._version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "([\\d.]+)?/modernizr(?:\\.([\\d.]+))?.*\\.js\\;version:\\1?\\1:\\2"
      ],
      "website": "https://modernizr.com"
    },
    "Modified": {
      "cats": [
        6
      ],
      "icon": "modified.png",
      "meta": {
        "generator": "\\(c\\) by modified eCommerce Shopsoftware ------ http://www\\.modified-shop\\.org"
      },
      "website": "http://www.modified-shop.org/"
    },
    "Moguta.CMS": {
      "cats": [
        1,
        6
      ],
      "html": "<link[^>]+href=[\"'][^\"]+mg-(?:core|plugins|templates)/",
      "icon": "Moguta.CMS.png",
      "implies": "PHP",
      "script": "mg-(?:core|plugins|templates)/",
      "website": "https://moguta.ru"
    },
    "MoinMoin": {
      "cats": [
        8
      ],
      "cookies": {
        "MOIN_SESSION": ""
      },
      "cpe": "cpe:/a:moinmo:moinmoin",
      "icon": "MoinMoin.png",
      "implies": "Python",
      "js": {
        "show_switch2gui": ""
      },
      "script": "moin(?:_static(\\d)(\\d)(\\d)|.+)/common/js/common\\.js\\;version:\\1.\\2.\\3",
      "website": "https://moinmo.in"
    },
    "Mojolicious": {
      "cats": [
        18
      ],
      "headers": {
        "server": "^mojolicious",
        "x-powered-by": "mojolicious"
      },
      "icon": "Mojolicious.png",
      "implies": "Perl",
      "website": "http://mojolicio.us"
    },
    "Mollom": {
      "cats": [
        16
      ],
      "cpe": "cpe:/a:acquia:mollom",
      "html": "<img[^>]+\\.mollom\\.com",
      "icon": "Mollom.png",
      "script": "mollom(?:\\.min)?\\.js",
      "website": "http://mollom.com"
    },
    "Moment Timezone": {
      "cats": [
        59
      ],
      "icon": "Moment.js.svg",
      "implies": "Moment.js",
      "script": "moment-timezone(?:-data)?(?:\\.min)?\\.js",
      "website": "http://momentjs.com/timezone/"
    },
    "Moment.js": {
      "cats": [
        59
      ],
      "icon": "Moment.js.svg",
      "js": {
        "moment": "",
        "moment.version": "^(.+)$\\;version:\\1"
      },
      "script": "moment(?:\\.min)?\\.js",
      "website": "https://momentjs.com"
    },
    "Mondo Media": {
      "cats": [
        6
      ],
      "icon": "Mondo Media.png",
      "meta": {
        "generator": "Mondo Shop"
      },
      "website": "http://mondo-media.de"
    },
    "MongoDB": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:mongodb:mongodb",
      "icon": "MongoDB.png",
      "website": "http://www.mongodb.org"
    },
    "Mongrel": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:zed_shaw:mongrel",
      "headers": {
        "Server": "Mongrel"
      },
      "icon": "Mongrel.png",
      "implies": "Ruby",
      "website": "http://mongrel2.org"
    },
    "Monkey HTTP Server": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Monkey/?([\\d.]+)?\\;version:\\1"
      },
      "icon": "Monkey HTTP Server.png",
      "website": "http://monkey-project.com"
    },
    "Mono": {
      "cats": [
        18
      ],
      "cpe": "cpe:/a:mono:mono",
      "headers": {
        "X-Powered-By": "Mono"
      },
      "icon": "Mono.png",
      "website": "http://mono-project.com"
    },
    "Mono.net": {
      "cats": [
        1
      ],
      "icon": "Mono.net.png",
      "implies": "Matomo",
      "js": {
        "_monoTracker": ""
      },
      "script": "monotracker(?:\\.min)?\\.js",
      "website": "https://www.mono.net/en"
    },
    "MooTools": {
      "cats": [
        12
      ],
      "icon": "MooTools.png",
      "js": {
        "MooTools": "",
        "MooTools.version": "^(.+)$\\;version:\\1"
      },
      "script": "mootools.*\\.js",
      "website": "https://mootools.net"
    },
    "Moodle": {
      "cats": [
        21
      ],
      "cookies": {
        "MOODLEID_": "",
        "MoodleSession": ""
      },
      "cpe": "cpe:/a:moodle:moodle",
      "html": "<img[^>]+moodlelogo",
      "icon": "Moodle.png",
      "implies": "PHP",
      "js": {
        "M.core": "",
        "Y.Moodle": ""
      },
      "meta": {
        "keywords": "^moodle"
      },
      "website": "http://moodle.org"
    },
    "Moon": {
      "cats": [
        12
      ],
      "icon": "moon.svg",
      "script": "/moon(?:\\.min)?\\.js$",
      "website": "https://kbrsh.github.io/moon/"
    },
    "MotoCMS": {
      "cats": [
        1
      ],
      "html": "<link [^>]*href=\"[^>]*\\/mt-content\\/[^>]*\\.css",
      "icon": "MotoCMS.svg",
      "implies": [
        "PHP",
        "AngularJS",
        "jQuery"
      ],
      "script": "/mt-includes/js/website(?:assets)?\\.(?:min)?\\.js",
      "website": "http://motocms.com"
    },
    "Mouse Flow": {
      "cats": [
        10
      ],
      "icon": "mouseflow.png",
      "js": {
        "_mfq": ""
      },
      "script": [
        "cdn\\.mouseflow\\.com"
      ],
      "website": "https://mouseflow.com/"
    },
    "Movable Type": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:sixapart:movable_type",
      "icon": "Movable Type.png",
      "meta": {
        "generator": "Movable Type"
      },
      "website": "http://movabletype.org"
    },
    "Mozard Suite": {
      "cats": [
        1
      ],
      "icon": "Mozard Suite.png",
      "meta": {
        "author": "Mozard"
      },
      "url": "/mozard/!suite",
      "website": "http://mozard.nl"
    },
    "Mura CMS": {
      "cats": [
        1,
        11
      ],
      "icon": "Mura CMS.png",
      "implies": "Adobe ColdFusion",
      "meta": {
        "generator": "Mura CMS ([\\d]+)\\;version:\\1"
      },
      "website": "http://www.getmura.com"
    },
    "Mustache": {
      "cats": [
        12
      ],
      "icon": "Mustache.png",
      "js": {
        "Mustache.version": "^(.+)$\\;version:\\1"
      },
      "script": "mustache(?:\\.min)?\\.js",
      "website": "https://mustache.github.io"
    },
    "MyBB": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:mybb:mybb",
      "html": "(?:<script [^>]+\\s+<!--\\s+lang\\.no_new_posts|<a[^>]* title=\"Powered By MyBB)",
      "icon": "MyBB.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "MyBB": ""
      },
      "website": "https://mybb.com"
    },
    "MyBlogLog": {
      "cats": [
        5
      ],
      "icon": "MyBlogLog.png",
      "script": "pub\\.mybloglog\\.com",
      "website": "http://www.mybloglog.com"
    },
    "MyCashFlow": {
      "cats": [
        6
      ],
      "headers": {
        "X-MCF-ID": ""
      },
      "icon": "mycashflow.png",
      "website": "https://www.mycashflow.fi/"
    },
    "MySQL": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:mysql:mysql",
      "icon": "MySQL.svg",
      "website": "http://mysql.com"
    },
    "MyWebsite": {
      "cats": [
        1
      ],
      "icon": "Ionos-by-1and1-logo.svg",
      "js": {
        "SystemID": "^.*1AND1.*$",
        "version": "^(.*)$\\;version:\\1\\;confidence:0"
      },
      "meta": {
        "generator": "^.*MyWebsite.*$\\;version:8"
      },
      "script": "\\/\\/integration\\.mywebsite-editor\\.com.*\\.js\\;version:9",
      "website": "https://www.ionos.com"
    },
    "Mynetcap": {
      "cats": [
        1
      ],
      "icon": "Mynetcap.png",
      "meta": {
        "generator": "Mynetcap"
      },
      "website": "http://www.netcap-creation.fr"
    },
    "NEO - Omnichannel Commerce Platform": {
      "cats": [
        6
      ],
      "headers": {
        "powered": "jet-neo"
      },
      "icon": "Plataforma NEO.svg",
      "website": "http://www.jetecommerce.com.br/"
    },
    "NVD3": {
      "cats": [
        25
      ],
      "html": "<link[^>]* href=[^>]+nv\\.d3(?:\\.min)?\\.css",
      "icon": "NVD3.png",
      "implies": "D3",
      "js": {
        "nv.addGraph": "",
        "nv.version": "^(.+)$\\;confidence:0\\;version:\\1"
      },
      "script": "nv\\.d3(?:\\.min)?\\.js",
      "website": "http://nvd3.org"
    },
    "Navegg": {
      "cats": [
        10
      ],
      "icon": "Navegg.png",
      "script": "tag\\.navdmp\\.com",
      "website": "https://www.navegg.com/"
    },
    "Neos CMS": {
      "cats": [
        1
      ],
      "excludes": "TYPO3 CMS",
      "headers": {
        "X-Flow-Powered": "Neos/?(.+)?$\\;version:\\1"
      },
      "icon": "Neos.svg",
      "implies": "Neos Flow",
      "url": "/neos/",
      "website": "https://neos.io"
    },
    "Neos Flow": {
      "cats": [
        18
      ],
      "excludes": "TYPO3 CMS",
      "headers": {
        "X-Flow-Powered": "Flow/?(.+)?$\\;version:\\1"
      },
      "icon": "Neos.svg",
      "implies": "PHP",
      "website": "https://flow.neos.io"
    },
    "Nepso": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-CMS": "Nepso"
      },
      "icon": "nepso.svg",
      "website": "https://www.nepso.com"
    },
    "NetSuite": {
      "cats": [
        6
      ],
      "cookies": {
        "NS_VER": ""
      },
      "icon": "NetSuite.png",
      "website": "http://netsuite.com"
    },
    "Netlify": {
      "cats": [
        62,
        31
      ],
      "headers": {
        "Server": "^Netlify",
        "X-NF-Request-ID": ""
      },
      "icon": "Netlify.svg",
      "url": "^https?://[^/]+\\.netlify\\.(?:com|app)/",
      "website": "https://www.netlify.com/"
    },
    "Neto": {
      "cats": [
        6
      ],
      "icon": "Neto.svg",
      "js": {
        "NETO": ""
      },
      "script": "jquery\\.neto.*\\.js",
      "website": "https://www.neto.com.au"
    },
    "Nette Framework": {
      "cats": [
        18
      ],
      "cookies": {
        "nette-browser": ""
      },
      "headers": {
        "X-Powered-By": "^Nette Framework"
      },
      "html": [
        "<input[^>]+data-nette-rules",
        "<div[^>]+id=\"snippet-",
        "<input[^>]+id=\"frm-"
      ],
      "icon": "Nette Framework.png",
      "implies": "PHP",
      "js": {
        "Nette": "",
        "Nette.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://nette.org"
    },
    "New Relic": {
      "cats": [
        10
      ],
      "icon": "New Relic.png",
      "js": {
        "NREUM": "",
        "newrelic": ""
      },
      "website": "https://newrelic.com"
    },
    "Next.js": {
      "cats": [
        18,
        22
      ],
      "cpe": "cpe:/a:zeit:next.js",
      "headers": {
        "x-powered-by": "^Next\\.js ?([0-9.]+)?\\;version:\\1"
      },
      "icon": "vercel.svg",
      "implies": [
        "React",
        "webpack",
        "Node.js"
      ],
      "js": {
        "__NEXT_DATA__": ""
      },
      "website": "https://nextjs.org"
    },
    "NextGEN Gallery": {
      "cats": [
        7
      ],
      "cpe": "cpe:/a:imagely:nextgen_gallery",
      "html": [
        "<!-- <meta name=\"NextGEN\" version=\"([\\d.]+)\" /> -->\\;version:\\1"
      ],
      "icon": "NextGEN Gallery.png",
      "implies": "WordPress",
      "script": "/nextgen-gallery/js/",
      "website": "https://www.imagely.com/wordpress-gallery-plugin"
    },
    "Nginx": {
      "cats": [
        22,
        64
      ],
      "cpe": "cpe:/a:nginx:nginx",
      "headers": {
        "Server": "nginx(?:/([\\d.]+))?\\;version:\\1",
        "X-Fastcgi-Cache": ""
      },
      "icon": "Nginx.svg",
      "website": "http://nginx.org/en"
    },
    "NivCMS": {
      "cats": [
        1
      ],
      "cookies": {
        "cookie_name": "NivCMSPro"
      },
      "headers": {
        "X-Powered-By": "NivCMS"
      },
      "icon": "nivsoft.png",
      "meta": {
        "generator": "^NivCMS"
      },
      "website": "https://NivSoft.ir"
    },
    "Node.js": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:nodejs:node.js",
      "icon": "node.js.png",
      "website": "http://nodejs.org"
    },
    "NodeBB": {
      "cats": [
        2
      ],
      "cpe": "cpe:/a:nodebb:nodebb",
      "headers": {
        "X-Powered-By": "^NodeBB$"
      },
      "icon": "NodeBB.png",
      "implies": "Node.js",
      "script": "^/nodebb\\.min\\.js\\?",
      "website": "https://nodebb.org"
    },
    "Nuvemshop": {
      "cats": [
        6
      ],
      "html": "<a target=\"_blank\" title=\"Nuvemshop\"",
      "icon": "nuvem.png",
      "script": "Nuvem",
      "website": "https://www.nuvemshop.com.br/"
    },
    "Nuxt.js": {
      "cats": [
        12
      ],
      "html": [
        "<div [^>]*id=\"__nuxt\"",
        "<script [^>]*>window\\.__NUXT__"
      ],
      "icon": "Nuxt.js.svg",
      "implies": [
        "Vue.js",
        "Node.js"
      ],
      "js": {
        "$nuxt": ""
      },
      "script": [
        "/_nuxt/"
      ],
      "website": "https://nuxtjs.org"
    },
    "OWL Carousel": {
      "cats": [
        5
      ],
      "html": "<link [^>]*href=\"[^\"]+owl\\.carousel(?:\\.min)?\\.css",
      "icon": "OWL Carousel.png",
      "implies": "jQuery",
      "script": "owl\\.carousel.*\\.js",
      "website": "https://owlcarousel2.github.io/OwlCarousel2/"
    },
    "OXID eShop": {
      "cats": [
        6
      ],
      "html": "<!--[^-]*OXID eShop",
      "icon": "OXID eShop.png",
      "js": {
        "oxCookieNote": "",
        "oxInputValidator": "",
        "oxLoginBox": "",
        "oxModalPopup": "",
        "oxTopMenu": ""
      },
      "website": "https://en.oxid-esales.com/en/home.html"
    },
    "October CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "october_session": ""
      },
      "icon": "October CMS.png",
      "implies": "Laravel",
      "meta": {
        "generator": "OctoberCMS"
      },
      "website": "http://octobercms.com"
    },
    "Octopress": {
      "cats": [
        57
      ],
      "html": "Powered by <a href=\"http://octopress\\.org\">",
      "icon": "octopress.png",
      "implies": "Jekyll",
      "meta": {
        "generator": "Octopress"
      },
      "script": "/octopress\\.js",
      "website": "http://octopress.org"
    },
    "Odoo": {
      "cats": [
        1,
        6
      ],
      "cpe": "cpe:/a:odoo:odoo",
      "html": "<link[^>]* href=[^>]+/web/css/(?:web\\.assets_common/|website\\.assets_frontend/)\\;confidence:25",
      "icon": "Odoo.png",
      "implies": [
        "Python",
        "PostgreSQL",
        "Node.js",
        "Less"
      ],
      "meta": {
        "generator": "Odoo"
      },
      "script": "/web/js/(?:web\\.assets_common/|website\\.assets_frontend/)\\;confidence:25",
      "website": "http://odoo.com"
    },
    "Olark": {
      "cats": [
        52
      ],
      "icon": "Olark.png",
      "script": "^https?:\\/\\/static\\.olark\\.com\\/jsclient\\/loader1\\.js",
      "website": "https://www.olark.com/"
    },
    "OneAPM": {
      "cats": [
        10
      ],
      "icon": "OneAPM.png",
      "js": {
        "BWEUM": ""
      },
      "website": "http://www.oneapm.com"
    },
    "OneStat": {
      "cats": [
        10
      ],
      "icon": "OneStat.png",
      "js": {
        "OneStat_Pageview": ""
      },
      "website": "http://www.onestat.com"
    },
    "Onshop": {
      "cats": [
        6
      ],
      "excludes": "OpenCart",
      "icon": "Onshop.svg",
      "implies": "PHP",
      "meta": {
        "generator": "Onshop Ecommerce"
      },
      "script": "/opencart_custom\\.js",
      "website": "https://onshop.asia"
    },
    "Open AdStream": {
      "cats": [
        36
      ],
      "icon": "Open AdStream.png",
      "js": {
        "OAS_AD": ""
      },
      "website": "https://www.xaxis.com"
    },
    "Open Classifieds": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:open-classifieds:open_classifieds",
      "icon": "Open Classifieds.png",
      "meta": {
        "author": "open-classifieds\\.com",
        "copyright": "Open Classifieds ?([0-9.]+)?\\;version:\\1"
      },
      "website": "http://open-classifieds.com"
    },
    "Open Journal Systems": {
      "cats": [
        50
      ],
      "cookies": {
        "OJSSID": ""
      },
      "cpe": "cpe:/a:public_knowledge_project:open_journal_systems",
      "icon": "Open Journal Systems.png",
      "implies": "PHP",
      "meta": {
        "generator": "Open Journal Systems(?: ([\\d.]+))?\\;version:\\1"
      },
      "website": "http://pkp.sfu.ca/ojs"
    },
    "Open Web Analytics": {
      "cats": [
        10
      ],
      "cpe": "cpe:/a:openwebanalytics:open_web_analytics",
      "html": "<!-- (?:Start|End) Open Web Analytics Tracker -->",
      "icon": "Open Web Analytics.png",
      "js": {
        "OWA.config.baseUrl": "",
        "owa_baseUrl": "",
        "owa_cmds": ""
      },
      "website": "http://www.openwebanalytics.com"
    },
    "Open eShop": {
      "cats": [
        6
      ],
      "icon": "Open eShop.png",
      "implies": "PHP",
      "meta": {
        "author": "open-eshop\\.com",
        "copyright": "Open eShop ?([0-9.]+)?\\;version:\\1"
      },
      "website": "http://open-eshop.com/"
    },
    "OpenBSD httpd": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^OpenBSD httpd"
      },
      "website": "https://man.openbsd.org/httpd.8"
    },
    "OpenCart": {
      "cats": [
        6
      ],
      "cookies": {
        "OCSESSID": ""
      },
      "cpe": "cpe:/a:opencart:opencart",
      "icon": "OpenCart.png",
      "implies": "PHP",
      "website": "http://www.opencart.com"
    },
    "OpenCms": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:alkacon:opencms",
      "headers": {
        "Server": "OpenCms"
      },
      "html": "<link href=\"/opencms/",
      "icon": "OpenCms.png",
      "implies": "Java",
      "script": "opencms",
      "website": "http://www.opencms.org"
    },
    "OpenGSE": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "GSE"
      },
      "icon": "Google.svg",
      "implies": "Java",
      "website": "http://code.google.com/p/opengse"
    },
    "OpenGrok": {
      "cats": [
        19
      ],
      "cookies": {
        "OpenGrok": ""
      },
      "icon": "OpenGrok.png",
      "implies": "Java",
      "meta": {
        "generator": "OpenGrok(?: v?([\\d.]+))?\\;version:\\1"
      },
      "website": "http://hub.opensolaris.org/bin/view/Project+opengrok/WebHome"
    },
    "OpenLayers": {
      "cats": [
        35
      ],
      "icon": "OpenLayers.png",
      "js": {
        "OpenLayers.VERSION_NUMBER": "([\\d.]+)\\;version:\\1",
        "ol.CanvasMap": ""
      },
      "script": "openlayers",
      "website": "https://openlayers.org"
    },
    "OpenNemas": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "OpenNemas"
      },
      "icon": "OpenNemas.png",
      "meta": {
        "generator": "OpenNemas"
      },
      "website": "http://www.opennemas.com"
    },
    "OpenResty": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "openresty(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "OpenResty.png",
      "implies": [
        "Nginx",
        "Lua"
      ],
      "website": "http://openresty.org"
    },
    "OpenSSL": {
      "cats": [
        33
      ],
      "cpe": "cpe:/a:openssl:openssl",
      "headers": {
        "Server": "OpenSSL(?:/([\\d.]+[a-z]?))?\\;version:\\1"
      },
      "icon": "OpenSSL.png",
      "website": "http://openssl.org"
    },
    "OpenText Web Solutions": {
      "cats": [
        1
      ],
      "html": "<!--[^>]+published by Open Text Web Solutions",
      "icon": "OpenText Web Solutions.png",
      "implies": "Microsoft ASP.NET",
      "website": "http://websolutions.opentext.com"
    },
    "OpenUI5": {
      "cats": [
        12
      ],
      "icon": "OpenUI5.png",
      "js": {
        "sap.ui.version": "^(.+)$\\;version:\\1"
      },
      "script": "sap-ui-core\\.js",
      "website": "http://openui5.org/"
    },
    "OpenX": {
      "cats": [
        36
      ],
      "cpe": "cpe:/a:openx:openx",
      "icon": "OpenX.png",
      "script": [
        "https?://[^/]*\\.openx\\.net",
        "https?://[^/]*\\.servedbyopenx\\.com"
      ],
      "website": "http://openx.com"
    },
    "Optimizely": {
      "cats": [
        10
      ],
      "icon": "Optimizely.png",
      "js": {
        "optimizely": ""
      },
      "script": "optimizely\\.com.*\\.js",
      "website": "https://www.optimizely.com"
    },
    "Oracle Application Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:oracle:application_server",
      "headers": {
        "Server": "Oracle[- ]Application[- ]Server(?: Containers for J2EE)?(?:[- ](\\d[\\da-z./]+))?\\;version:\\1"
      },
      "icon": "Oracle.png",
      "website": "http://www.oracle.com/technetwork/middleware/ias/overview/index.html"
    },
    "Oracle Commerce": {
      "cats": [
        6
      ],
      "cpe": "cpe:/a:oracle:commerce_platform",
      "headers": {
        "X-ATG-Version": "(?:ATGPlatform/([\\d.]+))?\\;version:\\1"
      },
      "html": "<[^>]+_dyncharset",
      "icon": "Oracle.png",
      "website": "http://www.oracle.com/applications/customer-experience/commerce/products/commerce-platform/index.html"
    },
    "Oracle Commerce Cloud": {
      "cats": [
        6
      ],
      "headers": {
        "OracleCommerceCloud-Version": "^(.+)$\\;version:\\1"
      },
      "html": "<[^>]+id=\"oracle-cc\"",
      "icon": "Oracle.png",
      "website": "http://cloud.oracle.com/commerce-cloud"
    },
    "Oracle Dynamic Monitoring Service": {
      "cats": [
        19
      ],
      "headers": {
        "x-oracle-dms-ecid": ""
      },
      "icon": "Oracle.png",
      "website": "http://oracle.com"
    },
    "Oracle HTTP Server": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:oracle:http_server",
      "headers": {
        "Server": "Oracle-HTTP-Server(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Oracle.png",
      "website": "http://oracle.com"
    },
    "Oracle Recommendations On Demand": {
      "cats": [
        10
      ],
      "icon": "Oracle.png",
      "script": "atgsvcs.+atgsvcs\\.js",
      "website": "http://www.oracle.com/us/products/applications/commerce/recommendations-on-demand/index.html"
    },
    "Oracle Web Cache": {
      "cats": [
        23
      ],
      "cpe": "cpe:/a:oracle:web_cache",
      "headers": {
        "Server": "Oracle(?:AS)?[- ]Web[- ]Cache(?:[- /]([\\da-z./]+))?\\;version:\\1"
      },
      "icon": "Oracle.png",
      "website": "http://oracle.com"
    },
    "Orchard CMS": {
      "cats": [
        1
      ],
      "icon": "Orchard CMS.png",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "Orchard"
      },
      "website": "http://orchardproject.net"
    },
    "OroCommerce": {
      "cats": [
        6
      ],
      "html": [
        "<script [^>]+data-requiremodule=\"oro/",
        "<script [^>]+data-requiremodule=\"oroui/"
      ],
      "icon": "orocommerce.svg",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "script": [
        "oro\\.min\\.js\\?version=([\\d.]+)\\;version:\\1"
      ],
      "website": "https://oroinc.com"
    },
    "Outbrain": {
      "cats": [
        5
      ],
      "icon": "Outbrain.png",
      "js": {
        "OB_releaseVer": "^(.+)$\\;version:\\1",
        "OutbrainPermaLink": ""
      },
      "script": "widgets\\.outbrain\\.com/outbrain\\.js",
      "website": "https://www.outbrain.com"
    },
    "Outlook Web App": {
      "cats": [
        30
      ],
      "html": "<link\\s[^>]*href=\"[^\"]*?([\\d.]+)/themes/resources/owafont\\.css\\;version:\\1",
      "icon": "Outlook.svg",
      "implies": "Microsoft ASP.NET",
      "js": {
        "IsOwaPremiumBrowser": ""
      },
      "url": "/owa/auth/log(?:on|off)\\.aspx",
      "website": "http://help.outlook.com"
    },
    "PDF.js": {
      "cats": [
        19
      ],
      "html": "<\\/div>\\s*<!-- outerContainer -->\\s*<div\\s*id=\"printContainer\"><\\/div>",
      "icon": "PDF.js.svg",
      "js": {
        "PDFJS": "",
        "PDFJS.version": "^(.+)$\\;version:\\1",
        "_pdfjsCompatibilityChecked": "",
        "pdfjs-dist/build/pdf.version": "^(.+)$\\;version:\\1",
        "pdfjsDistBuildPdf.version": "^(.+)$\\;version:\\1",
        "pdfjsLib.version": "^(.+)$\\;version:\\1"
      },
      "url": "/web/viewer\\.html?file=[^&]\\.pdf",
      "website": "https://mozilla.github.io/pdf.js/"
    },
    "PHP": {
      "cats": [
        27
      ],
      "cookies": {
        "PHPSESSID": ""
      },
      "cpe": "cpe:/a:php:php",
      "headers": {
        "Server": "php/?([\\d.]+)?\\;version:\\1",
        "X-Powered-By": "^php/?([\\d.]+)?\\;version:\\1"
      },
      "icon": "PHP.svg",
      "url": "\\.php(?:$|\\?)",
      "website": "http://php.net"
    },
    "PHP-Fusion": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:php-fusion:php-fusion",
      "headers": {
        "X-Powered-By": "PHP-Fusion (.+)$\\;version:\\1"
      },
      "html": "Powered by <a href=\"[^>]+php-fusion",
      "icon": "PHP-Fusion.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "website": "https://www.php-fusion.co.uk"
    },
    "PHP-Nuke": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:phpnuke:php-nuke",
      "html": "<[^>]+Powered by PHP-Nuke",
      "icon": "PHP-Nuke.png",
      "implies": "PHP",
      "meta": {
        "generator": "PHP-Nuke"
      },
      "website": "http://phpnuke.org"
    },
    "PHPDebugBar": {
      "cats": [
        47
      ],
      "icon": "phpdebugbar.png",
      "js": {
        "PhpDebugBar": "",
        "phpdebugbar": ""
      },
      "script": [
        "debugbar.*\\.js"
      ],
      "website": "http://phpdebugbar.com/"
    },
    "PageFly": {
      "cats": [
        51
      ],
      "icon": "pagefly.png",
      "script": "pagefly\\.io",
      "website": "https://pagefly.io"
    },
    "Pagekit": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:pagekit:pagekit",
      "icon": "Pagekit.png",
      "meta": {
        "generator": "Pagekit"
      },
      "website": "http://pagekit.com"
    },
    "Pagely": {
      "cats": [
        62
      ],
      "headers": {
        "Server": "^Pagely"
      },
      "icon": "pagely.svg",
      "implies": [
        "WordPress",
        "Amazon Web Services"
      ],
      "website": "https://pagely.com/"
    },
    "Pagevamp": {
      "cats": [
        1
      ],
      "headers": {
        "X-ServedBy": "pagevamp"
      },
      "icon": "Pagevamp.png",
      "js": {
        "Pagevamp": ""
      },
      "website": "https://www.pagevamp.com"
    },
    "Pantheon": {
      "cats": [
        62
      ],
      "headers": {
        "Server": "^Pantheon",
        "x-pantheon-styx-hostname": ""
      },
      "icon": "pantheon.svg",
      "implies": [
        "PHP",
        "Nginx",
        "MariaDB"
      ],
      "website": "https://pantheon.io/"
    },
    "Pardot": {
      "cats": [
        32
      ],
      "headers": {
        "X-Pardot-LB": "",
        "X-Pardot-Route": "",
        "X-Pardot-Rsp": ""
      },
      "icon": "Pardot.png",
      "js": {
        "piAId": "",
        "piCId": "",
        "piHostname": "",
        "piProtocol": "",
        "piTracker": ""
      },
      "website": "https://www.pardot.com"
    },
    "Pars Elecom Portal": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "Pars Elecom Portal"
      },
      "icon": "parselecom.png",
      "implies": [
        "Microsoft ASP.NET",
        "IIS",
        "Windows Server"
      ],
      "meta": {
        "copyright": "Pars Elecom Portal"
      },
      "website": "http://parselecom.net"
    },
    "Parse.ly": {
      "cats": [
        10
      ],
      "icon": "Parse.ly.png",
      "js": {
        "PARSELY": ""
      },
      "website": "https://www.parse.ly"
    },
    "Paths.js": {
      "cats": [
        25
      ],
      "script": "paths(?:\\.min)?\\.js",
      "website": "https://github.com/andreaferretti/paths-js"
    },
    "PayPal": {
      "cats": [
        41
      ],
      "cpe": "cpe:/a:paypal:paypal",
      "html": "<input[^>]+_s-xclick",
      "icon": "PayPal.svg",
      "js": {
        "PAYPAL": ""
      },
      "script": "paypalobjects\\.com/js",
      "website": "https://paypal.com"
    },
    "Pelican": {
      "cats": [
        57
      ],
      "html": [
        "powered by <a href=\"[^>]+getpelican\\.com",
        "powered by <a href=\"https?://pelican\\.notmyidea\\.org"
      ],
      "icon": "pelican.png",
      "implies": "Python",
      "website": "https://blog.getpelican.com/"
    },
    "PencilBlue": {
      "cats": [
        1,
        11
      ],
      "headers": {
        "X-Powered-By": "PencilBlue"
      },
      "icon": "PencilBlue.png",
      "implies": "Node.js",
      "website": "http://pencilblue.org"
    },
    "Percona": {
      "cats": [
        34
      ],
      "icon": "percona.svg",
      "website": "https://www.percona.com"
    },
    "Percussion": {
      "cats": [
        1
      ],
      "html": "<[^>]+class=\"perc-region\"",
      "icon": "Percussion.png",
      "meta": {
        "generator": "(?:Percussion|Rhythmyx)"
      },
      "website": "http://percussion.com"
    },
    "Perl": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:perl:perl",
      "headers": {
        "Server": "\\bPerl\\b(?: ?/?v?([\\d.]+))?\\;version:\\1"
      },
      "icon": "Perl.png",
      "website": "http://perl.org"
    },
    "Phabricator": {
      "cats": [
        13,
        47
      ],
      "cookies": {
        "phsid": ""
      },
      "html": "<[^>]+(?:class|id)=\"phabricator-",
      "icon": "Phabricator.png",
      "implies": "PHP",
      "script": "/phabricator/[a-f0-9]{8}/rsrc/js/phui/[a-z-]+\\.js$",
      "website": "http://phacility.com"
    },
    "Phaser": {
      "cats": [
        12
      ],
      "icon": "Phaser.png",
      "js": {
        "Phaser": "",
        "Phaser.VERSION": "^(.+)$\\;version:\\1"
      },
      "website": "https://phaser.io"
    },
    "Phenomic": {
      "cats": [
        57
      ],
      "html": [
        "<[^>]+id=\"phenomic(?:root)?\""
      ],
      "icon": "Phenomic.svg",
      "implies": "React",
      "script": "/phenomic\\.browser\\.[a-f0-9]+\\.js",
      "website": "https://phenomic.io/"
    },
    "Phoenix": {
      "cats": [
        18
      ],
      "icon": "sazito-phoenix.png",
      "implies": [
        "React",
        "webpack",
        "Node.js"
      ],
      "js": {
        "Phoenix": ""
      },
      "meta": {
        "generator": "^phoenix"
      },
      "website": "https://github.com/Sazito/phoenix/"
    },
    "PhotoShelter": {
      "cats": [
        1
      ],
      "html": [
        "<!--\\s+#+ Powered by the PhotoShelter Beam platform",
        "<link[^>]+c\\.photoshelter\\.com"
      ],
      "icon": "PhotoShelter.png",
      "implies": [
        "PHP",
        "MySQL",
        "jQuery"
      ],
      "url": "photoshelter\\.com",
      "website": "https://www.photoshelter.com"
    },
    "Phusion Passenger": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:phusionpassenger:phusion_passenger",
      "headers": {
        "Server": "Phusion Passenger ([\\d.]+)\\;version:\\1",
        "X-Powered-By": "Phusion Passenger ?([\\d.]+)?\\;version:\\1"
      },
      "icon": "Phusion Passenger.png",
      "website": "https://phusionpassenger.com"
    },
    "Pimcore": {
      "cats": [
        1,
        6
      ],
      "cpe": "cpe:/a:pimcore:pimcore",
      "headers": {
        "X-Powered-By": "^pimcore$"
      },
      "icon": "pimcore.svg",
      "implies": "PHP",
      "website": "http://pimcore.org"
    },
    "Pingoteam": {
      "cats": [
        1
      ],
      "icon": "Pingoteam.svg",
      "implies": "PHP",
      "meta": {
        "designer": "Pingoteam"
      },
      "website": "https://www.pingoteam.ir/"
    },
    "Pinterest": {
      "cats": [
        5
      ],
      "icon": "Pinterest.svg",
      "script": "//assets\\.pinterest\\.com/js/pinit\\.js",
      "website": "http://pinterest.com"
    },
    "Planet": {
      "cats": [
        49
      ],
      "icon": "Planet.png",
      "meta": {
        "generator": "^Planet(?:/([\\d.]+))?\\;version:\\1"
      },
      "website": "http://planetplanet.org"
    },
    "Platform.sh": {
      "cats": [
        62
      ],
      "headers": {
        "x-platform-cluster": "",
        "x-platform-processor": "",
        "x-platform-router": "",
        "x-platform-server": ""
      },
      "icon": "platformsh.svg",
      "website": "https://platform.sh"
    },
    "PlatformOS": {
      "cats": [
        1,
        62
      ],
      "headers": {
        "x-powered-by": "^platformOS$"
      },
      "icon": "PlatformOS.svg",
      "website": "https://www.platform-os.com"
    },
    "Play": {
      "cats": [
        18
      ],
      "cookies": {
        "PLAY_SESSION": ""
      },
      "cpe": "cpe:/a:playframework:play_framework",
      "icon": "Play.svg",
      "implies": "Scala",
      "website": "https://www.playframework.com"
    },
    "Plesk": {
      "cats": [
        9
      ],
      "headers": {
        "X-Powered-By": "^Plesk(?:L|W)in",
        "X-Powered-By-Plesk": "^Plesk"
      },
      "icon": "Plesk.png",
      "script": "common\\.js\\?plesk",
      "website": "https://www.plesk.com/"
    },
    "Pligg": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:pligg:pligg_cms",
      "html": "<span[^>]+id=\"xvotes-0",
      "icon": "Pligg.png",
      "js": {
        "pligg_": ""
      },
      "meta": {
        "generator": "Pligg"
      },
      "website": "http://pligg.com"
    },
    "Plone": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:plone:plone",
      "icon": "Plone.png",
      "implies": "Python",
      "meta": {
        "generator": "Plone"
      },
      "website": "http://plone.org"
    },
    "Plotly": {
      "cats": [
        25
      ],
      "icon": "Plotly.png",
      "implies": "D3",
      "js": {
        "Plotly.version": "([\\d.])\\;version:\\1"
      },
      "script": "https?://cdn\\.plot\\.ly/plotly",
      "website": "https://plot.ly/javascript/"
    },
    "Plyr": {
      "cats": [
        14
      ],
      "icon": "Plyr.png",
      "js": {
        "Plyr": ""
      },
      "script": "https://cdn\\.plyr\\.io/([0-9.]+)/.+\\.js\\;version:\\1",
      "website": "https://plyr.io/"
    },
    "Po.st": {
      "cats": [
        5
      ],
      "icon": "Po.st.png",
      "js": {
        "pwidget_config": ""
      },
      "website": "http://www.po.st/"
    },
    "Polyfill": {
      "cats": [
        59
      ],
      "icon": "polyfill.svg",
      "script": [
        "^https?://cdn\\.polyfill\\.io/",
        "/polyfill\\.min\\.js"
      ],
      "website": "https://polyfill.io"
    },
    "Polymer": {
      "cats": [
        12
      ],
      "html": "(?:<polymer-[^>]+|<link[^>]+rel=\"import\"[^>]+/polymer\\.html\")",
      "icon": "Polymer.png",
      "js": {
        "Polymer.version": "^(.+)$\\;version:\\1"
      },
      "script": "polymer\\.js",
      "website": "http://polymer-project.org"
    },
    "Posterous": {
      "cats": [
        1,
        11
      ],
      "html": "<div class=\"posterous",
      "icon": "Posterous.png",
      "js": {
        "Posterous": ""
      },
      "website": "http://posterous.com"
    },
    "PostgreSQL": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:postgresql:postgresql",
      "icon": "PostgreSQL.png",
      "website": "http://www.postgresql.org/"
    },
    "Powerboutique": {
      "cats": [
        6
      ],
      "icon": "powerboutique.png",
      "script": "powerboutique",
      "website": "https://www.powerboutique.com/"
    },
    "Powergap": {
      "cats": [
        6
      ],
      "html": [
        "<a[^>]+title=\"POWERGAP",
        "<input type=\"hidden\" name=\"shopid\""
      ],
      "icon": "Powergap.png",
      "website": "http://powergap.de"
    },
    "Prebid": {
      "cats": [
        36
      ],
      "icon": "Prebid.png",
      "js": {
        "PREBID_TIMEOUT": "",
        "pbjs": ""
      },
      "script": [
        "/prebid\\.js",
        "adnxs\\.com/[^\"]*(?:prebid|/pb\\.js)"
      ],
      "website": "http://prebid.org"
    },
    "Prefix-Free": {
      "cats": [
        19
      ],
      "icon": "Prefix-Free.png",
      "js": {
        "PrefixFree": ""
      },
      "script": "prefixfree\\.js",
      "website": "https://leaverou.github.io/prefixfree/"
    },
    "PrestaShop": {
      "cats": [
        6
      ],
      "cookies": {
        "PrestaShop": ""
      },
      "cpe": "cpe:/a:prestashop:prestashop",
      "headers": {
        "Powered-By": "^Prestashop$"
      },
      "html": [
        "Powered by <a\\s+[^>]+>PrestaShop",
        "<!-- /Block [a-z ]+ module (?:HEADER|TOP)?\\s?-->",
        "<!-- /Module Block [a-z ]+ -->"
      ],
      "icon": "PrestaShop.svg",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "freeProductTranslation": "\\;confidence:25",
        "priceDisplayMethod": "\\;confidence:25",
        "priceDisplayPrecision": "\\;confidence:25"
      },
      "meta": {
        "generator": "PrestaShop"
      },
      "website": "http://www.prestashop.com"
    },
    "Prism": {
      "cats": [
        19
      ],
      "icon": "Prism.svg",
      "js": {
        "Prism": ""
      },
      "script": "prism\\.js",
      "website": "http://prismjs.com"
    },
    "Project Wonderful": {
      "cats": [
        36
      ],
      "html": "<div[^>]+id=\"pw_adbox_",
      "icon": "Project Wonderful.png",
      "js": {
        "pw_adloader": ""
      },
      "script": "^https?://(?:www\\.)?projectwonderful\\.com/(?:pwa\\.js|gen\\.php)",
      "website": "http://projectwonderful.com"
    },
    "Projesoft": {
      "cats": [
        6
      ],
      "icon": "projesoft.png",
      "script": [
        "projesoft\\.js"
      ],
      "website": "https://www.projesoft.com.tr"
    },
    "Prototype": {
      "cats": [
        12
      ],
      "icon": "Prototype.png",
      "js": {
        "Prototype.Version": "^(.+)$\\;version:\\1"
      },
      "script": "(?:prototype|protoaculous)(?:-([\\d.]*[\\d]))?.*\\.js\\;version:\\1",
      "website": "http://www.prototypejs.org"
    },
    "Protovis": {
      "cats": [
        25
      ],
      "js": {
        "protovis": ""
      },
      "script": "protovis.*\\.js",
      "website": "http://mbostock.github.io/protovis"
    },
    "Proximis": {
      "cats": [
        5,
        6
      ],
      "icon": "Proximis Omnichannel.png",
      "script": "widget-commerce(?:\\.min)?\\.js",
      "website": "https://www.proximis.com"
    },
    "Proximis Unified Commerce": {
      "cats": [
        6,
        1
      ],
      "html": "<html[^>]+data-ng-app=\"RbsChangeApp\"",
      "icon": "Proximis Omnichannel.png",
      "implies": [
        "PHP",
        "AngularJS"
      ],
      "js": {
        "__change": ""
      },
      "meta": {
        "generator": "Proximis Unified Commerce"
      },
      "website": "https://www.proximis.com"
    },
    "PubMatic": {
      "cats": [
        36
      ],
      "icon": "PubMatic.png",
      "script": "https?://[^/]*\\.pubmatic\\.com",
      "website": "http://www.pubmatic.com/"
    },
    "Public CMS": {
      "cats": [
        1
      ],
      "cookies": {
        "PUBLICCMS_USER": ""
      },
      "headers": {
        "X-Powered-PublicCMS": "^(.+)$\\;version:\\1"
      },
      "icon": "Public CMS.png",
      "implies": "Java",
      "website": "http://www.publiccms.com"
    },
    "Pure CSS": {
      "cats": [
        66
      ],
      "html": [
        "<link[^>]+(?:([\\d.])+/)?pure(?:-min)?\\.css\\;version:\\1",
        "<div[^>]+class=\"[^\"]*pure-u-(?:sm-|md-|lg-|xl-)?\\d-\\d"
      ],
      "icon": "Pure CSS.png",
      "website": "http://purecss.io"
    },
    "Pushnami": {
      "cats": [
        32
      ],
      "icon": "Pushnami.svg",
      "script": "api\\.pushnami\\.com",
      "website": "https://pushnami.com"
    },
    "Pygments": {
      "cats": [
        19
      ],
      "cpe": "cpe:/a:pygments:pygments",
      "html": "<link[^>]+pygments\\.css[\"']",
      "icon": "pygments.png",
      "website": "http://pygments.org"
    },
    "PyroCMS": {
      "cats": [
        1
      ],
      "cookies": {
        "pyrocms": ""
      },
      "headers": {
        "X-Streams-Distribution": "PyroCMS"
      },
      "icon": "PyroCMS.png",
      "implies": "Laravel",
      "website": "http://pyrocms.com"
    },
    "Python": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:python:python",
      "headers": {
        "Server": "(?:^|\\s)Python(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Python.png",
      "website": "http://python.org"
    },
    "Quantcast": {
      "cats": [
        10
      ],
      "icon": "Quantcast.png",
      "js": {
        "quantserve": ""
      },
      "script": "\\.quantserve\\.com/quant\\.js",
      "website": "http://www.quantcast.com"
    },
    "Question2Answer": {
      "cats": [
        15
      ],
      "html": "<!-- Powered by Question2Answer",
      "icon": "question2answer.png",
      "implies": "PHP",
      "script": "\\./qa-content/qa-page\\.js\\?([0-9.]+)\\;version:\\1",
      "website": "http://www.question2answer.org"
    },
    "Quick.CMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:opensolution:quick.cms",
      "html": "<a href=\"[^>]+opensolution\\.org/\">CMS by",
      "icon": "Quick.CMS.png",
      "meta": {
        "generator": "Quick\\.CMS(?: v([\\d.]+))?\\;version:\\1"
      },
      "website": "http://opensolution.org"
    },
    "Quick.Cart": {
      "cats": [
        6
      ],
      "html": "<a href=\"[^>]+opensolution\\.org/\">(?:Shopping cart by|Sklep internetowy)",
      "icon": "Quick.Cart.png",
      "meta": {
        "generator": "Quick\\.Cart(?: v([\\d.]+))?\\;version:\\1"
      },
      "website": "http://opensolution.org"
    },
    "Quill": {
      "cats": [
        24
      ],
      "icon": "Quill.png",
      "js": {
        "Quill": ""
      },
      "website": "http://quilljs.com"
    },
    "RBS Change": {
      "cats": [
        1,
        6
      ],
      "html": "<html[^>]+xmlns:change=",
      "icon": "RBS Change.png",
      "implies": "PHP",
      "meta": {
        "generator": "RBS Change"
      },
      "website": "http://www.rbschange.fr"
    },
    "RCMS": {
      "cats": [
        1
      ],
      "icon": "RCMS.png",
      "meta": {
        "generator": "^(?:RCMS|ReallyCMS)"
      },
      "website": "http://www.rcms.fi"
    },
    "RD Station": {
      "cats": [
        32
      ],
      "icon": "RD Station.png",
      "js": {
        "RDStation": ""
      },
      "script": "d335luupugsy2\\.cloudfront\\.net/js/loader-scripts/.*-loader\\.js",
      "website": "http://rdstation.com.br"
    },
    "RDoc": {
      "cats": [
        4
      ],
      "cpe": "cpe:/a:dave_thomas:rdoc",
      "html": [
        "<link[^>]+href=\"[^\"]*rdoc-style\\.css",
        "Generated by <a[^>]+href=\"https?://rdoc\\.rubyforge\\.org[^>]+>RDoc</a> ([\\d.]*\\d)\\;version:\\1",
        "<footer(?:(?!<\\/footer>)[^]){1,500}<p>\\s*Generated by <a href=\"https:\\/\\/ruby\\.github\\.io\\/rdoc\\/\">RDoc<\\/a> ([\\d.]*\\d)\\;version:\\1"
      ],
      "icon": "RDoc.png",
      "implies": "Ruby",
      "js": {
        "rdoc_rel_prefix": ""
      },
      "website": "https://github.com/ruby/rdoc"
    },
    "RX Web Server": {
      "cats": [
        22
      ],
      "headers": {
        "X-Powered-By": "RX-WEB"
      },
      "icon": "RXWeb.svg",
      "website": "http://developers.rokitax.co.uk/projects/rxweb"
    },
    "RackCache": {
      "cats": [
        23
      ],
      "headers": {
        "X-Rack-Cache": ""
      },
      "icon": "RackCache.png",
      "implies": "Ruby",
      "website": "https://github.com/rtomayko/rack-cache"
    },
    "RainLoop": {
      "cats": [
        30
      ],
      "headers": {
        "Server": "^RainLoop"
      },
      "html": [
        "<link[^>]href=\"rainloop/v/([0-9.]+)/static/apple-touch-icon\\.png/>\\;version:\\1"
      ],
      "icon": "RainLoop.png",
      "implies": "PHP",
      "js": {
        "rainloop": "",
        "rainloopI18N": ""
      },
      "meta": {
        "rlAppVersion": "^([0-9.]+)$\\;version:\\1"
      },
      "script": "^rainloop/v/([0-9.]+)/\\;version:\\1",
      "website": "https://www.rainloop.net/"
    },
    "Rakuten Digital Commerce": {
      "cats": [
        6
      ],
      "icon": "RakutenDigitalCommerce.png",
      "js": {
        "RakutenApplication": ""
      },
      "website": "https://digitalcommerce.rakuten.com.br"
    },
    "Ramda": {
      "cats": [
        59
      ],
      "icon": "Ramda.png",
      "script": "ramda.*\\.js",
      "website": "http://ramdajs.com"
    },
    "Raphael": {
      "cats": [
        25
      ],
      "icon": "Raphael.png",
      "js": {
        "Raphael.version": "^(.+)$\\;version:\\1"
      },
      "script": "raphael(?:-([\\d.]+))?(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://dmitrybaranovskiy.github.io/raphael/"
    },
    "Raspbian": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Raspbian",
        "X-Powered-By": "Raspbian"
      },
      "icon": "Raspbian.svg",
      "website": "https://www.raspbian.org/"
    },
    "Raychat": {
      "cats": [
        52
      ],
      "icon": "raychat.png",
      "js": {
        "Raychat": ""
      },
      "script": "app\\.raychat\\.io/scripts/js",
      "website": "https://raychat.io"
    },
    "Rayo": {
      "cats": [
        1
      ],
      "icon": "Rayo.png",
      "implies": [
        "AngularJS",
        "Microsoft ASP.NET"
      ],
      "js": {
        "Rayo": ""
      },
      "meta": {
        "generator": "^Rayo"
      },
      "website": "http://www.rayo.ir"
    },
    "ReDoc": {
      "cats": [
        4
      ],
      "html": "<redoc ",
      "icon": "redoc.png",
      "implies": "React",
      "js": {
        "Redoc.version": "^(.+)$\\;version:\\1"
      },
      "script": "/redoc\\.(?:min\\.)?js",
      "website": "https://github.com/Rebilly/ReDoc"
    },
    "React": {
      "cats": [
        12
      ],
      "cpe": "cpe:/a:facebook:react",
      "html": "<[^>]+data-react",
      "icon": "React.png",
      "js": {
        "React.version": "^(.+)$\\;version:\\1",
        "react.version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "react(?:-with-addons)?[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "/([\\d.]+)/react(?:\\.min)?\\.js\\;version:\\1",
        "^react\\b.*\\.js"
      ],
      "website": "https://reactjs.org"
    },
    "RebelMouse": {
      "cats": [
        1
      ],
      "headers": {
        "x-rebelmouse-cache-control": "",
        "x-rebelmouse-surrogate-control": ""
      },
      "html": "<!-- Powered by RebelMouse\\.",
      "icon": "RebelMouse.svg",
      "website": "https://www.rebelmouse.com/"
    },
    "Red Hat": {
      "cats": [
        28
      ],
      "cpe": "cpe:/o:redhat:linux",
      "headers": {
        "Server": "Red Hat",
        "X-Powered-By": "Red Hat"
      },
      "icon": "Red Hat.svg",
      "website": "https://www.redhat.com"
    },
    "Redaxscript": {
      "cats": [
        1
      ],
      "icon": "Redaxscript.svg",
      "implies": "PHP",
      "meta": {
        "generator": "^Redaxscript ([\\d\\.]+)\\;version:\\1"
      },
      "website": "https://redaxscript.com"
    },
    "Reddit": {
      "cats": [
        2
      ],
      "html": "(?:<a[^>]+Powered by Reddit|powered by <a[^>]+>reddit<)",
      "icon": "Reddit.png",
      "implies": "Python",
      "js": {
        "reddit": ""
      },
      "url": "^https?://(?:www\\.)?reddit\\.com",
      "website": "http://code.reddit.com"
    },
    "Redis": {
      "cats": [
        34
      ],
      "cpe": "cpe:/a:redislabs:redis",
      "icon": "Redis.svg",
      "website": "https://redis.io"
    },
    "Redis Object Cache": {
      "cats": [
        23
      ],
      "html": "<!--\\s+Performance optimized by Redis Object Cache",
      "icon": "RedisObjectCache.svg",
      "implies": [
        "Redis",
        "WordPress"
      ],
      "website": "https://wprediscache.com"
    },
    "Redmine": {
      "cats": [
        13
      ],
      "cookies": {
        "_redmine_session": ""
      },
      "cpe": "cpe:/a:redmine:redmine",
      "html": "Powered by <a href=\"[^>]+Redmine",
      "icon": "Redmine.png",
      "implies": "Ruby on Rails",
      "meta": {
        "description": "Redmine"
      },
      "website": "http://www.redmine.org"
    },
    "Reinvigorate": {
      "cats": [
        10
      ],
      "icon": "Reinvigorate.png",
      "js": {
        "reinvigorate": ""
      },
      "website": "http://www.reinvigorate.net"
    },
    "RequireJS": {
      "cats": [
        12
      ],
      "icon": "RequireJS.png",
      "js": {
        "requirejs.version": "^(.+)$\\;version:\\1"
      },
      "script": "require.*\\.js",
      "website": "http://requirejs.org"
    },
    "Resin": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:caucho:resin",
      "headers": {
        "Server": "^Resin(?:/(\\S*))?\\;version:\\1"
      },
      "icon": "Resin.png",
      "implies": "Java",
      "website": "http://caucho.com"
    },
    "Reveal.js": {
      "cats": [
        12
      ],
      "icon": "Reveal.js.png",
      "implies": "Highlight.js",
      "js": {
        "Reveal.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": "(?:^|/)reveal(?:\\.min)?\\.js",
      "website": "http://lab.hakim.se/reveal-js"
    },
    "Revel": {
      "cats": [
        18
      ],
      "cookies": {
        "REVEL_FLASH": "",
        "REVEL_SESSION": ""
      },
      "icon": "Revel.png",
      "implies": "Go",
      "website": "https://revel.github.io"
    },
    "Revslider": {
      "cats": [
        19
      ],
      "html": [
        "<link[^>]* href=[\\'\"][^']+revslider[/\\w-]+\\.css\\?ver=([0-9.]+)[\\'\"]\\;version:\\1"
      ],
      "icon": "revslider.png",
      "script": "/revslider/[/\\w-]+/js",
      "website": "https://revolution.themepunch.com/"
    },
    "Rickshaw": {
      "cats": [
        25
      ],
      "implies": "D3",
      "js": {
        "Rickshaw": ""
      },
      "script": "rickshaw(?:\\.min)?\\.js",
      "website": "http://code.shutterstock.com/rickshaw/"
    },
    "RightJS": {
      "cats": [
        12
      ],
      "icon": "RightJS.png",
      "js": {
        "RightJS": ""
      },
      "script": "right\\.js",
      "website": "http://rightjs.org"
    },
    "Riot": {
      "cats": [
        12
      ],
      "icon": "Riot.png",
      "js": {
        "riot": ""
      },
      "script": "riot(?:\\+compiler)?(?:\\.min)?\\.js",
      "website": "https://riot.js.org/"
    },
    "Riskified": {
      "cats": [
        6
      ],
      "headers": {
        "server": "Riskified Server"
      },
      "html": [
        "<[^>]*beacon\\.riskified\\.com",
        "<[^>]*c\\.riskified\\.com"
      ],
      "icon": "riskified.png",
      "js": {
        "RISKX": "",
        "riskifiedBeaconLoad": ""
      },
      "website": "https://www.riskified.com/"
    },
    "RiteCMS": {
      "cats": [
        1
      ],
      "icon": "RiteCMS.png",
      "implies": [
        "PHP",
        "SQLite\\;confidence:80"
      ],
      "meta": {
        "generator": "^RiteCMS(?: (.+))?\\;version:\\1"
      },
      "website": "http://ritecms.com"
    },
    "Roadiz CMS": {
      "cats": [
        1,
        11
      ],
      "headers": {
        "X-Powered-By": "Roadiz CMS"
      },
      "icon": "Roadiz CMS.png",
      "implies": [
        "PHP",
        "Symfony"
      ],
      "meta": {
        "generator": "^Roadiz ?(?:master|develop)? v?([0-9\\.]+)\\;version:\\1"
      },
      "website": "https://www.roadiz.io"
    },
    "Robin": {
      "cats": [
        6
      ],
      "icon": "Robin.png",
      "js": {
        "_robin_getRobinJs": "",
        "robin_settings": "",
        "robin_storage_settings": ""
      },
      "website": "http://www.robinhq.com"
    },
    "RockRMS": {
      "cats": [
        1,
        11,
        32
      ],
      "icon": "RockRMS.svg",
      "implies": [
        "Windows Server",
        "IIS",
        "Microsoft ASP.NET"
      ],
      "meta": {
        "generator": "^Rock v([0-9.]+)\\;version:\\1"
      },
      "website": "http://www.rockrms.com"
    },
    "RoundCube": {
      "cats": [
        30
      ],
      "html": "<title>RoundCube",
      "icon": "RoundCube.png",
      "implies": "PHP",
      "js": {
        "rcmail": "",
        "roundcube": ""
      },
      "website": "http://roundcube.net"
    },
    "Rubicon Project": {
      "cats": [
        36
      ],
      "icon": "Rubicon Project.png",
      "script": "https?://[^/]*\\.rubiconproject\\.com",
      "website": "http://rubiconproject.com/"
    },
    "Ruby": {
      "cats": [
        27
      ],
      "cpe": "cpe:/a:ruby-lang:ruby",
      "headers": {
        "Server": "(?:Mongrel|WEBrick|Ruby)"
      },
      "icon": "Ruby.png",
      "website": "http://ruby-lang.org"
    },
    "Ruby on Rails": {
      "cats": [
        18
      ],
      "cookies": {
        "_session_id": "\\;confidence:75"
      },
      "cpe": "cpe:/a:rubyonrails:rails",
      "headers": {
        "Server": "mod_(?:rails|rack)",
        "X-Powered-By": "mod_(?:rails|rack)"
      },
      "icon": "Ruby on Rails.png",
      "implies": "Ruby",
      "meta": {
        "csrf-param": "^authenticity_token$\\;confidence:50"
      },
      "script": "/assets/application-[a-z\\d]{32}/\\.js\\;confidence:50",
      "website": "https://rubyonrails.org"
    },
    "Ruxit": {
      "cats": [
        10
      ],
      "icon": "Ruxit.png",
      "script": "ruxitagentjs",
      "website": "http://ruxit.com"
    },
    "RxJS": {
      "cats": [
        12
      ],
      "icon": "RxJS.png",
      "js": {
        "Rx.CompositeDisposable": "",
        "Rx.Symbol": ""
      },
      "script": "rx(?:\\.\\w+)?(?:\\.compat|\\.global)?(?:\\.min)?\\.js",
      "website": "http://reactivex.io"
    },
    "S.Builder": {
      "cats": [
        1
      ],
      "icon": "S.Builder.png",
      "meta": {
        "generator": "S\\.Builder"
      },
      "website": "http://www.sbuilder.ru"
    },
    "SAP": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "SAP NetWeaver Application Server"
      },
      "icon": "SAP.png",
      "website": "http://sap.com"
    },
    "SAP Commerce Cloud": {
      "cats": [
        6
      ],
      "cookies": {
        "_hybris": ""
      },
      "cpe": "cpe:/a:sap:commerce_cloud",
      "html": "<[^>]+/(?:sys_master|hybr|_ui/(?:responsive/)?(?:desktop|common(?:/images|/img)?))/",
      "icon": "SAP.png",
      "implies": "Java",
      "website": "https://www.sap.com/products/crm/e-commerce-platforms.html"
    },
    "SDL Tridion": {
      "cats": [
        1
      ],
      "html": "<img[^>]+_tcm\\d{2,3}-\\d{6}\\.",
      "icon": "SDL Tridion.png",
      "website": "http://www.sdl.com/products/tridion"
    },
    "SIMsite": {
      "cats": [
        1
      ],
      "icon": "SIMsite.png",
      "meta": {
        "SIM.medium": ""
      },
      "script": "/sim(?:site|core)/js",
      "website": "http://simgroep.nl/internet/portfolio-contentbeheer_41623/"
    },
    "SMF": {
      "cats": [
        2
      ],
      "html": "credits/?\" title=\"Simple Machines Forum\" target=\"_blank\" class=\"new_win\">SMF ([0-9.]+)</a>\\;version:\\1",
      "icon": "SMF.png",
      "implies": "PHP",
      "js": {
        "smf_": ""
      },
      "website": "http://www.simplemachines.org"
    },
    "SOBI 2": {
      "cats": [
        19
      ],
      "html": "(?:<!-- start of Sigsiu Online Business Index|<div[^>]* class=\"sobi2)",
      "icon": "SOBI 2.png",
      "implies": "Joomla",
      "website": "http://www.sigsiu.net/sobi2.html"
    },
    "SPDY": {
      "cats": [
        19
      ],
      "excludes": "HTTP/2",
      "headers": {
        "X-Firefox-Spdy": "\\d\\.\\d"
      },
      "icon": "SPDY.png",
      "website": "http://chromium.org/spdy"
    },
    "SPIP": {
      "cats": [
        1
      ],
      "headers": {
        "Composed-By": "SPIP ([\\d.]+) @\\;version:\\1",
        "X-Spip-Cache": ""
      },
      "icon": "spip.svg",
      "implies": "PHP",
      "meta": {
        "generator": "(?:^|\\s)SPIP(?:\\s([\\d.]+(?:\\s\\[\\d+\\])?))?\\;version:\\1"
      },
      "website": "http://www.spip.net"
    },
    "SQL Buddy": {
      "cats": [
        3
      ],
      "html": "(?:<title>SQL Buddy</title>|<[^>]+onclick=\"sideMainClick\\(\"home\\.php)",
      "icon": "SQL Buddy.png",
      "implies": "PHP",
      "website": "http://www.sqlbuddy.com"
    },
    "SQLite": {
      "cats": [
        34
      ],
      "icon": "SQLite.png",
      "website": "http://www.sqlite.org"
    },
    "SUSE": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "SUSE(?:/?\\s?-?([\\d.]+))?\\;version:\\1",
        "X-Powered-By": "SUSE(?:/?\\s?-?([\\d.]+))?\\;version:\\1"
      },
      "icon": "SUSE.png",
      "website": "http://suse.com"
    },
    "SWFObject": {
      "cats": [
        19
      ],
      "icon": "SWFObject.png",
      "js": {
        "SWFObject": ""
      },
      "script": "swfobject.*\\.js",
      "website": "https://github.com/swfobject/swfobject"
    },
    "Saber": {
      "cats": [
        57
      ],
      "html": [
        "<div [^>]*id=\"_saber\""
      ],
      "icon": "Saber.svg",
      "implies": "Vue.js",
      "meta": {
        "generator": "^Saber v([\\d.]+)$\\;version:\\1"
      },
      "website": "https://saber.land/"
    },
    "Sails.js": {
      "cats": [
        18
      ],
      "cookies": {
        "sails.sid": ""
      },
      "headers": {
        "X-Powered-By": "^Sails(?:$|[^a-z0-9])"
      },
      "icon": "Sails.js.svg",
      "implies": "Express",
      "website": "http://sailsjs.org"
    },
    "Salesforce": {
      "cats": [
        53
      ],
      "cookies": {
        "com.salesforce": ""
      },
      "html": "<[^>]+=\"brandQuaternaryFgrs\"",
      "icon": "Salesforce.svg",
      "js": {
        "SFDCApp": "",
        "SFDCCmp": "",
        "SFDCPage": "",
        "SFDCSessionVars": ""
      },
      "website": "https://www.salesforce.com"
    },
    "Salesforce Commerce Cloud": {
      "cats": [
        6
      ],
      "headers": {
        "Server": "Demandware eCommerce Server"
      },
      "html": "<[^>]+demandware\\.edgesuite",
      "icon": "Salesforce.svg",
      "js": {
        "dwAnalytics": ""
      },
      "script": "/demandware\\.static/",
      "website": "http://demandware.com"
    },
    "Sapper": {
      "cats": [
        18
      ],
      "html": [
        "<script[^>]*>__SAPPER__"
      ],
      "icon": "Sapper.svg",
      "implies": [
        "Svelte",
        "Node.js"
      ],
      "js": {
        "__SAPPER__": ""
      },
      "website": "https://sapper.svelte.dev"
    },
    "Sarka-SPIP": {
      "cats": [
        1
      ],
      "icon": "Sarka-SPIP.png",
      "implies": "SPIP",
      "meta": {
        "generator": "Sarka-SPIP(?:\\s([\\d.]+))?\\;version:\\1"
      },
      "website": "http://sarka-spip.net"
    },
    "Sazito": {
      "cats": [
        6
      ],
      "icon": "Sazito.svg",
      "js": {
        "Sazito": ""
      },
      "meta": {
        "generator": "^Sazito"
      },
      "website": "http://sazito.com"
    },
    "Scala": {
      "cats": [
        27
      ],
      "icon": "Scala.png",
      "website": "http://www.scala-lang.org"
    },
    "Scenari": {
      "cats": [
        1,
        11
      ],
      "icon": "Scenari.png",
      "implies": [
        "Roadiz CMS",
        "PHP",
        "Symfony"
      ],
      "meta": {
        "generator": "^Roadiz ?(?:master|develop)? v?[0-9\\.]+ - Scenari v?([0-9\\.]+)\\;version:\\1"
      },
      "website": "https://demo.scenari.site"
    },
    "Scholica": {
      "cats": [
        21
      ],
      "headers": {
        "X-Scholica-Version": ""
      },
      "icon": "Scholica.svg",
      "website": "http://scholica.com"
    },
    "Scientific Linux": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Scientific Linux",
        "X-Powered-By": "Scientific Linux"
      },
      "icon": "Scientific Linux.png",
      "website": "http://scientificlinux.org"
    },
    "SeamlessCMS": {
      "cats": [
        1
      ],
      "icon": "SeamlessCMS.png",
      "meta": {
        "generator": "^Seamless\\.?CMS"
      },
      "website": "http://www.seamlesscms.com"
    },
    "Section.io": {
      "cats": [
        31
      ],
      "headers": {
        "section-io-id": "",
        "section-io-origin-status": "",
        "section-io-origin-time-seconds": ""
      },
      "icon": "sectionio.svg",
      "website": "https://www.section.io"
    },
    "Segment": {
      "cats": [
        10
      ],
      "icon": "Segment.png",
      "js": {
        "analytics": ""
      },
      "script": "cdn\\.segment\\.com/analytics\\.js",
      "website": "https://segment.com"
    },
    "Select2": {
      "cats": [
        59
      ],
      "icon": "Select2.png",
      "implies": "jQuery",
      "js": {
        "jQuery.fn.select2": ""
      },
      "script": "select2(?:\\.min|\\.full)?\\.js",
      "website": "https://select2.org/"
    },
    "Semantic-ui": {
      "cats": [
        66
      ],
      "html": [
        "<link[^>]+semantic(?:\\.min)\\.css\""
      ],
      "icon": "Semantic-ui.png",
      "script": "/semantic(?:-([\\d.]+))?(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://semantic-ui.com"
    },
    "Sencha Touch": {
      "cats": [
        12,
        26
      ],
      "icon": "Sencha Touch.png",
      "script": "sencha-touch.*\\.js",
      "website": "http://www.sencha.com/products/touch"
    },
    "Sensors Data": {
      "cats": [
        10
      ],
      "cookies": {
        "sensorsdata2015jssdkcross": "",
        "sensorsdata2015session": ""
      },
      "icon": "Sensors Data.svg",
      "js": {
        "sa.lib_version": "([\\d.]+)\\;version:\\1",
        "sensorsdata_app_js_bridge_call_js": ""
      },
      "script": "sensorsdata",
      "website": "https://www.sensorsdata.cn"
    },
    "Sentry": {
      "cats": [
        13
      ],
      "html": "<script[^>]*>\\s*Raven\\.config\\('[^']*', \\{\\s+release: '([0-9\\.]+)'\\;version:\\1",
      "icon": "Sentry.svg",
      "js": {
        "Raven.config": "",
        "Sentry": "",
        "Sentry.SDK_VERSION": "(.+)\\;version:\\1",
        "__SENTRY__": "",
        "ravenOptions.whitelistUrls": ""
      },
      "website": "https://sentry.io/"
    },
    "Seravo": {
      "cats": [
        62
      ],
      "headers": {
        "x-powered-by": "^Seravo"
      },
      "icon": "seravo.svg",
      "implies": "WordPress",
      "website": "https://seravo.com"
    },
    "Serendipity": {
      "cats": [
        1,
        11
      ],
      "icon": "Serendipity.png",
      "implies": "PHP",
      "meta": {
        "Powered-By": "Serendipity v\\.([\\d.]+)\\;version:\\1",
        "generator": "Serendipity(?: v\\.([\\d.]+))?\\;version:\\1"
      },
      "website": "http://s9y.org"
    },
    "Shapecss": {
      "cats": [
        66
      ],
      "html": "<link[^>]* href=\"[^\"]*shapecss(?:\\.min)?\\.css",
      "icon": "Shapecss.svg",
      "js": {
        "Shapecss": ""
      },
      "script": [
        "shapecss[-.]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "/([\\d.]+)/shapecss(?:\\.min)?\\.js\\;version:\\1",
        "shapecss.*\\.js"
      ],
      "website": "https://shapecss.com"
    },
    "ShareThis": {
      "cats": [
        5
      ],
      "icon": "ShareThis.png",
      "js": {
        "SHARETHIS": ""
      },
      "script": "w\\.sharethis\\.com/",
      "website": "http://sharethis.com"
    },
    "ShellInABox": {
      "cats": [
        46
      ],
      "html": [
        "<title>Shell In A Box</title>",
        "must be enabled for ShellInABox</noscript>"
      ],
      "icon": "ShellInABox.png",
      "js": {
        "ShellInABox": ""
      },
      "website": "http://shellinabox.com"
    },
    "Shiny": {
      "cats": [
        18
      ],
      "icon": "Shiny.png",
      "js": {
        "Shiny.addCustomMessageHandler": ""
      },
      "website": "https://shiny.rstudio.com"
    },
    "ShinyStat": {
      "cats": [
        10
      ],
      "html": "<img[^>]*\\s+src=['\"]?https?://www\\.shinystat\\.com/cgi-bin/shinystat\\.cgi\\?[^'\"\\s>]*['\"\\s/>]",
      "icon": "ShinyStat.png",
      "js": {
        "SSsdk": ""
      },
      "script": "^https?://codice(?:business|ssl|pro|isp)?\\.shinystat\\.com/cgi-bin/getcod\\.cgi",
      "website": "http://shinystat.com"
    },
    "Shopatron": {
      "cats": [
        6
      ],
      "html": [
        "<body class=\"shopatron",
        "<img[^>]+mediacdn\\.shopatron\\.com\\;confidence:50"
      ],
      "icon": "Shopatron.png",
      "js": {
        "shptUrl": ""
      },
      "meta": {
        "keywords": "Shopatron"
      },
      "script": "mediacdn\\.shopatron\\.com",
      "website": "http://ecommerce.shopatron.com"
    },
    "Shopcada": {
      "cats": [
        6
      ],
      "icon": "Shopcada.png",
      "js": {
        "Shopcada": ""
      },
      "website": "http://shopcada.com"
    },
    "Shoper": {
      "cats": [
        6
      ],
      "icon": "Shoper.svg",
      "js": {
        "shoper": ""
      },
      "website": "https://www.shoper.pl"
    },
    "Shopery": {
      "cats": [
        6
      ],
      "headers": {
        "X-Shopery": ""
      },
      "icon": "Shopery.svg",
      "implies": [
        "PHP",
        "Symfony",
        "Elcodi"
      ],
      "website": "http://shopery.com"
    },
    "Shopfa": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "^ShopFA ([\\d.]+)$\\;version:\\1"
      },
      "icon": "Shopfa.svg",
      "js": {
        "shopfa": ""
      },
      "meta": {
        "generator": "^ShopFA ([\\d.]+)$\\;version:\\1"
      },
      "website": "https://shopfa.com"
    },
    "Shopify": {
      "cats": [
        6
      ],
      "headers": {
        "x-shopid": "\\;confidence:50",
        "x-shopify-stage": "\\;confidence:50"
      },
      "html": "<link[^>]+=['\"]//cdn\\.shopify\\.com\\;confidence:25",
      "icon": "Shopify.svg",
      "js": {
        "Shopify": "\\;confidence:25"
      },
      "url": "^https?//.+\\.myshopify\\.com",
      "website": "http://shopify.com"
    },
    "Shopline": {
      "cats": [
        6
      ],
      "icon": "shopline.png",
      "meta": {
        "og:image": "https\\:\\/\\/img\\.shoplineapp\\.com"
      },
      "website": "https://shoplineapp.com/"
    },
    "Shoptet": {
      "cats": [
        6
      ],
      "html": "<link [^>]*href=\"https?://cdn\\.myshoptet\\.com/",
      "icon": "Shoptet.svg",
      "implies": "PHP",
      "js": {
        "shoptet": ""
      },
      "meta": {
        "web_author": "^Shoptet"
      },
      "script": [
        "^https?://cdn\\.myshoptet\\.com/"
      ],
      "website": "http://www.shoptet.cz"
    },
    "Shopware": {
      "cats": [
        6
      ],
      "headers": {
        "sw-context-token": "^[\\w]{32}$\\;version:6",
        "sw-invalidation-states": "\\;version:6",
        "sw-language-id": "^[a-fA-F0-9]{32}$\\;version:6",
        "sw-version-id": "\\;version:6"
      },
      "html": "<title>Shopware ([\\d\\.]+) [^<]+\\;version:\\1",
      "icon": "Shopware.svg",
      "implies": [
        "PHP",
        "MySQL",
        "jQuery",
        "Symfony"
      ],
      "meta": {
        "application-name": "Shopware"
      },
      "script": [
        "(?:(shopware)|/web/cache/[0-9]{10}_.+)\\.js\\;version:\\1?4:5",
        "/jquery\\.shopware\\.min\\.js",
        "/engine/Shopware/"
      ],
      "website": "https://www.shopware.com"
    },
    "Signal": {
      "cats": [
        32
      ],
      "icon": "signal.png",
      "js": {
        "signalData": ""
      },
      "script": [
        "//s\\.btstatic\\.com/tag\\.js",
        "//s\\.thebrighttag\\.com/iframe\\?"
      ],
      "website": "https://www.signal.co/"
    },
    "Silva": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "SilvaCMS"
      },
      "icon": "Silva.png",
      "website": "http://silvacms.org"
    },
    "SilverStripe": {
      "cats": [
        1
      ],
      "html": "Powered by <a href=\"[^>]+SilverStripe",
      "icon": "SilverStripe.svg",
      "implies": "PHP",
      "meta": {
        "generator": "^SilverStripe"
      },
      "website": "https://www.silverstripe.org"
    },
    "Simbel": {
      "cats": [
        6
      ],
      "headers": {
        "powered": "simbel"
      },
      "icon": "simbel.svg",
      "website": "http://simbel.com.ar/"
    },
    "Simple Analytics": {
      "cats": [
        10
      ],
      "icon": "SimpleAnalytics.svg",
      "script": "^https:\\/\\/cdn\\.simpleanalytics\\.io\\/hello\\.js",
      "website": "https://simpleanalytics.com"
    },
    "SimpleHTTP": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "SimpleHTTP(?:/([\\d.]+))?\\;version:\\1"
      },
      "website": "http://example.com"
    },
    "Simplébo": {
      "cats": [
        1
      ],
      "headers": {
        "X-ServedBy": "simplebo"
      },
      "icon": "Simplebo.png",
      "website": "https://www.simplebo.fr"
    },
    "Site Meter": {
      "cats": [
        10
      ],
      "icon": "Site Meter.png",
      "script": "sitemeter\\.com/js/counter\\.js\\?site=",
      "website": "http://www.sitemeter.com"
    },
    "SiteCatalyst": {
      "cats": [
        10
      ],
      "icon": "SiteCatalyst.png",
      "js": {
        "s_INST": "",
        "s_account": "",
        "s_code": "",
        "s_objectID": ""
      },
      "script": "/s[_-]code.*\\.js",
      "website": "http://www.adobe.com/solutions/digital-marketing.html"
    },
    "SiteEdit": {
      "cats": [
        1
      ],
      "icon": "SiteEdit.png",
      "meta": {
        "generator": "SiteEdit"
      },
      "website": "http://www.siteedit.ru"
    },
    "SiteGround": {
      "cats": [
        62
      ],
      "headers": {
        "host-header": "192fc2e7e50945beb8231a492d6a8024|b7440e60b07ee7b8044761568fab26e8|624d5be7be38418a3e2a818cc8b7029b|6b7412fb82ca5edfd0917e3957f05d89"
      },
      "icon": "siteground.svg",
      "website": "https://www.siteground.com"
    },
    "Sitecore": {
      "cats": [
        1
      ],
      "cookies": {
        "SC_ANALYTICS_GLOBAL_COOKIE": ""
      },
      "html": "<img[^>]+src=\"[^>]*/~/media/[^>]+\\.ashx",
      "icon": "Sitecore.png",
      "website": "http://sitecore.net"
    },
    "Sitefinity": {
      "cats": [
        1
      ],
      "icon": "Sitefinity.svg",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "^Sitefinity (.+)$\\;version:\\1"
      },
      "website": "http://www.sitefinity.com"
    },
    "Siteglide": {
      "cats": [
        1,
        61,
        53,
        6
      ],
      "icon": "Siteglide.svg",
      "implies": "PlatformOS",
      "script": "siteglide\\.js",
      "website": "https://www.siteglide.com"
    },
    "Sivuviidakko": {
      "cats": [
        1
      ],
      "icon": "Sivuviidakko.png",
      "meta": {
        "generator": "Sivuviidakko"
      },
      "website": "http://sivuviidakko.fi"
    },
    "Sizmek": {
      "cats": [
        36
      ],
      "html": "(?:<a [^>]*href=\"[^/]*//[^/]*serving-sys\\.com/|<img [^>]*src=\"[^/]*//[^/]*serving-sys\\.com/)",
      "icon": "Sizmek.png",
      "script": "serving-sys\\.com/",
      "website": "http://sizmek.com"
    },
    "Slick": {
      "cats": [
        59
      ],
      "html": "<link [^>]+(?:/([\\d.]+)/)?slick-theme\\.css\\;version:\\1",
      "implies": "jQuery",
      "script": "(?:/([\\d.]+))?/slick(?:\\.min)?\\.js\\;version:\\1",
      "website": "https://kenwheeler.github.io/slick"
    },
    "SlickStack": {
      "cats": [
        47,
        9
      ],
      "headers": {
        "x-powered-by": "SlickStack"
      },
      "icon": "SlickStack.png",
      "implies": "WordPress",
      "website": "https://slickstack.io"
    },
    "Slimbox": {
      "cats": [
        59
      ],
      "html": "<link [^>]*href=\"[^/]*slimbox(?:-rtl)?\\.css",
      "icon": "Slimbox.png",
      "implies": "MooTools",
      "script": "slimbox\\.js",
      "website": "http://www.digitalia.be/software/slimbox"
    },
    "Slimbox 2": {
      "cats": [
        59
      ],
      "html": "<link [^>]*href=\"[^/]*slimbox2(?:-rtl)?\\.css",
      "icon": "Slimbox 2.png",
      "implies": "jQuery",
      "script": "slimbox2\\.js",
      "website": "http://www.digitalia.be/software/slimbox2"
    },
    "Smart Ad Server": {
      "cats": [
        36
      ],
      "html": "<img[^>]+smartadserver\\.com\\/call",
      "icon": "Smart Ad Server.png",
      "js": {
        "SmartAdServer": ""
      },
      "website": "http://smartadserver.com"
    },
    "SmartSite": {
      "cats": [
        1
      ],
      "html": "<[^>]+/smartsite\\.(?:dws|shtml)\\?id=",
      "icon": "SmartSite.png",
      "meta": {
        "author": "Redacteur SmartInstant"
      },
      "website": "http://www.seneca.nl/pub/Smartsite/Smartsite-Smartsite-iXperion"
    },
    "Smartstore": {
      "cats": [
        6
      ],
      "icon": "Smartstore.png",
      "script": "smjslib\\.js",
      "website": "http://smartstore.com"
    },
    "Snap": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "Server": "Snap/([.\\d]+)\\;version:\\1"
      },
      "icon": "Snap.png",
      "implies": "Haskell",
      "website": "http://snapframework.com"
    },
    "Snap.svg": {
      "cats": [
        59
      ],
      "icon": "Snap.svg.png",
      "js": {
        "Snap.version": "^(.+)$\\;version:\\1"
      },
      "script": "snap\\.svg(?:-min)?\\.js",
      "website": "http://snapsvg.io"
    },
    "Snoobi": {
      "cats": [
        10
      ],
      "icon": "Snoobi.png",
      "js": {
        "snoobi": ""
      },
      "script": "snoobi\\.com/snoop\\.php",
      "website": "http://www.snoobi.com"
    },
    "SobiPro": {
      "cats": [
        19
      ],
      "icon": "SobiPro.png",
      "implies": "Joomla",
      "js": {
        "SobiProUrl": ""
      },
      "website": "http://sigsiu.net/sobipro.html"
    },
    "Socket.io": {
      "cats": [
        12
      ],
      "icon": "Socket.io.png",
      "implies": "Node.js",
      "js": {
        "io.Socket": "",
        "io.version": "^(.+)$\\;version:\\1"
      },
      "script": "socket\\.io.*\\.js",
      "website": "https://socket.io"
    },
    "SoftTr": {
      "cats": [
        6
      ],
      "icon": "softtr.png",
      "meta": {
        "author": "SoftTr E-Ticaret Sitesi Yazılımı"
      },
      "website": "http://www.softtr.com"
    },
    "Solodev": {
      "cats": [
        1
      ],
      "headers": {
        "solodev_session": ""
      },
      "html": "<div class=[\"']dynamicDiv[\"'] id=[\"']dd\\.\\d\\.\\d(?:\\.\\d)?[\"']>",
      "icon": "Solodev.png",
      "implies": "PHP",
      "website": "http://www.solodev.com"
    },
    "Solr": {
      "cats": [
        34
      ],
      "icon": "Solr.png",
      "implies": "Lucene",
      "website": "http://lucene.apache.org/solr/"
    },
    "Solusquare OmniCommerce Cloud": {
      "cats": [
        6
      ],
      "cookies": {
        "_solusquare": ""
      },
      "icon": "Solusquare.png",
      "implies": "Adobe ColdFusion",
      "meta": {
        "generator": "^Solusquare$"
      },
      "website": "https://www.solusquare.com"
    },
    "Solve Media": {
      "cats": [
        16,
        36
      ],
      "icon": "Solve Media.png",
      "js": {
        "ACPuzzle": "",
        "_ACPuzzle": "",
        "_adcopy-puzzle-image-image": "",
        "adcopy-puzzle-image-image": ""
      },
      "script": "^https?://api\\.solvemedia\\.com/",
      "website": "http://solvemedia.com"
    },
    "SonarQubes": {
      "cats": [
        47
      ],
      "html": [
        "<link href=\"/css/sonar\\.css\\?v=([\\d.]+)\\;version:\\1",
        "<title>SonarQube</title>"
      ],
      "icon": "sonar.png",
      "implies": "Java",
      "js": {
        "SonarMeasures": "",
        "SonarRequest": ""
      },
      "meta": {
        "application-name": "^SonarQubes$"
      },
      "script": "^/js/bundles/sonar\\.js?v=([\\d.]+)$\\;version:\\1",
      "website": "https://www.sonarqube.org/"
    },
    "Sotel": {
      "cats": [
        1
      ],
      "icon": "default.svg",
      "meta": {
        "generator": "sotel"
      },
      "website": "https://www.soteledu.com/en/"
    },
    "SoundManager": {
      "cats": [
        59
      ],
      "icon": "SoundManager.png",
      "js": {
        "BaconPlayer": "",
        "SoundManager": "",
        "soundManager.version": "V(.+) \\;version:\\1"
      },
      "website": "http://www.schillmania.com/projects/soundmanager2"
    },
    "Sphinx": {
      "cats": [
        4
      ],
      "html": "Created using <a href=\"https?://sphinx-doc\\.org/\">Sphinx</a> ([0-9.]+)\\.\\;version:\\1",
      "icon": "Sphinx.png",
      "js": {
        "DOCUMENTATION_OPTIONS": ""
      },
      "website": "http://sphinx.pocoo.org"
    },
    "SpinCMS": {
      "cats": [
        1
      ],
      "cookies": {
        "spincms_session": ""
      },
      "icon": "SpinCMS.png",
      "implies": "PHP",
      "website": "http://www.spin.cw"
    },
    "Splitbee": {
      "cats": [
        10
      ],
      "icon": "splitbee.svg",
      "script": "^https:\\/\\/cdn\\.splitbee\\.io\\/sb\\.js",
      "website": "https://splitbee.io"
    },
    "Splunk": {
      "cats": [
        19
      ],
      "html": "<p class=\"footer\">&copy; [-\\d]+ Splunk Inc\\.(?: Splunk ([\\d\\.]+(?: build [\\d\\.]*\\d)?))?[^<]*</p>\\;version:\\1",
      "icon": "Splunk.png",
      "meta": {
        "author": "Splunk Inc\\;confidence:50"
      },
      "website": "http://splunk.com"
    },
    "Splunkd": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Splunkd"
      },
      "icon": "Splunk.png",
      "website": "http://splunk.com"
    },
    "Spree": {
      "cats": [
        6
      ],
      "html": "(?:<link[^>]*/assets/store/all-[a-z\\d]{32}\\.css[^>]+>|<script>\\s*Spree\\.(?:routes|translations|api_key))",
      "icon": "Spree.png",
      "implies": "Ruby on Rails",
      "website": "https://spreecommerce.org"
    },
    "Spring": {
      "cats": [
        18
      ],
      "headers": {
        "X-Application-Context": ""
      },
      "icon": "Spring.png",
      "implies": "Java",
      "website": "https://spring.io/"
    },
    "Sqreen": {
      "cats": [
        19
      ],
      "headers": {
        "X-Protected-By": "^Sqreen$"
      },
      "icon": "Sqreen.png",
      "website": "https://sqreen.io"
    },
    "Squarespace": {
      "cats": [
        1
      ],
      "headers": {
        "X-ServedBy": "squarespace"
      },
      "html": "<!-- This is Squarespace\\. -->",
      "icon": "Squarespace.png",
      "js": {
        "Squarespace": ""
      },
      "website": "http://www.squarespace.com"
    },
    "SquirrelMail": {
      "cats": [
        30
      ],
      "html": "<small>SquirrelMail version ([.\\d]+)[^<]*<br \\;version:\\1",
      "icon": "SquirrelMail.png",
      "implies": "PHP",
      "js": {
        "squirrelmail_loginpage_onload": ""
      },
      "url": "/src/webmail\\.php(?:$|\\?)",
      "website": "http://squirrelmail.org"
    },
    "Squiz Matrix": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "Squiz Matrix"
      },
      "html": "<!--\\s+Running (?:MySource|Squiz) Matrix",
      "icon": "Squiz Matrix.png",
      "implies": "PHP",
      "meta": {
        "generator": "Squiz Matrix"
      },
      "website": "http://squiz.net"
    },
    "Stackla": {
      "cats": [
        5
      ],
      "icon": "Stackla.png",
      "js": {
        "Stackla": ""
      },
      "script": "assetscdn\\.stackla\\.com\\/media\\/js\\/widget\\/(?:[a-zA-Z0-9.]+)?\\.js",
      "website": "http://stackla.com/"
    },
    "Starlet": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Plack::Handler::Starlet"
      },
      "icon": "Starlet.png",
      "implies": "Perl",
      "website": "http://metacpan.org/pod/Starlet"
    },
    "Statcounter": {
      "cats": [
        10
      ],
      "icon": "Statcounter.svg",
      "js": {
        "_statcounter": "",
        "sc_project": "\\;confidence:50",
        "sc_security": "\\;confidence:50"
      },
      "script": "statcounter\\.com/counter/counter",
      "website": "http://www.statcounter.com"
    },
    "Store Systems": {
      "cats": [
        6
      ],
      "html": "Shopsystem von <a href=[^>]+store-systems\\.de\"|\\.mws_boxTop",
      "icon": "Store Systems.png",
      "website": "http://store-systems.de"
    },
    "Storeden": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "Storeden"
      },
      "icon": "storeden.svg",
      "website": "https://www.storeden.com"
    },
    "Storyblok": {
      "cats": [
        1
      ],
      "icon": "storyblok.png",
      "meta": {
        "generator": "storyblok"
      },
      "website": "https://www.storyblok.com"
    },
    "Strapdown.js": {
      "cats": [
        12
      ],
      "icon": "strapdown.js.png",
      "implies": [
        "Bootstrap",
        "Google Code Prettify"
      ],
      "script": "strapdown\\.js",
      "website": "http://strapdownjs.com"
    },
    "Strapi": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "^Strapi"
      },
      "icon": "Strapi.png",
      "website": "https://strapi.io"
    },
    "Strato": {
      "cats": [
        6
      ],
      "html": "<a href=\"http://www\\.strato\\.de/\" target=\"_blank\">",
      "icon": "strato.png",
      "website": "http://shop.strato.com"
    },
    "Strikingly": {
      "cats": [
        1
      ],
      "html": "<!-- Powered by Strikingly\\.com",
      "icon": "Strikingly.png",
      "website": "https://strikingly.com"
    },
    "Stripe": {
      "cats": [
        41
      ],
      "html": "<input[^>]+data-stripe",
      "icon": "Stripe.png",
      "js": {
        "Stripe.version": "^(.+)$\\;version:\\1"
      },
      "script": "js\\.stripe\\.com",
      "website": "http://stripe.com"
    },
    "SublimeVideo": {
      "cats": [
        14
      ],
      "icon": "SublimeVideo.png",
      "js": {
        "sublimevideo": ""
      },
      "script": "cdn\\.sublimevideo\\.net/js/[a-z\\d]+\\.js",
      "website": "http://sublimevideo.net"
    },
    "Subrion": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-CMS": "Subrion CMS"
      },
      "icon": "Subrion.png",
      "implies": "PHP",
      "meta": {
        "generator": "^Subrion "
      },
      "website": "http://subrion.com"
    },
    "Sucuri": {
      "cats": [
        31
      ],
      "headers": {
        "x-sucuri-cache:": "",
        "x-sucuri-id": ""
      },
      "icon": "sucuri.png",
      "website": "https://sucuri.net/"
    },
    "Sulu": {
      "cats": [
        1
      ],
      "headers": {
        "X-Generator": "Sulu/?(.+)?$\\;version:\\1"
      },
      "icon": "Sulu.svg",
      "implies": "Symfony",
      "website": "http://sulu.io"
    },
    "SumoMe": {
      "cats": [
        5,
        32
      ],
      "icon": "SumoMe.png",
      "script": "load\\.sumome\\.com",
      "website": "http://sumome.com"
    },
    "SunOS": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "SunOS( [\\d\\.]+)?\\;version:\\1",
        "Servlet-engine": "SunOS( [\\d\\.]+)?\\;version:\\1"
      },
      "icon": "Oracle.png",
      "website": "http://oracle.com/solaris"
    },
    "Supersized": {
      "cats": [
        25
      ],
      "icon": "Supersized.png",
      "script": "supersized(?:\\.([\\d.]*[\\d]))?.*\\.js\\;version:\\1",
      "website": "http://buildinternet.com/project/supersized"
    },
    "Svbtle": {
      "cats": [
        11
      ],
      "icon": "svbtle.png",
      "meta": {
        "generator": "^Svbtle\\.com$"
      },
      "url": "^https?://[^/]+\\.svbtle\\.com",
      "website": "https://www.svbtle.com"
    },
    "Svelte": {
      "cats": [
        12
      ],
      "html": "<[^>]+class=\\\"[^\\\"]+\\ssvelte-[\\w]*\\\"",
      "icon": "Svelte.svg",
      "website": "https://svelte.dev"
    },
    "SweetAlert": {
      "cats": [
        59
      ],
      "html": "<link[^>]+?href=\"[^\"]+sweet-alert(?:\\.min)?\\.css",
      "icon": "SweetAlert.png",
      "js": {
        "swal": ""
      },
      "script": "sweet-alert(?:\\.min)?\\.js",
      "website": "https://t4t5.github.io/sweetalert/"
    },
    "SweetAlert2": {
      "cats": [
        59
      ],
      "excludes": "SweetAlert",
      "html": "<link[^>]+?href=\"[^\"]+sweetalert2(?:\\.min)?\\.css",
      "icon": "SweetAlert2.png",
      "js": {
        "Sweetalert2": ""
      },
      "script": "sweetalert2(?:\\.all)?(?:\\.min)?\\.js",
      "website": "https://sweetalert2.github.io/"
    },
    "Swell": {
      "cats": [
        6
      ],
      "cookies": {
        "swell-session": ""
      },
      "html": [
        "<[^>]*swell\\.is",
        "<[^>]*swell\\.store",
        "<[^>]*schema\\.io"
      ],
      "icon": "Swell.svg",
      "js": {
        "swell.version": "^(.+)$\\;version:\\1"
      },
      "website": "https://www.swell.is/"
    },
    "Swiftlet": {
      "cats": [
        18
      ],
      "headers": {
        "X-Generator": "Swiftlet",
        "X-Powered-By": "Swiftlet",
        "X-Swiftlet-Cache": ""
      },
      "html": "Powered by <a href=\"[^>]+Swiftlet",
      "icon": "Swiftlet.png",
      "implies": "PHP",
      "meta": {
        "generator": "Swiftlet"
      },
      "website": "http://swiftlet.org"
    },
    "Swiftype": {
      "cats": [
        29
      ],
      "icon": "swiftype.png",
      "js": {
        "Swiftype": ""
      },
      "script": "swiftype\\.com/embed\\.js$",
      "website": "http://swiftype.com"
    },
    "Swiper Slider": {
      "cats": [
        19
      ],
      "html": "<[^>]+=swiper-container",
      "icon": "swiper.svg",
      "js": {
        "Swiper": ""
      },
      "script": "swiper(?:\\.min)?\\.js",
      "website": "https://swiperjs.com"
    },
    "Symfony": {
      "cats": [
        18
      ],
      "cookies": {
        "sf_redirect": ""
      },
      "html": "(?:<div class=\"sf-toolbar[^>]+?>[^]+<span class=\"sf-toolbar-value\">([\\d.])+|<div id=\"sfwdt[^\"]+\" class=\"[^\"]*sf-toolbar)\\;version:\\1",
      "icon": "Symfony.svg",
      "implies": "PHP",
      "js": {
        "Sfjs": ""
      },
      "website": "http://symfony.com"
    },
    "Sympa": {
      "cats": [
        30
      ],
      "html": "<a href=\"https?://www\\.sympa\\.org\">\\s*Powered by Sympa\\s*</a>",
      "icon": "sympa.png",
      "implies": "Perl",
      "meta": {
        "generator": "^Sympa$"
      },
      "website": "https://www.sympa.org/"
    },
    "Synology DiskStation": {
      "cats": [
        48
      ],
      "html": "<noscript><div class='syno-no-script'",
      "icon": "Synology DiskStation.png",
      "meta": {
        "application-name": "Synology DiskStation",
        "description": "^DiskStation provides a full-featured network attached storage"
      },
      "script": "webapi/entry\\.cgi\\?api=SYNO\\.(?:Core|Filestation)\\.Desktop\\.",
      "website": "http://synology.com"
    },
    "SyntaxHighlighter": {
      "cats": [
        19
      ],
      "html": "<(?:script|link)[^>]*sh(?:Core|Brush|ThemeDefault)",
      "icon": "SyntaxHighlighter.png",
      "js": {
        "SyntaxHighlighter": ""
      },
      "website": "https://github.com/syntaxhighlighter"
    },
    "T-Soft": {
      "cats": [
        6
      ],
      "html": "<a href=\"http://www\\.tsoft\\.com\\.tr\" target=\"_blank\" title=\"T-Soft E-ticaret Sistemleri\">",
      "icon": "Tsoft.png",
      "website": "https://www.tsoft.com.tr/"
    },
    "TN Express Web": {
      "cats": [
        1
      ],
      "cookies": {
        "TNEW": ""
      },
      "icon": "tessitura.svg",
      "implies": "Tessitura",
      "website": "https://www.tessituranetwork.com"
    },
    "TWiki": {
      "cats": [
        8
      ],
      "cookies": {
        "TWIKISID": ""
      },
      "html": "<img [^>]*(?:title|alt)=\"This site is powered by the TWiki collaboration platform",
      "icon": "TWiki.png",
      "implies": "Perl",
      "script": "(?:TWikiJavascripts|twikilib(?:\\.min)?\\.js)",
      "website": "http://twiki.org"
    },
    "TYPO3 CMS": {
      "cats": [
        1
      ],
      "html": [
        "<link[^>]+ href=\"/?typo3(?:conf|temp)/",
        "<img[^>]+ src=\"/?typo3(?:conf|temp)/",
        "<!--\n\tThis website is powered by TYPO3"
      ],
      "icon": "TYPO3.svg",
      "implies": "PHP",
      "meta": {
        "generator": "TYPO3\\s+(?:CMS\\s+)?(?:[\\d.]+)?(?:\\s+CMS)?"
      },
      "script": "^/?typo3(?:conf|temp)/",
      "url": "/typo3/",
      "website": "https://typo3.org/"
    },
    "TagCommander": {
      "cats": [
        42
      ],
      "icon": "tagcommander.png",
      "js": {
        "tc_vars": ""
      },
      "script": "\\.tagcommander\\.com",
      "website": "https://www.commandersact.com/en/solutions/tagcommander/"
    },
    "Taiga": {
      "cats": [
        13
      ],
      "icon": "Taiga.png",
      "implies": [
        "Django",
        "AngularJS"
      ],
      "js": {
        "taigaConfig": ""
      },
      "website": "http://taiga.io"
    },
    "Tamago": {
      "cats": [
        5
      ],
      "html": "<link [^>]*href=\"http://tamago\\.temonalab\\.com",
      "icon": "Tamago.png",
      "website": "http://tamago.temonalab.com"
    },
    "Tawk.to": {
      "cats": [
        52
      ],
      "icon": "TawkTo.png",
      "script": "//embed\\.tawk\\.to",
      "website": "http://tawk.to"
    },
    "Tealeaf": {
      "cats": [
        10
      ],
      "icon": "Tealeaf.png",
      "js": {
        "TeaLeaf": ""
      },
      "website": "http://www.tealeaf.com"
    },
    "Tealium": {
      "cats": [
        36
      ],
      "icon": "Tealium.png",
      "js": {
        "TEALIUMENABLED": ""
      },
      "script": [
        "^(?:https?:)?//tags\\.tiqcdn\\.com/",
        "/tealium/utag\\.js$"
      ],
      "website": "http://tealium.com"
    },
    "TeamCity": {
      "cats": [
        44
      ],
      "html": "<span class=\"versionTag\"><span class=\"vWord\">Version</span> ([\\d\\.]+)\\;version:\\1",
      "icon": "TeamCity.svg",
      "implies": [
        "Apache Tomcat",
        "Java",
        "jQuery",
        "Moment.js",
        "Prototype",
        "React",
        "Underscore.js"
      ],
      "meta": {
        "application-name": "TeamCity"
      },
      "website": "https://www.jetbrains.com/teamcity/"
    },
    "Tebex": {
      "cats": [
        6
      ],
      "icon": "Tebex.png",
      "script": "https://server\\.tebex\\.io/tebexAccounts/tebexaccounts\\.js",
      "website": "https://www.tebex.io/"
    },
    "Telescope": {
      "cats": [
        1
      ],
      "icon": "Telescope.png",
      "implies": [
        "Meteor",
        "React"
      ],
      "js": {
        "Telescope": ""
      },
      "website": "http://telescopeapp.org"
    },
    "Tencent Analytics (腾讯分析)": {
      "cats": [
        10
      ],
      "icon": "tajs.png",
      "script": "tajs\\.qq\\.com/stats",
      "website": "https://ta.qq.com/"
    },
    "Tencent Waterproof Wall": {
      "cats": [
        9,
        16
      ],
      "icon": "TencentWaterproofWall.png",
      "script": [
        "/TCaptcha\\.js",
        "captcha\\.qq\\.com/.*"
      ],
      "website": "https://007.qq.com/"
    },
    "Tengine": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Tengine"
      },
      "icon": "Tengine.png",
      "website": "http://tengine.taobao.org"
    },
    "Tessitura": {
      "cats": [
        53
      ],
      "html": "<!--[^>]+Tessitura Version: (\\d*\\.\\d*\\.\\d*)?\\;version:\\1",
      "icon": "tessitura.svg",
      "implies": [
        "Microsoft ASP.NET",
        "IIS",
        "Windows Server"
      ],
      "website": "https://www.tessituranetwork.com"
    },
    "Textalk": {
      "cats": [
        6
      ],
      "icon": "textalk.png",
      "meta": {
        "generator": "Textalk Webshop"
      },
      "website": "https://www.textalk.se"
    },
    "Textpattern CMS": {
      "cats": [
        1
      ],
      "icon": "Textpattern CMS.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "meta": {
        "generator": "Textpattern"
      },
      "website": "http://textpattern.com"
    },
    "Thelia": {
      "cats": [
        1,
        6
      ],
      "html": "<(?:link|style|script)[^>]+/assets/frontOffice/",
      "icon": "Thelia.png",
      "implies": [
        "PHP",
        "Symfony"
      ],
      "website": "http://thelia.net"
    },
    "ThinkPHP": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "ThinkPHP"
      },
      "icon": "ThinkPHP.png",
      "implies": "PHP",
      "website": "http://www.thinkphp.cn"
    },
    "Ticimax": {
      "cats": [
        6
      ],
      "icon": "Ticimax.png",
      "script": [
        "cdn\\.ticimax\\.com/"
      ],
      "website": "https://www.ticimax.com"
    },
    "Tictail": {
      "cats": [
        6
      ],
      "html": "<link[^>]*tictail\\.com",
      "icon": "tictail.png",
      "website": "https://tictail.com"
    },
    "TiddlyWiki": {
      "cats": [
        1,
        2,
        4,
        8
      ],
      "html": "<[^>]*type=[^>]text\\/vnd\\.tiddlywiki",
      "icon": "TiddlyWiki.png",
      "js": {
        "tiddler": ""
      },
      "meta": {
        "application-name": "^TiddlyWiki$",
        "copyright": "^TiddlyWiki created by Jeremy Ruston",
        "generator": "^TiddlyWiki$",
        "tiddlywiki-version": "^(.+)$\\;version:\\1"
      },
      "website": "http://tiddlywiki.com"
    },
    "Tiki Wiki CMS Groupware": {
      "cats": [
        1,
        2,
        8,
        11,
        13
      ],
      "icon": "Tiki Wiki CMS Groupware.png",
      "meta": {
        "generator": "^Tiki"
      },
      "script": "(?:/|_)tiki",
      "website": "http://tiki.org"
    },
    "Tilda": {
      "cats": [
        1
      ],
      "html": "<link[^>]* href=[^>]+tilda(?:cdn|\\.ws|-blocks)",
      "icon": "Tilda.svg",
      "script": "tilda(?:cdn|\\.ws|-blocks)",
      "website": "https://tilda.cc"
    },
    "Timeplot": {
      "cats": [
        25
      ],
      "icon": "Timeplot.png",
      "js": {
        "Timeplot": ""
      },
      "script": "timeplot.*\\.js",
      "website": "http://www.simile-widgets.org/timeplot/"
    },
    "TinyMCE": {
      "cats": [
        24
      ],
      "icon": "TinyMCE.png",
      "js": {
        "tinyMCE.majorVersion": "([\\d.]+)\\;version:\\1"
      },
      "script": "/tiny_?mce(?:\\.min)?\\.js",
      "website": "http://tinymce.com"
    },
    "Titan": {
      "cats": [
        36
      ],
      "icon": "Titan.png",
      "js": {
        "titan": "",
        "titanEnabled": ""
      },
      "website": "http://titan360.com"
    },
    "TomatoCart": {
      "cats": [
        6
      ],
      "icon": "TomatoCart.png",
      "js": {
        "AjaxShoppingCart": ""
      },
      "meta": {
        "generator": "TomatoCart"
      },
      "website": "http://tomatocart.com"
    },
    "TornadoServer": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "TornadoServer(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "TornadoServer.png",
      "website": "http://tornadoweb.org"
    },
    "TotalCode": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "^TotalCode$"
      },
      "icon": "TotalCode.png",
      "website": "http://www.totalcode.com"
    },
    "Trac": {
      "cats": [
        13
      ],
      "html": [
        "<a id=\"tracpowered",
        "Powered by <a href=\"[^\"]*\"><strong>Trac(?:[ /]([\\d.]+))?\\;version:\\1"
      ],
      "icon": "Trac.png",
      "implies": "Python",
      "website": "http://trac.edgewall.org"
    },
    "TrackJs": {
      "cats": [
        10
      ],
      "icon": "TrackJs.png",
      "js": {
        "TrackJs": ""
      },
      "script": "tracker\\.js",
      "website": "http://trackjs.com"
    },
    "Transifex": {
      "cats": [
        12
      ],
      "icon": "transifex.png",
      "js": {
        "Transifex.live.lib_version": "(.+)\\;version:\\1"
      },
      "website": "https://www.transifex.com"
    },
    "Translucide": {
      "cats": [
        1
      ],
      "icon": "translucide.svg",
      "implies": [
        "PHP",
        "jQuery"
      ],
      "script": "lucide\\.init(?:\\.min)?\\.js",
      "website": "http://www.translucide.net"
    },
    "Tray": {
      "cats": [
        6
      ],
      "icon": "tray.png",
      "script": "tcdn\\.com\\.br",
      "website": "https://www.tray.com.br"
    },
    "Tumblr": {
      "cats": [
        11
      ],
      "headers": {
        "X-Tumblr-User": ""
      },
      "html": "<iframe src=\"[^>]+tumblr\\.com",
      "icon": "Tumblr.png",
      "url": "^https?://(?:www\\.)?[^/]+\\.tumblr\\.com/",
      "website": "http://www.tumblr.com"
    },
    "Twilight CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-CMS": "Twilight CMS"
      },
      "icon": "Twilight CMS.png",
      "website": "http://www.twilightcms.com"
    },
    "TwistPHP": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "TwistPHP"
      },
      "icon": "TwistPHP.png",
      "implies": "PHP",
      "website": "http://twistphp.com"
    },
    "TwistedWeb": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "TwistedWeb(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "TwistedWeb.png",
      "website": "http://twistedmatrix.com/trac/wiki/TwistedWeb"
    },
    "Twitter": {
      "cats": [
        5
      ],
      "icon": "Twitter.svg",
      "script": "//platform\\.twitter\\.com/widgets\\.js",
      "website": "http://twitter.com"
    },
    "Twitter Emoji (Twemoji)": {
      "cats": [
        19
      ],
      "js": {
        "twemoji": ""
      },
      "script": "twemoji(?:\\.min)?\\.js",
      "website": "https://twitter.github.io/twemoji/"
    },
    "Twitter Flight": {
      "cats": [
        12
      ],
      "icon": "Twitter Flight.png",
      "implies": "jQuery",
      "js": {
        "flight": ""
      },
      "website": "https://flightjs.github.io/"
    },
    "Twitter typeahead.js": {
      "cats": [
        59
      ],
      "icon": "Twitter typeahead.js.png",
      "implies": "jQuery",
      "js": {
        "typeahead": ""
      },
      "script": "(?:typeahead|bloodhound)\\.(?:jquery|bundle)?(?:\\.min)?\\.js",
      "website": "https://twitter.github.io/typeahead.js"
    },
    "TypePad": {
      "cats": [
        11
      ],
      "icon": "TypePad.png",
      "meta": {
        "generator": "typepad"
      },
      "url": "typepad\\.com",
      "website": "http://www.typepad.com"
    },
    "Typecho": {
      "cats": [
        11
      ],
      "icon": "typecho.svg",
      "implies": "PHP",
      "js": {
        "TypechoComment": ""
      },
      "meta": {
        "generator": "Typecho( [\\d.]+)?\\;version:\\1"
      },
      "url": "/admin/login\\.php?referer=http%3A%2F%2F",
      "website": "http://typecho.org/"
    },
    "Typekit": {
      "cats": [
        17
      ],
      "icon": "Typekit.png",
      "js": {
        "Typekit.config.js": "^(.+)$\\;version:\\1"
      },
      "script": "use\\.typekit\\.com",
      "website": "http://typekit.com"
    },
    "UIKit": {
      "cats": [
        66
      ],
      "html": "<[^>]+class=\"[^\"]*(?:uk-container|uk-section)",
      "icon": "UIKit.png",
      "script": "uikit.*\\.js",
      "website": "https://getuikit.com"
    },
    "UMI.CMS": {
      "cats": [
        1
      ],
      "headers": {
        "X-Generated-By": "UMI\\.CMS"
      },
      "icon": "UMI.CMS.png",
      "implies": "PHP",
      "website": "https://www.umi-cms.ru"
    },
    "UNIX": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Unix"
      },
      "icon": "UNIX.png",
      "website": "http://unix.org"
    },
    "Ubercart": {
      "cats": [
        6
      ],
      "icon": "Ubercart.png",
      "implies": "Drupal",
      "script": "uc_cart/uc_cart_block\\.js",
      "website": "http://www.ubercart.org"
    },
    "Ubuntu": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Ubuntu",
        "X-Powered-By": "Ubuntu"
      },
      "icon": "Ubuntu.png",
      "website": "http://www.ubuntu.com/server"
    },
    "UltraCart": {
      "cats": [
        6
      ],
      "html": "<form [^>]*action=\"[^\"]*\\/cgi-bin\\/UCEditor\\?(?:[^\"]*&)?merchantId=[^\"]",
      "icon": "UltraCart.png",
      "js": {
        "ucCatalog": ""
      },
      "script": "cgi-bin\\/UCJavaScript\\?",
      "url": "/cgi-bin/UCEditor\\?",
      "website": "http://ultracart.com"
    },
    "Umbraco": {
      "cats": [
        1
      ],
      "headers": {
        "X-Umbraco-Version": "^(.+)$\\;version:\\1"
      },
      "html": "powered by <a href=[^>]+umbraco",
      "icon": "Umbraco.png",
      "implies": "Microsoft ASP.NET",
      "js": {
        "UC_IMAGE_SERVICE|ITEM_INFO_SERVICE": "",
        "UC_ITEM_INFO_SERVICE": "",
        "UC_SETTINGS": "",
        "Umbraco": ""
      },
      "meta": {
        "generator": "umbraco"
      },
      "url": "/umbraco/login\\.aspx(?:$|\\?)",
      "website": "http://umbraco.com"
    },
    "Unbounce": {
      "cats": [
        20,
        51
      ],
      "headers": {
        "X-Unbounce-PageId": ""
      },
      "icon": "Unbounce.png",
      "script": "ubembed\\.com",
      "website": "http://unbounce.com"
    },
    "Underscore.js": {
      "cats": [
        59
      ],
      "excludes": "Lodash",
      "icon": "Underscore.js.png",
      "js": {
        "_.VERSION": "^(.+)$\\;confidence:0\\;version:\\1",
        "_.restArguments": ""
      },
      "script": "underscore.*\\.js(?:\\?ver=([\\d.]+))?\\;version:\\1",
      "website": "http://underscorejs.org"
    },
    "Usabilla": {
      "cats": [
        13
      ],
      "icon": "Usabilla.svg",
      "js": {
        "usabilla_live": ""
      },
      "website": "http://usabilla.com"
    },
    "UserLike": {
      "cats": [
        52
      ],
      "icon": "UserLike.svg",
      "script": [
        "userlike\\.min\\.js",
        "userlikelib\\.min\\.js"
      ],
      "website": "http://userlike.com"
    },
    "UserRules": {
      "cats": [
        13
      ],
      "icon": "UserRules.png",
      "js": {
        "_usrp": ""
      },
      "website": "http://www.userrules.com"
    },
    "UserVoice": {
      "cats": [
        13
      ],
      "icon": "UserVoice.png",
      "js": {
        "UserVoice": ""
      },
      "website": "http://uservoice.com"
    },
    "Ushahidi": {
      "cats": [
        1,
        35
      ],
      "cookies": {
        "ushahidi": ""
      },
      "icon": "Ushahidi.png",
      "implies": [
        "PHP",
        "MySQL",
        "OpenLayers"
      ],
      "js": {
        "Ushahidi": ""
      },
      "script": "/js/ushahidi\\.js$",
      "website": "http://www.ushahidi.com"
    },
    "VIVVO": {
      "cats": [
        1
      ],
      "cookies": {
        "VivvoSessionId": ""
      },
      "icon": "VIVVO.png",
      "js": {
        "vivvo": ""
      },
      "website": "http://vivvo.net"
    },
    "VP-ASP": {
      "cats": [
        6
      ],
      "html": "<a[^>]+>Powered By VP-ASP Shopping Cart</a>",
      "icon": "VP-ASP.png",
      "implies": "Microsoft ASP.NET",
      "script": "vs350\\.js",
      "website": "http://www.vpasp.com"
    },
    "VTEX": {
      "cats": [
        6
      ],
      "cookies": {
        "VtexFingerPrint": "",
        "VtexWorkspace": "",
        "vtex_session": ""
      },
      "headers": {
        "Server": "^VTEX IO$",
        "powered": "vtex"
      },
      "icon": "VTEX.svg",
      "website": "https://vtex.com/"
    },
    "Vaadin": {
      "cats": [
        18
      ],
      "icon": "Vaadin.svg",
      "implies": "Java",
      "js": {
        "vaadin": ""
      },
      "script": "vaadinBootstrap\\.js(?:\\?v=([\\d.]+))?\\;version:\\1",
      "website": "https://vaadin.com"
    },
    "Vanilla": {
      "cats": [
        2
      ],
      "headers": {
        "X-Powered-By": "Vanilla"
      },
      "html": "<body id=\"(?:DiscussionsPage|vanilla)",
      "icon": "Vanilla.png",
      "implies": "PHP",
      "website": "http://vanillaforums.org"
    },
    "Varbase": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:vardot:varbase",
      "icon": "varbase.png",
      "implies": "Drupal",
      "meta": {
        "generator": "Varbase"
      },
      "website": "https://drupal.org/project/varbase"
    },
    "Varnish": {
      "cats": [
        23
      ],
      "headers": {
        "Via": "varnish(?: \\(Varnish/([\\d.]+)\\))?\\;version:\\1",
        "X-Varnish": "",
        "X-Varnish-Action": "",
        "X-Varnish-Age": "",
        "X-Varnish-Cache": "",
        "X-Varnish-Hostname": ""
      },
      "icon": "Varnish.svg",
      "website": "http://www.varnish-cache.org"
    },
    "Veoxa": {
      "cats": [
        36
      ],
      "html": "<img [^>]*src=\"[^\"]+tracking\\.veoxa\\.com",
      "icon": "Veoxa.png",
      "js": {
        "VuVeoxaContent": ""
      },
      "script": "tracking\\.veoxa\\.com",
      "website": "http://veoxa.com"
    },
    "Vercel": {
      "cats": [
        22
      ],
      "headers": {
        "server": "^now$",
        "x-now-trace": "",
        "x-vercel-cache": "",
        "x-vercel-id": ""
      },
      "icon": "vercel.svg",
      "website": "https://vercel.com"
    },
    "VideoJS": {
      "cats": [
        14
      ],
      "html": "<div[^>]+class=\"video-js+\">",
      "icon": "VideoJS.svg",
      "js": {
        "VideoJS": "",
        "videojs": "",
        "videojs.VERSION": "^(.+)$\\;version:\\1"
      },
      "script": [
        "zencdn\\.net/c/video\\.js",
        "cdnjs\\.cloudflare\\.com\\/ajax\\/libs\\/video\\.js\\/([\\d\\.]+)\\/\\;version:\\1"
      ],
      "website": "http://videojs.com"
    },
    "VigLink": {
      "cats": [
        36
      ],
      "icon": "VigLink.png",
      "js": {
        "vglnk": "",
        "vl_cB": "",
        "vl_disable": ""
      },
      "script": "(?:^[^/]*//[^/]*viglink\\.com/api/|vglnk\\.js)",
      "website": "http://viglink.com"
    },
    "Vigbo": {
      "cats": [
        1
      ],
      "cookies": {
        "_gphw_mode": ""
      },
      "html": "<link[^>]* href=[^>]+(?:\\.vigbo\\.com|\\.gophotoweb\\.com)",
      "icon": "vigbo.png",
      "script": "(?:\\.vigbo\\.com|\\.gophotoweb\\.com)",
      "website": "https://vigbo.com"
    },
    "Vignette": {
      "cats": [
        1
      ],
      "html": "<[^>]+=\"vgn-?ext",
      "icon": "Vignette.png",
      "website": "http://www.vignette.com"
    },
    "Vimeo": {
      "cats": [
        14
      ],
      "html": "(?:<(?:param|embed)[^>]+vimeo\\.com/moogaloop|<iframe[^>]player\\.vimeo\\.com)",
      "icon": "Vimeo.png",
      "website": "http://vimeo.com"
    },
    "Virgool": {
      "cats": [
        11
      ],
      "headers": {
        "X-Powered-By": "^Virgool$"
      },
      "icon": "Virgool.svg",
      "url": "^https?://(?:www\\.)?virgool\\.io",
      "website": "https://virgool.io"
    },
    "VirtueMart": {
      "cats": [
        6
      ],
      "html": "<div id=\"vmMainPage",
      "icon": "VirtueMart.png",
      "implies": "Joomla",
      "website": "http://virtuemart.net"
    },
    "Virtuoso": {
      "cats": [
        34
      ],
      "headers": {
        "Server": "Virtuoso/?([0-9.]+)?\\;version:\\1"
      },
      "meta": {
        "Copyright": "^Copyright &copy; \\d{4} OpenLink Software",
        "Keywords": "^OpenLink Virtuoso Sparql"
      },
      "url": "/sparql",
      "website": "https://virtuoso.openlinksw.com/"
    },
    "Visual Website Optimizer": {
      "cats": [
        10
      ],
      "html": [
        "<!-- (?:Start|End) Visual Website Optimizer A?Synchronous Code -->"
      ],
      "icon": "vwo.svg",
      "js": {
        "VWO": "",
        "__vwo": ""
      },
      "script": [
        "dev\\.visualwebsiteoptimizer\\.com"
      ],
      "website": "https://vwo.com/"
    },
    "VisualPath": {
      "cats": [
        10
      ],
      "icon": "VisualPath.png",
      "script": "visualpath[^/]*\\.trackset\\.it/[^/]+/track/include\\.js",
      "website": "http://www.trackset.com/web-analytics-software/visualpath"
    },
    "Volusion": {
      "cats": [
        6
      ],
      "html": [
        "<link [^>]*href=\"[^\"]*/vspfiles/\\;version:1",
        "<body [^>]*data-vn-page-name\\;version:2"
      ],
      "icon": "Volusion.svg",
      "js": {
        "volusion": ""
      },
      "script": "/volusion\\.js(?:\\?([\\d.]*))?\\;version:\\1",
      "website": "https://www.volusion.com"
    },
    "Vue.js": {
      "cats": [
        12
      ],
      "html": "<[^>]+\\sdata-v(?:ue)?-",
      "icon": "Vue.js.png",
      "js": {
        "Vue.version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "vue[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "(?:/([\\d.]+))?/vue(?:\\.min)?\\.js\\;version:\\1"
      ],
      "website": "https://vuejs.org"
    },
    "VuePress": {
      "cats": [
        57
      ],
      "icon": "VuePress.svg",
      "implies": "Vue.js",
      "meta": {
        "generator": "^VuePress(?: ([0-9.]+))?$\\;version:\\1"
      },
      "website": "https://vuepress.vuejs.org/"
    },
    "W3 Total Cache": {
      "cats": [
        23
      ],
      "headers": {
        "X-Powered-By": "W3 Total Cache(?:/([\\d.]+))?\\;version:\\1"
      },
      "html": "<!--[^>]+W3 Total Cache",
      "icon": "W3 Total Cache.png",
      "implies": "WordPress",
      "website": "http://www.w3-edge.com/wordpress-plugins/w3-total-cache"
    },
    "W3Counter": {
      "cats": [
        10
      ],
      "icon": "W3Counter.png",
      "script": "w3counter\\.com/tracker\\.js",
      "website": "http://www.w3counter.com"
    },
    "WEBXPAY": {
      "cats": [
        6
      ],
      "html": "Powered by <a href=\"https://www\\.webxpay\\.com\">WEBXPAY<",
      "icon": "WEBXPAY.png",
      "js": {
        "WEBXPAY": ""
      },
      "website": "https://webxpay.com"
    },
    "WHMCS": {
      "cats": [
        6
      ],
      "icon": "WHMCS.png",
      "js": {
        "WHMCS": ""
      },
      "website": "http://www.whmcs.com"
    },
    "WP Engine": {
      "cats": [
        62
      ],
      "headers": {
        "X-Pass-Why": "",
        "X-Powered-By": "WP Engine",
        "X-WPE-Loopback-Upstream-Addr": "",
        "wpe-backend": ""
      },
      "icon": "wpengine.svg",
      "implies": "WordPress",
      "website": "https://wpengine.com"
    },
    "WP Rocket": {
      "cats": [
        23
      ],
      "headers": {
        "X-Powered-By": "WP Rocket(?:/([\\d.]+))?\\;version:\\1",
        "X-Rocket-Nginx-Bypass": ""
      },
      "html": "<!--[^>]+WP Rocket",
      "icon": "WP Rocket.png",
      "implies": "WordPress",
      "website": "http://wp-rocket.me"
    },
    "WP-Statistics": {
      "cats": [
        10
      ],
      "html": [
        "<!-- Analytics by WP-Statistics v([\\d.]+) -\\;version:\\1"
      ],
      "icon": "WP-Statistics.png",
      "implies": "WordPress",
      "website": "https://wp-statistics.com"
    },
    "WPCacheOn": {
      "cats": [
        23
      ],
      "headers": {
        "x-powered-by": "^Optimized by WPCacheOn"
      },
      "icon": "WPCacheOn.png",
      "implies": [
        "WordPress"
      ],
      "website": "https://wpcacheon.io"
    },
    "Warp": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Warp/(\\d+(?:\\.\\d+)+)?$\\;version:\\1"
      },
      "icon": "Warp.png",
      "implies": "Haskell",
      "website": "http://www.stackage.org/package/warp"
    },
    "Web2py": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "web2py"
      },
      "icon": "Web2py.png",
      "implies": [
        "Python",
        "jQuery"
      ],
      "meta": {
        "generator": "^Web2py"
      },
      "script": "web2py\\.js",
      "website": "http://web2py.com"
    },
    "WebGUI": {
      "cats": [
        1
      ],
      "cookies": {
        "wgSession": ""
      },
      "icon": "WebGUI.png",
      "implies": "Perl",
      "meta": {
        "generator": "^WebGUI ([\\d.]+)\\;version:\\1"
      },
      "website": "http://www.webgui.org"
    },
    "WebPublisher": {
      "cats": [
        1
      ],
      "icon": "WebPublisher.png",
      "meta": {
        "generator": "WEB\\|Publisher"
      },
      "website": "http://scannet.dk"
    },
    "WebSite X5": {
      "cats": [
        20
      ],
      "icon": "WebSite X5.png",
      "meta": {
        "generator": "Incomedia WebSite X5 (\\w+ [\\d.]+)\\;version:\\1"
      },
      "website": "http://websitex5.com"
    },
    "Webdev": {
      "cats": [
        20
      ],
      "headers": {
        "WebDevSrc": ""
      },
      "html": "<!-- [a-zA-Z0-9_]+ [\\d/]+ [\\d:]+ WebDev \\d\\d ([\\d.]+) -->\\;version:\\1",
      "icon": "webdev.png",
      "meta": {
        "generator": "^WEBDEV$"
      },
      "website": "https://www.windev.com/webdev/index.html"
    },
    "Webflow": {
      "cats": [
        51
      ],
      "html": "<html[^>]+data-wf-site",
      "icon": "webflow.svg",
      "js": {
        "Webflow": ""
      },
      "meta": {
        "generator": "Webflow"
      },
      "website": "https://webflow.com"
    },
    "Webix": {
      "cats": [
        12
      ],
      "icon": "Webix.png",
      "js": {
        "webix": ""
      },
      "script": "\\bwebix\\.js",
      "website": "http://webix.com"
    },
    "Webmine": {
      "cats": [
        56
      ],
      "html": "<iframe[^>]+src=[\\'\"]https://webmine\\.cz/miner\\?key=",
      "icon": "webmine.png",
      "website": "https://webmine.cz/"
    },
    "WebsPlanet": {
      "cats": [
        1
      ],
      "icon": "WebsPlanet.png",
      "meta": {
        "generator": "WebsPlanet"
      },
      "website": "http://websplanet.com"
    },
    "Websale": {
      "cats": [
        6
      ],
      "cookies": {
        "websale_ac": ""
      },
      "icon": "Websale.png",
      "website": "http://websale.de"
    },
    "Website Creator": {
      "cats": [
        1
      ],
      "icon": "WebsiteCreator.png",
      "implies": [
        "PHP",
        "MySQL",
        "Vue.js"
      ],
      "meta": {
        "generator": "Website Creator by hosttech",
        "wsc_rendermode": ""
      },
      "website": "https://www.hosttech.ch/websitecreator"
    },
    "WebsiteBaker": {
      "cats": [
        1
      ],
      "icon": "WebsiteBaker.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "meta": {
        "generator": "WebsiteBaker"
      },
      "website": "http://websitebaker2.org/en/home.php"
    },
    "Websocket": {
      "cats": [
        19
      ],
      "html": [
        "<link[^>]+rel=[\"']web-socket[\"']",
        "<(?:link|a)[^>]+href=[\"']wss?://"
      ],
      "icon": "websocket.png",
      "website": "https://en.wikipedia.org/wiki/WebSocket"
    },
    "Webtrekk": {
      "cats": [
        10
      ],
      "icon": "Webtrekk.png",
      "js": {
        "WebtrekkV3": "",
        "webtrekk": "",
        "webtrekkConfig": "",
        "webtrekkHeatmapObjects": "",
        "webtrekkLinktrackObjects": "",
        "webtrekkUnloadObjects": "",
        "webtrekkV3": "",
        "wt_tt": "",
        "wt_ttv2": ""
      },
      "website": "http://www.webtrekk.com"
    },
    "Webtrends": {
      "cats": [
        10
      ],
      "html": "<img[^>]+id=\"DCSIMG\"[^>]+webtrends",
      "icon": "Webtrends.png",
      "js": {
        "WTOptimize": "",
        "WebTrends": ""
      },
      "website": "http://worldwide.webtrends.com"
    },
    "Webzi": {
      "cats": [
        1
      ],
      "icon": "Webzi.svg",
      "js": {
        "Webzi": ""
      },
      "meta": {
        "generator": "^Webzi"
      },
      "script": "cdn\\.6th\\.ir",
      "website": "https://webzi.ir"
    },
    "Weebly": {
      "cats": [
        1
      ],
      "icon": "Weebly.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "_W.configDomain": ""
      },
      "script": "cdn\\d+\\.editmysite\\.com",
      "website": "https://www.weebly.com"
    },
    "Weglot": {
      "cats": [
        19
      ],
      "headers": {
        "Weglot-Translated": ""
      },
      "icon": "Weglot.png",
      "script": [
        "cdn\\.weglot\\.com",
        "wp-content/plugins/weglot"
      ],
      "website": "https://www.weglot.com"
    },
    "Welcart": {
      "cats": [
        6
      ],
      "cookies": {
        "usces_cookie": ""
      },
      "cpe": "cpe:/a:welcart:welcart",
      "html": [
        "<link[^>]+?href=\"[^\"]+usces_default(?:\\.min)?\\.css",
        "<!-- Welcart version : v([\\d.]+)\\;version:\\1"
      ],
      "icon": "welcart.png",
      "implies": [
        "PHP",
        "WordPress"
      ],
      "script": "uscesL10n",
      "website": "https://www.welcart.com"
    },
    "Whooshkaa": {
      "cats": [
        5
      ],
      "html": "<iframe src=\"[^>]+whooshkaa\\.com",
      "icon": "Whooshkaa.svg",
      "website": "https://www.whooshkaa.com"
    },
    "Wikinggruppen": {
      "cats": [
        6
      ],
      "html": [
        "<!-- WIKINGGRUPPEN"
      ],
      "icon": "wikinggruppen.png",
      "website": "https://wikinggruppen.se/"
    },
    "WikkaWiki": {
      "cats": [
        8
      ],
      "html": "Powered by <a href=\"[^>]+WikkaWiki",
      "icon": "WikkaWiki.png",
      "meta": {
        "generator": "WikkaWiki"
      },
      "website": "http://wikkawiki.org"
    },
    "Windows CE": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "\\bWinCE\\b"
      },
      "icon": "Microsoft.png",
      "website": "http://microsoft.com"
    },
    "Windows Server": {
      "cats": [
        28
      ],
      "headers": {
        "Server": "Win32|Win64"
      },
      "icon": "WindowsServer.png",
      "website": "http://microsoft.com/windowsserver"
    },
    "Wink": {
      "cats": [
        26,
        12
      ],
      "icon": "Wink.png",
      "js": {
        "wink.version": "^(.+)$\\;version:\\1"
      },
      "script": "(?:_base/js/base|wink).*\\.js",
      "website": "http://winktoolkit.org"
    },
    "Winstone Servlet Container": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Winstone Servlet (?:Container|Engine) v?([\\d.]+)?\\;version:\\1",
        "X-Powered-By": "Winstone(?:\\.([\\d.]+))?\\;version:\\1"
      },
      "website": "http://winstone.sourceforge.net"
    },
    "Wix": {
      "cats": [
        1,
        6,
        11
      ],
      "cookies": {
        "Domain": "\\.wix\\.com"
      },
      "headers": {
        "X-Wix-Renderer-Server": "",
        "X-Wix-Request-Id": "",
        "X-Wix-Server-Artifact-Id": ""
      },
      "icon": "Wix.png",
      "implies": "React",
      "js": {
        "wixBiSession": ""
      },
      "meta": {
        "generator": "Wix\\.com Website Builder"
      },
      "script": "static\\.parastorage\\.com",
      "website": "https://www.wix.com"
    },
    "Wolf CMS": {
      "cats": [
        1
      ],
      "html": "(?:<a href=\"[^>]+wolfcms\\.org[^>]+>Wolf CMS(?:</a>)? inside|Thank you for using <a[^>]+>Wolf CMS)",
      "icon": "Wolf CMS.png",
      "implies": "PHP",
      "website": "http://www.wolfcms.org"
    },
    "Woltlab Community Framework": {
      "cats": [
        1
      ],
      "html": "var WCF_PATH[^>]+",
      "icon": "Woltlab Community Framework.png",
      "implies": "PHP",
      "script": "WCF\\..*\\.js",
      "website": "http://www.woltlab.com"
    },
    "WooCommerce": {
      "cats": [
        6
      ],
      "html": [
        "<!-- WooCommerce",
        "<link rel='[^']+' id='woocommerce-(?:layout|smallscreen|general)-css'  href='https?://[^/]+/wp-content/plugins/woocommerce/assets/css/woocommerce(?:-layout|-smallscreen)?\\.css?ver=([\\d.]+)'\\;version:\\1"
      ],
      "icon": "WooCommerce.png",
      "implies": "WordPress",
      "js": {
        "woocommerce_params": ""
      },
      "meta": {
        "generator": "WooCommerce ([\\d.]+)\\;version:\\1"
      },
      "script": "/woocommerce(?:\\.min)?\\.js(?:\\?ver=([0-9.]+))?\\;version:\\1",
      "website": "https://woocommerce.com"
    },
    "Woopra": {
      "cats": [
        10
      ],
      "icon": "Woopra.png",
      "script": "static\\.woopra\\.com",
      "website": "http://www.woopra.com"
    },
    "WordPress": {
      "cats": [
        1,
        11
      ],
      "cpe": "cpe:/a:wordpress:wordpress",
      "headers": {
        "X-Pingback": "/xmlrpc\\.php$",
        "link": "rel=\"https://api\\.w\\.org/\""
      },
      "html": [
        "<link rel=[\"']stylesheet[\"'] [^>]+/wp-(?:content|includes)/",
        "<link[^>]+s\\d+\\.wp\\.com"
      ],
      "icon": "WordPress.svg",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "wp_username": ""
      },
      "meta": {
        "generator": "^WordPress ?([\\d.]+)?\\;version:\\1",
        "shareaholic:wp_version": ""
      },
      "script": "/wp-(?:content|includes)/",
      "website": "https://wordpress.org"
    },
    "WordPress Super Cache": {
      "cats": [
        23
      ],
      "headers": {
        "WP-Super-Cache": ""
      },
      "html": "<!--[^>]+WP-Super-Cache",
      "icon": "wp_super_cache.png",
      "implies": "WordPress",
      "website": "http://z9.io/wp-super-cache/"
    },
    "WordPress VIP": {
      "cats": [
        62
      ],
      "headers": {
        "x-powered-by": "^WordPress\\.com VIP"
      },
      "icon": "wpvip.svg",
      "implies": "WordPress",
      "website": "https://wpvip.com"
    },
    "Wowza Media Server": {
      "cats": [
        38
      ],
      "html": "<title>Wowza Media Server \\d+ ((?:\\w+ Edition )?\\d+\\.[\\d\\.]+(?: build\\d+)?)?\\;version:\\1",
      "icon": "Wowza Media Server.png",
      "website": "http://www.wowza.com"
    },
    "X-Cart": {
      "cats": [
        6
      ],
      "cookies": {
        "xid": "[a-z\\d]{32}(?:;|$)"
      },
      "html": [
        "Powered by X-Cart(?: (\\d+))? <a[^>]+href=\"http://www\\.x-cart\\.com/\"[^>]*>\\;version:\\1",
        "<a[^>]+href=\"[^\"]*(?:\\?|&)xcart_form_id=[a-z\\d]{32}(?:&|$)"
      ],
      "icon": "X-Cart.png",
      "implies": "PHP",
      "js": {
        "xcart_web_dir": "",
        "xliteConfig": ""
      },
      "meta": {
        "generator": "X-Cart(?: (\\d+))?\\;version:\\1"
      },
      "script": "/skin/common_files/modules/Product_Options/func\\.js",
      "website": "http://x-cart.com"
    },
    "XAMPP": {
      "cats": [
        22
      ],
      "html": "<title>XAMPP(?: Version ([\\d\\.]+))?</title>\\;version:\\1",
      "icon": "XAMPP.png",
      "implies": [
        "Apache",
        "MySQL",
        "PHP",
        "Perl"
      ],
      "meta": {
        "author": "Kai Oswald Seidler\\;confidence:10"
      },
      "website": "http://www.apachefriends.org/en/xampp.html"
    },
    "XMB": {
      "cats": [
        2
      ],
      "html": "<!-- Powered by XMB",
      "icon": "XMB.png",
      "website": "http://www.xmbforum.com"
    },
    "XOOPS": {
      "cats": [
        1
      ],
      "icon": "XOOPS.png",
      "implies": "PHP",
      "js": {
        "xoops": ""
      },
      "meta": {
        "generator": "XOOPS"
      },
      "website": "http://xoops.org"
    },
    "XRegExp": {
      "cats": [
        59
      ],
      "icon": "XRegExp.png",
      "js": {
        "XRegExp.version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "xregexp[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "/([\\d.]+)/xregexp(?:\\.min)?\\.js\\;version:\\1",
        "xregexp.*\\.js"
      ],
      "website": "http://xregexp.com"
    },
    "XWiki": {
      "cats": [
        8
      ],
      "excludes": "MediaWiki",
      "html": [
        "<html[^>]data-xwiki-[^>]>"
      ],
      "icon": "xwiki.png",
      "implies": "Java\\;confidence:99",
      "meta": {
        "wiki": "xwiki"
      },
      "website": "http://www.xwiki.org"
    },
    "Xajax": {
      "cats": [
        59
      ],
      "icon": "Xajax.png",
      "script": "xajax_core.*\\.js",
      "website": "http://xajax-project.org"
    },
    "Xanario": {
      "cats": [
        6
      ],
      "icon": "Xanario.png",
      "meta": {
        "generator": "xanario shopsoftware"
      },
      "website": "http://xanario.de"
    },
    "XenForo": {
      "cats": [
        2
      ],
      "cookies": {
        "xf_csrf": "",
        "xf_session": ""
      },
      "html": [
        "(?:jQuery\\.extend\\(true, XenForo|Forum software by XenForo™|<!--XF:branding|<html[^>]+id=\"XenForo\")",
        "<html id=\"XF\" "
      ],
      "icon": "XenForo.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "XF.GuestUsername": ""
      },
      "website": "http://xenforo.com"
    },
    "Xeora": {
      "cats": [
        18
      ],
      "headers": {
        "Server": "XeoraEngine",
        "X-Powered-By": "XeoraCube"
      },
      "html": "<input type=\"hidden\" name=\"_sys_bind_\\d+\" id=\"_sys_bind_\\d+\" />",
      "icon": "xeora.png",
      "implies": "Microsoft ASP.NET",
      "script": "/_bi_sps_v.+\\.js",
      "website": "http://www.xeora.org"
    },
    "Xitami": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Xitami(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Xitami.png",
      "website": "http://xitami.com"
    },
    "Xonic": {
      "cats": [
        6
      ],
      "html": [
        "Powered by <a href=\"http://www\\.xonic-solutions\\.de/index\\.php\" target=\"_blank\">xonic-solutions Shopsoftware</a>"
      ],
      "icon": "xonic.png",
      "meta": {
        "keywords": "xonic-solutions"
      },
      "script": "core/jslib/jquery\\.xonic\\.js\\.php",
      "website": "http://www.xonic-solutions.de"
    },
    "XpressEngine": {
      "cats": [
        1
      ],
      "icon": "XpressEngine.png",
      "meta": {
        "generator": "XpressEngine"
      },
      "website": "http://www.xpressengine.com/"
    },
    "YUI": {
      "cats": [
        59
      ],
      "icon": "YUI.png",
      "js": {
        "YAHOO.VERSION": "^(.+)$\\;version:\\1",
        "YUI.version": "^(.+)$\\;version:\\1"
      },
      "script": "(?:/yui/|yui\\.yahooapis\\.com)",
      "website": "http://yuilibrary.com"
    },
    "YUI Doc": {
      "cats": [
        4
      ],
      "html": "(?:<html[^>]* yuilibrary\\.com/rdf/[\\d.]+/yui\\.rdf|<body[^>]+class=\"yui3-skin-sam)",
      "icon": "yahoo.png",
      "website": "http://developer.yahoo.com/yui/yuidoc"
    },
    "YaBB": {
      "cats": [
        2
      ],
      "html": "Powered by <a href=\"[^>]+yabbforum",
      "icon": "YaBB.png",
      "website": "http://www.yabbforum.com"
    },
    "Yahoo Advertising": {
      "cats": [
        36
      ],
      "html": [
        "<iframe[^>]+adserver\\.yahoo\\.com",
        "<img[^>]+clicks\\.beap\\.bc\\.yahoo\\.com"
      ],
      "icon": "yahoo.png",
      "js": {
        "adxinserthtml": ""
      },
      "script": "adinterax\\.com",
      "website": "http://advertising.yahoo.com"
    },
    "Yahoo! Ecommerce": {
      "cats": [
        6
      ],
      "headers": {
        "X-XRDS-Location": "/ystore/"
      },
      "html": "<link[^>]+store\\.yahoo\\.net",
      "icon": "yahoo.png",
      "js": {
        "YStore": ""
      },
      "website": "http://smallbusiness.yahoo.com/ecommerce"
    },
    "Yahoo! Tag Manager": {
      "cats": [
        42
      ],
      "html": "<!-- (?:End )?Yahoo! Tag Manager -->",
      "icon": "yahoo.png",
      "script": "b\\.yjtag\\.jp/iframe",
      "website": "https://tagmanager.yahoo.co.jp/"
    },
    "Yahoo! Web Analytics": {
      "cats": [
        10
      ],
      "icon": "yahoo.png",
      "js": {
        "YWA": ""
      },
      "script": "d\\.yimg\\.com/mi/ywa\\.js",
      "website": "http://web.analytics.yahoo.com"
    },
    "Yandex.Direct": {
      "cats": [
        36
      ],
      "html": "<yatag class=\"ya-partner__ads\">",
      "icon": "Yandex.Direct.png",
      "js": {
        "yandex_ad_format": "",
        "yandex_partner_id": ""
      },
      "script": "https?://an\\.yandex\\.ru/",
      "website": "http://partner.yandex.com"
    },
    "Yandex.Metrika": {
      "cats": [
        10
      ],
      "icon": "Yandex.Metrika.png",
      "js": {
        "yandex_metrika": ""
      },
      "script": [
        "mc\\.yandex\\.ru\\/metrika\\/watch\\.js",
        "cdn\\.jsdelivr\\.net\\/npm\\/yandex-metrica-watch\\/watch\\.js"
      ],
      "website": "http://metrika.yandex.com"
    },
    "Yaws": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "Yaws(?: ([\\d.]+))?\\;version:\\1"
      },
      "icon": "Yaws.png",
      "implies": "Erlang",
      "website": "http://yaws.hyber.org"
    },
    "Yepcomm": {
      "cats": [
        6
      ],
      "icon": "yepcomm.png",
      "meta": {
        "author": "Yepcomm Tecnologia",
        "copyright": "Yepcomm Tecnologia"
      },
      "website": "https://www.yepcomm.com.br"
    },
    "Yieldlab": {
      "cats": [
        36
      ],
      "icon": "Yieldlab.png",
      "script": "^https?://(?:[^/]+\\.)?yieldlab\\.net/",
      "website": "http://yieldlab.de"
    },
    "Yii": {
      "cats": [
        18
      ],
      "cookies": {
        "YII_CSRF_TOKEN": ""
      },
      "html": [
        "Powered by <a href=\"http://www\\.yiiframework\\.com/\" rel=\"external\">Yii Framework</a>",
        "<input type=\"hidden\" value=\"[a-zA-Z0-9]{40}\" name=\"YII_CSRF_TOKEN\" \\/>",
        "<!\\[CDATA\\[YII-BLOCK-(?:HEAD|BODY-BEGIN|BODY-END)\\]"
      ],
      "icon": "Yii.png",
      "implies": "PHP",
      "script": [
        "/assets/[a-zA-Z0-9]{8}\\/yii\\.js$",
        "/yii\\.(?:validation|activeForm)\\.js"
      ],
      "website": "https://www.yiiframework.com"
    },
    "Yoast SEO": {
      "cats": [
        54
      ],
      "html": [
        "<!-- This site is optimized with the Yoast (?:WordPress )?SEO plugin v([\\d.]+) -\\;version:\\1"
      ],
      "icon": "Yoast SEO.png",
      "implies": "WordPress",
      "website": "http://yoast.com"
    },
    "YouTrack": {
      "cats": [
        13
      ],
      "html": [
        "no-title=\"YouTrack\">",
        "data-reactid=\"[^\"]+\">youTrack ([0-9.]+)<\\;version:\\1",
        "type=\"application/opensearchdescription\\+xml\" title=\"YouTrack\"/>"
      ],
      "icon": "YouTrack.png",
      "website": "http://www.jetbrains.com/youtrack/"
    },
    "YouTube": {
      "cats": [
        14
      ],
      "html": "<(?:param|embed|iframe)[^>]+youtube(?:-nocookie)?\\.com/(?:v|embed)",
      "icon": "YouTube.png",
      "website": "http://www.youtube.com"
    },
    "ZK": {
      "cats": [
        18
      ],
      "html": "<!-- ZK [.\\d\\s]+-->",
      "icon": "ZK.png",
      "implies": "Java",
      "script": "zkau/",
      "website": "http://zkoss.org"
    },
    "ZURB Foundation": {
      "cats": [
        66
      ],
      "html": [
        "<link[^>]+foundation[^>\"]+css",
        "<div [^>]*class=\"[^\"]*(?:small|medium|large)-\\d{1,2} columns"
      ],
      "icon": "ZURB Foundation.png",
      "js": {
        "Foundation.version": "([\\d.]+)\\;version:\\1"
      },
      "website": "http://foundation.zurb.com"
    },
    "Zabbix": {
      "cats": [
        19
      ],
      "html": "<body[^>]+zbxCallPostScripts",
      "icon": "Zabbix.png",
      "implies": "PHP",
      "js": {
        "zbxCallPostScripts": ""
      },
      "meta": {
        "Author": "ZABBIX SIA\\;confidence:70"
      },
      "url": "\\/zabbix\\/\\;confidence:30",
      "website": "http://zabbix.com"
    },
    "Zanox": {
      "cats": [
        36
      ],
      "html": "<img [^>]*src=\"[^\"]+ad\\.zanox\\.com",
      "icon": "Zanox.png",
      "js": {
        "zanox": ""
      },
      "script": "zanox\\.com/scripts/zanox\\.js$",
      "website": "http://zanox.com"
    },
    "Zen Cart": {
      "cats": [
        6
      ],
      "icon": "Zen Cart.png",
      "meta": {
        "generator": "Zen Cart"
      },
      "website": "http://www.zen-cart.com"
    },
    "Zend": {
      "cats": [
        22
      ],
      "cookies": {
        "ZENDSERVERSESSID": ""
      },
      "headers": {
        "X-Powered-By": "Zend(?:Server)?(?:[\\s/]?([0-9.]+))?\\;version:\\1"
      },
      "icon": "Zend.png",
      "website": "http://zend.com"
    },
    "Zendesk": {
      "cats": [
        1,
        52,
        61
      ],
      "cookies": {
        "_help_center_session": "",
        "_zendesk_cookie": "",
        "_zendesk_shared_session": ""
      },
      "headers": {
        "x-zendesk-user-id": ""
      },
      "icon": "Zendesk.png",
      "website": "https://zendesk.com"
    },
    "Zendesk Chat": {
      "cats": [
        52
      ],
      "icon": "Zendesk Chat.png",
      "script": "v2\\.zopim\\.com",
      "website": "http://zopim.com"
    },
    "Zenfolio": {
      "cats": [
        7
      ],
      "icon": "Zenfolio.png",
      "js": {
        "Zenfolio": ""
      },
      "website": "https://zenfolio.com"
    },
    "Zepto": {
      "cats": [
        59
      ],
      "icon": "Zepto.png",
      "js": {
        "Zepto": ""
      },
      "script": "zepto.*\\.js",
      "website": "http://zeptojs.com"
    },
    "Zimbra": {
      "cats": [
        30
      ],
      "cookies": {
        "ZM_TEST": "true"
      },
      "html": "<script>(?:\\.|\\n)*\"refresh\":\\{\"version\":\"([\\w\\.]+)\\s\\;version:\\1",
      "icon": "Zimbra.png",
      "implies": "Java",
      "website": "https://www.zimbra.com/"
    },
    "Zinnia": {
      "cats": [
        11
      ],
      "icon": "Zinnia.png",
      "implies": "Django",
      "meta": {
        "generator": "Zinnia"
      },
      "website": "http://django-blog-zinnia.com"
    },
    "Zipkin": {
      "cats": [
        10
      ],
      "headers": {
        "X-B3-Flags": "",
        "X-B3-ParentSpanId": "",
        "X-B3-Sampled": "",
        "X-B3-SpanId": "",
        "X-B3-TraceId": ""
      },
      "icon": "Zipkin.png",
      "website": "https://zipkin.io/"
    },
    "Zone.js": {
      "cats": [
        12
      ],
      "js": {
        "Zone.root": ""
      },
      "website": "https://github.com/angular/angular/tree/master/packages/zone.js"
    },
    "Zope": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "^Zope/"
      },
      "icon": "Zope.png",
      "website": "http://zope.org"
    },
    "a-blog cms": {
      "cats": [
        1
      ],
      "icon": "a-blog cms.svg",
      "implies": "PHP",
      "meta": {
        "generator": "a-blog cms"
      },
      "website": "http://www.a-blogcms.jp"
    },
    "actionhero.js": {
      "cats": [
        18,
        22
      ],
      "headers": {
        "X-Powered-By": "actionhero API"
      },
      "icon": "actionhero.js.png",
      "implies": "Node.js",
      "js": {
        "actionheroClient": ""
      },
      "script": "actionheroClient\\.js",
      "website": "http://www.actionherojs.com"
    },
    "amCharts": {
      "cats": [
        25
      ],
      "html": "<svg[^>]*><desc>JavaScript chart by amCharts ([\\d.]*)\\;version:\\1",
      "icon": "amCharts.png",
      "js": {
        "AmCharts": ""
      },
      "script": "amcharts.*\\.js",
      "website": "http://amcharts.com"
    },
    "animate.css": {
      "cats": [
        66
      ],
      "html": [
        "<link [^>]+(?:/([\\d.]+)/)?animate\\.(?:min\\.)?css\\;version:\\1"
      ],
      "website": "https://daneden.github.io/animate.css/"
    },
    "basket.js": {
      "cats": [
        59
      ],
      "icon": "basket.js.png",
      "js": {
        "basket.isValidItem": ""
      },
      "script": "basket.*\\.js\\;confidence:10",
      "website": "https://addyosmani.github.io/basket.js/"
    },
    "cPanel": {
      "cats": [
        9
      ],
      "cookies": {
        "cprelogin": "",
        "cpsession": ""
      },
      "headers": {
        "Server": "cpsrvd/([\\d.]+)\\;version:\\1"
      },
      "html": "<!-- cPanel",
      "icon": "cPanel.png",
      "website": "http://www.cpanel.net"
    },
    "cgit": {
      "cats": [
        19
      ],
      "html": [
        "<[^>]+id='cgit'",
        "generated by <a href='http://git\\.zx2c4\\.com/cgit/about/'>cgit v([\\d.a-z-]+)</a>\\;version:\\1"
      ],
      "icon": "cgit.png",
      "implies": "git",
      "meta": {
        "generator": "^cgit v([\\d.a-z-]+)$\\;version:\\1"
      },
      "website": "http://git.zx2c4.com/cgit"
    },
    "comScore": {
      "cats": [
        10
      ],
      "html": "<iframe[^>]* (?:id=\"comscore\"|scr=[^>]+comscore)|\\.scorecardresearch\\.com/beacon\\.js|COMSCORE\\.beacon",
      "icon": "comScore.png",
      "js": {
        "COMSCORE": "",
        "_COMSCORE": ""
      },
      "script": "\\.scorecardresearch\\.com/beacon\\.js|COMSCORE\\.beacon",
      "website": "http://comscore.com"
    },
    "debut": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "debut\\/?([\\d\\.]+)?\\;version:\\1"
      },
      "icon": "debut.png",
      "website": "http://www.brother.com"
    },
    "decimal.js": {
      "cats": [
        59
      ],
      "icon": "decimal.js.png",
      "js": {
        "Decimal.ROUND_HALF_FLOOR": ""
      },
      "script": [
        "decimal[.-]([\\d.]*\\d+)(?:\\.min)?\\.js\\;version:\\1",
        "/([\\d.]*\\d+)/decimal(?:\\.min)?\\.js\\;version:\\1",
        "decimal(?:\\.min)?\\.js(?:\\?ver(?:sion)?=([\\d.]*\\d+))?\\;version:\\1"
      ],
      "website": "https://mikemcl.github.io/decimal.js/"
    },
    "deepMiner": {
      "cats": [
        56
      ],
      "icon": "deepminer.png",
      "js": {
        "deepMiner": ""
      },
      "script": "deepMiner\\.js",
      "website": "https://github.com/deepwn/deepMiner"
    },
    "e107": {
      "cats": [
        1
      ],
      "cookies": {
        "e107_tz": ""
      },
      "headers": {
        "X-Powered-By": "e107"
      },
      "icon": "e107.png",
      "implies": "PHP",
      "script": "[^a-z\\d]e107\\.js",
      "website": "http://e107.org"
    },
    "eSyndiCat": {
      "cats": [
        1
      ],
      "headers": {
        "X-Drectory-Script": "^eSyndiCat"
      },
      "icon": "eSyndiCat.png",
      "implies": "PHP",
      "js": {
        "esyndicat": ""
      },
      "meta": {
        "generator": "^eSyndiCat "
      },
      "website": "http://esyndicat.com"
    },
    "eZ Platform": {
      "cats": [
        1,
        6
      ],
      "icon": "eZ.svg",
      "implies": "Symfony",
      "meta": {
        "generator": "eZ Platform"
      },
      "website": "https://ezplatform.com/"
    },
    "eZ Publish": {
      "cats": [
        1,
        6
      ],
      "cookies": {
        "eZSESSID": ""
      },
      "headers": {
        "X-Powered-By": "^eZ Publish"
      },
      "icon": "eZ.svg",
      "implies": "PHP",
      "meta": {
        "generator": "eZ Publish"
      },
      "website": "https://github.com/ezsystems/ezpublish-legacy"
    },
    "ef.js": {
      "cats": [
        12
      ],
      "icon": "ef.js.svg",
      "js": {
        "ef.version": "^(.+)$\\;version:\\1",
        "efCore": ""
      },
      "script": "/ef(?:-core)?(?:\\.min|\\.dev)?\\.js",
      "website": "http://ef.js.org"
    },
    "enduro.js": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "^enduro\\.js"
      },
      "icon": "enduro.js.svg",
      "implies": "Node.js",
      "website": "http://endurojs.com"
    },
    "experiencedCMS": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:experiencedcms:experiencedcms",
      "icon": "experiencedCMS_Logo.png",
      "implies": "PHP",
      "meta": {
        "generator": "^experiencedCMS$"
      },
      "website": "https://experiencedcms.berkearas.de"
    },
    "gRPC": {
      "cats": [
        18
      ],
      "headers": {
        "Content-Type": "^application\\/grpc"
      },
      "icon": "gRPC.png",
      "website": "https://grpc.io"
    },
    "git": {
      "cats": [
        47
      ],
      "cpe": "cpe:/a:git-scm:git",
      "icon": "git.svg",
      "meta": {
        "generator": "\\bgit/([\\d.]+\\d)\\;version:\\1"
      },
      "website": "http://git-scm.com"
    },
    "gitlist": {
      "cats": [
        47
      ],
      "cpe": "cpe:/a:gitlist:gitlist",
      "html": "<p>Powered by <a[^>]+>GitList ([\\d.]+)\\;version:\\1",
      "implies": [
        "PHP",
        "git"
      ],
      "website": "http://gitlist.org"
    },
    "gitweb": {
      "cats": [
        47
      ],
      "html": "<!-- git web interface version ([\\d.]+)?\\;version:\\1",
      "icon": "git.svg",
      "implies": [
        "Perl",
        "git"
      ],
      "meta": {
        "generator": "gitweb(?:/([\\d.]+\\d))?\\;version:\\1"
      },
      "script": "static/gitweb\\.js$",
      "website": "http://git-scm.com"
    },
    "govCMS": {
      "cats": [
        1
      ],
      "icon": "govCMS.svg",
      "implies": "Drupal",
      "meta": {
        "generator": "Drupal ([\\d]+) \\(http:\\/\\/drupal\\.org\\) \\+ govCMS\\;version:\\1"
      },
      "website": "https://www.govcms.gov.au"
    },
    "gunicorn": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "gunicorn(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "gunicorn.png",
      "implies": "Python",
      "website": "http://gunicorn.org"
    },
    "hCaptcha": {
      "cats": [
        16
      ],
      "html": "<style[^>]+[^<]+#cf-hcaptcha-container[^<]+</style>",
      "icon": "hcaptcha-symbol-256.png",
      "script": "https://hcaptcha.com/([\\d]+?)/api.js\\;version:\\1",
      "website": "https://www.hcaptcha.com/"
    },
    "iEXExchanger": {
      "cats": [
        1
      ],
      "cookies": {
        "iexexchanger_session": ""
      },
      "icon": "iEXExchanger.png",
      "implies": [
        "PHP",
        "Apache",
        "Angular"
      ],
      "meta": {
        "generator": "iEXExchanger"
      },
      "website": "https://exchanger.iexbase.com"
    },
    "iPresta": {
      "cats": [
        6
      ],
      "icon": "iPresta.png",
      "implies": [
        "PHP",
        "PrestaShop"
      ],
      "meta": {
        "designer": "iPresta"
      },
      "website": "http://ipresta.ir"
    },
    "iWeb": {
      "cats": [
        20
      ],
      "icon": "iWeb.png",
      "meta": {
        "generator": "^iWeb( [\\d.]+)?\\;version:\\1"
      },
      "website": "http://apple.com/ilife/iweb"
    },
    "ikiwiki": {
      "cats": [
        8
      ],
      "html": [
        "<link rel=\"alternate\" type=\"application/x-wiki\" title=\"Edit this page\" href=\"[^\"]*/ikiwiki\\.cgi",
        "<a href=\"/(?:cgi-bin/)?ikiwiki\\.cgi\\?do="
      ],
      "icon": "ikiwiki.png",
      "website": "http://ikiwiki.info"
    },
    "imperia CMS": {
      "cats": [
        1
      ],
      "html": "<imp:live-info sysid=\"[0-9a-f-]+\"(?: node_id=\"[0-9/]*\")? *\\/>",
      "icon": "imperiaCMS.svg",
      "implies": "Perl",
      "meta": {
        "GENERATOR": "^IMPERIA ([0-9.]{2,3})\\;version:\\1",
        "X-Imperia-Live-Info": ""
      },
      "url": "imperia/md/",
      "website": "https://www.pirobase-imperia.com/de/produkte/produktuebersicht/imperia-cms"
    },
    "io4 CMS": {
      "cats": [
        1
      ],
      "icon": "io4 CMS.png",
      "meta": {
        "generator": "GO[ |]+CMS Enterprise"
      },
      "website": "http://notenbomer.nl/Producten/Content_management/io4_|_cms"
    },
    "ip-label": {
      "cats": [
        10
      ],
      "icon": "iplabel.svg",
      "js": {
        "clobs": ""
      },
      "script": "clobs\\.js",
      "website": "http://www.ip-label.com"
    },
    "jComponent": {
      "cats": [
        12,
        59
      ],
      "icon": "jComponent.png",
      "implies": "jQuery",
      "js": {
        "MAIN.version": ".*\\;version:\\1"
      },
      "website": "https://componentator.com"
    },
    "jQTouch": {
      "cats": [
        26
      ],
      "icon": "jQTouch.png",
      "js": {
        "jQT": ""
      },
      "script": "jqtouch.*\\.js",
      "website": "http://jqtouch.com"
    },
    "jQuery": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:jquery:jquery",
      "icon": "jQuery.svg",
      "js": {
        "jQuery.fn.jquery": "([\\d.]+)\\;version:\\1"
      },
      "script": [
        "jquery[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "/([\\d.]+)/jquery(?:\\.min)?\\.js\\;version:\\1",
        "jquery.*\\.js(?:\\?ver(?:sion)?=([\\d.]+))?\\;version:\\1"
      ],
      "website": "https://jquery.com"
    },
    "jQuery Migrate": {
      "cats": [
        59
      ],
      "icon": "jQuery.svg",
      "implies": "jQuery",
      "js": {
        "jQuery.migrateVersion": "([\\d.]+)\\;version:\\1",
        "jQuery.migrateWarnings": "",
        "jqueryMigrate": ""
      },
      "script": "jquery[.-]migrate(?:-([\\d.]+))?(?:\\.min)?\\.js(?:\\?ver=([\\d.]+))?\\;version:\\1?\\1:\\2",
      "website": "https://github.com/jquery/jquery-migrate"
    },
    "jQuery Mobile": {
      "cats": [
        26
      ],
      "icon": "jQuery Mobile.svg",
      "implies": "jQuery",
      "js": {
        "jQuery.mobile.version": "^(.+)$\\;version:\\1"
      },
      "script": "jquery[.-]mobile(?:-([\\d.]))?(?:\\.min)?\\.js(?:\\?ver=([\\d.]+))?\\;version:\\1?\\1:\\2",
      "website": "https://jquerymobile.com"
    },
    "jQuery Sparklines": {
      "cats": [
        25
      ],
      "implies": "jQuery",
      "script": "jquery\\.sparkline.*\\.js",
      "website": "http://omnipotent.net/jquery.sparkline/"
    },
    "jQuery UI": {
      "cats": [
        59
      ],
      "cpe": "cpe:/a:jquery:jquery_ui",
      "icon": "jQuery UI.svg",
      "implies": "jQuery",
      "js": {
        "jQuery.ui.version": "^(.+)$\\;version:\\1"
      },
      "script": [
        "jquery-ui[.-]([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
        "([\\d.]+)/jquery-ui(?:\\.min)?\\.js\\;version:\\1",
        "jquery-ui.*\\.js"
      ],
      "website": "http://jqueryui.com"
    },
    "jQuery-pjax": {
      "cats": [
        26
      ],
      "html": "<div[^>]+data-pjax-container",
      "implies": "jQuery",
      "js": {
        "jQuery.pjax": ""
      },
      "meta": {
        "pjax-push": "",
        "pjax-replace": "",
        "pjax-timeout": ""
      },
      "script": "jquery[.-]pjax(?:-([\\d.]))?(?:\\.min)?\\.js(?:\\?ver=([\\d.]+))?\\;version:\\1?\\1:\\2",
      "website": "https://github.com/defunkt/jquery-pjax"
    },
    "jqPlot": {
      "cats": [
        25
      ],
      "icon": "jqPlot.png",
      "implies": "jQuery",
      "script": "jqplot.*\\.js",
      "website": "http://www.jqplot.com"
    },
    "jsDelivr": {
      "cats": [
        31
      ],
      "html": "<[^>]+?//cdn\\.jsdelivr\\.net/",
      "icon": "jsdelivr-icon.svg",
      "script": "//cdn\\.jsdelivr\\.net/",
      "website": "https://www.jsdelivr.com/"
    },
    "kolors4u": {
      "cats": [
        1,
        11,
        23,
        6
      ],
      "headers": {
        "X-Content-Encoded-By": "kolors4u ([\\d.]+)\\;version:\\1"
      },
      "icon": "kolors4u.png",
      "implies": "WordPress",
      "meta": {
        "generator": "kolors4u (?: ([\\d.]+))?\\;version:\\1"
      },
      "website": "http://kolors4u.com"
    },
    "libwww-perl-daemon": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "libwww-perl-daemon(?:/([\\d\\.]+))?\\;version:\\1"
      },
      "icon": "libwww-perl-daemon.png",
      "implies": "Perl",
      "website": "http://metacpan.org/pod/HTTP::Daemon"
    },
    "lighttpd": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "lighttpd(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "lighttpd.png",
      "website": "http://www.lighttpd.net"
    },
    "math.js": {
      "cats": [
        59
      ],
      "icon": "math.js.png",
      "js": {
        "mathjs": ""
      },
      "script": "math(?:\\.min)?\\.js",
      "website": "http://mathjs.org"
    },
    "mini_httpd": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "mini_httpd(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "mini_httpd.png",
      "website": "http://acme.com/software/mini_httpd"
    },
    "mod_auth_pam": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_auth_pam(?:/([\\d\\.]+))?\\;version:\\1"
      },
      "icon": "Apache.svg",
      "implies": "Apache",
      "website": "http://pam.sourceforge.net/mod_auth_pam"
    },
    "mod_dav": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "\\b(?:mod_)?DAV\\b(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Apache.svg",
      "implies": "Apache",
      "website": "http://webdav.org/mod_dav"
    },
    "mod_fastcgi": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_fastcgi(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Apache.svg",
      "implies": "Apache",
      "website": "http://www.fastcgi.com/mod_fastcgi/docs/mod_fastcgi.html"
    },
    "mod_jk": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_jk(?:/([\\d\\.]+))?\\;version:\\1"
      },
      "icon": "Apache.svg",
      "implies": [
        "Apache Tomcat",
        "Apache"
      ],
      "website": "http://tomcat.apache.org/tomcat-3.3-doc/mod_jk-howto.html"
    },
    "mod_perl": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_perl(?:/([\\d\\.]+))?\\;version:\\1"
      },
      "icon": "mod_perl.png",
      "implies": [
        "Perl",
        "Apache"
      ],
      "website": "http://perl.apache.org"
    },
    "mod_python": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_python(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "mod_python.png",
      "implies": [
        "Python",
        "Apache"
      ],
      "website": "http://www.modpython.org"
    },
    "mod_rack": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_rack(?:/([\\d.]+))?\\;version:\\1",
        "X-Powered-By": "mod_rack(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Phusion Passenger.png",
      "implies": [
        "Ruby on Rails\\;confidence:50",
        "Apache"
      ],
      "website": "http://phusionpassenger.com"
    },
    "mod_rails": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_rails(?:/([\\d.]+))?\\;version:\\1",
        "X-Powered-By": "mod_rails(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "Phusion Passenger.png",
      "implies": [
        "Ruby on Rails\\;confidence:50",
        "Apache"
      ],
      "website": "http://phusionpassenger.com"
    },
    "mod_ssl": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_ssl(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "mod_ssl.png",
      "implies": "Apache",
      "website": "http://modssl.org"
    },
    "mod_wsgi": {
      "cats": [
        33
      ],
      "headers": {
        "Server": "mod_wsgi(?:/([\\d.]+))?\\;version:\\1",
        "X-Powered-By": "mod_wsgi(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "mod_wsgi.png",
      "implies": [
        "Python\\;confidence:50",
        "Apache"
      ],
      "website": "https://code.google.com/p/modwsgi"
    },
    "nghttpx - HTTP/2 proxy": {
      "cats": [
        22
      ],
      "headers": {
        "Server": "nghttpx nghttp2/?([\\d.]+)?\\;version:\\1"
      },
      "website": "https://nghttp2.org"
    },
    "nopCommerce": {
      "cats": [
        6
      ],
      "cookies": {
        "Nop.customer": ""
      },
      "html": "(?:<!--Powered by nopCommerce|Powered by: <a[^>]+nopcommerce)",
      "icon": "nopCommerce.png",
      "implies": "Microsoft ASP.NET",
      "meta": {
        "generator": "^nopCommerce$"
      },
      "website": "http://www.nopcommerce.com"
    },
    "osCommerce": {
      "cats": [
        6
      ],
      "cookies": {
        "osCsid": ""
      },
      "html": [
        "<br />Powered by <a href=\"https?://www\\.oscommerce\\.com",
        "<(?:input|a)[^>]+name=\"osCsid\"",
        "<(?:tr|td|table)class=\"[^\"]*infoBoxHeading"
      ],
      "icon": "osCommerce.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "website": "https://www.oscommerce.com"
    },
    "osTicket": {
      "cats": [
        13
      ],
      "cookies": {
        "OSTSESSID": ""
      },
      "icon": "osTicket.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "website": "http://osticket.com"
    },
    "otrs": {
      "cats": [
        13
      ],
      "headers": {
        "X-Powered-By": "OTRS ([\\d.]+)\\;version:\\1"
      },
      "html": "<!--\\s+OTRS: Copyright",
      "icon": "otrs.png",
      "implies": "Perl",
      "script": "^/otrs-web/js/",
      "website": "https://www.otrs.com"
    },
    "ownCloud": {
      "cats": [
        19
      ],
      "html": "<a href=\"https://owncloud\\.com\" target=\"_blank\">ownCloud Inc\\.</a><br/>Your Cloud, Your Data, Your Way!",
      "icon": "ownCloud.png",
      "implies": "PHP",
      "meta": {
        "apple-itunes-app": "app-id=543672169"
      },
      "website": "https://owncloud.org"
    },
    "papaya CMS": {
      "cats": [
        1
      ],
      "html": "<link[^>]*/papaya-themes/",
      "icon": "papaya CMS.png",
      "implies": "PHP",
      "website": "https://papaya-cms.com"
    },
    "parcel": {
      "cats": [
        19
      ],
      "icon": "Parcel.png",
      "js": {
        "parcelRequire": ""
      },
      "website": "https://parceljs.org/"
    },
    "particles.js": {
      "cats": [
        25
      ],
      "html": "<div id=\"particles-js\">",
      "js": {
        "particlesJS": ""
      },
      "script": "/particles(?:\\.min)?\\.js",
      "website": "https://vincentgarreau.com/particles.js/"
    },
    "phpAlbum": {
      "cats": [
        7
      ],
      "html": "<!--phpalbum ([.\\d\\s]+)-->\\;version:\\1",
      "icon": "phpAlbum.png",
      "implies": "PHP",
      "website": "http://phpalbum.net"
    },
    "phpBB": {
      "cats": [
        2
      ],
      "cookies": {
        "phpbb": ""
      },
      "html": [
        "Powered by <a[^>]+phpBB",
        "<div class=phpbb_copyright>",
        "<[^>]+styles/(?:sub|pro)silver/theme",
        "<img[^>]+i_icon_mini",
        "<table class=\"[^\"]*forumline"
      ],
      "icon": "phpBB.png",
      "implies": "PHP",
      "js": {
        "phpbb": "",
        "style_cookie_settings": ""
      },
      "meta": {
        "copyright": "phpBB Group"
      },
      "website": "https://phpbb.com"
    },
    "phpCMS": {
      "cats": [
        1
      ],
      "icon": "PHP.svg",
      "implies": "PHP",
      "js": {
        "phpcms": ""
      },
      "website": "http://phpcms.de"
    },
    "phpDocumentor": {
      "cats": [
        4
      ],
      "html": "<!-- Generated by phpDocumentor",
      "icon": "phpDocumentor.png",
      "implies": "PHP",
      "website": "https://www.phpdoc.org"
    },
    "phpMyAdmin": {
      "cats": [
        3
      ],
      "html": [
        "!\\[CDATA\\[[^<]*PMA_VERSION:\\\"([\\d.]+)\\;version:\\1",
        "(?: \\| phpMyAdmin ([\\d.]+)<\\/title>|PMA_sendHeaderLocation\\(|<link [^>]*href=\"[^\"]*phpmyadmin\\.css\\.php)\\;version:\\1"
      ],
      "icon": "phpMyAdmin.png",
      "implies": [
        "PHP",
        "MySQL"
      ],
      "js": {
        "pma_absolute_uri": ""
      },
      "website": "https://www.phpmyadmin.net"
    },
    "phpPgAdmin": {
      "cats": [
        3
      ],
      "html": "(?:<title>phpPgAdmin</title>|<span class=\"appname\">phpPgAdmin)",
      "icon": "phpPgAdmin.png",
      "implies": "PHP",
      "website": "http://phppgadmin.sourceforge.net"
    },
    "phpSQLiteCMS": {
      "cats": [
        1
      ],
      "icon": "phpSQLiteCMS.png",
      "implies": [
        "PHP",
        "SQLite"
      ],
      "meta": {
        "generator": "^phpSQLiteCMS(?: (.+))?$\\;version:\\1"
      },
      "website": "http://phpsqlitecms.net"
    },
    "phpwind": {
      "cats": [
        1,
        2
      ],
      "html": "(?:Powered|Code) by <a href=\"[^\"]+phpwind\\.net",
      "icon": "phpwind.png",
      "implies": "PHP",
      "meta": {
        "generator": "^phpwind(?: v([0-9-]+))?\\;version:\\1"
      },
      "website": "https://www.phpwind.net"
    },
    "pinoox": {
      "cats": [
        18
      ],
      "cookies": {
        "pinoox_session": ""
      },
      "icon": "pinoox.png",
      "implies": "PHP",
      "js": {
        "pinoox": ""
      },
      "website": "https://pinoox.com"
    },
    "pirobase CMS": {
      "cats": [
        1
      ],
      "html": [
        "<(?:script|link)[^>]/site/[a-z0-9/._-]+/resourceCached/[a-z0-9/._-]+",
        "<input[^>]+cbi:///cms/"
      ],
      "icon": "pirobaseCMS.svg",
      "implies": "Java",
      "website": "https://www.pirobase-imperia.com/de/produkte/produktuebersicht/pirobase-cms"
    },
    "plentymarkets": {
      "cats": [
        6
      ],
      "headers": {
        "X-Plenty-Shop": ""
      },
      "icon": "plentymarkets.svg",
      "meta": {
        "generator": "plentymarkets"
      },
      "script": [
        "plenty\\.shop\\.(?:min\\.)?js"
      ],
      "website": "https://www.plentymarkets.com/"
    },
    "prettyPhoto": {
      "cats": [
        59
      ],
      "html": "(?:<link [^>]*href=\"[^\"]*prettyPhoto(?:\\.min)?\\.css|<a [^>]*rel=\"prettyPhoto)",
      "icon": "prettyPhoto.png",
      "implies": "jQuery",
      "js": {
        "pp_alreadyInitialized": "",
        "pp_descriptions": "",
        "pp_images": "",
        "pp_titles": ""
      },
      "script": "jquery\\.prettyPhoto\\.js",
      "website": "http://no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/"
    },
    "punBB": {
      "cats": [
        2
      ],
      "html": "Powered by <a href=\"[^>]+punbb",
      "icon": "punBB.png",
      "implies": "PHP",
      "js": {
        "PUNBB": ""
      },
      "website": "http://punbb.informer.com"
    },
    "reCAPTCHA": {
      "cats": [
        16
      ],
      "html": [
        "<div[^>]+id=\"recaptcha_image",
        "<link[^>]+recaptcha",
        "<div[^>]+class=\"g-recaptcha\""
      ],
      "icon": "reCAPTCHA.png",
      "js": {
        "Recaptcha": "",
        "recaptcha": ""
      },
      "script": [
        "api-secure\\.recaptcha\\.net",
        "recaptcha_ajax\\.js",
        "/recaptcha/api\\.js"
      ],
      "website": "https://www.google.com/recaptcha/"
    },
    "sIFR": {
      "cats": [
        17
      ],
      "icon": "sIFR.png",
      "script": "sifr\\.js",
      "website": "https://www.mikeindustries.com/blog/sifr"
    },
    "sNews": {
      "cats": [
        1
      ],
      "icon": "sNews.png",
      "meta": {
        "generator": "sNews"
      },
      "website": "https://snewscms.com"
    },
    "script.aculo.us": {
      "cats": [
        59
      ],
      "icon": "script.aculo.us.png",
      "js": {
        "Scriptaculous.Version": "^(.+)$\\;version:\\1"
      },
      "script": "/(?:scriptaculous|protoaculous)(?:\\.js|/)",
      "website": "https://script.aculo.us"
    },
    "scrollreveal": {
      "cats": [
        59
      ],
      "html": "<[^>]+data-sr(?:-id)",
      "icon": "scrollreveal.svg",
      "js": {
        "ScrollReveal().version": "^(.+)$\\;version:\\1"
      },
      "script": "scrollreveal(?:\\.min)(?:\\.js)",
      "website": "https://scrollrevealjs.org"
    },
    "shine.js": {
      "cats": [
        25
      ],
      "js": {
        "Shine": ""
      },
      "script": "shine(?:\\.min)?\\.js",
      "website": "https://bigspaceship.github.io/shine.js/"
    },
    "shoperfa": {
      "cats": [
        6
      ],
      "headers": {
        "X-Powered-By": "^Shoperfa$"
      },
      "icon": "Shoperfa.png",
      "url": "^https?://(?:www\\.)?shoperfa\\.com",
      "website": "https://shoperfa.com"
    },
    "styled-components": {
      "cats": [
        12,
        47
      ],
      "html": [
        "<style[^>]*data-styled(?:-components)?[\\s\"]",
        "<style[^>]+data-styled-version=\"([0-9]+)\"\\;version:\\1",
        "<[^>]+sc-component-id: sc-"
      ],
      "icon": "styled-components.png",
      "implies": "React",
      "js": {
        "styled": ""
      },
      "website": "https://styled-components.com"
    },
    "swift.engine": {
      "cats": [
        1
      ],
      "headers": {
        "X-Powered-By": "swift\\.engine"
      },
      "icon": "swift.engine.png",
      "website": "http://mittec.ru/default"
    },
    "tailwindcss": {
      "cats": [
        66
      ],
      "html": [
        "<link[^>]+?href=\"[^\"]+tailwindcss(?:\\.min)?\\.css"
      ],
      "icon": "tailwindcss.svg",
      "website": "https://tailwindcss.com/"
    },
    "three.js": {
      "cats": [
        25
      ],
      "icon": "three.js.png",
      "js": {
        "THREE.REVISION": "^(.+)$\\;version:\\1"
      },
      "script": "three(?:\\.min)?\\.js",
      "website": "https://threejs.org"
    },
    "thttpd": {
      "cats": [
        22
      ],
      "cpe": "cpe:/a:acme:thttpd",
      "headers": {
        "Server": "\\bthttpd(?:/([\\d.]+))?\\;version:\\1"
      },
      "icon": "thttpd.png",
      "website": "https://acme.com/software/thttpd"
    },
    "total.js": {
      "cats": [
        18
      ],
      "headers": {
        "X-Powered-By": "^total\\.js"
      },
      "icon": "total.js.png",
      "implies": "Node.js",
      "website": "https://totaljs.com"
    },
    "uCoz": {
      "cats": [
        1
      ],
      "cookies": {
        "uCoz": ""
      },
      "icon": "uCoz.svg",
      "website": "https://ucoz.ru"
    },
    "uKnowva": {
      "cats": [
        1,
        2,
        50
      ],
      "headers": {
        "X-Content-Encoded-By": "uKnowva ([\\d.]+)\\;version:\\1"
      },
      "html": "<a[^>]+>Powered by uKnowva</a>",
      "icon": "uKnowva.png",
      "implies": "PHP",
      "meta": {
        "generator": "uKnowva (?: ([\\d.]+))?\\;version:\\1"
      },
      "script": "/media/conv/js/jquery\\.js",
      "website": "https://uknowva.com"
    },
    "user.com": {
      "cats": [
        10
      ],
      "html": "<div[^>]+/id=\"ue_widget\"",
      "icon": "user.com.svg",
      "js": {
        "UserEngage": ""
      },
      "website": "https://user.com"
    },
    "vBulletin": {
      "cats": [
        2
      ],
      "cookies": {
        "bblastactivity": "",
        "bblastvisit": "",
        "bbsessionhash": ""
      },
      "cpe": "cpe:/a:vbulletin:vbulletin",
      "html": "<div id=\"copyright\">Powered by vBulletin",
      "icon": "vBulletin.png",
      "implies": "PHP",
      "js": {
        "vBulletin": ""
      },
      "meta": {
        "generator": "vBulletin ?([\\d.]+)?\\;version:\\1"
      },
      "website": "https://www.vbulletin.com"
    },
    "vibecommerce": {
      "cats": [
        6
      ],
      "excludes": "PrestaShop",
      "icon": "vibecommerce.png",
      "implies": "PHP",
      "meta": {
        "designer": "vibecommerce",
        "generator": "vibecommerce"
      },
      "website": "http://vibecommerce.com.br"
    },
    "webEdition": {
      "cats": [
        1
      ],
      "cpe": "cpe:/a:webedition:webedition_cms",
      "icon": "webEdition.png",
      "meta": {
        "DC.title": "webEdition",
        "generator": "webEdition"
      },
      "website": "http://webedition.de/en"
    },
    "webpack": {
      "cats": [
        19
      ],
      "icon": "webpack.svg",
      "js": {
        "webpackJsonp": ""
      },
      "website": "https://webpack.js.org/"
    },
    "wisyCMS": {
      "cats": [
        1
      ],
      "icon": "wisyCMS.svg",
      "meta": {
        "generator": "^wisy CMS[ v]{0,3}([0-9.,]*)\\;version:\\1"
      },
      "website": "https://wisy.3we.de"
    },
    "wpCache": {
      "cats": [
        23
      ],
      "headers": {
        "X-Powered-By": "wpCache(?:/([\\d.]+))?\\;version:\\1"
      },
      "html": "<!--[^>]+wpCache",
      "icon": "wpCache.png",
      "implies": [
        "WordPress",
        "PHP"
      ],
      "meta": {
        "generator": "wpCache",
        "keywords": "wpCache"
      },
      "url": "^https?://[^/]+\\.wpcache\\.co",
      "website": "https://wpcache.co"
    },
    "xCharts": {
      "cats": [
        25
      ],
      "html": "<link[^>]* href=\"[^\"]*xcharts(?:\\.min)?\\.css",
      "implies": "D3",
      "js": {
        "xChart": ""
      },
      "script": "xcharts\\.js",
      "website": "https://tenxer.github.io/xcharts/"
    },
    "xtCommerce": {
      "cats": [
        6
      ],
      "html": "<div class=\"copyright\">[^<]+<a[^>]+>xt:Commerce",
      "icon": "xtCommerce.png",
      "meta": {
        "generator": "xt:Commerce"
      },
      "website": "https://www.xt-commerce.com"
    }
  },
  "categories_original": {
    "1": {
      "name": "CMS",
      "priority": 1
    },
    "2": {
      "name": "Message boards",
      "priority": 1
    },
    "3": {
      "name": "Database managers",
      "priority": 2
    },
    "4": {
      "name": "Documentation tools",
      "priority": 2
    },
    "5": {
      "name": "Widgets",
      "priority": 9
    },
    "6": {
      "name": "Ecommerce",
      "priority": 1
    },
    "7": {
      "name": "Photo galleries",
      "priority": 1
    },
    "8": {
      "name": "Wikis",
      "priority": 1
    },
    "9": {
      "name": "Hosting panels",
      "priority": 1
    },
    "10": {
      "name": "Analytics",
      "priority": 9
    },
    "11": {
      "name": "Blogs",
      "priority": 1
    },
    "12": {
      "name": "JavaScript frameworks",
      "priority": 8
    },
    "13": {
      "name": "Issue trackers",
      "priority": 2
    },
    "14": {
      "name": "Video players",
      "priority": 7
    },
    "15": {
      "name": "Comment systems",
      "priority": 9
    },
    "16": {
      "name": "Captchas",
      "priority": 9
    },
    "17": {
      "name": "Font scripts",
      "priority": 9
    },
    "18": {
      "name": "Web frameworks",
      "priority": 7
    },
    "19": {
      "name": "Miscellaneous",
      "priority": 9
    },
    "20": {
      "name": "Editors",
      "priority": 4
    },
    "21": {
      "name": "LMS",
      "priority": 1
    },
    "22": {
      "name": "Web servers",
      "priority": 8
    },
    "23": {
      "name": "Caching",
      "priority": 7
    },
    "24": {
      "name": "Rich text editors",
      "priority": 5
    },
    "25": {
      "name": "JavaScript graphics",
      "priority": 6
    },
    "26": {
      "name": "Mobile frameworks",
      "priority": 8
    },
    "27": {
      "name": "Programming languages",
      "priority": 5
    },
    "28": {
      "name": "Operating systems",
      "priority": 6
    },
    "29": {
      "name": "Search engines",
      "priority": 4
    },
    "30": {
      "name": "Webmail",
      "priority": 2
    },
    "31": {
      "name": "CDN",
      "priority": 9
    },
    "32": {
      "name": "Marketing automation",
      "priority": 9
    },
    "33": {
      "name": "Web server extensions",
      "priority": 7
    },
    "34": {
      "name": "Databases",
      "priority": 5
    },
    "35": {
      "name": "Maps",
      "priority": 6
    },
    "36": {
      "name": "Advertising",
      "priority": 9
    },
    "37": {
      "name": "Network devices",
      "priority": 2
    },
    "38": {
      "name": "Media servers",
      "priority": 1
    },
    "39": {
      "name": "Webcams",
      "priority": 9
    },
    "41": {
      "name": "Payment processors",
      "priority": 8
    },
    "42": {
      "name": "Tag managers",
      "priority": 9
    },
    "44": {
      "name": "CI",
      "priority": 3
    },
    "45": {
      "name": "Control systems",
      "priority": 2
    },
    "46": {
      "name": "Remote access",
      "priority": 1
    },
    "47": {
      "name": "Development",
      "priority": 2
    },
    "48": {
      "name": "Network storage",
      "priority": 2
    },
    "49": {
      "name": "Feed readers",
      "priority": 1
    },
    "50": {
      "name": "DMS",
      "priority": 1
    },
    "51": {
      "name": "Page builders",
      "priority": 2
    },
    "52": {
      "name": "Live chat",
      "priority": 8
    },
    "53": {
      "name": "CRM",
      "priority": 5
    },
    "54": {
      "name": "SEO",
      "priority": 8
    },
    "55": {
      "name": "Accounting",
      "priority": 1
    },
    "56": {
      "name": "Cryptominers",
      "priority": 5
    },
    "57": {
      "name": "Static site generator",
      "priority": 1
    },
    "58": {
      "name": "User Onboarding",
      "priority": 8
    },
    "59": {
      "name": "JavaScript libraries",
      "priority": 9
    },
    "60": {
      "name": "Containers",
      "priority": 8
    },
    "61": {
      "name": "SaaS",
      "priority": 8
    },
    "62": {
      "name": "PaaS",
      "priority": 8
    },
    "63": {
      "name": "IaaS",
      "priority": 8
    },
    "64": {
      "name": "Reverse proxies",
      "priority": 7
    },
    "65": {
      "name": "Load balancers",
      "priority": 7
    },
    "66": {
      "name": "UI frameworks",
      "priority": 7
    }
  },
  "categories": {
		"1": "cms",
		"2": "message-boards",
		"3": "database-managers",
		"4": "documentation-tools",
		"5": "widgets",
		"6": "ecommerce",
		"7": "photo-galleries",
		"8": "wikis",
		"9": "hosting-panels",
		"10": "analytics",
		"11": "blogs",
		"12": "javascript-frameworks",
		"13": "issue-trackers",
		"14": "video-players",
		"15": "comment-systems",
		"16": "captchas",
		"17": "font-scripts",
		"18": "web-frameworks",
		"19": "miscellaneous",
		"20": "editors",
		"21": "lms",
		"22": "web-servers",
		"23": "cache-tools",
		"24": "rich-text-editors",
		"25": "javascript-graphics",
		"26": "mobile-frameworks",
		"27": "programming-languages",
		"28": "operating-systems",
		"29": "search-engines",
		"30": "web-mail",
		"31": "cdn",
		"32": "marketing-automation",
		"33": "web-server-extensions",
		"34": "databases",
		"35": "maps",
		"36": "advertising-networks",
		"37": "network-devices",
		"38": "media-servers",
		"39": "webcams",
		"40": "printers",
		"41": "payment-processors",
		"42": "tag-managers",
		"43": "paywalls",
		"44": "build-ci-systems",
		"45": "control-systems",
		"46": "remote-access",
		"47": "dev-tools",
		"48": "network-storage",
		"49": "feed-readers",
		"50": "document-management-systems",
		"51": "landing-page-builders",
        "52": "None",
        "53": "None",
        "54": "None",
        "55": "None",
        "56": "None",
        "57": "None",
        "58": "None",
        "59": "None",
        "60": "None",
        "61": "None",
        "62": "None",
        "63": "None",
        "64": "None",
        "65": "None",
        "66": "None"
	}
}