import os
import csv
import pandas as pd
import json


try:
  with open(r"C:\Users\Daniel_Yang\Desktop\Test.csv") as f:
    full_data = pd.read_csv(filepath_or_buffer=f)
  with open(r"D:\Downloads\Match 4_ 2789.json") as f:
    data = json.load(f)
    data['Match Number']=(f.name[f.name.index('Match ')+6])
    data['Team Number']=(f.name[f.name.index('_ ')+2:f.name.index('.json')])
  
  full_data = full_data.append(data,ignore_index=True)
  full_data.to_csv(r"C:\Users\Daniel_Yang\Desktop\Test.csv", index=False)

except FileNotFoundError:
  with open(r"D:\Downloads\Match 4_ 2789.json") as f:
    data = json.load(f)
    data['Match Number']=(f.name[f.name.index('Match ')+6])
    data['Team Number']=(f.name[f.name.index('_ ')+2:f.name.index('.json')])
  
  full_data = pd.DataFrame(data,index=[0])
  full_data.to_csv(r"C:\Users\Daniel_Yang\Desktop\Test.csv", index=False)


