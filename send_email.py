# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""

import smtplib 
import email_connection as ec 
from email.parser import BytesParser, Parser
from email.policy import default

def send_mail(toaddrs):
    
    server = smtplib.SMTP(ec.domain)
    server.set_debuglevel(1)
    
    # Create the container email message.
    headers = Parser(policy=default).parsestr(
            'From: Agile24x7 Assistance <appsupport@novisync.com>\n'
            'To: <{}>\n'
            'Subject: Reply from Agile24x7 Assitance\n'
            '\n'
            'Hello,\n'
            'Thank you for getting in touch Agile24x7, Please do let us know how can we help you. Is there a number on which Support person can reach you at.\n\n'
            'Regards,\n'
            'Support Team, Agile24x7.\n'.format(toaddrs))


    # sending the mail
    server.login(ec.fromaddr, ec.password)
    server.send_message(headers, ec.fromaddr, toaddrs)
    server.quit()
    return "Mail send."



