# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""

from pymysql import connect
from pymysql.cursors import DictCursor
import pandas as pd


class Database():
    
    def __init__(self, host, user_db, password_db, db):
        self.host = host
        self.user_db = user_db
        self.password_db = password_db
        self.db = db
        
        
    def get_dataset(self):
    
        try:
            connection = connect(host= self.host, user= self.user_db, password= self.password_db, db= self.db) 
            cursor = connection.cursor(DictCursor)
            sql_get_dataset = "SELECT * FROM `Agile24x7_bot_from_gui`"
            cursor.execute(sql_get_dataset)
            result = cursor.fetchall()
            connection.commit()
            return result
        except:
            return None
        
        
    def dataset_from_db(self):
        
        try:
            data = self.get_dataset()
            dataset = pd.DataFrame(data)
            return dataset
        
        except:
            None
            
            
c = Database("192.168.0.26","chatbot","chatbot@123","chatbot_db")
data = c.dataset_from_db()

'''

for x in range(3,24):
    data1 = data.drop(index=x, inplace= True)
''' 

data.to_csv("new_data.csv")

'''
df = pd.read_csv("new_data.csv")
print(df['Context'])
print(df['Text_Responce'])
'''