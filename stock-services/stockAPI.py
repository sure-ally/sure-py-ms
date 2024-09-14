import http.client
import json
from flask import Flask

def getStockDetails(symbol = 'MSFT'):
    conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "abc123",
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

    urlPostfix = "/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&datatype=json"

    conn.request("GET", urlPostfix, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data)
    de_json= data.decode("utf-8")

    json_data = json.loads(de_json.rstrip().replace("\n", ""))
    return json_data

# companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/stock/<symbol>', methods=['GET'])
def getStock(symbol):
    print("Stock Symbol: " + symbol)
    stockRes =  getStockDetails(symbol)
    return stockRes

if __name__ == '__main__':
    api.run(host="0.0.0.0")