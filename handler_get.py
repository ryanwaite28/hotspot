from flask import jsonify, make_response, render_template
from flask import redirect, flash, jsonify, send_from_directory

def welcome(request, user_session):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('welcome.html', logged_in = logged_in, you_id = you_id)

def check_session(request, user_session):
    if 'session_id' in user_session:
        you_id = user_session['you_id']
        user = {}
        return jsonify(online = True, user = user)
    else:
        return jsonify(online = False)