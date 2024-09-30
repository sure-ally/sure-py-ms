# MicroServices in Python: News services
Open Python Microservices

Create Python virtual env: 
sure-ally\sure-py-ms> python -m venv ms
sure-ally\sure-py-ms> .\ms\Scripts\activate
sure-ally\sure-py-ms> pip list
Package Version
------- -------
pip     24.0

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

sure-ally\sure-py-ms\stock-services> pip install -r .\requirements.txt

Set API key of newapi.org:
$Env:NEWS_API_KEY='abc123'

sure-ally\sure-py-ms\news-services> python .\newsAPI.py        
 * Serving Flask app 'newsAPI'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.182:5000
Press CTRL+C to quit


Test http://127.0.0.1:5000/news/goog

sure-ally\sure-py-ms\news-services> docker build -t sure-py-news-services .

To test:
sure-ally\sure-py-ms\news-services> docker run -e NEWS_API_KEY='abc123' -d -p 5008:5000 --name sure-py-news-services sure-py-news-services:latest

Test http://127.0.0.1:5008/news/goog

sure-ally\sure-py-ms\news-services> docker tag sure-py-news-services:latest ysurendrak/sure-py-news-services:v1.0  
sure-ally\sure-py-ms\news-services> docker push ysurendrak/sure-py-news-services:v1.0    

-- To update docker image
sure-ally\sure-py-ms\news-services> docker build -t sure-py-stock-services .
sure-ally\sure-py-ms\news-services> docker tag sure-py-stock-services:latest ysurendrak/sure-py-stock-services:latest
sure-ally\sure-py-ms\news-services> docker push ysurendrak/sure-py-stock-services:latest  