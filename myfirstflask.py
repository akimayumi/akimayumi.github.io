# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 19:38:37 2023

@author: janet
"""

#Basic structure
#Flask login
from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

#flask routing
@app.route("/")
@app.route("/home")

def home():
    return render_template("home.html")

@app.route("/html")
def html():
    return render_template("new.html")

@app.route("/home/<name>")
def user(name):
    return f"Hello {name}! Welcome to this page."

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/logout")
def logout():
    return redirect(url_for("home")) #passing the name of homepage function

@app.route("/submit",methods=['POST','GET'])
#note get method will display the content. DON'T use in passwords.
def submit():
    if request.method =='POST':
        user = request.form['nm']
        return f" Login Successfully. Hello {user}!"
    else:
        user = request.args.get('nm')
        return f" Login Successfully. Hello {user}!"

if __name__ =='__main__':
    app.run()
    

