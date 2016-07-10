import numpy as np
import cv2
import urllib2
import cookielib
from getpass import getpass
import os
import sys
import webbrowser #lib for opening the link
import time
#import sys
import select
import time, msvcrt


global count
count=0
global p
p="123"

def readInput( caption, timeout = 10):
    start_time = time.time()
    sys.stdout.write('%s: '%(caption));
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche()
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) >= 32: #space_char
                input += chr
                #print input
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print ''  # needed to move to next line
    if len(input) > 0:
        print type(input)
        return input
    else:
        #print "lolpol"
        return "lolpol"
    
def messg():
  
    #username = "9871973676"
        

    #passwd = "S9246Q"

    username = "8447204783"
    passwd = "A9958K"

    message = "SOMEONE HAS ENTERED YOUR RESTRICTED AREA"

    number = "8447204783" #senders number


    message = "+".join(message.split(' '))


        #Logging into the SMS Site

    url = 'http://site24.way2sms.com/Login1.action?'

    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
        

        #For Cookies:

    cj = cookielib.CookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


        # Adding Header detail:

    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


    try:

        usock = opener.open(url, data)

    except IOError:

        print "\n[-] CAN NOT CONNECT TO SERVER...CHECK USERNAME AND PASSWORD AND INTERNET CONNECTION ALSO"

        raw_input("\n[-] PRESS ENTER TO EXIT")

        sys.exit(1)



    jession_id = str(cj).split('~')[1].split(' ')[0]

    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'

    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'

    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        

    try:

        sms_sent_page = opener.open(send_sms_url,send_sms_data)

    except IOError:

        print "\n[-] ERROR WHILE SENDING THE SMS...PLEASE UPDATE THE CONTACT LIST"

        

        sys.exit(1)

    print "\n\n\t[+] SMS SENT"
        
        

cap =cv2.VideoCapture(0)




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    
    res,img=cap.read()
    #time.sleep(1)
    res,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) :
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            
            cv2.imshow('img',img)
            
            
          
            if count==0:
                cv2.imshow('img',img)
                cv2.putText(img,'SECURITY BREACH',(40,75), font, 2,(255,255,255),3)
                cv2.imshow('img',img)
                cv2.waitKey(10)
                print("\n")
                i = readInput('Please enter your password in ten seconds')
              
   
                if i!=p:
                    messg()
                    
                    webbrowser.open('http://caller.site88.net/ta3/makecall3.php')#call is my domain name
                    

                    cv2.putText(img,'WRONG PASSWORD OWNER ALERTED',(10,250), font, 1,(255,255,255),2)
                    cv2.imshow('img',img)
                    print("\n")
                    print("OWNER ALERTED")
                    print("TIMEOUT")
                    print("NO PASSWORD ENTERED")
                    cv2.waitKey(10)
                    b=input("press any numeric key to move forward : ")
                    time.sleep(5)
                    exit(0)
                    
                else:
        
                    cv2.putText(img,'OWNER ITSELF',(200,250), font, 1,(255,255,255),2)
                    cv2.imshow('img',img)
                    print("RIGHT PASSWORD : OWNER ITSELF")

                
                    b=input("Press any numeric key to move forward : ")
                    print("\nRESET THE SYSTEM")

                    
                    reset=input("[yes=1 or no=2] : ")
                    
                    if reset==1:
                        
                        count=-1
                    else:
                        count=count+1
                    #wait till owner is out cfrom the frame
                    print("RESETING")
                    
                    
                    
                    
                    
                    #owner()
                    
                
                count=count+1
                time.sleep(2)
                
                print("RESETED")
            

    else :
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Detecting Intrusion',(25,75), font, 2,(255,255,255),3)
        cv2.imshow('img',img)
        

                    
     

    k=cv2.waitKey(10)
    if k==27:
        cap.release()
        cv2.destroyAllWindows()
        
        break


