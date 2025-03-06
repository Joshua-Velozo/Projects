import random
from flask import Flask, jsonify
from hashlib import sha256


app = Flask(__name__)


@app.route('/')
def hello_world():
   # return true or false
   return random.choice(['true', 'false'])




@app.route('/get_chain/<name>', methods=['GET'])
def chain(name):
   return jsonify({"chain": sha256(name.encode()).hexdigest(), "length": 16})




if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5555)
