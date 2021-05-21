# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""


import database_connection as dc
from database import Exls_to_DB
import pandas as pd


class data_insertion():
    
    def __init__(self):
        
        self.df = pd.read_csv('new_data.csv', encoding= 'unicode_escape')
        self.db = Exls_to_DB(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME)
        
        
    def get_data_into_db(self):

        for ind in self.df.index:
            context = self.df['Context'][ind]
            text_response = self.df['Text_Responce'][ind]
            self.db.exls_to_mysql_db(context, text_response)
            print("wait")
            
            
data = data_insertion()
data.get_data_into_db()