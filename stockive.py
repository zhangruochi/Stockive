import json
import requests
import pandas as pd


apikey = "L8KVYT9ERPAC16J7"
symbol = "MSFT"
function = "TIME_SERIES_DAILY"
outputsize = "full"
api = "https://www.alphavantage.co/query?function={}&symbol={}&outputsize={}&apikey={}".format(function,symbol,outputsize,apikey)

def get_realtime_stock_data():
    responses = requests.get(api)
    raw_data = responses.json()

    time_series = raw_data["Time Series (Daily)"]


    meta_data = raw_data["Meta Data"]

    with open('true_data.json', 'w') as outfile:
        json.dump(time_series, outfile)
    

    df = pd.DataFrame(data = time_series).T
    df.columns = df.columns.to_series().apply(lambda x: x.split(".")[-1].strip())

    print(df.shape)

    return df



def main():
    pass
    





if __name__ == '__main__':
    get_realtime_stock_data()
