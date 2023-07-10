 # -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:03:39 2023

@author: Alya
"""
#Using the export platemap to convert the plate to data with concentrations

import pandas as pd


def final_df(plate_plan, results): #takes the plate plan and the results dic as input
#returns a df with the luminescence reading in the columns labeled by names=dic.keys()
    plate_plan_c=plate_plan.copy().iloc[:384]
    for key in results.keys():
        new_series=[]
        for location in plate_plan_c['Dest Well']:
            new_series.append(results[key].loc[location[0]][int(location[1:])-1])
        plate_plan_c[key]=pd.Series(new_series)
    return plate_plan_c
