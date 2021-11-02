from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key= 'The Cake is a Lie'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'WonderousTrope'
app.config['MYSQL_PORT'] = 3306

db= MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)