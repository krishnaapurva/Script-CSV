# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import os
with open(r'PATH FOR CSV FILE','w', newline = '') as f:
    fieldnames = ['COLUMN 1','COLUMN 2']
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    
    thewriter.writeheader()
    for img in os.listdir(r'PATH OF DIRECTORY/FOLDER'):
        thewriter.writerow({'COLUMN 1':img,'COLUMN 2':1})