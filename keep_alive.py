from flask import Flask
from threading import Thread

app = Flask(_name_)

@app.roete('/')
def home():
  return "Bot is running!"

def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
