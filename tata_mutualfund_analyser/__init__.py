# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:18:51 2020

@author: Naga Raghavendra
"""

import pandas as pd
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

df_new = pd.ExcelFile('.//data//in//monthly_portfolio_as_on_31st_march_2020.xls')
df_old = pd.ExcelFile('.//data//in//monthly-portfolio-as-on-29th-february-2020.xls')
output_file = ".//data//out//MutualFund_Analysis_Mar_Feb.xlsx"