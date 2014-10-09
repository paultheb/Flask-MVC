from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db

#from app.mod_home.models import Base

mod_home = Blueprint('home', __name__, url_prefix='/')


# default index route
@mod_home.route('/', methods=['GET', 'POST'])
@mod_home.route('index', methods=['GET', 'POST'])
def index():
	return render_template('home/index.html', content = 'home')

# test route
@mod_home.route('test', methods=['GET', 'POST'])
def test():
	return render_template('home/index.html', content = 'test')
