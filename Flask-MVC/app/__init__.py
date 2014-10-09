from flask import Flask, render_template

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error = error), 404

from app.mod_home.controllers import mod_home as home_module
from app.mod_test.controllers import mod_test as test_module
app.register_blueprint(home_module)
app.register_blueprint(test_module)

db.create_all()
