import pandas as pd
from textblob import TextBlob
import os

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t')


os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('1/2 done.')

## WH briefing
data = pd.read_csv('../../gen/data-preparation/temp/parsed-data2.csv', sep = '\t')

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset2.csv', index = False)

print('1/2 done.')
