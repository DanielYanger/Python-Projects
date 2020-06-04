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
#folder=sys.argv[1]
folder = r"D:\Downloads\testing"
onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))] 



try:
  full_data = pd.read_csv(filepath_or_buffer=f'C:\\Users\\{username}\\Desktop\\MatchData.csv')
  dir = join(folder, "complete")
  if not os.path.exists(dir):
    os.mkdir(dir)
  for i in onlyfiles:
    with open(join(folder, i)) as f:
      data = json.load(f)
      data['Match Number']=(f.name[f.name.index('Match ')+6])
      data['Team Number']=(f.name[f.name.index('_ ')+2:f.name.index('.json')])
      full_data = full_data.append(data,ignore_index=True)
    shutil.move(join(folder, i),join(dir,i))
    
  
except FileNotFoundError:
  dir = join(folder, "complete")
  if not os.path.exists(dir):
    os.mkdir(dir)
  for i in onlyfiles:
    with open(join(folder, i)) as f:
      data = json.load(f)
      data['Match Number']=(f.name[f.name.index('Match ')+6])
      data['Team Number']=(f.name[f.name.index('_ ')+2:f.name.index('.json')])
      try:
        full_data = full_data.append(data,ignore_index=True)
      except:
        full_data = pd.DataFrame(data,index=[0])
    shutil.move(join(folder, i),join(dir,i))

full_data.to_csv(f'C:\\Users\\{username}\\Desktop\\MatchData.csv', index=False)


