#! /usr/local/bin/python3

import sys
import pandas as pd
import os
from tqdm import tqdm
import math
import numpy as np
import platform
from sklearn import linear_model
from sklearn import model_selection
from scipy import stats
from sklearn import linear_model
import pickle
import gzip
import csv


def make_folder () :
    if platform.system() == 'Windows':
        path_sep = "\\"
    else:
        path_sep = "/"

    result_pass= os.path.abspath(os.path.dirname(__file__))+ path_sep+ "Results"
    if not os.path.isdir(result_pass) :
        os.mkdir(result_pass)
    folder_path = os.path.abspath(os.path.dirname(__file__))+ path_sep+ "Results"+ path_sep+\
                                                           os.path.splitext(os.path.basename(sys.argv[0]))[0]+"_result"
    i = 0
    if os.path.isdir(folder_path) :
        while os.path.exists(folder_path+"_"+str(i)) :
            i = i+1
            
        folder_path=folder_path+"_"+str(i)
        os.mkdir(folder_path)
    else :
        os.mkdir(folder_path)
    return (folder_path+path_sep)

def main(df) :
    #print(df.head())
    y_array = df["CS"].values

    gene_list = df["Gene_id"].values
    
    df = df.drop(["CS","Gene_id"],axis=1)

    feature_columns = list(df.columns)
    x_array = df.values

    for i in tqdm(range(x_array.shape[1])) :
        x_array[:,i] = (x_array[:,i]-np.mean(x_array[:,i]))/np.std(x_array[:,i],ddof = 1) #standardization

    x_array[np.isnan(x_array)] = 0
    model = linear_model.Lasso(alpha=0.01) #alpha value was determined using model_selection.cross_val_score from the Python package scikit-learn
    model=model.fit(x_array,y_array)

    y_array_predicted = model.predict(x_array) #prediction
    
    folder_path = make_folder ()
    with open(folder_path+'_model.pickle', mode = 'wb') as f: #Saving model
        pickle.dump(model, f)

    table=pd.DataFrame()
    table["Gene_id"] = gene_list
    table["Measured"] = y_array
    table["Predicted"] = y_array_predicted
    table.to_csv(folder_path + "_prediction_value.txt",index=False,sep="\t") #Saving prediction_value

    table_coef=pd.DataFrame([feature_columns,list(model.coef_)],index=["Factor","Weight"]).T
    table_coef.to_csv(folder_path + "_model_coef.txt",index=False,sep="\t") #Saving feature's coefficient

            
if __name__ == "__main__":

    df = pd.read_csv(sys.argv[1], sep='\t') #log10 conversion were conducted in CSsite values
    main(df)















