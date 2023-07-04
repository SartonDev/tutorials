from flask import *
from db import *
from threading import Thread
from random import randint

user.create()
if not user.get(123):
  for e in [{
      'id': 123,
      'token': 'hDie38NCXka'
  }, {
      'id': 145,
      'token': 'uei32CCaks'
  }, {
      'id': 167,
      'token': 'AEcDJKwk08'
  }, {
      'id': 189,
      'token': '4778SHasqNC'
  }, {
      'id': 200,
      'token': 'LQP10VX6SbnV'
  }]:
    user.insert(e['id'], randint(0, 100000), e['token'])

app = Flask('')


@app.route('/')
def index():
  return '<h1> Hello, World! </h1><br><h2> With love, SARTON DEV! </h2>'


@app.route('/user')
def get_user():
  value = request.args.get('id')
  if value:
    user_data = user.get(value)
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
        for i in data:
          json['data'].append({'user_id': i[0], 'balance': i[1]})
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
