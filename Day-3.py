from flask import Flask
import os
import json
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s")
log=logging.getLogger(__name__)
app=Flask(__name__)
@app.route("/")
def hello():
   return "hello dostoh"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
