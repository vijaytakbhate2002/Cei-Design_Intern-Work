import requests
import pandas as pd
import time
URL = 'http://api.open-notify.org/iss-now.json'
response = requests.get(URL)

if response.status_code == 200:
    info = response.json()
    df = pd.DataFrame([[info['timestamp'], info['iss_position']['latitude'], info['iss_position']['longitude']]],
                      columns=['timestamp', 'latitude', 'longitude'])
    for i in range(102):
        info = response.json()
        df1 = pd.DataFrame([[info['timestamp'], info['iss_position']['latitude'], info['iss_position']['longitude']]],
                      columns=['timestamp', 'latitude', 'longitude'])
        df = pd.concat([df, df1])
        time.sleep(0.2)
    df.to_csv("Day 2\\Data\\loc_time.csv")

    