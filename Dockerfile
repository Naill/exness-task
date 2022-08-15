FROM python:3.8
MAINTAINER Dmitriy Penkrat
VOLUME http-server
COPY . /app
RUN pip3 install -r requirements.txt
# Надо подправить установку необходимых пакетов и модулей
# так же надо произвести очистку образа после

ENTRYPOINT ["python3.8", "/app/main.py"]