from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#DB
app.config()

# Routes

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Here we go again'})



# run server
if __name__ == '__main__':
    app.run(debug=True)


