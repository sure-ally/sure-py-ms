# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

WORKDIR /sure-py-news-api

COPY newsAPI.py requirements.txt /sure-py-news-api/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# The EXPOSE instruction doesn't actually publish the port. 
# It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. 
EXPOSE 5000

#Start NginxService 
ENTRYPOINT ["python"]

CMD ["newsAPI.py"]