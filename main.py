import code.scrap
import os
import pandas as pd

request_data = pd.read_csv('getdata.csv', names=("name", "address"))
for index, data in request_data.iterrows():
    print(data["name"], data["address"])
    os.makedirs("output/" + data["name"], exist_ok=True)
    code.scrap.imageUrl(data["address"], data["name"])
    # code.scrap.imagebigger(data["name"], 2, 2)
