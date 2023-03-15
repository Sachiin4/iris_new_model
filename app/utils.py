import json,numpy as np,pandas as pd
import pickle
import os
from flask import Flask,request,render_template
import CONFIG

class predictions():
    def __init__(self):
        print(os.getcwd())

    def load_raw_model(self):
        with open(CONFIG.MODEL_PATH,'rb') as model_file: 
            self.model = pickle.load(model_file)
    
        with open(CONFIG.ASSET_PATH,'r') as col_file: 
            self.column_names = json.load(col_file)

    def predicted_species(self,data):

        self.load_raw_model()
        self.data = data
        
        user_input = np.zeros(len(self.column_names['Column Names']))
        
        SepalLengthCm=self.data['html_slength']
        SepalWidthCm=self.data['html_swidth']
        PetalLengthCm=self.data['html_plength']
        PetalWidthCm=self.data['html_pwidth']

        user_input[0] = SepalLengthCm
        user_input[1] = SepalWidthCm
        user_input[2] = PetalLengthCm
        user_input[3] = PetalWidthCm

        #print(f"{user_input=}")
        #Species = {0:'Setosa',1:'Versicolor',2:'Virginica'}
        
        result= self.model.predict([user_input])
        if result[0] == 0:
            Species = "SETOSA"
        if result[0] == 1:
            Species = "VERSICOLOR"
        if result[0] == 2:
            Species = "VIRGINICA"
        print(f"Predicted Species = {Species[result[0]]}")

        return render_template("iris.html",PREDICT_VALUE=Species)

if __name__=="__main__":

    pred_obj=predictions()
    pred_obj.load_raw_model()