# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:22:56 2020

@author: Naga Raghavendra
"""

import patterns as pt
import datetime
import re
from __init__ import logger

def date_extract(df):
    date_loc = df.iloc[3:4,1]
    date_loc1 = re.findall(pt.date_pat1, str(date_loc))
    date_loc2 = re.findall(pt.date_pat2, str(date_loc))
    if len(date_loc1) != 0:
        logger.debug("%s",date_loc1)
        date = datetime.datetime.strptime(date_loc1[0], "%d-%m-%y")
        return date
    elif len(date_loc2) != 0:
        logger.debug("%s",date_loc2)
        date = datetime.datetime.strptime(date_loc2[0], "%d/%m/%y")
        return date
    else:
        date = 'Null'
        return date

def create_df(df, month_date):
    qty = 'Quantity_'+month_date
    mkt_val = 'Market_val_'+month_date
    nav = 'pnav_'+month_date
    dftmp = df.iloc[8:,1:7]
    dftmp = dftmp.rename(columns = {df.columns[1]:'Stock_Name', 'Unnamed: 2' : 'INDUSTRY', 'Unnamed: 3' : 'ISIN Code',
       'Unnamed: 4' : qty, 'Unnamed: 5' : mkt_val, 'Unnamed: 6': nav })
    return dftmp, qty, mkt_val, nav


def find_change(new, old):
    try:
        old = int(old)
        new = int(new)
        if old==0:
            return "New"
        elif new == 0:
            return "Sold"
        elif old > new:
            return "Decrease"
        elif old == new:
            return "No Change"
        elif old < new:
            return "Increase"
    except Exception:
        return "NA"
    
    
def find_act_change(new, old):
    try:
        old = int(old)
        new = int(new)
        if old == 0:
            return 100
        elif new == 0:
            return 0
        else:
            chg = abs(new - old)*100/ old
            return int(chg)
    except Exception:
        return "NA"
    
    
