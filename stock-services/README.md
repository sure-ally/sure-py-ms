# sure-py-ms
Open Python Microservices

sure-ally\sure-py-ms> python -m venv ms
sure-ally\sure-py-ms> .\ms\Scripts\activate
sure-ally\sure-py-ms> pip list
Package Version
------- -------
pip     24.0

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

sure-ally\sure-py-ms> pip install -r .\requirements.txt
sure-ally\sure-py-ms> python .\getStockQuote.py        
 * Serving Flask app 'getStockQuote'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit


Test http://127.0.0.1:5000/stock/NVDA