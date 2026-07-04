from flask import Flask
import os
import json
app=Flask(__name__)
@app.route("/")
def hello():
   return {"hello dostoh"}

app.run(host="0.0.0.0",port=8000)
