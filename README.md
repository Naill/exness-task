# Сборка и запуск приложения

1. Необходимо собрать контейнер, а так же указать в файле конфигурации использовать sqlite или файл для сохранения данных  пост запросов. True сохранять в базе,  False сохранять в файле.

```
[default]
db_safe=True
```

2. Если проверяем в minikube, то необходимо собрать наш контейнер для него
```
eval $(minikube docker-env)
https://minikube.sigs.k8s.io/docs/handbook/pushing/
```

3. Сборка контейнера:
```
docker build -t http-server .
```

4. В случае, если мы разворачиваем на голом кластере, то необходимо добавить сущности prometheus-operator: servicemonitor, alertmanager etc.:
```
kubectl create -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/master/bundle.yaml
```

5. Задеплоить контейнер в Kubernetes:
```
helm upgrade --install  -f ./http-server/values.yaml   http ./http-server
```
6. Мы можем поднять контейнер и с него отправить запросы на наш под, сервис:
```
kubectl run -t -i --rm --image amouat/network-utils netwutils bash
Отправка запроса
curl -X GET http-http-server/hello
```

# Задание
# DevOps/SRE Engineer BI

1. Написать web-сервер на Go/Python:

    1.1 При **GET** запросе на эндпойнт **/hello** сервер должен отдавать текст “Hello Page”

    1.2 При **POST** запросе на эндпойнт **/user** с параметром **name=\*имя пользователя\*** (пример: **.../user name=Joe**) сервер должен сохранять в текстовых лог-файл имя пользователя и время запроса (формат - **name: hh:mm:ss - dd.mm.yyyy**)

    1.3 Добавить возможность опционально использования SQLite вместо файла лога для сохранения имени пользователя и времени в таблицу **users** и возвращать эти данные по **GET** запросу с теми же параметрами (пример: **.../user?name=Joe**)

    1.4 Добавить эндпойнт **/metrics** который в prometheus-совместимом формате будет отдавать метрики по количеству обработанных **GET** и **POST** запросов

2. Написать helm-chart для вашего приложения.

    2.1 Чарт должен создавать service, deployment c томом для сохранения лог-файла или SQLite db-файла

    2.2 Возможность опционально указать селектор ноды на которую необходимо выкатить приложение

    2.3 Возможность опционально добавить serviceMonitor для сбора метрик prometheus-сервером