from flask import Flask, render_template, request, redirect, session
from users_app import app
from User import User

app = Flask( __name__ )
app.secret_key = "secret"

@app.route( "/users", methods=['GET'] )
def displayAllUsers():
    loginError = ""
    if 'loginError' in session:
        loginError = session['loginError']
    return render_template( "index.html", loginError=loginError )


@app.route( "/users/new", methods=['POST'] )
def validateCredentials():
    userName = request.form['userName']
    userPassword = request.form['userPassword']
    identifier = request.form['identifier']
    print( 'Identifier', identifier )
    for user in users:
        if user['username'] == userName and user['password'] == userPassword:
            session['userName'] = userName
            if 'loginError' in session:
                session.pop( 'loginError' )
            return redirect( '/home' )
    session['loginError'] = "Wrong credentials provided."
    return redirect( '/login' )





if __name__ == "__main__":
    app.run( debug = True )




