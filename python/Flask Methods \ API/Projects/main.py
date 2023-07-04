from flask import *
from db import *
from threading import Thread
from random import randint

user.create()

if not user.get(123):
  user.insert(123, randint(1, 10000), 'None')
  user.insert(145, randint(1, 10000), 'None')
  user.insert(167, randint(1, 10000), 'None')
  user.insert(189, randint(1, 10000), 'None')
  user.insert(200, randint(1, 10000), 'None')

app = Flask('')


@app.route('/')
def index():
  return '<h1> Hello, World! </h1><br><h2> With love, SARTON DEV! </h2>'


@app.route('/user')
def get_user():
  value = request.args.get('id')
  if value:
    user_data = user.get(int(value))
    if user_data:
      return str(user_data)
    else:
      return 'Unknown user.'
  else:
    return 'Unknown parameter "id".'


@app.route('/user.get', methods=['GET', 'POST'])
def post_user():
  if request.method == "POST":
    value = request.json
    if type(value['id']) in [int, list]:
      json = {'data': []}
      data = user.get(value['id'])
      if data:
        if type(data) == list:
          for i in data:
            json['data'].append({'user_id': i[0], 'balance': i[1]})
        else:
          json['data'].append({'user_id': value['id'], 'balance': data})
        return jsonify(json)
      else:
        return jsonify({"Error": "Unknown user."})
    else:
      return jsonify({"Error": "Unsupported value."})


def run():
  app.run(host='0.0.0.0', port=8080)


def th_start():
  site = Thread(target=run)
  site.start()


th_start()
