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
            sql_get_dataset = "SELECT * from agile_bot"
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


        
def user_que_to_mysql_db(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, Context):
    try:

        connection = connect(host= DB_HOST, user= DB_USER, password= DB_PASSWORD, db= DB_NAME) 
        cursor = connection.cursor(DictCursor)
        data_insertion_queery = "INSERT INTO `agile_bot_user_questions`(`Context`) VALUES (%s)"
        cursor.execute(data_insertion_queery,(Context))
        connection.commit()
        
        return None
    except:
        None

        
        
def user_data_to_mysql_db(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, user_contact1, user_time1):
    try:

        connection = connect(host= DB_HOST, user= DB_USER, password= DB_PASSWORD, db= DB_NAME)
        cursor = connection.cursor(DictCursor)
        user_insertion_queery = "INSERT INTO `agile_bot_user_details`(`user_contact`, `prefer_time`) VALUES (%s, %s)"
        cursor.execute(user_insertion_queery,(user_contact1, user_time1))
        connection.commit()
        
        return None
    except:
        None
        
def user_data_to_mysql_db1(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, user_contact1, user_que1, user_time1):
    try:

        connection = connect(host= DB_HOST, user= DB_USER, password= DB_PASSWORD, db= DB_NAME)
        cursor = connection.cursor(DictCursor)
        user_insertion_queery = "INSERT INTO `agile_bot_user_details`(`user_contact`,`user_que`,`prefer_time`) VALUES (%s, %s, %s)"
        cursor.execute(user_insertion_queery,(user_contact1, user_que1, user_time1))
        connection.commit()
        
        return None
    except:
        None      
        
def user_data_to_mysql_db2(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, user_contact1, user_que1):
    try:

        connection = connect(host= DB_HOST, user= DB_USER, password= DB_PASSWORD, db= DB_NAME)
        cursor = connection.cursor(DictCursor)
        user_insertion_queery = "INSERT INTO `agile_bot_user_details`(`user_contact`,`user_que`) VALUES (%s, %s)"
        cursor.execute(user_insertion_queery,(user_contact1, user_que1))
        connection.commit()
        
        return None
    except:
        None   
        
class Exls_to_DB():
    
    def __init__(self, host, user_db, password_db, db):
        self.host = host
        self.user_db = user_db
        self.password_db = password_db
        self.db = db
        
        
    def exls_to_mysql_db(self, Context, Text_Response):
    
        try:
            connection = connect(host= self.host, user= self.user_db, password= self.password_db, db= self.db) 
            cursor = connection.cursor(DictCursor)
            data_insertion_queery = "INSERT INTO `agile_bot`(`Context`, `Text_Response`) VALUES (%s,%s)"
            cursor.execute(data_insertion_queery,(Context, Text_Response))
            connection.commit()
            return None
        
        except:
            return None