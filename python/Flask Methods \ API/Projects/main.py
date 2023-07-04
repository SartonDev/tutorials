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

def run():
  app.run(host='0.0.0.0', port=8080)


def th_start():
  site = Thread(target=run)
  site.start()


th_start()
