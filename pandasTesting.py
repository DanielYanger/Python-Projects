import os
import shutil

try:
  import pandas as pd
except:
  print ("Trying to Install required modules: pandas")
  os.system('python -m pip install pandas')
  import pandas as pd
  print("hello")

