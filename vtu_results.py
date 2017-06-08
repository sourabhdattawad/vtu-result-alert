# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import re
from mechanize import Browser
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
import time
from selenium import webdriver
from depot.manager import DepotManager
import telegram
bot = telegram.Bot(token="YOUR TELEGRAM TOKEN")


res_available = False


def sendalert():
    message = "Results are out!"
    numbers = ["PHONE NUMBER"]
    USN = "YOUR USN"
    
    if __name__ == "__main__":    
        username = "WAY2SMS_USERNAME"
        passwd = "WAY2SMS_PASSWORD"
    
        message = "+".join(message.split(' '))
    
     #logging into the sms site
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
    
     #For cookies
    
        cj= cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    
     #Adding header details
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock =opener.open(url, data)
        except IOError:
            print "error"
            #return()
        for number in numbers:
            
            jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
            try:
                sms_sent_page = opener.open(send_sms_url,send_sms_data)
            except IOError:
                print "error"
                #return()
        
            print "success" 
            #return ()
        
	
        depot = DepotManager.get()
        driver = webdriver.PhantomJS()
        driver.set_window_size(1024, 768) # set the window size that you need 
        driver.get('http://results.vtu.ac.in/results/result_page.php?usn='+USN)
        driver.save_screenshot('res.png')
        bot.send_photo(chat_id="telegram group-chat id", photo=open('res.png', 'rb'))

        
def checkresult():
    browser = Browser()
    content = ''
    try:
        rep = browser.open("http://results.vtu.ac.in/results/result_page.php?usn="+USN)
        content = rep.read()
         
    except:
        content = 'not available'
        
        
    if('not available' not in content):
        res_available = True
        sendalert()
        

count = 0
while True:
    checkresult()
    count+=1
    print count
    time.sleep(10)

    



    



    

# <codecell>

