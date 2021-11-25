from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:27072000@localhost/finalproj?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# Cần có key để thao tác với session
app.secret_key = "AG(ASDAGIA(*&!@"

#đặt tên j cx dc: PAGE_SIZE
#app.config["PAGE_SIZE"] = 3

db = SQLAlchemy(app=app)
admin = Admin(app=app, name = "MY SHOP", template_mode = 'bootstrap4')
my_login = LoginManager(app=app)
CART_KEY = "cart" 


from flask_mail import Mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":'hieuduong959@gmail.com',
    "MAIL_PASSWORD": 'llwajaaonjffyxgv'
}

app.config.update(mail_settings)
mail = Mail(app)