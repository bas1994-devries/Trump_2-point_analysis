from zipfile import ZipFile
import os
import time
import datetime

fn = '../../data/team23_trump_medical_suggestions_usa.zip'
fn2='../../data/team13_covid19_briefing_usa.zip'
extract_dir = '../../gen/data-preparation/temp'

os.makedirs(extract_dir, exist_ok=True)

# Create a ZipFile Object and load sample.zip in it
with ZipFile(fn, 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(extract_dir)

f = open('../../gen/data-preparation/temp/unzipping.log','w')
ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
f.write('done at ' + sttime + '\n')
f.close()

with ZipFile(fn2, 'r') as zipObj2:
   # Extract all the contents of zip file in different directory
   zipObj2.extractall(extract_dir)

f = open('../../gen/data-preparation/temp/unzipping.log','a')
ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
f.write('done at ' + sttime + '\n')
f.close()
