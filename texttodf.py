# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:01:17 2023

@author: Alya
"""
import os
import pandas as pd

def createFiles(path_to_files, path_to_cleaned):
    for filename in os.listdir(path_to_files):
        if 'txt' in filename: #checks that it's a text file
            file=open(path_to_files+"\\"+filename)
            try:
                        # read the content of the file opened
                content = file.readlines()
        
                # read from 21th line to the end from the file
                content=content[21:]
            finally:
                file.close()
            if os.path.isfile(path_to_cleaned+'\\'+filename):
                os.remove(path_to_cleaned+'\\'+filename)
            with open(path_to_cleaned+'\\'+filename, 'a+') as f:
                for line in content:
                    f.write("%s\n" % line)
            f.close()
    return

def textToDf(path_to_cleaned):#returns a dict
    dico=dict()
    for file in os.listdir(path_to_cleaned):
        dataframe=pd.read_csv(path_to_cleaned+'\\'+file, sep='\t', index_col=[0]).iloc[: , :-1]
        dataframe.rename(columns = {'Unnamed: 0':'0'}, inplace = True)
        name=file.split('_')
        if 'KO' in file:
            key=name[1]+name[2]+name[3]
        else:
            key=name[1]+name[2]
        dico[key]=dataframe
    return dico
 #returns a dictionary mapping names to dataframes
 

