from flask import Flask
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A5CF8ZH73XOSXG4PH9BD'

from app import routes
