from flask import Flask
import peewee
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')
manager = Manager(app)
from banco_config import BancoConfig
from app.models import dados
from app.controllers import default