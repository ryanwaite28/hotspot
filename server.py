import sqlite3, json, random, string

from functools import wraps
from datetime import timedelta
from threading import Timer
from werkzeug.utils import secure_filename

from flask import Flask
from flask import request, redirect, jsonify
from flask import session as user_session

from flask_socketio import SocketIO

import handler_get as GET 
import handler_post as POST 
import handler_put as PUT 
import handler_delete as DELETE 



# --- Setup --- #

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DF6Y#6G15$B^*R&&NT*Y(U)I_+DF&D((A-_*DFj/Y4DR'
socketio = SocketIO(app)

def login_required(f):
  ''' Checks If User Is Logged In '''
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'session_id' in user_session:
      return f(*args, **kwargs)
    else:
      # flash('Please Log In To Use This Site.')
      return redirect('/signin')

  return decorated_function

def ajax_login_required(f):
  ''' Checks If User Is Logged In '''
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'session_id' in user_session:
      return f(*args, **kwargs)
    else:
      return jsonify(error = True, message = 'Not signed in')

  return decorated_function

# --- Routes --- #

@app.route('/', methods=['GET'])
def welcome():
  return GET.welcome(request, user_session)

@app.route('/check_session', methods=['GET'])
def check_session():
  return GET.check_session(request, user_session)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)