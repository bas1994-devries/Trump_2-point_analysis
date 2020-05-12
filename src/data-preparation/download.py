import requests
import os

print('Downloading raw data... please wait.')

data = requests.get('https://uvt-public.s3.eu-central-1.amazonaws.com/data/rsm2020/team23_trump_medical_suggestions_usa.zip')
data2 = requests.get('https://uvt-public.s3.eu-central-1.amazonaws.com/data/rsm2020/team13_covid19_briefing_usa.zip')

print('Writing raw data to file')

os.makedirs('../../data', exist_ok=True)

f = open('../../data/team23_trump_medical_suggestions_usa.zip', 'wb')
f2 = open('../../data/team13_covid19_briefing_usa.zip', 'wb')

f.write(data.content)
f2.write(data2.content)


f.close()
f2.close()

print('Done.')
