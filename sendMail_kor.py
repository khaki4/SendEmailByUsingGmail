# -*- coding:utf-8 -*- 
import os, smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase 
from email.MIMEText import MIMEText 
from email.header import Header 
from email import Encoders 
import time 
import datetime 
import random 

gmail_username="gmail username" 
gmail_user="gmail account" 
gmail_pwd="password" 
attach_file="name of attachfile" 

def send_gmail(to, subject, text, html, attach):
    msg=MIMEMultipart('alternative')
    msg['From']=gmail_username
    msg['To']=to
    msg['Subject']=Header(subject,'utf-8')
    msg.attach(MIMEText(text, 'plain', 'utf-8'))
    msg.attach(MIMEText(html, 'html', 'utf-8'))
    
    # comment when doesn't exist attachment file
    part=MIMEBase('application','octet-stream') 
    part.set_payload(open(attach, 'rb').read()) 
    Encoders.encode_base64(part) 
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach)) 
    msg.attach(part)
    # ------------------------------------------------------
    
    mailServer=smtplib.SMTP("smtp.gmail.com",587) 
    mailServer.ehlo() 
    mailServer.starttls() 
    mailServer.ehlo() 
    mailServer.login(gmail_user,gmail_pwd) 
    mailServer.sendmail(gmail_user, to, msg.as_string()) 
    mailServer.close() 
    
def mainLoop(): 
    f = open("test.txt", "r") 
    message = f.read() 
    f.close() 
    
    f = open("content.html", "r") 
    html = f.read() 
    f.close() 
    
    title="test mail" 
    print "Program Ready" 
    print "----------------------" 
    f = open("list.txt", "r") 
    emails = f.readlines() 
    for email in emails: 
        rand = random.randrange(1,5) # Set range of the waiting time. 
        email = email.strip() # Removing White spaces. 
        if email == "" : 
            continue 
        print "[" + str(datetime.datetime.now()) + "] Sending email to " + email + "..." 
        send_gmail(email,title,message,html,attach_file) 
        print "[" + str(datetime.datetime.now()) + "] Complete... Waiting for " + str(rand) +" seconds." 
        time.sleep(rand) 
    print "Mails have just been sent. The program is going to end." 
    
if __name__ == "__main__": 
    mainLoop() 
