# This is whre you can start you python file for your week1 web app
# Name: Tharathorn Rimchala

#!/usr/bin/env python 
import flask, flask.views
import os
import functools
app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

# Dictionary of username and password
users = {'jrimchala':'bacon', 
		'jrimchala2':'lovebacon',
		'jrim':'bacony'}

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self):
    	# Check if user need to log out
    	if 'logout' in flask.request.form:
    		# Pop user out of session
    		flask.session.pop('usr', None)
    		return flask.redirect(flask.url_for('index'))

    	required = ['usr','pswd']
    	for r in required:
    		if r not in flask.request.form:
    			flask.flash("Error: {0} is required.".format(r))
    			return flask.redirect(flask.url_for('index'))
    	# Receive usr, pwd input
    	usr = flask.request.form['usr']
    	pswd = flask.request.form['pswd']
    	# Check that usr and pwd exist in dictionary
    	if usr in users and users[usr] == pswd:
    		# Accept user
    		flask.session['usr'] = usr
    	else:
    		flask.flash("Username does not exist or incorrect password")
    	# Return to index paage
    	return flask.redirect(flask.url_for('index'))

# Decorator protecting Remote view
def login_required(method):
	@functools.wraps(method)
	# Define wrapper
	def wrapper(*args, **kwargs):
		if 'usr' in flask.session:
			# User in session, Ok to call method
			return method(*args, **kwargs)
		else:
			flask.flash("Please log in to access your dashboard")
			return flask.redirect(flask.url_for('index'))
	return wrapper

class Remote(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remote.html')

	@login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

class Music(flask.views.MethodView):
    @login_required
    def get(self):
        # Song directory
        songs = os.listdir('static/music/')
        return flask.render_template('music.html', songs=songs)
    
app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])

app.debug = True
app.run()