# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:20:49 2020

@author: Naga Raghavendra
"""
from __init__ import *
import pandas as pd
import numpy as np
import functions as f
"""
try:
    sheet_name = 'Index'
    df_temp1 = df_new.parse(sheet_name)
    df_temp2 = df_old.parse(sheet_name)
    df_temp1 = df_temp1[df_temp1['Index'] == 'Equity']
    df_temp2 = df_temp2[df_temp2['Index'] == 'Equity']
    sheet_names_new = df_temp1['Unnamed: 1'].tolist()
    sheet_names_old = df_temp2['Unnamed: 1'].tolist()
except Exception:
    print("Error")    
"""
def main():
    try:
        sheet_name = 'Index'
        df_temp1 = df_new.parse(sheet_name)
        df_temp2 = df_old.parse(sheet_name)
        df_temp1 = df_temp1[df_temp1['Index'] == 'Equity']
        df_temp2 = df_temp2[df_temp2['Index'] == 'Equity']
        sheet_names_new = df_temp1['Unnamed: 1'].tolist()
        sheet_names_old = df_temp2['Unnamed: 1'].tolist()
        writer = pd.ExcelWriter(output_file, mode='w')
        for name in sheet_names_new:
            if name in sheet_names_old:
                print(name)
                df1 = df_new.parse(name)
                df2 = df_old.parse(name)
                date1 = f.date_extract(df1)
                month_date1 = str(date1.month)+'_'+str(date1.day)
                logging.debug(" Month df1 : %s",month_date1)
                date2 = f.date_extract(df2)
                month_date2 = str(date2.month)+'_'+str(date2.day)
                logging.debug(" Month df2 : %s",month_date2)
                assert(date1.month - date2.month == 1)
                logging.debug("Assertion correct")
                dftmp1, qty1, mkt1, pnav1 = f.create_df(df1,month_date1)
                dftmp2, qty2, mkt2, pnav2 = f.create_df(df2,month_date2)
                logging.debug("new df created")
                dftmpx1 = dftmp1[dftmp1['INDUSTRY'].notna()]
                logger.debug("df1_shape : %s",dftmpx1.shape)
                dftmpx2 = dftmp2[dftmp2['INDUSTRY'].notna()]
                logger.debug("df2_shape : %s",dftmpx2.shape)
                dftmpx1 = dftmp1[dftmp1['ISIN Code'].notna()]
                print(dftmpx1.columns)
                dftmpx2 = dftmp2[dftmp2['ISIN Code'].notna()]
                #dftmpx1 = dftmp1[dftmp1[nav].notna()]
                #dftmpx2 = dftmp2[dftmp2[nav].notna()]
                dftmp = pd.merge(dftmpx1, dftmpx2, how = 'outer', on = ['Stock_Name', 'INDUSTRY', 'ISIN Code'])
                dftmp = dftmp.replace(np.nan, 0)
                dftmp['change'] = dftmp[[qty1, qty2]].apply(lambda x: f.find_change(x[0],x[1]), axis=1)
                dftmp['change_val'] = dftmp[[qty1, qty2]].apply(lambda x: f.find_act_change(x[0],x[1]), axis=1)
                dftmp.to_excel(writer, sheet_name=name)
        writer.save()
    except Exception:
        logger.debug("Unexpected Error")
main()        