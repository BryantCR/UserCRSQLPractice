from flask import render_template, request, redirect
from users_app import app
from users_app.models.User import User

@app.route( "/hola", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "users.html", users=users )

@app.route( "/hola/add", methods=['POST'] )
def addUser():
    username = request.form['username']
    password = request.form['password']

    newUser = User( username, password )
    result = User.add_user( newUser )
    print( result )
    return redirect( "/users" )

@app.route( "/hola/delete", methods=['POST'] )
def deleteUser():
    username = request.form['deleteUsername']
    result = User.delete_user( username )
    print( result )
    return redirect( "/users" )