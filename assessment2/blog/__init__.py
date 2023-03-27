from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fce01844fa93949a97f8e015a26a1fec71dda83c37c45a17'

# DB Connection

# suppress SQLAlchemy warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# get abs path to the app dir to create the db here
#basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21013017:Tyy19970428@csmysql.cs.cf.ac.uk:3306/c21013017_flask_lab_db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes
