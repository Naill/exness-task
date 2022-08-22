FROM python:3.8
MAINTAINER Dmitriy Penkrat <penkrat.dm@gmail.com>

EXPOSE 8080
VOLUME http-server /app/data
COPY . /app
RUN pip3 install -r /app/requirements.txt
# Надо подправить установку необходимых пакетов и модулей
# Надо произвести очистку образа после
# Надо добавить проброс портов и под каким портом работать контейнеру
WORKDIR /app
ENTRYPOINT ["python3.8", "/app/main.py"]