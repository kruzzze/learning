from flask import Flask
from flask import request,jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
  
@app.route('/users/')
def getUsers():
  return jsonify({'status': 200,
                  'msg': 'NU PRIVET'}), 200

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)