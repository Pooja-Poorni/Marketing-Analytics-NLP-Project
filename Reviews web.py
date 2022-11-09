import pandas as pd
from tqdm import tqdm
from google_play_scraper import Sort, reviews, app

app_packages = [
   'com.dts.freefiremax',                                           # Action Game
   'com.squareenix.relicrun',              
   'com.horus.beach.head',
   'com.generagames.resistance',
   'com.byril.stickmanarcher',
   'com.madfingergames.unkilled',
   'com.ea.gp.apexlegendsmobilefps',
   'com.hotheadgames.google.free.survivors',
   'zombie.survival.dead.shooting',
   'com.mobirix.zombiefire',
   'com.mgs.sniper1',
   'com.madfingergames.deadtrigger',
   'com.cle.dday',
   'com.gameloft.android.ANMP.GloftM5HM',
   'com.feelingtouch.zfsniper',
   
   'com.viki.android',                                          # Entertainment
   'com.gohitv.hitv',  
   'in.startv.hotstar',
   'com.discoveryplus.mobile.android',
   'com.balaji.alt',
   'ahaflix.tv',
   'com.graymatrix.did',              
   'com.bt.bms',
   'cdi.videostreaming.app',
   'com.netflix.mediaclient',
   'tv.hinow.mobile',
   'com.funnypuri.client',
   'com.sonyliv',
   'com.amazon.avod.thirdpartyclient',
   'com.fun.share',
   
   'com.flipkart.android',                                      # Shopping  
   'com.flipkart.shopsy',
   'com.snapdeal.main',                
   'com.meesho.supply',
   'com.myntra.android',
   'in.amazon.mShop.android.shopping',
   'com.ebay.mobile',
   'com.lazada.android',
   'com.alibaba.intl.android.apps.poseidon',
   'com.bigbasket.mobileapp',
   'com.fsn.nds',
   'com.jpl.jiomart',
   'com.nike.omega',
   'com.bewakoof.bewakoof',
   'fc.admin.fcexpressadmin',
   
    'com.snapchat.android',                                     # Communication
    'org.telegram.messenger',
    'com.skype.raider',
    'com.facebook.orca',                  
    'com.facebook.mlite',
    'com.discord',
    'com.azarlive.android',
    'com.microsoft.emmx',
    'com.sec.android.app.sbrowser',
    'com.opera.mini.native',
    'com.whatsapp.w4b',
    'com.truecaller', 
    'com.whatsapp',
    'com.imo.android.imoim',
    'com.touchtalent.bobbleapp',
    
    'com.instagram.android',                                   # Social
    'com.facebook.katana',
    'com.newsdistill.mobile',
    'in.mohalla.sharechat',
    'com.parau.pro.videochat',             
    'com.facebook.lite',
    'com.blued.international',
    'com.sgiggle.production',
    'com.mumu.videochat',
    'com.vkontakte.android',
    'com.parame.live.chat',
    'com.blued.international',
    'com.cardfeed.video_public',
    'com.instagram.lite',
    'video.tiki',
    
    'com.shazam.android',                                      # Music & Audio
    'musicplayer.musicapps.music.mp3player',
    'com.amazon.mp3',
    'com.gaana',
    'com.bsbportal.music',
    'media.music.musicplayer',
    'com.starmakerinteractive.starmaker',        
    'com.pratilipi.android.pratilipifm',
    'com.google.android.apps.youtube.music',
    'com.vlv.aravali',
    'com.sec.android.app.music',
    'com.starmakerinteractive.thevoice',
    'com.dolby.dolby234',
    'com.spotify.lite',
    'com.miui.player',
    
    'com.phonepe.app',                                         # Finance
    'net.one97.paytm',
    'com.google.android.apps.nbu.paisa.user',
    'com.myairtelapp',
    'org.altruist.BajajExperia',
    'com.mobikwik_new',
    'com.tradingview.tradingviewapp',
    'com.droid4you.application.wallet',           
    'com.realbyteapps.moneymanagerfree',
    'com.whizdm.moneyview.loans',
    'com.ge.capital.konysbiapp',
    'com.csam.icici.bank.imobile',
    'in.bajajfinservmarkets.app',
    'com.cleevio.spendee',
    'com.fusionmedia.investing',
    
    'com.microsoft.skydrive',                                  # Productivity 
    'com.microsoft.office.excel',
    'cn.wps.moffice_eng',
    'com.microsoft.office.powerpoint',
    'com.adobe.reader',
    'com.microsoft.office.officehubrow',     
    'com.microsoft.office.onenote',
    'com.samsung.android.app.notes',
    'com.microsoft.office.word',
    'share.sharekaro.pro',
    'com.microsoft.appmanager',
    'com.microsoft.mobile.polymer',
    'com.kmo.pdf.editor',
    'com.voyagerx.scanner',
    'com.ilovepdf.www',
    
    'com.duolingo',                                            # Education
    'co.brainly',
    'com.byjus.thelearningapp',
    'com.testbook.tbapp',
    'co.gradeup.android',
    'me.entri.entrime',
    'com.udemy.android',                     
    'com.linkedin.android.learning',
    'in.gov.epathshala',
    'com.studysmarter',
    'com.vedantu.app',
    'com.unacademyapp',
    'org.coursera.android',
    'in.oliveboard.prep',
    'com.noonEdu.k12App',
    
    'com.sec.android.app.shealth',                             # Health and Fitness
    'com.huawei.health',
    'com.google.android.apps.fitness',
    'steptracker.healthandfitness.walkingtracker.pedometer',
    'com.healthifyme.basic',
    'com.myfitnesspal.android',
    'com.sillens.shapeupclub',        
    'cc.pacer.androidapp',
    'com.runtastic.android',
    'nl.appyhapps.healthsync',
    'com.samsung.android.service.health',
    'pedometer.steptracker.calorieburner.stepcounter',
    'com.lge.lifetracker',
    'com.tayu.tau.pedometer',
    'com.fitbit.FitbitMobile'
]
len(app_packages)


app_reviews = []

for ap in tqdm(app_packages):
  for score in list(range(1, 6)):
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, _ = reviews(
        ap,
        lang='en',
        country='us',
        sort=sort_order,
        count= 400 if score == 3 else 500,
        filter_score_with = score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
      app_reviews.extend(rvs)



app_reviews_df = pd.DataFrame(app_reviews)
app_reviews_df.to_csv('Reviews.csv', index=None, header=True)


