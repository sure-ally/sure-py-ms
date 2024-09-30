import os
import http.client
import json
from flask import Flask

# https://newsapi.org/v2/everything?q=TSLA&sortBy=publishedAt&apiKey=abc123&pageSize=2
def getNewsEverything(search = 'MSFT'):

    api_key = os.getenv('NEWS_API_KEY') 
    conn = http.client.HTTPSConnection("newsapi.org")

    headers = {
         'User-Agent': "sure-ally/1.0.0"
    }

    urlPostfix = "/v2/everything?q=" + search + "&sortBy=publishedAt&apiKey=" + api_key + "&pageSize=2"
    print("urlPostfix", urlPostfix, sep=" - ")

    conn.request("GET", urlPostfix, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data)
    de_json= data.decode("utf-8")

    json_data = json.loads(de_json.rstrip().replace("\n", ""))
    return json_data

# APIs start here

api = Flask(__name__)

@api.route('/health', methods=['GET'])
def healthCheck():
    print("Health passed")
    return 'OK', 200  # This will return with a 200 status code
    # If any check fails:
    # return 'ERROR', 500 

@api.route('/news/<search>', methods=['GET'])
def getNewsAll(search):
    print("Search text: " + search)
    newsRes =  getNewsEverything(search)
    return newsRes

if __name__ == '__main__':
    api.run(host="0.0.0.0")