# -*- coding:utf-8 -*-
# Created at 2015/9/2

"""
    Function:
        Tag Data
"""
__author__ = 'Zachary Marv - 马子昂'

import json

input_d = "../raw_data/st1.dat"
output_d = "../raw_data/st2.dat"

lib_list = {
    "com/google/android/gms": "Google GMS;谷歌GMS",
    "com/google/android/gcm": "Google GCM;谷歌GCM",
    "com/google/ads": "Google Ads;谷歌广告",
    "com/google/analysis": "Google Analysis;谷歌分析",
    "com/google/gson": "Google Gson;谷歌Gson",
    "com/google/gdata": "Google GData;谷歌Gdata",
    "com/google/android/net": "Google Android Net",
    "com/google/analytics": "Google Analysis",
    "org/apache/http": "Apache Http;阿帕奇HTTP",
    "com/admob": "Google Ads;谷歌广告",
    "org/apache/cordova": "Apache Cordova",
    "org/apache/log4j": "Apache Log4j",
    "org/apache/james": "Apache James",
    "com/squareup": "SquareUp",
    "com/umeng/fb": "Umeng feedback;友盟反馈SDK",
    "com/umeng/analytics": "Umeng Analytics;友盟分析",
    "com/umeng/common": "Umeng Common;友盟Common",
    "com/umeng/update": "Umeng Update;友盟自动更新",
    "com/umeng/social_analytic": "Umeng Social Analytic;友盟社会化分析",
    "com/android/vending": "Google Play;谷歌官方应用市场",
    "com/google/android/vending": "Google Play;谷歌官方应用市场",
    "com/googlecode/apdfviewer": "Google Docs PDF Viewer;谷歌PDF查看器",
    "com/jasonkostempski": "Jasonkostempski",
    "android/support/v4": "Android Support v4",
    "android/support/v7": "Android Support v7",
    "android/support/v13": "Android Support v13",
    "xamarin": "1;Xamarin;C# Android应用开发包",
    "opentk": "1;OpenTK;The Open Toolkit Library",
    "org/jsoup": "Jsoup;JSOUP Java HTML Parser",
    "com/ansca/corona": "Corona",
    "jsr166y": "JSR-166y Java",
    "pagerslidingtabstrip": "PagerSlidingTabStrip UI Framework",
    "aurelienribon": "AurelienRibon Animation Library",
    "android/opengl": "OpenGL",
    "com/google/zxing": "Google Zxing;谷歌Zxing",
    "com/facebook": "Facebook",
    "org/junit": "jUnit Java Unit Test",
    "bolts": "Bolts Base Library",
    "com/daggertech": "Dagger Tech",
    "dagger": "Dagger",
    "okio": "OkHttp okio Framework",
    "roboguice": "Roboguice",
    "com/onbarcode": "onbarcode",
    "rajawali/wallpaper": "rajawali WallPapper",
    "retrofit": "retrofit RESTful Library",
    "greendroid": "GreenDroid: Android UI Library",
    "nl/siegmann/epublib": "EPublib",
    "butterknife": "butterknife UI Framework",
    "pl/polidea": "Polidea",
    "com/pagecurl": "pagecurl",
    "flexjson": "FlexJson Library",
    "mono/twitter4j": "Mono Twitter",
    "twitter4j": "Twitter;推特",
    "com/maximono": "Maximono.com",
    "kawa": "Kawa for Android",
    "gnu/kawa" : "GNU KAWA",
    "javax": "0;javax",
    "com/amazonaws": "Amazon AWS;亚马逊云平台",
    "com/amazon": "Amazon;亚马逊",
    "pdftron": "Pdftron PDF Widget",
    "appmachine": "AppMachine App Generator",
    "microsoft/mappoint": "Microsoft MapPoint",
    "org/jdeferred": "Java jdeferred Library",
    "kankan/wheel": "Kankan Wheel Android scroller;仿iPhone滚轮控件 ",
    "org/slf4j": "SLF4J",
    "org/andengine": "Andengine Game Engine",
    "org/anddev/andengine": "Andengine Game Engine",
    "com/openfeint": "OpenFeint",
    "com/flurry": "Flurry",
    "com/aviary": "Aviary photo editing SDK",
    "com/scoreloop": "Scoreloop Game",
    "com/tencent/mm": "Tencent Wechat;微信",
    "com/tencent/map": "Tencent Map;腾讯地图",
    "com/tencent/lbs": "Tencent Map LBS;腾讯地图LBS",
    "com/tencent/mta": "Tencent MTA;腾讯云",
    "com/tencent/qzone": "Tencent Qzone;QQ空间",
    "com/tencent/mobwin": "Tencent MobWin;腾讯聚赢广告",
    "com/tencent/webnet": "Tencent WebNet;腾讯Webnet",
    "com/tencent/connect": "Tencent Login;腾讯互联",
    "com/tencent/qqconnect": "Tencent Login;腾讯互联",
    "com/tencent/tauth": "Tencent Login;腾讯互联",
    "com/tencent/open": "Tencent Login;腾讯互联",
    "com/tencent/jsutil": "Tencent Login;腾讯互联",
    "com/tencent/plus": "Tencent Login;腾讯互联",
    "com/tencent/utils": "Tencent Login;腾讯互联",
    "com/tencent/common": "Tencent Login;腾讯互联",
    "com/tencent/wpa": "Tencent WPA;腾讯WPA",
    "com/tencent/record": "Tencent Login;腾讯互联",
    "com/tencent/stat": "Tencent Analysis;腾讯云分析",
    "com/tencent/weiyun": "Tencent Weiyun;腾讯微云",
    "com/tencent/weibo": "Tencent Weibo;腾讯微博",
    "com/tencent/t": "Tencent Login;腾讯互联",
    "com/sina/weibo": "Sina Weibo;新浪微博",
    "com/sina/sso": "Sina SSO;新浪微博开放平台SSO授权",
    "net/sourceforge/pinyin4j": "Pinyin4j",
    "com/nostra13": "Nostra13 Image Loading;Nostra13图像加载",
    "com/appmakr": "Appmakr",
    "com/qoppa": "Qoppa Software",
    "biz/neoline": "Neoline",
    "org/apache/commons": "Apache Common",
    "org/apache/harmony": "Apache Harmony",
    "com/mopub/nativeads": "Native Ads",
    "org/hamcrest": "hamcrest",
    "org/fmod": "Fmod",
    "com/appflood": "appflood",
    "com/appbrain": "appbrain",
    "com/pollfish": "pollfish",
    "com/scarysd": "scarySD",
    "com/applovin": "applovin",
    "com/loopj": "Loopj",
    "com/urbanairship": "urbanairship",
    "com/startapp": "StartApp",
    "com/newrelic": "newrelic",
    "oauth/signpost": "Signpost Oauth;Signpost OAuth认证",
    "org/cocos2dx": "cocos2DX",
    "org/cocos2d": "cocos2D",
    "com/leadbolt": "Leadbolt",
    "com/mongodb": "mongoDB",
    "com/actionbarsherlock": "ActionBarSherlock",
    "org/htmlcleaner": "htmlCleaner",
    "com/subsplash": "subsplash",
    "org/dom4j": "Dom4j",
    "com/yixia": "Yixia",
    "com/inmobi": "Inmobi",
    "com/ngpinc/": "ngpinc",
    "anywheresoftware": "anywheresoftware",
    "org/kobjects/mime": "kobjects",
    "com/adobe/air": "Adobe Air",
    "com/adobe/fre": "Adobe Air FRE",
    "com/adobe/xmp": "Adobe XMP",
    "com/adobe/flashplayer": "Adobe FlashPlayer",
    "com/adobe/flashruntime": "Adobe FlashPlayer",
    "com/adobe/plugin": "Adobe plugin;Adobe插件",
    "com/parse": "Parse.com",
    "com/magtab": "Magtab",
    "org/appcelerator": "Appcelerator",
    "com/jirbo": "Jirbo",
    "org/mozilla": "Mozilla",
    "com/vercoop": "Vercoop",
    "com/phonegap": "PhoneGap",
    "com/appyet": "Appyet",
    "com/apache": "Apache",
    "com/millennialmedia": "millennialmedia",
    "net/sourceforge/zbar": "SourceForge ZBar",
    "com/papaya": "Papaya",
    "com/comscore": "comscore",
    "com/vpon": "Vpon",
    "de/greenrobot/dao": "GreenDao;轻量级ORM框架",
    "com/adwhirl": "Adwhirl Ads",
    "com/revmob": "Revmob",
    "com/kakao/talk": "Kakao",
    "com/viewpagerindicator": "Android Viewpagerindicator Widget",
    "org/kxml2": "Kxml2",
    "gnu/mapping": "GNU Mapping",
    "android/widget": "android widget",
    "com/mobfox": "mobfox",
    "gnu/xml": "GNU XML",
    "org/xmlpull": "XML Pull",
    "ti/map": "Ti Map",
    "com/deploygate": "com/deploygate",
    "com/dobao": "com/dobao",
    "com/crowdcompass": "crowdcompass",
    "com/slidingmenu": "SlidingMenu",
    "com/adtech": "Adtech",
    "org/codehaus": "Codehaus",
    "gnu/ecmascript": "ECMAScript",
    "com/doapps": "doapps",
    "gnu/commonlisp": "GNU Common Lisp",
    "org/jaxen": "Jaxen",
    "ti/imagefactory": "Titanium Image Factory",
    "org/acra": "ACRA",
    "com/smaato/SOMA": "Smaato",
    "com/bump": "Bump pay",
    "com/crowdcompass": "crowdcompass",
    "com/thirdparty": "Thirdparty",
    "com/badlogic": "badlogic",
    "com/github": "Github",
    "com/goodbarber": "goodbarber",
    "com/ironsource": "IronSource",
    "net/authorize": "Authorize.NET",
    "com/sun/mail": "Sun Mail.jar",
    "com/tapit": "Tapit;Tapit NFC技术",
    "com/conduit/app": "Conduit App",
    "com/samsung/spen": "Samsung Spen",
    "com/paypal":"PayPal",
    "com/fasterxml": "Fasterxml",
    "com/skplanet": "skplanet",
    "net/youmi": "Youmi",
    "com/chartboost/sdk": "ChartBoost",
    "com/doapps": "Doapps",
    "cn/domob": "domob",
    "com/astuetz": "Astuetz Pager Sliding Tab Strip",
    "com/naef/jnlua": "jnlua",
    "com/qwapi": "qwapi",
    "com/verizon": "Verizon",
    "com/spoledge": "Spoledge AAC Decoder",
    "com/esotericsoftware": "Esoteric Software 2D",
    "com/polites": "GestureImageView polites.com",
    "de/keyboardsurfer": "Keyboard Surfer",
    "org/scribe": "Scribe Java Lib",
    "com/j256": "J256",
    "com/inneractive": "Inneractive",
    "com/handmark": "handmark",
    "fr/castorfle": "castorfle Smooth Progress Bar",
    "com/jumptap": "移动广告服务商JumpTap",
    "com/bugsense": "BugSense",
    "com/espian/showcaseview": "Espian ShowcaseView",
    "me/kiip": "KIIP Mobile Ads",
    "com/myappengine": "myappengine",
    "com/qbiki": "qbiki",
    "com/huntmads": "HUNT Mobile Ads",
    "com/nuance": "Nuance Speech Kit Library",
    "com/mobeta": "Mobeta",
    "com/biznessapps": "biznessapps",
    "com/adfonic": "Adfonic Mobile Ads",
    "com/baidu/android/pushservice": "baidu push service",
    "com/baidu/mapapi/": "Baidu Map 百度地图",
    "com/baidu/mobstat": "Baidu Mobile Stat",
    "com/baidu/platform": "Baidu APP SDK",
    "com/baidu/location": "Baidu Location",
    "com/baidu/android": "Baidu APP SDK",
    "com/baidu/mobads": "Baidu Mobile Ads",
    "org/ksoap2": "ksoap2",
    "org/json": "Json org",
    "org/metalev/multitouch": "Metalev Multi Touch",
    "com/apperhand": "apperhand",
    "com/pocketchange/": "pocketchange",
    "com/unity3d": "Unity3D",
    "com/adsdk": "AdSDK",
    "com/alipay": "Alipay",
    "com/Tobit": "Tobit",
    "com/adsmogo": "adsmogo",
    "com/nineoldandroids": "Nine Old Androids;开源Android动画库",
    "v2/com/playhaven": "PlayHaven Mobile Ads",
    "com/playhaven": "PlayHaven Mobile Ads",
    "Appinventor": "appinventor",
    "com/google/appinventor": "Google Appinventor",
    "org/simpleframework": "simple framework",
    "com/amap": "Alibaba Amap;高德地图",
    "org/openudid": "OpenUDID Salama Generator",
    "org/vudroid": "Vudroid PDF Reader",
    "uk/co/senab/actionbarpulltorefresh": "actionbarpulltorefresh",
    "com/handmark/pulltorefresh": "pulltorefresh",
    "com/wm/pulltorefresh": "pulltorefresh",
    "com/vl/pulltorefresh": "pulltorefresh",
    "com/vjianke/pulltorefresh": "pulltorefresh",
    "com/nv/support/pulltorefresh": "pulltorefresh",
    "ti/modules/titanium": "Titanium-Modules",
    "org/kobjects": "KObjects",
    #"com/google": "Nope",
    #"com/google/android": "Nope",
    #"android": "Nope",
    #"org/apache": "Nope",
    #"android/support": "Nope",
    }

not_tagged = []

dep_max_list = {}

input = open(input_d, 'r')
output = open(output_d, 'w')
for line in input:
    i = json.loads(line)
    if len(i['pp'][0].split('/')) <= 4:
        if i['pp'][0] in dep_max_list:
            dep_max_list[i['pp'][0]] += i['dep_num']
        else:
            dep_max_list[i['pp'][0]] = i['dep_num']
    o = {'lib': ""}
    paths = i[u'pp']
    paths.reverse()
    for s_path in paths:
        s_lower = s_path.lower()
        for lib in lib_list:
            if lib in s_lower:
                o['lib'] = lib_list[lib]
                break
        if o['lib'] != "":
            break
    o['s_path'] = s_path
    o['b_hash'] = i['b_hash']
    o['b_total_num'] = i['b_total_num']
    o['b_total_call'] = i['b_total_call']
    if o['lib'] == "":
        if len(paths) > 10:
            o['paths'] = paths[:10]
        else:
            o['paths'] = paths
        o['dep_num'] = i['dep_num']
        not_tagged.append(o)
        # if i['dep_num'] > 2000 and i['dep_num'] <= 5000:
        #     print o
    output.write(json.dumps(o)+'\n')

out = open('../raw_data/top_libs.txt', 'w')
for i in sorted(dep_max_list.items(), key=lambda u: u[1], reverse=True):
    out.write(json.dumps(i) + '\n')
out.close()

'''
cnt = 0
for i in sorted(not_tagged, key=lambda u: u['dep_num'], reverse=True):
    cnt += 1
    if cnt > 200:
        break
    print i
    '''


input.close()
output.close()