# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""

from database import *
from send_email import send_mail
import database_connection as dc
from data_pre_processing import DataPreProcessing
from model import Model
import re
import utils

class Contact():
    
    user_contact = None
    user_time = None
    user_que = None
    
    
class PreProcessing():
    
    def __init__(self):
        
        self.db = Database(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME)
        self.df = self.db.dataset_from_db()
        self.contact = Contact()
        self.model = Model()
        self.data_pre_processing1 = DataPreProcessing()
        
        
    def check_no(self, text):
        for i in re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text):
            return i
        
        
    
    def check_time(self, text):
        for i in re.findall(r'(([0-9]:[0-9][0-9]|[0-9]) [pmamAMPM]|([0-9]:[0-9][0-9]|[0-9])[pmamAMPM])|([0-9][ampmAMPM]|[0-9] [ampmAMPM])|([0-9]:[0-9][0-9])', text):
            return i[0]
        
        
        
    def check_mail(self, text):
        
        match = re.search('[@]', text)
        match1 = re.search('[.com]', text)
        if match is not None and match1 is not None:
            return text
        
        
    def do_data(self, string_1):
        s_st = string_1
        d_li = []
        s_data = self.data_pre_processing1.make_pre_processed_string(string_1)
        s_data = s_data.split()
        print(s_data)
        if 'do you' in s_st.lower():
            for u_data in utils.do_data:
                for s_item in s_data:
                    if s_item.lower() in u_data.lower():
                        d_li.append(s_item.lower())
                    else:
                        None
        print(d_li)
        if set(s_data) == set(d_li):
            return 'Yes'
        else:
            return 'No'
        
        
        
        
    def prediction(self, input_to_bot):
        
        try:
           
            mobile_no = self.check_no(input_to_bot)
            email = self.check_mail(input_to_bot)
            
            if mobile_no is not None or email is not None:
                
                if mobile_no is not None:
                    self.contact.user_contact = mobile_no
                    return "May i know your good time to get in touch with you..."

                    
                
                if email is not None:
                    self.contact.user_contact = email
                    send_mail(self.contact.user_contact)
                    user_data_to_mysql_db2(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME, self.contact.user_contact, self.contact.user_que)
                    return "Our Representative will get in touch with you..... Thank you for connecting with Agile24x7....! "
        except:
            None
            
            
            
        try:
            self.contact.user_time = self.check_time(input_to_bot)
            if self.contact.user_time is not None:
                user_data_to_mysql_db1(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME, self.contact.user_contact, self.contact.user_que, self.contact.user_time)
                return "Our Representative will get in touch with you..... Thank you for connecting with Agile24x7....! "
        except:
            return None
        
        try:
            if ('do you' in input_to_bot.lower()):
                res = self.do_data(input_to_bot)
                if res == "Yes":
                    return res
                else:
                    return "No, If you have more question then please share your Email Id or Mobile Number our representative will get in touch with you..."
        except:
            None    
                
            
        bot_responce = None
        input_bot = input_to_bot
        self.contact.user_que = input_to_bot
        
        
        
        try:
            bot_responce = self.model.predict(input_bot)
            print(bot_responce)
            user_que_to_mysql_db(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME, input_bot)
            
            if bot_responce['class_probability'] < 9.09:
                return "Please leave a phone number or email and one of our Reps will contact you..."
    
            
            return bot_responce['predict_name']
        
        except:
            return bot_responce
