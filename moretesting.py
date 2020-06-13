
import json
import os
import sys

try:
  import requests
except ImportError:
  print ("Trying to Install required modules: requests")
  os.system('python -m pip install requests')


#creating a new file
username = os.getlogin()
f = open(f'C:\\Users\\{username}\\Desktop\\schedule.txt',"w")

#making a sorted list
qual_matches=[]
file = open(r"D:\Documents\JSON\PitMasterData.json")
json_data = json.load(file)


#yeet decided to learn json instead
for i in json_data:
    print(i)


