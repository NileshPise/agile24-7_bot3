# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:07:22 2021
Project: Chat bot (AI Based) Application
@author: Nilesh Pise
"""


from flask import render_template
from flask_cors import CORS
from flask import Flask, request, jsonify
from pre_processing import PreProcessing
import database_connection as dc
from database import *


prepross = PreProcessing()
app = Flask(__name__)
CORS(app)

class my_v():
    key = None
    value = None


@app.route('/apicheck', methods = ['GET'])
def apicheck():

    return "API IS WORKING...!"


@app.route('/agile_bot', methods = ['POST'])
def agile_bot():
    
    input_to_bot = request.get_json(force= True)
    bot_text = input_to_bot['bot_text']
    bot_responce = prepross.prediction(bot_text)
    
    return jsonify(bot_responce)


if __name__ == '__main__':
    app.run(host='192.168.7.162',port = 5018, threaded=True)
