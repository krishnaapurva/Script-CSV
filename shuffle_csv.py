# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:11:50 2019

@author: Hp
"""

import numpy as np
import pandas as pd

def shuffler(filename):
  df = pd.read_csv(filename, header=0)
  # return the pandas dataframe
  return df.reindex(np.random.permutation(df.index))


def main(outputfilename):
  shuffler('combine_csv.csv').to_csv(outputfilename, sep=',')

if __name__ == '__main__': 
  main('final.csv')