from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db

mod_test = Blueprint('test', __name__, url_prefix='/module')

#default index route for this module
@mod_test.route('/', methods=['GET', 'POST'])
def index():
	return render_template('test/index.html', content = 'the index page for the "test" module')
