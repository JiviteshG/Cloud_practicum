"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CloudFlask import app
from flask import Flask, render_template, request, flash, logging, url_for, redirect, jsonify, make_response, session, g
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github 
@app.route('/')
def home(): 
# if github.authorized:
	print("A")
	account_info = github.get('/user')
	print(account_info)
	git_username = ''
	print(git_username)
	print('Checking uname')
	if account_info.ok:
		print('Checking uname started')
		account_info_json = account_info.json()
		git_username = account_info_json['login']
		print(git_username)
		session['user'] = git_username
		print("Reach")
		return redirect(url_for('addEmployer',  username=session['user']))
	return render_template('employer_home.html')

@app.route('/github_login', methods=['GET', 'POST'])
def github_login():

	

	session.pop('user', None)
	# print('1')
	# if not twitter.authorized:
	# 	print('2')
	# 	return redirect(url_for('twitter.login'))
	# print('3')
	# account_info = twitter.get('account/settings')
	# print('4')
	# if account_info.ok:
	# 	account_info_json = account_info.json()

	# 	return '<h1> Your Twitter name is @{}'.format(account_info_json['screen_name'])

	# Correct code
	# if not github.authorized:
	# 	return redirect(url_for('github.login'))
	# account_info = github.get('/user')
	# git_username = ''
	# if account_info.ok:
	# 	account_info_json = account_info.json()
	# 	git_username = account_info_json['login']



	f = open("log1.txt", "a+")
	f.write("method: GET \nEnd-point: http://127.0.0.1:8001/login \nparameters: None\n" )
	f.close()
	# Employee_details1 = Employee_details.query.filter_by(username=username),first()
	
	

	if request.method == 'POST':
		f = open("log1.txt", "a+")
		f.write("method: POST \nEnd-point: http://127.0.0.1:8001/login \nparameters: Login from git ")
		f.close()

		### CODE FOR OAUTH
		print("Reach0")
		if not github.authorized:
			print("NA")
			return redirect(url_for('github.login'))
		print("A")
		account_info = github.get('/user')
		print(account_info)
		git_username = ''
		print(git_username)
		print('Checking uname')
		if account_info.ok:
			print('Checking uname started')
			account_info_json = account_info.json()
			git_username = account_info_json['login']
			print(git_username)
			session['user'] = git_username
			print("Reach")
			return redirect(url_for('addEmployer',  username=session['user']))

		## MAINSTREAM LOGIN
		# for i in range(1):
		# 	f.write("POST, http://127.0.0.1:8001/login, username: "+request.form['username']+", password: "+request.form['password']+" %d\r\n" % (i))
		# emppass = request.form
		# username = request.form['username']
		# get_emp = Employee_details.query.filter_by(username=username).first()
		# password = request.form['password']


		# pathToXML = "Salt.xml"
		# tree = ET.parse(pathToXML)
		# root = tree.getroot()

		# # all items data
		# print('Expertise Data:'+str(root)+str(tree))
		# salt = ''
		# for elem in root:
		# 	salt = elem.text


		# if get_emp is None:
		# 	error = 'User not present! Try again.'
		# 	return render_template('login.html', error = error)
		# if  get_emp.password != password+salt:
		# 	error = 'Password do not match! Try again.'
		# 	return render_template('login.html', error = error)
		# else:
		# session['user'] = username
		# return redirect(url_for('addEmployer',  username=session['user']))
		
		
	# return '<h1>Request failed! <h1>'
	# return render_template('login.html')
	return render_template('github_login.html')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
