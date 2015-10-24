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
    "com/google/android/gms": "da;Google GMS;https://developers.google.com/android/reference/com/google/android/gms/package-summary",
    "com/google/android/gcm": "da;Google GCM;https://developers.google.com/cloud-messaging/",
    "com/google/ads": "ad;Google Ads;https://www.google.com/ads/",
    "com/google/analysis": "ma;Google Analysis;https://www.google.com/analytics/",
    "com/google/analytics": "ma;Google Analytics;https://www.google.com/analytics/",
    "com/google/gson": "da;Google Gson;https://github.com/google/gson",
    "com/google/gdata": "da;Google GData;code.google.com/p/google-gdata/",
    "com/google/android/net": "da;Google Android Net;http://developer.android.com/reference/android/net/package-summary.html",
    "org/apache/http": "da;Apache Http;https://hc.apache.org/",
    "com/admob": "ad;Google Admob;https://www.google.com/admob/",
    "org/apache/cordova": "da;Apache Cordova;https://cordova.apache.org/",
    "org/apache/log4j": "da;Apache Log4j;http://logging.apache.org/log4j/2.x/",
    "org/apache/james": "da;Apache James Mail Enterprise Serve;http://james.apache.org",
    "com/squareup/timessquare": "da;timessquare;https://github.com/square/android-times-square",
    "com/squareup/assertj": "da;assertj;https://github.com/square/assertj-android",
    "com/squareup/okhttp": "da;OkHttp;https://github.com/square/okhttp",
    "com/squareup/picasso": "da;picasso;https://github.com/square/picasso",
    "com/squareup/dagger": "da;Dagger;http://square.github.io/dagger/",
    "com/squareup/otto": "da;otto;http://square.github.io/otto/",
    "com/squareup/pollexor": "da;pollexor;http://square.github.io/pollexor/",
    "com/squareup/spoon": "da;spoon;http://square.github.io/spoon/",
    "com/squareup/wire": "da;wire;https://github.com/square/wire",
    "com/squareup": "pa;SquareUp;https://squareup.com",
    "com/umeng/fb": "ma;Umeng feedback;dev.umeng.com/feedback",
    "com/umeng/analytics": "ma;Umeng Analytics;https://www.umeng.com/analytics",
    "com/umeng/common": "da;Umeng Common;http://dev.umeng.com/",
    "com/umeng/update": "da;Umeng Update;https://www.umeng.com/component_update",
    "com/umeng/social_analytic": "da;Umeng Social Analytic;dev.umeng.com/analytics",
    "com/android/vending": "am;Google Play;https://play.google.com",
    "com/google/android/vending": "am;Google Play;https://play.google.com",
    "com/googlecode/apdfviewer": "ut;Google Docs PDF Viewer;https://code.google.com/p/apdfviewer/source/browse/trunk/src/com/googlecode/apdfviewer/?r=3",
    "com/jasonkostempski": "ut;Jasonkostempski;https://github.com/jasonkostempski/",
    "android/support/v4": "da;Android Support v4;http://developer.android.com/reference/android/support/v4/app/package-summary.html",
    "android/support/v7": "da;Android Support v7;https://developer.android.com/reference/android/support/v7/app/package-summary.html",
    "android/support/v13": "da;Android Support v13;https://developer.android.com/reference/android/support/v13/app/package-summary.html",
    "xamarin": "da;Xamarin;https://xamarin.com/",
    "opentk": "da;The Open Toolkit Library;www.opentk.com/",
    "org/jsoup": "da;Jsoup;http://jsoup.org/",
    "com/ansca/corona": "da;Corona;https://docs.coronalabs.com/native/android/html/com/ansca/corona/package-summary.html",
    "jsr166y": "da;JSR-166y Java;http://g.oswego.edu/dl/concurrency-interest/",
    "pagerslidingtabstrip": "ui;PagerSlidingTabStrip UI Framework;https://github.com/astuetz/PagerSlidingTabStrip",
    "aurelienribon": "ut;AurelienRibon Animation Library;http://www.aurelienribon.com",
    "android/opengl": "ut;OpenGL;http://developer.android.com/reference/android/opengl/package-summary.html",
    "com/google/zxing": "da;ZXing ('Zebra Crossing');https://github.com/zxing/zxing",
    "com/facebook": "sn;Facebook;https://developers.facebook.com",
    "org/junit": "da;jUnit Java Unit Test;junit.org/",
    "bolts": "da;Bolts Base Library;https://github.com/BoltsFramework/Bolts-Android",
    "com/daggertech": "da;Dagger Tech;",
    "dagger": "da;Dagger;http://square.github.io/dagger/",
    "okio": "da;OkHttp okio Framework;https://github.com/square/okio",#Okio是一个新的Java库，它补充了java.io和java.nio库，让其更易于访问，存储和处理你的数据。
    "roboguice": "da;Roboguice;https://github.com/roboguice/roboguice",
    "com/onbarcode": "da;onbarcode;www.onbarcode.com/",
    "rajawali/wallpaper": "da;rajawali WallPapper;https://github.com/Rajawali/RajawaliWallpaperTemplate",
    "retrofit": "da;retrofit RESTful Library;square.github.io/retrofit/",#Retrofit  和Java领域的ORM概念类似， ORM把结构化数据转换为Java对象，而Retrofit 把REST API返回的数据转化为Java对象方便操作。同时还封装了网络代码的调用.
    "greendroid": "ui;GreenDroid;https://github.com/cyrilmottier/GreenDroid",
    "nl/siegmann/epublib": "da;EPublib;www.siegmann.nl/epublib",
    "butterknife": "ui;butterknife UI Framework;https://github.com/JakeWharton/butterknife",
    "pl/polidea": "da;Polidea;https://www.polidea.com/",
    "com/pagecurl": "ui;pagecurl;",
    "flexjson": "da;FlexJson Library;flexjson.sourceforge.net/",
    "mono/twitter4j": "sn;Mono Twitter;",
    "twitter4j": "sn;Twitter;twitter4j.org/",
    "com/maximono": "sn;Maximono;Maximono.com",
    "gnu/kawa" : "da;GNU KAWA;https://www.gnu.org/software/kawa/Building-for-Android.html",
    "kawa": "da;Kawa for Android;https://www.gnu.org/software/kawa/Building-for-Android.html",
    "javax": "da;javax;",
    "com/amazonaws": "ut;Amazon AWS;mvnrepository.com/artifact/com.amazonaws",
    "com/amazon": "ut;Amazon;",
    "pdftron": "ut;Pdftron PDF Widget;https://www.pdftron.com/",
    "appmachine": "da;AppMachine App Generator;www.appmachine.com/",
    "microsoft/mappoint": "mp;Microsoft MapPoint;www.microsoft.com/mappoint/",
    "org/jdeferred": "da;Java jdeferred Library;jdeferred.org/",
    "kankan/wheel": "ui;Kankan Wheel Android scroller;https://github.com/chemalarrea/Android-wheel/blob/master/wheel-demo/src/kankan/wheel/demo/DateActivity.java",
    "org/slf4j": "da;SLF4J;www.slf4j.org/",
    "org/andengine": "ge;Andengine Game Engine;www.andengine.org/",
    "org/anddev/andengine": "ge;Andengine Game Engine;www.andengine.org/",
    "com/openfeint": "ge;OpenFeint;",
    "com/flurry": "ma;Flurry;flurry.com",
    "com/aviary": "ut;Aviary photo editing SDK;https://developers.aviary.com/docs/android",
    "com/scoreloop": "ge;Scoreloop Game;",
    "com/tencent/mm": "sn;Tencent Wechat;https://open.weixin.qq.com/",
    "com/tencent/map": "mp;Tencent Map;lbs.qq.com/",
    "com/tencent/lbs": "mp;Tencent Map LBS;lbs.qq.com/",
    "com/tencent/mta": "ma;Tencent MTA;https://mta.qq.com/",
    "com/tencent/qzone": "sn;Tencent Qzone;",
    "com/tencent/mobwin": "ad;Tencent MobWin;",
    "com/tencent/webnet": "da;Tencent WebNet;",
    "com/tencent/connect": "sn;Tencent Login;connect.qq.com",
    "com/tencent/qqconnect": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/tauth": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/open": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/jsutil": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/plus": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/utils": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/common": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/wpa": "da;Tencent WPA;wiki.open.qq.com/wiki/mobile/API",
    "com/tencent/record": "sn;Tencent Login;wiki.open.qq.com/wiki/mobile/Android_SDK",
    "com/tencent/stat": "ma;Tencent Analysis;mta.qq.com/mta/wiki/index.php/Android快速指南",
    "com/tencent/weiyun": "ma;Tencent Weiyun;www.weiyun.com",
    "com/tencent/weibo": "sn;Tencent Weibo;t.qq.com",
    "com/tencent/t": "sn;Tencent Login;t.qq.com",
    "com/sina/weibo": "sn;Weibo;weibo.com/",
    "com/sina/sso": "sn;Sina SSO;open.weibo.com/",
    "net/sourceforge/pinyin4j": "ut;Pinyin4j;pinyin4j.sourceforge.net/",#得到拼音！
    "com/nostra13": "ut;Nostra13 Image Loading;https://github.com/nostra13/Android-Universal-Image-Loader",
    "com/appmakr": "da;Appmakr;https://www.appmakr.com/",
    "com/qoppa": "da;Qoppa Software;https://www.qoppa.com/",
    "biz/neoline": "da;Neoline;www.neoline.biz/",
    "org/apache/commons": "da;Apache Common;https://commons.apache.org/",
    "org/apache/harmony": "da;Apache Harmony;https://harmony.apache.org/",
    "com/mopub/nativeads": "ad;Native Ads;",
    "org/hamcrest": "da;hamcrest;hamcrest.org/",
    "org/fmod": "ge;Fmod;www.fmod.org/",
    "com/appflood": "ad;Appflood;appflood.com",
    "com/appbrain": "da;Appbrain;www.appbrain.com/",
    "com/pollfish": "da;Pollfish;https://www.pollfish.com/",
    "com/applovin": "ad;Applovin;https://www.applovin.com/",
    "com/loopj": "da;Loopj;https://github.com/loopj/android-async-http",
    "com/urbanairship": "ui;urbanairship;https://www.urbanairship.com/",#推送通知栏用的
    "com/startapp": "ad;StartApp;www.startapp.com/",
    "com/newrelic": "da;newrelic;newrelic.com/",
    "oauth/signpost": "da;Signpost Oauth;https://code.google.com/p/oauth-signpost/",
    "org/cocos2dx": "ge;cocos2DX;www.cocos2d-x.org/",#cocos2d是一个基于MIT协议的开源框架，用于构建游戏、应用程序和其他图形界面交互应用
    "org/cocos2d": "ge;cocos2D;www.cocos2d-x.org/",
    "com/leadbolt": "da;Leadbolt;https://www.leadbolt.com/",
    "com/mongodb": "da;mongoDB;http://mongodb.github.io/mongo-java-driver/2.13/getting-started/quick-tour/",
    "com/actionbarsherlock": "da;ActionBarSherlock;actionbarsherlock.com/",
    "org/htmlcleaner": "da;htmlCleaner;http://htmlcleaner.sourceforge.net",#文档解析器,解析html
    "org/dom4j": "da;Dom4j;dom4j.sourceforge.net/",#解析xml
    "com/subsplash": "da;subsplash;www.subsplash.com/",
    "com/yixia": "da;Yixia;www.yixia.com/",
    "com/inmobi": "ad;Inmobi;http://inmobi.com",#印度最大的移动广告公司
    "com/ngpinc/": "ma;ngpinc:National Guard Products;www.ngpinc.com/",
    "anywheresoftware": "ut;anywheresoftware;",
    "org/kobjects/mime": "da;kobjects;",
    "com/adobe/air": "da;Adobe Air;www.adobe.com/cn/devnet/air/air_for_android.html",
    "com/adobe/fre": "da;Adobe Air FRE;www.adobe.com/cn/devnet/air/air_for_android.html",
    "com/adobe/xmp": "da;Adobe XMP;www.adobe.com/products/xmp.html",
    "com/adobe/flashplayer": "da;Adobe FlashPlayer;",
    "com/adobe/flashruntime": "da;Adobe FlashPlayer;",
    "com/adobe/plugin": "da;Adobe plugin;",
    "com/parse": "ma;Parse.com;https://parse.com/docs/cn/android/guide",
    "com/magtab": "ut;Magtab;https://www.magtab.com/",
    "org/appcelerator": "da;Appcelerator;www.appcelerator.org/",
    "com/jirbo": "da;Jirbo;www.jirbo.com/",
    "org/mozilla": "da;Mozilla;https://www.mozilla.org/",
    "com/vercoop": "da;Vercoop;www.vercoop.com/",
    "com/phonegap": "da;PhoneGap;phonegap.com/",
    "com/appyet": "da;Appyet;www.appyet.com/",
    "com/millennialmedia": "ad;millennialmedia;www.millennialmedia.com/",#移动广告平台
    "net/sourceforge/zbar": "ut;SourceForge ZBar;zbar.sourceforge.net/",#获取条形码和二维码
    "com/papaya": "ut;Papaya;en.papayamobile.com/",
    "com/comscore": "da;comscore;www.comscore.com/",#互联网市场调研
    "com/vpon": "ad;Vpon;www.vpon.com/",
    "de/greenrobot/dao": "da;GreenDao;https://github.com/greenrobot/greenDAO",
    "com/adwhirl": "ad;Adwhirl Ads;code.google.com/p/adwhirl/",
    "com/revmob": "ad;Revmob;https://www.revmobmobileadnetwork.com/",
    "com/kakao/talk": "sn;Kakao;https://developers.kakao.com/",
    "com/viewpagerindicator": "da;Android Viewpagerindicator Widget;https://github.com/JakeWharton/ViewPagerIndicator",
    "org/kxml2": "da;Kxml2;www.kxml.org/",#解析xml
    "gnu/mapping": "da;GNU Mapping;www.gnu.org/s/kawa/api/gnu/mapping/package-summary.html",
    "android/widget": "ui;android widget;",
    "com/mobfox": "da;mobfox;www.mobfox.com/",
    "gnu/xml": "da;GNU XML;www.gnu.org/s/kawa/api/gnu/xml/package-summary.html",
    "org/xmlpull": "da;XML Pull;www.xmlpull.org/",
    "ti/map": "mp;Ti Map;https://github.com/appcelerator-modules/ti.map",
    "com/deploygate": "da;com/deploygate;https://deploygate.com/",
    "com/dobao": "ut;com/dobao;",
    "com/crowdcompass": "da;crowdcompass;www.crowdcompass.com/",
    "com/slidingmenu": "ui;SlidingMenu;https://github.com/jfeinstein10/SlidingMenu",
    "com/adtech": "ad;Adtech;www.adtech.com/",
    "org/codehaus": "da;Codehaus;www.codehaus.org/",
    "gnu/ecmascript": "da;ECMAScript;www.gnu.org/s/kawa/api/gnu/ecmascript/package-frame.html",
    "com/doapps": "da;doapps;www.doapps.com/",
    "gnu/commonlisp": "da;GNU Common Lisp;www.gnu.org/s/gcl/",
    "org/jaxen": "da;Jaxen;jaxen.org/",
    "ti/imagefactory": "da;Titanium Image Factory;https://github.com/appcelerator-modules/ti.imagefactory",
    "org/acra": "da;ACRA;",
    "com/smaato/SOMA": "ad;Smaato;https://www.smaato.com/",
    "com/bump": "pa;Bump pay;",
    "com/crowdcompass": "da;crowdcompass;www.crowdcompass.com/",
    "com/thirdparty": "da;Thirdparty;thirdparty.com/",
    "com/badlogic": "ge;badlogic;www.badlogicgames.com/",
    "com/github": "da;Github;https://github.com/",
    "com/goodbarber": "ui;goodbarber;www.goodbarber.com/",
    "com/ironsource": "da;IronSource;www.ironsrc.com",
    "net/authorize": "da;Authorize.NET;www.authorize.net/",
    "com/sun/mail": "ut;Sun Mail.jar;",
    "com/tapit": "ut;Tapit;Tapit NFC技术",
    "com/conduit/app": "da;Conduit App;apps.conduit.com/",
    "com/samsung/spen": "ui;Samsung Spen;developer.samsung.com/galaxy",
    "com/paypal":"pa;PayPal;https://developer.paypal.com/docs/integration/mobile/android-integration-guide/",
    "com/fasterxml": "da;Fasterxml;fasterxml.com/",
    "com/skplanet": "ut;skplanet;www.skplanet.com",
    "net/youmi": "sn;Youmi Ads;www.youmi.net/",
    "com/chartboost/sdk": "ad;ChartBoost;www.chartboost.com/ ",
    "cn/domob": "ad;domob;www.domob.cn/",
    "com/astuetz": "ui;Astuetz Pager Sliding Tab Strip;https://github.com/astuetz",
    "com/naef/jnlua": "da;jnlua;Java Lua 互联工具",#With JNLua, you can access Java from Lua and Lua from Java.
    "com/qwapi": "da;qwapi;",
    "com/verizon": "ut;Verizon;https://www.verizon.com/",
    "com/spoledge": "ut;Spoledge AAC Decoder;https://code.google.com/p/aacdecoder-android/",
    "com/esotericsoftware": "ut;Esoteric Software 2D;https://github.com/EsotericSoftware",
    "com/polites": "ui;GestureImageView polites.com;polites.com",
    "de/keyboardsurfer": "ui;Keyboard Surfer;https://github.com/keyboardsurfer",
    "org/scribe": "da;Scribe Java Lib;https://github.com/scribejava/scribejava",
    "com/j256": "da;J256;https://github.com/j256/ormlite-android",
    "com/inneractive": "ad;Inneractive;inner-active.com/",
    "com/handmark": "ui;handmark;https://github.com/chrisbanes/Android-PullToRefresh",#下拉刷新
    "fr/castorfle": "ui;castorfle Smooth Progress Bar;https://github.com/castorflex/SmoothProgressBar",
    "com/jumptap": "ad;jumptap;jumptap.com/",
    "com/bugsense": "da;BugSense;https://github.com/wrapp/bugsense-android",
    "com/espian/showcaseview": "ui;Espian ShowcaseView;https://github.com/arianvp/ShowcaseView",
    "me/kiip": "ad;KIIP Mobile Ads;www.kiip.me/",
    "com/myappengine": "eg;myappengine;https://appengine.google.com/",
    "com/huntmads": "ad;HUNT Mobile Ads;www.huntmads.com/",
    "com/nuance": "ut;Nuance Speech Kit Library;nuance.com/",
    "com/mobeta": "ui;Mobeta ListView;https://github.com/bauerca/drag-sort-listview",
    "com/biznessapps": "da;biznessapps;https://www.biznessapps.com/",
    "com/adfonic": "ad;Adfonic Mobile Ads;http://www.adfonic.com",
    "com/baidu/android/pushservice": "da;baidu push service;developer.baidu.com",
    "com/baidu/mapapi/": "mp;Baidu Map;lbsyun.baidu.com/",
    "com/baidu/mobstat": "ma;Baidu Mobile Stat;developer.baidu.com/",
    "com/baidu/platform": "da;Baidu APP SDK;developer.baidu.com/",
    "com/baidu/location": "mp;Baidu Location;developer.baidu.com/",
    "com/baidu/android": "da;Baidu APP SDK;developer.baidu.com/",
    "com/baidu/mobads": "ad;Baidu Mobile Ads;developer.baidu.com/",
    "org/ksoap2": "da;ksoap2;ksoap2.sourceforge.net/",
    "org/json": "da;Json org;www.json.org/",
    "org/metalev/multitouch": "ui;Metalev Multi Touch;https://code.google.com/p/android-multitouch-controller/",
    "com/apperhand": "ad;apperhand;",
    "com/pocketchange/": "pa;pocketchange;www.pocketchange.com/",
    "com/unity3d": "ge;Unity3D;https://unity3d.com/",
    "com/adsdk": "ad;AdSDK;",
    "com/alipay": "pa;Alipay;https://dev.alipay.com/",
    "com/Tobit": "da;Tobit;",
    "com/adsmogo": "ad;adsmogo;www.adsmogo.com/",
    "com/nineoldandroids": "ut;Nine Old Androids;https://github.com/JakeWharton/NineOldAndroids",
    "v2/com/playhaven": "ad;PlayHaven Mobile Ads;www.playhaven.com/",
    "com/playhaven": "ad;PlayHaven Mobile Ads;www.playhaven.com/",
    "com/google/appinventor": "da;Google Appinventor;https://code.google.com/p/app-inventor-for-android/",
    "appinventor": "da;Appinventor;appinventor.mit.edu/",
    "org/simpleframework": "da;simple framework;www.simpleframework.org/",
    "com/amap": "mp;Alibaba Amap;lbs.amap.com/",
    "org/openudid": "da;OpenUDID Salama Generator;https://github.com/vieux/OpenUDID",
    "org/vudroid": "ut;Vudroid PDF Reader;",
    "uk/co/senab/actionbarpulltorefresh": "ui;actionbarpulltorefresh;https://github.com/chrisbanes/ActionBar-PullToRefresh",#上拉效果,下拉效果
    "com/handmark/pulltorefresh": "ui;pulltorefresh;https://github.com/chrisbanes/Android-PullToRefresh",#上拉效果,下拉效果
    "com/wm/pulltorefresh": "ui;pulltorefresh;",
    "com/vl/pulltorefresh": "ui;pulltorefresh;",
    "com/vjianke/pulltorefresh": "ui;pulltorefresh;",
    "com/nv/support/pulltorefresh": "ui;pulltorefresh;",
    "ti/modules/titanium": "da;Titanium-Modules;",
    "org/kobjects": "da;KObjects;http://kobjects.org",  # 可拆分
    #"com/google": "Nope",
    #"com/google/android": "Nope",
    #"android": "Nope",
    #"org/apache": "Nope",
    #"android/support": "Nope",
    }

not_tagged = []

dep_max_list = {}


for ii in lib_list:
    if len(lib_list[ii].split(';')) > 3:
        print ii
        exit()
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
