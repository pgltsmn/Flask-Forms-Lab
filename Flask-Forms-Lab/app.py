from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "pgltsmn"
password = "ILovePotatoes"
facebook_friends=["Lian","Katya","Anton", "Dima", "Julia", "Lour"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if username == request.form['username'] and password == request.form['password']:
			return render_template('home.html', friends = facebook_friends)
		else:
			return "no"
  
@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def nofriends(name):
	 if name in facebook_friends:
	 	return "yes true"
	 else: 
	 	return "no"



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)