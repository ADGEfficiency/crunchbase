import csv

import requests


url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"
querystring = {"locations": "Berlin"}
headers = {
    'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
    'x-rapidapi-key': "df8b647b2cmsh81bb0369bb5eed1p1d8a9cjsn39ae7bdb735d"
    }
response = requests.request("GET", url, headers=headers, params=querystring).json()

header = response['data']['items'][0]['properties'].keys()

with open('crunchbase.csv', 'a') as f:
    w = csv.DictWriter(f, header)
    # w.writeheader()
    for data in response['data']['items']:
        w.writerow(data['properties'])
