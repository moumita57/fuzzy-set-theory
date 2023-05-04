"""
  Author: Dr Moumita Deb
  This script demonstrates how python can parse a csv file using csv and pandas data frames
"""

import csv
import pandas as pd

filename = "data.csv"

with open(filename, 'r') as output:
  csv_reader = csv.reader(f, quotechar="'", skipinitialspace=True)
  for line in csv_reader:
        print(line)
      

df = pd.read_csv(filename)
print(df)
print(type(df['Age'][0]))
print(type(df['Height(cm)'][0]))
print(type(df['Weight(kg)'][0]))

df = pd.read_csv(filename, 
            index_col='Name', 
            names=['Name', 'Age', 'Height(cm)', 'Weight(kg)']
                    )
print(df)
df = pd.read_csv(filename, 
            index_col='Name', 
            names=['Name', 'Age', 'Height(cm)', 'Weight(kg)']
                    )
df.to_csv('my_new_family.csv')
