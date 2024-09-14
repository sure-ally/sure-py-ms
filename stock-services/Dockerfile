# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

WORKDIR /sure-py-stock-api

COPY stockAPI.py requirements.txt /sure-py-stock-api/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#Start NginxService 
ENTRYPOINT ["python"]

CMD ["stockAPI.py"]