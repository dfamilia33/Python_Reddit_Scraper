# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:11:57 2018

@author: Daniel
"""

import smtplib
import config

def email_self(subject,post_title, link = "No link Provided"):

    msg = post_title + '\n' + link

    message = "Subject: {}\n\n{}".format(subject,msg)

    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()

    mail.starttls()

    mail.login(config.botmail,config.botpass)

    mail.sendmail(config.botmail, config.persmail, message)
    
    
    mail.close()

