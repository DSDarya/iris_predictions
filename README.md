# iris_predictions

## Даные

Ирисы Фишера состоят из данных о 150 экземплярах ириса, по 50 экземпляров из трёх видов — Ирис щетинистый (Iris setosa), Ирис виргинский (Iris virginica) и Ирис разноцветный (Iris versicolor). Для каждого экземпляра измерялись четыре характеристики (в сантиметрах):

1. Длина наружной доли околоцветника (sepal length);
2. Ширина наружной доли околоцветника (sepal width);
3. Длина внутренней доли околоцветника (petal length);
4. Ширина внутренней доли околоцветника (petal width).
На основании этого набора данных требуется построино правило классификации, определяющее вид растения по данным измерений (три вида ириса).

## Руководство

Убедитeсь, что Docker установлен на устройстве.

### Для запуска без отладки 
1. Загрузите образ https://hub.docker.com/r/dsdarya1/iris_app?uuid=6F30575E-5D7C-4695-8C80-EE24C8253ACD
2. Создайте файл .env, который будет содержать переменную порта APP_PORT (docker port) и AUTHOR.
  Пример:
  APP_PORT=8888
  AUTHOR="developer"
3. Запустите контейнер командой docker container run --publish **your_device_port**:	**your_app_port** --env-file 	**your_path_to_env/**.env  -d  dsdarya1/iris_app
Пример: *docker container run --publish 8015:8888 --env-file iris_predictions/.env  -d  dsdarya1/iris_app*

### Для запуска с возможностью отладки
1. Загрузите образ https://hub.docker.com/r/dsdarya1/iris_app?uuid=6F30575E-5D7C-4695-8C80-EE24C8253ACD
2. Склонируйте репозиторий https://github.com/DSDarya/iris_prediction
3. Запустите контейнер с дополнительным флагом --volume
Пример: *docker container run --publish 8015:8888 --env-file .env --volume=/home/klokonos/iris/project/app:/app/app -d  iris_app*

## Работа с контейнером
Перейти по http://localhost:{your_port}/docs#
1. Выполнить get-запрос. Если отобразится {"status": "OK"}, контейнер запущен правильно.
2. Выполнить post-запрос http://localhost:8015/docs#/default/iris_predictions_species__post - предсказание вида ириса, либо http://localhost:8015/docs#/default/iris_predictions_species_probability__post - вероятность принадлежности к каждому из классов.
Необходимо установить каждый из параметров:
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm  
Пример запроса: *{"SepalLengthCm": 1,"SepalWidthCm": 2,"PetalLengthCm": 3.4,"PetalWidthCm": 5.0}*
