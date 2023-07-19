from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

#----------------------------------------------------------------------------------------
username = "adamrmb07"
password = "123"



@app.route('/', methods=['GET', 'POST'])  # '/' for the default pageFouad
def login():
	if request.method == 'POST':
		user_name = request.form["username"]
		p_word = request.form["password"]
		if user_name == username and p_word == password:
			return redirect(url_for('home'))

	else:
		return render_template('login.html')
	
@app.route('/home', methods=['GET', 'POST'])
def home():
		return render_template('home.html')

def friends():
		facebook_friends=["Nahar","Yanai","Shiraz", "Sasha", "Naama", "Oded", "DanDan", "Benda"]
		return render_template('home.html', my_friends = friends, no_friends = False)

@app.route('/friends_exists/<string:name>',methods=['GET','POST'])
def friends_exists_route(name):
    return render_template('friends_exists.html', n = name)




#----------------------------------------------------------------------------------------
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
	debug=True
		)