# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""



import nltk
import string
import pandas as pd
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('stopwords')


class DataPreProcessing(object):
    
    def __init__(self):
        
        self.tag_map = defaultdict(lambda : wn.NOUN)
        self.tag_map['J'] = wn.ADJ
        self.tag_map['V'] = wn.VERB
        self.tag_map['R'] = wn.ADV
        
        self.lmtzr = WordNetLemmatizer()
    
    def tokenizer(self, sentence):
        # creating works token
        word_tokens = word_tokenize(sentence)
        return word_tokens
    
    def remove_punctuation(self, tokens):
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [word.translate(table) for word in tokens]
        return stripped
    
    def remove_non_alphabetic(self, tokens):
        # remove all tokens that are not alphabetic
        words = [word for word in tokens if word.isalpha()]
        return words
    
    def word_normalization(self, tokens):
        # convert to lower case
        words = [word.lower() for word in tokens]
        return words
    
    def remove_stopwords(self, tokens):
        # removing stopwords
        tokens_without_sw = [word for word in tokens if not word in stopwords.words()]
        return tokens_without_sw
        
    
    def word_lemmatization(self, tokens):
        # word lemmatization
        new_data = []
        for token, tag in pos_tag(tokens):
            lemma = self.lmtzr.lemmatize(token, self.tag_map[tag[0]])
            new_data.append(lemma)
            
        return new_data
    
    
    def make_pre_processed_dataset(self, dataset):
        Data = None
        Context = []
        words_vect = []
        Text_Responce = []

        for i in range(0,len(dataset.index)):
            sen = dataset.Context[i]
            tar = dataset.Text_Response[i]
            token = self.tokenizer(sen)
            non_pun_token = self.remove_punctuation(token)
            non_pu_tk = self.remove_non_alphabetic(non_pun_token)
            tok = self.word_normalization(non_pu_tk)
            tok1 = self.remove_stopwords(tok)
            tok2 = self.word_lemmatization(tok1)
            tok3 = ' '.join([str(elem) for elem in tok2])
            words_vect.append(tok3)
            Context.append(sen)
            Text_Responce.append(tar)
            print(i)
        Data = [Context, words_vect, Text_Responce]
        return Data

    def get_pre_processed_dataset(self, dataset):
        dataset1 = pd.DataFrame(self.make_pre_processed_dataset(dataset), ['Context', 'Word_Vect', 'Text_Response']).T
        return dataset1
    
    
    def make_pre_processed_string(self, input_string):
        
        token = self.tokenizer(input_string)
        non_pun_token = self.remove_punctuation(token)
        non_pu_tk = self.remove_non_alphabetic(non_pun_token)
        tok = self.word_normalization(non_pu_tk)
        tok1 = self.remove_stopwords(tok)
        tok2 = self.word_lemmatization(tok1)
        pre_processed_string = ' '.join([str(elem) for elem in tok2])
        return pre_processed_string
    