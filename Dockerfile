FROM python:3.8
MAINTAINER Dmitriy Penkrat <penkrat.dm@gmail.com>

#Port 8001 for prometheus
#Port 8000 for other requests
EXPOSE 8001 8000

VOLUME http-server /app/data
COPY . /app
RUN pip3 install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python3.8", "-u", "/app/main.py"]