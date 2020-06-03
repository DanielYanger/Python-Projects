import os
import csv

import json

with open(r"D:\Downloads\Match 1_ 1477.json") as f:
  data = json.load(f)

for key in data:
    print(key)
    print(data[key])