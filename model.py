# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""
import pandas as pd
from sklearn.svm import SVC
from database import Database
import database_connection as dc
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
from data_pre_processing import DataPreProcessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score, confusion_matrix


class Model(object):
    
    def __init__(self):
        
        #self.db = Database(dc.DB_HOST, dc.DB_USER, dc.DB_PASSWORD, dc.DB_NAME)
        #self.dataset = self.db.dataset_from_db()
        self.dataset = pd.read_csv('new_data3.csv', encoding= 'unicode_escape')
        print(self.dataset)
        self.data_pre_processing = DataPreProcessing()
        self.data = self.data_pre_processing.get_pre_processed_dataset(self.dataset)
        print(self.data)
        self.trainX,self.testX, self.trainy, self.testy = train_test_split(self.data['Word_Vect'], self.data['Text_Response'], test_size = 0.001)
        
        print(self.trainX)
        
        self.count_vect = CountVectorizer()
        self.X_train_counts = self.count_vect.fit_transform(self.trainX)
        self.X_test_counts = self.count_vect.transform(self.testX)
        
        self.tfidf_transformer = TfidfTransformer()
        self.X_train_tfidf = self.tfidf_transformer.fit_transform(self.X_train_counts)
        self.X_test_tfidf = self.tfidf_transformer.transform(self.X_test_counts)
      
        # normalize input vectors
        self.in_encoder = Normalizer(norm='l2')
        self.X_train = self.in_encoder.fit_transform(self.X_train_tfidf)
        self.X_test = self.in_encoder.transform(self.X_test_tfidf)
        

        # label encode targets
        self.out_encoder = LabelEncoder()
        self.out_encoder.fit(self.trainy)
        self.trainy = self.out_encoder.transform(self.trainy)
        self.testy = self.out_encoder.transform(self.testy)
         
        # fit model
        self.model = SVC(kernel='linear', probability=True)
        self.model.fit(self.X_train, self.trainy)
        
        
        
        
        y_pred = self.model.predict(self.X_train)
        cm = confusion_matrix(self.trainy, y_pred)
        print("Training set -----------------------------------------------------------------------")
        print("Confusion Metrix")
        print(cm)
        print("------------------------------------------------------------------------------")
        ac = accuracy_score(self.trainy, y_pred)
        print("Accuracy Score : " + str(ac))
        
        
        y_pred = self.model.predict(self.X_test)
        cm = confusion_matrix(self.testy, y_pred)
        print("----------------------------------------------------------------------------")
        print("Confusion Metrix")
        print(cm)
        print("-------------------------------------------------------------------")
        ac = accuracy_score(self.testy, y_pred)
        print("Accuracy Score : " + str(ac))
        print("-----------------------------------------------------------------")
        
        
    def count_vector(self, input_bot):
        return self.count_vect.transform(input_bot)

    def tf_idf_trans(self, input_count_vect):
        return self.tfidf_transformer.fit_transform(input_count_vect)

    def normalizer(self,data):
        return self.in_encoder.transform(data)

    def labelencoder(self, data):
        data = self.out_encoder.transform(data)
        return data
    
    
    
    def predict(self,normalised_data):
        # prediction for the face
        normalised_data = self.data_pre_processing.make_pre_processed_string(normalised_data)
        print(normalised_data)
        sample_data = self.normalizer(self.tf_idf_trans(self.count_vector([normalised_data])))
        yhat_class = self.model.predict(sample_data)
        yhat_prob = self.model.predict_proba(sample_data)
        # get name
        class_index = yhat_class[0]
        class_probability = yhat_prob[0,class_index] * 100
        predict_names = self.out_encoder.inverse_transform(yhat_class)
        return {'predict_name':predict_names[0], 'class_probability':class_probability}