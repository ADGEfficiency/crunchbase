import csv

import requests

from keys import headers


url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"

querystring = {'pagesize': "10"}
response = requests.request("GET", url, headers=headers, params=querystring).json()

header = response['data']['items'][0]['properties'].keys()

with open('crunchbase.csv', 'a') as f:
    w = csv.DictWriter(f, header)
    for data in response['data']['items']:
        w.writerow(data['properties'])
