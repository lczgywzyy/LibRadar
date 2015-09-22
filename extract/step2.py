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

Type = {
    "da": "Development Aid",
    "sn": "Social Network",
    "ad": "Advertisement",
    "am": "App Market",
    "ma": "Mobile Analytics",
    "pa": "Payment",
    "ui": "UI Component",
    "ge": "Game Engine",
    "ut": "Utility",
    "mp": "Map"
}

lib_list = {
    "com/google/android/gms": "da;Google GMS;谷歌GMS",
    "com/google/android/gcm": "da;Google GCM;谷歌GCM",
    "com/google/ads": "ad;Google Ads;谷歌广告",
    "com/google/analysis": "ma;Google Analysis;谷歌分析",
    "com/google/gson": "da;Google Gson;谷歌Gson",
    "com/google/gdata": "da;Google GData;谷歌Gdata",
    "com/google/android/net": "da;Google Android Net",
    "com/google/analytics": "ma;Google Analysis",
    "org/apache/http": "da;Apache Http;阿帕奇HTTP",
    "com/admob": "ad;Google Ads;谷歌广告",
    "org/apache/cordova": "da;Apache Cordova",
    "org/apache/log4j": "da;Apache Log4j;阿帕奇Java日志工具",
    "org/apache/james": "da;Apache James Mail Enterprise Serve;阿帕奇James邮件系统",
    "com/squareup": "pa;SquareUp;SquareUp 移动支付",
    "com/umeng/fb": "ma;Umeng feedback;友盟反馈SDK",
    "com/umeng/analytics": "ma;Umeng Analytics;友盟分析",
    "com/umeng/common": "da;Umeng Common;友盟Common",
    "com/umeng/update": "da;Umeng Update;友盟自动更新",
    "com/umeng/social_analytic": "da;Umeng Social Analytic;友盟社会化分析",
    "com/android/vending": "am;Google Play;谷歌官方应用市场",
    "com/google/android/vending": "am;Google Play;谷歌官方应用市场",
    "com/googlecode/apdfviewer": "ut;Google Docs PDF Viewer;谷歌PDF查看器",
    "com/jasonkostempski": "ut;Jasonkostempski",
    "android/support/v4": "da;Android Support v4;Android支持库v4",
    "android/support/v7": "da;Android Support v7;Android支持库v7",
    "android/support/v13": "da;Android Support v13;Android支持库v13",
    "xamarin": "da;Xamarin;C# Android应用开发包",
    "opentk": "da;OpenTK;The Open Toolkit Library",
    "org/jsoup": "da;Jsoup;JSOUP Java HTML Parser",
    "com/ansca/corona": "da;Corona",
    "jsr166y": "da;JSR-166y Java",
    "pagerslidingtabstrip": "ui;PagerSlidingTabStrip UI Framework",
    "aurelienribon": "ut;AurelienRibon Animation Library",
    "android/opengl": "ut;OpenGL",
    "com/google/zxing": "da;Google Zxing;谷歌Zxing",
    "com/facebook": "sn;Facebook",
    "org/junit": "da;jUnit Java Unit Test",
    "bolts": "da;Bolts Base Library",
    "com/daggertech": "da;Dagger Tech",
    "dagger": "da;Dagger",
    "okio": "da;OkHttp okio Framework",#Okio是一个新的Java库，它补充了java.io和java.nio库，让其更易于访问，存储和处理你的数据。
    "roboguice": "da;Roboguice",
    "com/onbarcode": "da;onbarcode",
    "rajawali/wallpaper": "da;rajawali WallPapper",
    "retrofit": "da;retrofit RESTful Library",#Retrofit  和Java领域的ORM概念类似， ORM把结构化数据转换为Java对象，而Retrofit 把REST API返回的数据转化为Java对象方便操作。同时还封装了网络代码的调用.
    "greendroid": "ui;GreenDroid: Android UI Library",
    "nl/siegmann/epublib": "da;EPublib",
    "butterknife": "ui;butterknife UI Framework",
    "pl/polidea": "da;Polidea",
    "com/pagecurl": "ui;pagecurl",
    "flexjson": "da;FlexJson Library",
    "mono/twitter4j": "sn;Mono Twitter",
    "twitter4j": "sn;Twitter;推特",
    "com/maximono": "sn;Maximono.com",
    "kawa": "da;Kawa for Android",
    "gnu/kawa" : "da;GNU KAWA",
    "javax": "da;javax;JavaX开发库",
    "com/amazonaws": "ut;Amazon AWS;亚马逊云平台",
    "com/amazon": "ut;Amazon;亚马逊",
    "pdftron": "ut;Pdftron PDF Widget",
    "appmachine": "da;AppMachine App Generator",
    "microsoft/mappoint": "mp;Microsoft MapPoint",
    "org/jdeferred": "da;Java jdeferred Library",
    "kankan/wheel": "ui;Kankan Wheel Android scroller;仿iPhone滚轮控件 ",
    "org/slf4j": "da;SLF4J",
    "org/andengine": "ge;Andengine Game Engine",
    "org/anddev/andengine": "ge;Andengine Game Engine",
    "com/openfeint": "ge;OpenFeint",
    "com/flurry": "ma;Flurry",
    "com/aviary": "ut;Aviary photo editing SDK",
    "com/scoreloop": "ge;Scoreloop Game",
    "com/tencent/mm": "sn;Tencent Wechat;微信",
    "com/tencent/map": "mp;Tencent Map;腾讯地图",
    "com/tencent/lbs": "mp;Tencent Map LBS;腾讯地图LBS",
    "com/tencent/mta": "ma;Tencent MTA;腾讯云",
    "com/tencent/qzone": "sn;Tencent Qzone;QQ空间",
    "com/tencent/mobwin": "ad;Tencent MobWin;腾讯聚赢广告",
    "com/tencent/webnet": "da;Tencent WebNet;腾讯Webnet",
    "com/tencent/connect": "sn;Tencent Login;腾讯互联",
    "com/tencent/qqconnect": "sn;Tencent Login;腾讯互联",
    "com/tencent/tauth": "sn;Tencent Login;腾讯互联",
    "com/tencent/open": "sn;Tencent Login;腾讯互联",
    "com/tencent/jsutil": "sn;Tencent Login;腾讯互联",
    "com/tencent/plus": "sn;Tencent Login;腾讯互联",
    "com/tencent/utils": "sn;Tencent Login;腾讯互联",
    "com/tencent/common": "sn;Tencent Login;腾讯互联",
    "com/tencent/wpa": "da;Tencent WPA;腾讯WPA",
    "com/tencent/record": "sn;Tencent Login;腾讯互联",
    "com/tencent/stat": "ma;Tencent Analysis;腾讯云分析",
    "com/tencent/weiyun": "ma;Tencent Weiyun;腾讯微云",
    "com/tencent/weibo": "sn;Tencent Weibo;腾讯微博",
    "com/tencent/t": "sn;Tencent Login;腾讯互联",
    "com/sina/weibo": "sn;Sina Weibo;新浪微博",
    "com/sina/sso": "sn;Sina SSO;新浪微博开放平台SSO授权",
    "net/sourceforge/pinyin4j": "ut;Pinyin4j",#得到拼音！
    "com/nostra13": "ut;Nostra13 Image Loading;Nostra13图像加载",
    "com/appmakr": "da;Appmakr",
    "com/qoppa": "da;Qoppa Software",
    "biz/neoline": "da;Neoline",
    "org/apache/commons": "da;Apache Common",
    "org/apache/harmony": "da;Apache Harmony",
    "com/mopub/nativeads": "ad;Native Ads",
    "org/hamcrest": "da;hamcrest",
    "org/fmod": "ge;Fmod;Fmod游戏引擎",
    "com/appflood": "ad;Appflood;Appflood广告",
    "com/appbrain": "da;Appbrain",
    "com/pollfish": "da;Pollfish",
    "com/scarysd": "da;ScarySD",
    "com/applovin": "ad;Applovin",
    "com/loopj": "da;Loopj",
    "com/urbanairship": "ui;urbanairship",#推送通知栏用的
    "com/startapp": "ad;StartApp",
    "com/newrelic": "da;newrelic",
    "oauth/signpost": "da;Signpost Oauth;Signpost OAuth认证",
    "org/cocos2dx": "ge;cocos2DX",#cocos2d是一个基于MIT协议的开源框架，用于构建游戏、应用程序和其他图形界面交互应用
    "org/cocos2d": "ge;cocos2D",
    "com/leadbolt": "da;Leadbolt",
    "com/mongodb": "da;mongoDB",
    "com/actionbarsherlock": "da;ActionBarSherlock",
    "org/htmlcleaner": "da;htmlCleaner",#文档解析器,解析html
    "org/dom4j": "da;Dom4j;XML解析工具",#解析xml
    "com/subsplash": "da;subsplash",
    "com/yixia": "da;Yixia",
    "com/inmobi": "ad;Inmobi",#印度最大的移动广告公司
    "com/ngpinc/": "ma;ngpinc",
    "anywheresoftware": "ut;anywheresoftware",
    "org/kobjects/mime": "da;kobjects",
    "com/adobe/air": "da;Adobe Air",
    "com/adobe/fre": "da;Adobe Air FRE",
    "com/adobe/xmp": "da;Adobe XMP",
    "com/adobe/flashplayer": "da;Adobe FlashPlayer",
    "com/adobe/flashruntime": "da;Adobe FlashPlayer",
    "com/adobe/plugin": "da;Adobe plugin;Adobe插件",
    "com/parse": "ma;Parse.com",
    "com/magtab": "ut;Magtab",
    "org/appcelerator": "da;Appcelerator",
    "com/jirbo": "da;Jirbo",
    "org/mozilla": "da;Mozilla",
    "com/vercoop": "da;Vercoop",
    "com/phonegap": "da;PhoneGap",
    "com/appyet": "da;Appyet",
    "com/apache": "da;Apache",
    "com/millennialmedia": "ad;millennialmedia",#移动广告平台
    "net/sourceforge/zbar": "ut;SourceForge ZBar",#获取条形码和二维码
    "com/papaya": "ut;Papaya",
    "com/comscore": "da;comscore",#互联网市场调研
    "com/vpon": "ad;Vpon",
    "de/greenrobot/dao": "da;GreenDao;轻量级ORM框架",
    "com/adwhirl": "ad;Adwhirl Ads",
    "com/revmob": "ad;Revmob",
    "com/kakao/talk": "sn;Kakao;韩国最著名的社交平台",
    "com/viewpagerindicator": "da;Android Viewpagerindicator Widget",
    "org/kxml2": "da:Kxml2;XML解析工具",#解析xml
    "gnu/mapping": "da;GNU Mapping",
    "android/widget": "ui;android widget",
    "com/mobfox": "da;mobfox",
    "gnu/xml": "da;GNU XML",
    "org/xmlpull": "da;XML Pull",
    "ti/map": "mp;Ti Map",
    "com/deploygate": "da;com/deploygate",
    "com/dobao": "ut;com/dobao",
    "com/crowdcompass": "da;crowdcompass",
    "com/slidingmenu": "ui;SlidingMenu",
    "com/adtech": "ad;Adtech",
    "org/codehaus": "da;Codehaus",
    "gnu/ecmascript": "da;ECMAScript",
    "com/doapps": "da;doapps",
    "gnu/commonlisp": "da;GNU Common Lisp",
    "org/jaxen": "da;Jaxen",
    "ti/imagefactory": "da;Titanium Image Factory",
    "org/acra": "da;ACRA",
    "com/smaato/SOMA": "ad;Smaato",
    "com/bump": "pa;Bump pay",
    "com/crowdcompass": "da;crowdcompass",
    "com/thirdparty": "da;Thirdparty",
    "com/badlogic": "ge;badlogic",
    "com/github": "da;Github",
    "com/goodbarber": "ui;goodbarber",
    "com/ironsource": "da;IronSource",
    "net/authorize": "da;Authorize.NET",
    "com/sun/mail": "ut;Sun Mail.jar",
    "com/tapit": "ut;Tapit;Tapit NFC技术",
    "com/conduit/app": "da;Conduit App",
    "com/samsung/spen": "ui;Samsung Spen;三星 SPEN",
    "com/paypal":"pa;PayPal;PayPal支付",
    "com/fasterxml": "da;Fasterxml",
    "com/skplanet": "ut;skplanet",
    "net/youmi": "sn;Youmi",
    "com/chartboost/sdk": "ad;ChartBoost",
    "com/doapps": "da;Doapps;Doapps统计",
    "cn/domob": "ad;domob;Domob广告",
    "com/astuetz": "ui;Astuetz;Astuetz Pager Sliding Tab Strip",
    "com/naef/jnlua": "da;jnlua;Java Lua 互联工具",#With JNLua, you can access Java from Lua and Lua from Java.
    "com/qwapi": "da;qwapi",
    "com/verizon": "ut;Verizon;地平线",
    "com/spoledge": "ut;Spoledge AAC Decoder;音频解析",
    "com/esotericsoftware": "ut;Esoteric Software 2D;Esoteric 2D",
    "com/polites": "ui;GestureImageView polites.com;手势效果",
    "de/keyboardsurfer": "ui;Keyboard Surfer",
    "org/scribe": "da;Scribe Java Lib",
    "com/j256": "da;J256",
    "com/inneractive": "ad;Inneractive",
    "com/handmark": "ui;handmark;HandMark下拉刷新",#下拉刷新
    "fr/castorfle": "ui;castorfle Smooth Progress Bar",
    "com/jumptap": "ad;移动广告服务商JumpTap",
    "com/bugsense": "da;BugSense",
    "com/espian/showcaseview": "ui;Espian ShowcaseView",
    "me/kiip": "ad;KIIP Mobile Ads;KIIP移动广告",
    "com/myappengine": "eg;myappengine",
    "com/huntmads": "ad;HUNT Mobile Ads;HUNT移动广告",
    "com/nuance": "ut;Nuance Speech Kit Library",
    "com/mobeta": "ui;Mobeta ListView;可拖拽listview DragSortListView",
    "com/biznessapps": "da;biznessapps",
    "com/adfonic": "ad;Adfonic Mobile Ads",
    "com/baidu/android/pushservice": "da;baidu push service",
    "com/baidu/mapapi/": "mp;Baidu Map;百度地图",
    "com/baidu/mobstat": "ma;Baidu Mobile Stat",
    "com/baidu/platform": "da;Baidu APP SDK",
    "com/baidu/location": "mp;Baidu Location",
    "com/baidu/android": "da;Baidu APP SDK",
    "com/baidu/mobads": "ad;Baidu Mobile Ads",
    "org/ksoap2": "da;ksoap2",
    "org/json": "da;Json org",
    "org/metalev/multitouch": "ui;Metalev Multi Touch",
    "com/apperhand": "ad;apperhand",
    "com/pocketchange/": "pa;pocketchange",
    "com/unity3d": "ge;Unity3D",
    "com/adsdk": "ad;AdSDK",
    "com/alipay": "pa;Alipay",
    "com/Tobit": "da;Tobit",
    "com/adsmogo": "ad;adsmogo",
    "com/nineoldandroids": "ut;Nine Old Androids;开源Android动画库",
    "v2/com/playhaven": "ad;PlayHaven Mobile Ads",
    "com/playhaven": "ad;PlayHaven Mobile Ads",
    "appinventor": "da;Appinventor",
    "com/google/appinventor": "da;Google Appinventor",
    "org/simpleframework": "da;simple framework",
    "com/amap": "mp;Alibaba Amap;高德地图",
    "org/openudid": "da;OpenUDID Salama Generator",
    "org/vudroid": "ut;Vudroid PDF Reader",
    "uk/co/senab/actionbarpulltorefresh": "ui;actionbarpulltorefresh",#上拉效果,下拉效果
    "com/handmark/pulltorefresh": "ui;pulltorefresh",#上拉效果,下拉效果
    "com/wm/pulltorefresh": "ui;pulltorefresh",
    "com/vl/pulltorefresh": "ui;pulltorefresh",
    "com/vjianke/pulltorefresh": "ui;pulltorefresh",
    "com/nv/support/pulltorefresh": "ui;pulltorefresh",
    "ti/modules/titanium": "da;Titanium-Modules",
    "org/kobjects": "da;KObjects",
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
                o['pn'] = lib # package name
                break
        if o['lib'] != "":
            break
    o['sp'] = s_path  # sp: s_path
    o['bh'] = i['b_hash']  # bh: b_hash
    o['btn'] = i['b_total_num']     # btn: b_total_num
    o['btc'] = i['b_total_call']   # btc: b_total_call
    o['dn'] = i['dep_num'] # dn:dep_num
    if o['lib'] == "":
        if len(paths) > 10:
            o['ps'] = paths[:10]    # ps: paths
        else:
            o['ps'] = paths
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
