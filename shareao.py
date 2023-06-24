import requests,re,json,random,sys,os
import bs4,base64
from time import sleep
from time import sleep
from datetime import datetime
import random
from datetime import date
import requests, os, sys, re, json
from threading import Thread
import threading
import time
from random import choice, randint, shuffle
import json,requests,time
from time import strftime
os.system('title TOOL SHARE ẢO')
time = datetime.now()

from random import choice, randint, shuffle
def abbbabbabaaaaabbbbabbab(abbabbbabbb):
    print(abbabbbabbb)
def dk():
   a= "────"*31
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def sssh(tokenfb,linkbv):
   abbbbbababbbabababdababa = {
      'authority':'graph.facebook.com',
      'cache-control':'max-age=0',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
   requests.post(f"https://graph.facebook.com/me/feed?link="+linkbv+"&published=0&access_token="+tokenfb,headers=abbbbbababbbabababdababa).text
def aabbabababbabbababbababbbbaaabba(a):
   abbbabbabaaaaabbbbabbab("Success | "+str(a)+" | ")
def shareh(tokenfb,linkbv):
   head = {
      'authority':'graph.facebook.com',
      'cache-control':'max-age=0',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
   vvv = requests.post(f"https://graph.facebook.com/me/feed?link="+linkbv+"&published=0&access_token="+tokenfb,headers=head).text
   if 'id' in vvv:
     babbbdddabbaaaaabB = json.loads(vvv)['id']
     aabbabababbabbababbababbbbaaabba(babbbdddabbaaaaabB)
   else:
     abbbabbabaaaaabbbbabbab(aabbababababbbbbaaabbbbbaababb)
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()

##os.system('clear')
list_token = []
for i in range(9999):
   tks = input("Nhập Token Thứ "+str(i+1)+": ")
   if tks != '':
      list_token.append(tks)
   else:
    break
linkbv = str(input("Nhập Link Bài Viết: "))

print("──────────────────────────────────────────────────────────────────────")
while True:
   for a in range(len(list_token)):
        threading.Thread(target=shareh,args=(list_token[a],linkbv)).start()
