# -*- coding: utf-8 -*
from __future__ import unicode_literals
#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
from bs4 import BeautifulSoup
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)

fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                            
fw  =   Fore.WHITE                                            
fg  =   Fore.GREEN                                            
sd  =   Style.DIM                                            
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT   
if str(os.path.exists('Resultz')) == 'False':
    os.system('mkdir Resultz')
else:
    pass
if str(os.path.exists('Resultz')) == 'False':
    os.system('mkdir Resultz')
else:
    print ('')
def logo():
    curlear = "\x1b[0m"
    colors = [32]

    x = """

       _                                                        
                                     ..                       .                          
         .xHL                      dF                        @88>              .uef^"    
      .-`8888hxxx~                '88bu.         .u    .     %8P             :d88E       
   .H8X  `%888*"            u     '*88888bu    .d88B :@8c     .          .   `888E       
   888X     ..x..        us888u.    ^"*8888N  ="8888f8888r  .@88u   .udR88N   888E .z8k  
  '8888k .x8888888x   .@88 "8888"  beWE "888L   4888>'88"  ''888E` <888'888k  888E~?888L 
   ?8888X    "88888X  9888  9888   888E  888E   4888> '      888E  9888 'Y"   888E  888E 
    ?8888X    '88888> 9888  9888   888E  888E   4888>        888E  9888       888E  888E 
 H8H %8888     `8888> 9888  9888   888E  888F  .d888L .+     888E  9888       888E  888E 
'888> 888"      8888  9888  9888  .888N..888   ^"8888*"      888&  ?8888u../  888E  888E 
 "8` .8" ..     88*   "888*""888"  `"888*""       "Y"        R888"  "8888P'  m888N= 888> 
    `  x8888h. d*"     ^Y"   ^Y'      ""                      ""      "P'     `Y"   888  
      !""*888%~                                                                    J88"  
      !   `"  .                                                                    @%    
      '-....:~                                                                   :"      
                                                         

    \033[0;37;41m[ Coded by Hadrich.Alt-F4 ]
    \033[0;37;41m[ICQ:https://icq.im/hadrich]
    \033[0;37;41m[Not responsible for any illegal usage of this tool.]
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, curlear))
        time.sleep(0.05)
logo()


try:
    spy = raw_input("\n\033[91mCms\033[97m:~# \033[97m")
    crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
    with codecs.open(spy, mode='r', encoding='ascii', errors='ignore') as f:
        lists = f.read().splitlines()
except:
    print("open your eyes!")
lists = list((lists))


def filternowbanke(l):
    try:

        if '@gmail' in l:
            print '{}[>] {} {}   -  {}{} gmail'.format(sb, sd, l, fc,fc)
            open("Resultz/gmail.txt","a").write(l+"\n")
        elif '@yahoo' in l:
            print '{}[>] {} {}   -  {}{} yahoo'.format(sb, sd, l, fc,fc)
            open("Resultz/yahoo.txt","a").write(l+"\n")
        elif '@hotmail' in l:
            print '{}[>] {} {}   -  {}{} hotmail'.format(sb, sd, l, fc,fc)
            open("Resultz/hotmail.txt","a").write(l+"\n")
        elif '@live' in l:
            print '{}[>] {} {}   -  {}{} hotmail'.format(sb, sd, l, fc,fc)
            open("Resultz/hotmail.txt","a").write(l+"\n")
        elif '@msn' in l:
            print '{}[>] {} {}   -  {}{} hotmail'.format(sb, sd, l, fc,fc)
            open("Resultz/hotmail.txt","a").write(l+"\n")
        elif '@outlook' in l:
            print '{}[>] {} {}   -  {}{} hotmail'.format(sb, sd, l, fc,fc)
            open("Resultz/hotmail.txt","a").write(l+"\n")
        elif '@ymail' in l:
            print '{}[>] {} {}   -  {}{} yahoo'.format(sb, sd, l, fc,fc)
            open("Resultz/yahoo.txt","a").write(l+"\n")
        elif '@googlemail' in l:
            print '{}[>] {} {}   -  {}{} gmail'.format(sb, sd, l, fc,fc)
            open("Resultz/gmail.txt","a").write(l+"\n")
        elif '@aol' in l:
            print '{}[>] {} {}   -  {}{} aol'.format(sb, sd, l, fc,fc)
            open("Resultz/aol.txt","a").write(l+"\n")
        elif '@mail.ru' in l:
            print '{}[>] {} {}   -  {}{} mail.ru'.format(sb, sd, l, fc,fc)
            open("Resultz/mail_ru.txt","a").write(l+"\n")
        elif '@mac.' in l:
            print '{}[>] {} {}   -  {}{} mac'.format(sb, sd, l, fc,fc)
            open("Resultz/mac.txt","a").write(l+"\n")
        elif '@icloud.' in l:
            print '{}[>] {} {}   -  {}{} waicloudnadoo'.format(sb, sd, l, fc,fc)
            open("Resultz/icloud.txt","a").write(l+"\n")
        elif '@me' in l:
            print '{}[>] {} {}   -  {}{} me'.format(sb, sd, l, fc,fc)
            open("Resultz/me.txt","a").write(l+"\n")
        elif '@rocketmail.' in l:
            print '{}[>] {} {}   -  {}{} rocketmail'.format(sb, sd, l, fc,fc)
            open("Resultz/rocketmail.txt","a").write(l+"\n")

            open("Resultz/wanadoo.txt","a").write(l+"\n")
        elif '@ntlworld' in l:
            print '{}[>] {} {}   -  {}{} ntlworld'.format(sb, sd, l, fc,fc)
            open("Resultz/ntlworld.txt","a").write(l+"\n")
        elif '@virginmedia' in l:
            print '{}[>] {} {}   -  {}{} virginmedia'.format(sb, sd, l, fc,fc)
            open("Resultz/virginmedia.txt","a").write(l+"\n")
        elif '@virgin' in l:
            print '{}[>] {} {}   -  {}{} virgin'.format(sb, sd, l, fc,fc)
            open("Resultz/virgin.txt","a").write(l+"\n")
        elif '@comcast' in l:
            print '{}[>] {} {}   -  {}{} comcast'.format(sb, sd, l, fc,fc)
            open("Resultz/comcast.txt","a").write(l+"\n")
        elif '@sapo.pt' in l:
            print '{}[>] {} {}   -  {}{} sapo.pt'.format(sb, sd, l, fc,fc)
            open("Resultz/sapo.txt","a").write(l+"\n")
        elif '@gmx' in l:
            print '{}[>] {} {}   -  {}{} gmx'.format(sb, sd, l, fc,fc)
            open("Resultz/gmx.txt","a").write(l+"\n")
        elif '@web' in l:
            print '{}[>] {} {}   -  {}{} web'.format(sb, sd, l, fc,fc)
            open("Resultz/web.txt","a").write(l+"\n")
        elif '@rcn' in l:
            print '{}[>] {} {}   -  {}{} rcn'.format(sb, sd, l, fc,fc)
            open("Resultz/rcn.txt","a").write(l+"\n")
        elif '@cox' in l:
            print '{}[>] {} {}   -  {}{} cox'.format(sb, sd, l, fc,fc)
            open("Resultz/cox.txt","a").write(l+"\n")

        else:
            print '{}[>] {} {}   -  {}{} other'.format(sb, sd, l, fc,fc)
            open("Resultz/other.txt","a").write(l+"\n")






    except:
        pass



def Exploit(l):
    try:
        filternowbanke(l)

    except:
        pass


def Main():
    try:
        pp = Pool(int(crownes))
        pr = pp.map(Exploit, lists)
        sosa = l.count()
        print sosa
    except:
        pass


if __name__ == '__main__':
    Main()
