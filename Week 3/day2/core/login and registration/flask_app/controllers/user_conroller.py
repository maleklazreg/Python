from flask_app import app
from flask import render_template,redirect,request,session,flash # type: ignore
from flask_app.models.user_model import User 
from flask_bcrypt import Bcrypt   # type: ignore

bcrypt=Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["POST"]) 
def register():
    if User.validate(request.form):
        paw=bcrypt.generate_password_hash(request.form["password"])
        data={ 
            **request.form,
            "password":paw
        } 
        user_id=User.create(data) 
        session["user_id"]=user_id
        return redirect("/dashbord")
    
    return redirect("/")
    

@app.route("/login",methods=["POST"])
def login():
    user=User.get_by_email({'email':request.form["email"]})
    if not user: 
        flash("invalid email/pasword","login")
        return redirect('/') 
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("invalid email/pasword","login")
        return redirect('/') 
    session["user_id"]=user.id 
    return redirect('/dashbord') 




@app.route("/logout") 
def logout():
    session.clear()
    return redirect("/")  
    












# from flask_app import app
# from flask import render_template,redirect,request,session,flash # type: ignore
# from flask_app.models.user_model import User 
# from flask_bcrypt import Bcrypt   # type: ignore

# bcrypt=Bcrypt(app)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/register",methods=["POST"]) 
# def register():
#     if User.validate(request.form):
#         paw=bcrypt.generate_password_hash(request.form["password"])
#         data={ 
#             **request.form,
#             "password":paw
#         } 
#         user_id=User.register(data) 
#         session["user_id"]=user_id
#         return redirect("/dashbord")
    
#     return redirect("/")
    

# @app.route("/login",methods=["POST"])
# def login():
#     user=User.get_by_email({'email':request.form["email"]})
#     if not user: 
#         flash("invalid email/pasword","login")
#         return redirect('/') 
#     if not bcrypt.check_password_hash(user.password,request.form['password']):
#         flash("invalid email/pasword","login")
#         return redirect('/') 
#     session["user_id"]=user.id 
#     return redirect('/dashbord') 

#                                 @app.route("/dashbord")
#                                 def dashboard():   
#                                     if not 'user_id'in session:
#                                         return redirect('/')
#                                     logged_user=User.get_by_id({"id":session['user_id']})
#                                     return render_template("dashbord.html", logged_user=logged_user) 

# @app.route("/logout") 
# def logout():
#     session.clear()
#     return redirect("/")  
    