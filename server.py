from flask import Flask, render_template, request, redirect, session
from users_app import app
from users_app.controllers import users_controller

app = Flask( __name__ )
app.secret_key = "secret"

@app.route( "/" )
def displayLogin():
    return redirect ('/users')


@app.route( "/users" )
def displayAllUsers():
    return render_template( "Read.html")

@app.route('/user/new')
def new():
    return render_template("Create.html")


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
    return redirect( '/users' )





if __name__ == "__main__":
    app.run( debug = True )


# @app.route('/')
# def index():
#     return redirect('/users')


# @app.route('/users')
# def users():
#     return render_template("users.html",users=User.get_all())


# @app.route('/user/new')
# def new():
#     return render_template("new_user.html")

# @app.route('/user/create',methods=['POST'])
# def create():
#     print(request.form)
#     User.save(request.form)
#     return redirect('/users')


# if __name__=="__main__":
#     app.run(debug=True)

