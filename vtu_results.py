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


def sendalert():
    message = "Holy Shit! Results out!"
    number = "Your-mobile-no"
    
    if __name__ == "__main__":    
        username = "way2sms username(phone-no)"
        passwd = "way2sms password"
    
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

        
def checkresult():
    
    #use http://results.vtu.ac.in/vitavireval.php **for revaluation results**
    #use http://results.vtu.ac.in **for regular results**
    browser = Browser()
    browser.open("http://results.vtu.ac.in/vitavireval.php") 
    browser.select_form(nr=0)
    browser['rid'] = 'YOUR-USN'
    response = browser.submit()
    content = response.read() 
    if('Results are not yet available' not in content):
        res_available = True
        sendalert()

while True:
    checkresult()
    time.sleep(30)

    



    



    

