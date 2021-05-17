#! /usr/local/bin/python3
import pylab
import sys
import pandas as pd
import os
from tqdm import tqdm
import math
import numpy as np
import platform
#from numba import jit
from matplotlib import pyplot as plt
###############################################

#フォントサイズ、名前
font_name="Arial"
font_size=9

#カラム名を記入
column_1="A"
column_2="U"
column_3="G"
column_4="C"

#軸のラベル設定
label_1="Position"
label_2="Frequency (%)"

#軸の範囲
#x_range_1=[-5,4]  #X-axis
y_range=[0,100]  #Y-axis

legend=False
min_range=-20
max_range=20
figsize=[6.5,6.5]
#################################################
figsize[0]=figsize[0]*0.3937
figsize[1]=figsize[1]*0.3937
#windouwかmacか判断して正しく保存できるようにする
if platform.system() == 'Windows':
    path_sep = "\\"
else:
    path_sep = "/"
#-----------------------------------
File_Path = sys.argv
Input_Dir_Path_1 = os.path.abspath(os.path.dirname(sys.argv[1])) + path_sep
File_Name = os.path.splitext(os.path.basename(sys.argv[1]))[0]


def make_folder () :
    result_pass= os.path.abspath(os.path.dirname(File_Path[0]))+ path_sep+"Results"
    if not os.path.isdir(result_pass) :
        os.mkdir(result_pass)
    folder_path = result_pass+ path_sep+os.path.splitext(os.path.basename(sys.argv[0]))[0]+"_result"
    i = 0
    if os.path.isdir(folder_path) :
        while os.path.exists(folder_path+"_"+str(i)) :
            i = i+1
            
        folder_path=folder_path+"_"+str(i)
        os.mkdir(folder_path)

    else :
        os.mkdir(folder_path)
    return (folder_path+path_sep)

def main() :

    df1=pd.read_csv(File_Path[1],delimiter = "\t")
    df2=pd.read_csv(File_Path[2],delimiter = "\t")

    a = df1["Measured"]
    b = df2["Measured"]
    print(np.corrcoef(a, b)[0, 1])

    a = df1["Predicted"]
    b = df2["Predicted"]
    print(np.corrcoef(a, b)[0, 1])

    
if __name__ == "__main__":
        main()















