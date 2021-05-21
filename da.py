# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:40:07 2021

@author: vaish
"""

import utils
from data_pre_processing import DataPreProcessing
d = DataPreProcessing()
print(utils.do_data)

def st1(string_1):
    s_st = string_1
    d_li = []
    s_data = d.make_pre_processed_string(string_1)
    if 'do you have' in s_st.lower():
        for u_data in utils.do_data:
            if s_data.lower() in u_data.lower():
                d_li.append('Yes')
            else:
                d_li.append('No')
    if 'Yes' in d_li:
        return 'Yes'
    else:
        return 'No'
                
    