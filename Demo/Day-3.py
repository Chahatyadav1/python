from flask import Flask
import os
import json
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
log=logging.getLogger(__name__)
app=Flask(__name__)
@app.route("/")
def hello():
   return {"hello dostoh"}

app.run(host="0.0.0.0",port=8000)
