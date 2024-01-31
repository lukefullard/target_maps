"""
Created on Thu Jan 11 08:28:41 2024

@author: lfullard
"""

import pandas as pd

ecoli_file     =  r'ecoli_old.csv'
nutrients_file =  r'nutrients_old.csv'
column_to_remove = 'geometry'

###############################################################################
#ecoli
data = pd.read_csv(ecoli_file,encoding = 'utf-8-sig')
keep_columns = [x for x in data.columns if x != column_to_remove]
data[keep_columns].to_excel(r'ecoli_old.xlsx')
###############################################################################


###############################################################################
#nutrients
data = pd.read_csv(nutrients_file,encoding = 'utf-8-sig')
keep_columns = [x for x in data.columns if x != column_to_remove]
data[keep_columns].to_excel(r'nutrients_old.xlsx')
###############################################################################