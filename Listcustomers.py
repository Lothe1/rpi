from flask import Flask
app = Flask(__name__)
@app.route('/')

import mysql.connector
mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="",
    database="gamz"
    )

mycursor = mydb.cursor()

def hello():
    query = "select * from customers"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for row in result:
        return "<h1>"+ row "</h1>"


