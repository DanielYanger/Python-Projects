import os
import shutil

try:
  import pandas as pd
except ImportError:
  print ("Trying to Install required modules: pandas")
  os.system('python -m pip install pandas')

import csv
import pandas as pd
import json 
import sys
from os import listdir
from os.path import isfile, join


username = os.getlogin()
file = open(sys.argv[1])
json_data = json.load(file)


try:
  full_data = pd.read_csv(filepath_or_buffer=f'C:\\Users\\{username}\\Desktop\\MatchData.csv')
  for i in json_data:
    full_data = full_data.append(i,ignore_index=True)
    
  
except FileNotFoundError:
  for i in json_data:
      try:
        full_data = full_data.append(i,ignore_index=True)
      except:
        full_data = pd.DataFrame()
        full_data = full_data.append(i,ignore_index=True)

print(full_data)
duplicated = full_data.duplicated(keep='last', subset=["Team Number","Match Number"])
index=0
for i in duplicated:
  if i:
    full_data=full_data.drop(full_data.index[index])
    index-=1
  index+=1
print(full_data)

full_data.to_csv(f'C:\\Users\\{username}\\Desktop\\MatchData.csv', index=False)

