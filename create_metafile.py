import time
import os
import pandas as pd
import numpy as np
from utils import *

config = get_config()


meta_data = []
directory = "dance_moves//"
file_list = os.listdir('dance_moves')
mandatory = ['SitRelax.py','Sit.py','WipeForehead.py','Hello.py', 'Stand.py',
             'StandInit.py','StandZero.py','Crouch.py']

def calculate_duration(config,path):
    start_time = time.time()
    statement = "python " + path + " " + config['ip'] + " " + str(config['port'])
    os.system(statement)
    return round(float(time.time() - start_time),4)


for file_name in file_list:
    entry = {}
    entry['MoveName'] = file_name[:-3]
    entry['FileName'] = file_name
    if file_name in mandatory:
        entry['Mandatory'] = 1
    else:
        entry['Mandatory'] = 0
    entry['Duration'] = calculate_duration(config,directory+file_name)
    entry['Precond'] = np.nan
    entry['Postcond'] = np.nan
    meta_data.append(entry)
    
meta_df = pd.DataFrame().from_records(meta_data)
meta_df.to_csv("meta_data//metadata.csv", sep=";")
print('File created')


    
