# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:21:37 2020

@author: Naga Raghavendra
"""

import re

date_pat1 = re.compile(r'\d\d-\d\d-\d{2,4}')
date_pat2 = re.compile(r'\d\d/\d\d/\d{2,4}')

