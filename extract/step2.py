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
    "com/google/android/gms": "Google GMS",
    "com/google/android/gcm": "Google GCM",
    "com/google/ads": "Google Ads",
    "com/google/analysis": "Google Analysis",
    "com/google/gson": "Google Gson",
    "com/google/gdata": "Google GData",
    "com/google/android/net": "Google Android Net",
    "org/apache/http": "Apache Http",
    "com/admob": "Google Ads",
    "org/apache/cordova": "Apache Cordova",
    "org/apache/log4j": "Apache Log4j",
    "org/apache/james": "Apache James",
    "com/squareup": "SquareUp",
    "umeng": "Umeng",
    "com/android/vending": "Google Play",
    "com/google/android/vending": "Google Play",
    "googlecode/apdfviewer": "Google Docs PDF Viewer",
    "com/jasonkostempski": "Jasonkostempski",
    "android/support/v4": "Android Support v4",
    "android/support/v7": "Android Support v7",
    "android/support/v13": "Android Support v13",
    "xamarin": "Xamarin",
    "opentk": "OpenTK",
    "admob": "Admob",
    "org/jsoup": "Jsoup",
    "corona": "Corona",
    "jsr166y": "JSR-166y Java",
    "pagerslidingtabstrip": "PagerSlidingTabStrip UI Framework",
    "aurelienribon": "AurelienRibon Animation Library",
    "opengl": "OpenGL",
    "com/google/zxing": "Zxing",
    "com/facebook": "Facebook",
    "junit": "jUnit Java Unit Test",
    "bolts": "Bolts Base Library",
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
    "twitter": "Twitter",
    "mono": "Mono",
    "kawa": "Kawa for Android",
    "javax": "javax",
    "amazon": "Amazon",
    "pdftron": "PDF Widget",
    "appmachine": "AppMachine App Generator",
    "microsoft/mappoint": "Microsoft MapPoint",
    "jdeferred": "Java jdeferred Library",
    "kankan/wheel": "仿iPhone滚轮控件 Android scroller",
    "org/slf4j": "SLF4J",
    "andengine": "Andengine Game Engine",
    "openfeint": "OpenFeint",
    "flurry": "Flurry",
    "aviary": "Aviary photo editing SDK",
    "com/scoreloop": "Scoreloop Game",
    "com/tencent/mm": "Tencent Wechat",
    "weibo": "Weibo",
    "pinyin4j": "Pinyin4j",
    "nostra13": "Nostra13 Image Loading",
    "appmakr": "Appmakr",
    "qoppa": "Qoppa Software",
    "neoline": "Neoline",
    "org/apache/commons": "Apache Common",
    "com/mopub/nativeads": "Native Ads",
    "openuidi": "OpenUDID",
    "datamodel/v5": "Datamodel v5",
    "hamcrest": "hamcrest",
    "org/fmod": "Fmod",
    "appflood": "appflood",
    "appbrain": "appbrain",
    "pollfish": "pollfish",
    "scarysd": "scarySD",
    "applovin": "applovin",
    "com/loopj": "Loopj",
    "urbanairship": "urbanairship",
    "startapp": "StartApp",
    "newrelic": "newrelic",
    "startapp": "startapp",
    "cocos2d": "cocos2d",
    "leadbolt": "Leadbolt",
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
    "com/adobe": "Adobe",
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
    "adtech": "Adtech",
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
    "com/tapit": "Tapit",
    "com/conduit/app": "Conduit App",
    "com/samsung/spen": "Spen",
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
    "actionbarpulltorefresh": "actionbarpulltorefresh",
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
    "sina/sso": "Sina SSO",
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
    "metalev/multitouch": "Metalev Multi Touch",
    "com/apperhand": "apperhand",
    "com/pocketchange/": "pocketchange",
    "com/unity3d": "Unity3D",
    "com/adsdk": "AdSDK",
    "com/alipay": "Alipay",
    "com/Tobit": "Tobit",
    "com/adsmogo": "adsmogo",
    "nineoldandroids": "Nine Old Androids",
    "Playhaven": "PlayHaven Mobile Ads",
    "Appinventor": "appinventor",
    "org/simpleframework": "simple framework",
    "com/amap": "高德地图",
    "org/openudid": "Salama Generator",
    "org/vudroid": "Vudroid Reader",
    "com/google/analytics": "Google Analysis",
    "pulltorefresh": "pulltorefresh",
    "ti/modules/titanium": "Titanium-Modules",
    "org/kobjects": "KObjects",
    #"com/google": "Nope",
    #"com/google/android": "Nope",
    #"android": "Nope",
    #"org/apache": "Nope",
    #"android/support": "Nope",
    }

not_tagged = []

input = open(input_d, 'r')
output = open(output_d, 'w')
for line in input:
    i = json.loads(line)
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
        if i['dep_num'] > 2000 and i['dep_num'] <= 5000:
            print o
    output.write(json.dumps(o)+'\n')

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