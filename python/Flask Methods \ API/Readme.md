<h1> Hello, world! </h1>

<h2>Flask методы | Делаем первый API для сайта с использованием SQLite</h2>

<b>Преимущества:
> Данный урок научит вас создавать API для своего сайта или проекта. С помощью его вы сможете разнообразить функционал своего сайта или проекта, позволить другим пользователям работать с вашим сайтом или проектом через GET & (И) POST Запросы.</b>

И так, начнем с создания обычного сайта через Flask:
Данный урок посвящается другому, поэтому мы не будем разбирать основы создания самого обычного приложения (Или - сайта) Flask, сразу напишем самый стандартный готовый код обычного Flask, с использованием потоков (Чтобы данный код можно было запустить через другой код без перебоев):

main.py: (Основной файл)
```python
from flask import *
from db import *
from threading import Thread
from random import randint

user.create()
if not user.get(123):
  user.insert(189, randint(1,100000), "GheEufsbXJD")
  user.insert(123, randint(1,100000), "DFSHJejkrwDS")
  user.insert(167, randint(1,100000), "DHJFHuewyruGJgdhSG")
  user.insert(200, randint(1,100000), "HjSHJieUINXh")
  user.insert(145, randint(1,100000), "UIREUWIO832FDSdsk")

app = Flask('')

@app.route("/")
def index():
  return "Hello, World! It's me, SARTON!"

def run():
  app.run(host="0.0.0.0", port=8080)

def th_start():
  site = Thread(target=run).start()

th_start()
```

Файл db.py - это наша база SQLite, которую мы и будем использовать в нашем проекте как пример. Данный код достаточно большой, поэтому мы его просто загрузили как файл (В папке <b>Projects</b>)

<h3> Обрабокта GET Запроса </h3>
Продолжаем работу с предыдущим кодом.
Начнем работать с GET Запросом. Что работает метод GET?
- Просто и легко. Мы передаем прямо в ссылке нужные параметры, достаем их оттуда и совершаем необходимые действия.

Принимать запросы мы будем через ссылку: /user.get
Принимать будем параметр id - Идентификатор пользователя
Возвращать: balance - баланс пользователя с идентификатором id
Пример ссылки: URL/user.get?id=123

Обрабатываем ссылку:
```python
@app.route("/user.get")
def userget():
  ...
```

И так, чтобы достать из ссылки параметр id (URL/user.get?id=123), мы должны использовать функцию Flask'a - request:
```python
value = request.args.get('id')
```
> В данном коде мы достаем из ссылки параметр id и присваем значение параметры переменной value

Чтобы отправить пользователю ответ, мы должны использовать самый обычный return (Он возвращает самый обычный текст сайту), точнее:
```python
return 'Thanks for use GET Response!'
```

Сразу же добавим проверку переменной, чтобы отправить свою ошибку:
```python
if value:
  ...
else:
  return 'Unknown parameter id'
```

Но, наш урок посвящен файловой базе SQLite, поэтому мы получим баланс пользователя с переданным id и покажем его пользователю:
```python
user_data = user.get(value)
if user_data:
  return str(user.get(value))
else:
  return 'Unknown user.'
```

user.get(value) - это мы получаем баланс пользователя. Подробнее ознакомиться с базой вы можете в файле db.py (Расположен в папке <b>Project</b>)
По итогу получаем следующий код:
```python
@app.route('/user.get')
def userget():
  value = request.args.get('id')
  if value:
    user_data = user.get(value)
    if user_data:
      return str(user.get(value))
    else:
      return 'Unknown user'
  else:
    return 'Unknown parameter id'
```

Запускаем код. Выполняем GET запрос: .../user.get?id=123
Получаем: (Баланс)
GET Запрос готов.

<h3>Обработка POST Запроса</h3>
Тут уже слегка побольше придеться писать, но не на много.
Добавим обработку POST Запроса к ссылке: /user.get (Пока не используйте код с GET Запросом, либо поменяйте там ссылку)
```python
@app.route("/user.get", methods=["GET", "POST"])
def userget():
  ...
```
> В данной обработке обязательно в параметре methods нужно добавить GET, иначе будут неизбежные ошибки.

С POST Запросами необходимо добавить побольше условий, самое первое: проверка на сам запрос, чтобы мы работали именно с POST:
```python
if request.method == "POST":
  ...
```

Чтобы получить переданные данные JSON через POST Запрос, нужно использовать опять же функцию request:
```python
value = request.json
```
Мы будем рассматривать JSON, в котором будем передавать параметр id.

Далее, добавим проверку типа переданного значения в JSON:
```python
if type(value['id']) in [int, list]:
  ...
else:
  jsonify({"Error": "Unsupported value"})
```

> В данном коде мы проверяем тип значения переданного параметра id. Если тип этого значения равняется int (Числу) или list (Списку), то продолжим выполнять код, а иначе вернем JSON:
> ```json
> "Error": "Unsupported value"
> ```

Дальше, получим данные о пользователе с идентификатором id и сразу его проверим на наличие значения:
```python
data = user.get(value['id'])
if data:
  ...
else:
  jsonify({"Error": "Unknown user"})
```

Ну, поскольку user.get вернет нам список балансов даже если мы передадим 1 id (Не списком), то поочередно в json (возвращаемый объект) добавим все данные:
```python
for i in data:
json['data'].append(
  {
    "user_id": i[0],
    "balance": i[1]
  }
)
```

И, после чего, вернем переменную json со всеми данными пользователю, совершившому POST Запрос с помощью функции Flask - jsonify:
```python
return jsonify(json)
```

Итоговый код POST Запроса:
```python
@app.route('/user.get', methods=['GET', 'POST'])
def userget():
  if request.method == "POST":
    value = request.json
    if type(value['id']) in [int, list]:
      json = {
        'data': []
      }
      data = user.get(value['id'])
      if data:
        for i in data:
          json['data'].append({
            'user_id': i[0],
            'balance': i[1]
          })
          return jsonify(json)
      else:
        return jsonify({"Error": "Unknown user"})
    else:
      return jsonify({"Error": "Unsupported value"})
```

Готово. Проверим:
Выполним запрос к ссылке URL/user.get
Передадим JSON:
```python
{'id': 123}
```

Получим: 
```python
{
  'data': [
    {'user_id': 123, 'balance': (Баланс)}
  ]
}
```

Выполним опять такой же запрос, только в JSON укажем список нескольких ID:
```python
{'id': [123,145,189]}
```

Получим:
```python
{
  'data' [
    {'user_id': 123, 'balance': (Баланс)},
    {'user_id': 145, 'balance': (Баланс)},
    {'user_id': 189, 'balance': (Баланс)}
  ]
}
```

Конечный код main.py находится в папке <b>Projects</b> вместе с готовой базой db.py
Конечный код немного отличается ссылками: 
Для GET Запроса действует ссылка: URL/user?id=123
Для POST Запроса: URL/user.get
