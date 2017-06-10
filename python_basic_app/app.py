from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from models import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:prdxn2017@localhost/OZE-db'
app.debug = True
db = SQLAlchemy(app)


@app.route('/')
def index():
  return jsonify({'test': 'Ani'})


@app.route('/user-data', methods=['POST'])
def userData():
  name = request.form['name']
  email = request.form['email']
  userozeData = Useroze(name, email)
  db.session.add(userozeData)
  db.session.commit()
  return jsonify({'test': [{'name': name, 'email': email}]})


if __name__ == '__main__':
  app.debug = True
  app.run()