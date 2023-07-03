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

@app.route('/user')
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

def run():
  app.run(host="0.0.0.0", port=8080)

def th_start():
  site = Thread(target=run).start()

th_start()
