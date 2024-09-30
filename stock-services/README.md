# MicroServices in Python: Stock services
Open Python Microservices

sure-ally\sure-py-ms> python -m venv ms
sure-ally\sure-py-ms> .\ms\Scripts\activate
sure-ally\sure-py-ms> pip list
Package Version
------- -------
pip     24.0

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

sure-ally\sure-py-ms\stock-services> pip install -r .\requirements.txt
sure-ally\sure-py-ms\stock-services> python .\stockAPI.py        
 * Serving Flask app 'stockAPI'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit


Test http://127.0.0.1:5000/stock/NVDA

sure-ally\sure-py-ms\stock-services> docker build -t sure-py-stock-services .
sure-ally\sure-py-ms\stock-services> docker run -d -p 5000:5000 --name sure-py-stock-services sure-py-stock-services:latest

Test http://127.0.0.1:5000/stock/NVDA

sure-ally\sure-py-ms\stock-services> docker tag sure-py-stock-services:latest ysurendrak/sure-py-stock-services:latest  
sure-ally\sure-py-ms\stock-services> docker push ysurendrak/sure-py-stock-services:latest    

-- To update docker image
sure-ally\sure-py-ms\stock-services> docker build -t sure-py-stock-services .
sure-ally\sure-py-ms\stock-services> docker tag sure-py-stock-services:latest ysurendrak/sure-py-stock-services:latest
sure-ally\sure-py-ms\stock-services> docker push ysurendrak/sure-py-stock-services:latest  