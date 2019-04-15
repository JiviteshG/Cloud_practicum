"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CloudFlask import app, db
from flask import Flask, render_template, request, flash, logging, url_for, redirect, jsonify, make_response, session, g
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.github import make_github_blueprint, github 


class Mortgage_details(db.Model):
	__tablename__ = 'mbr_mortgage_details'
	id = db.Column('id', db.Unicode, primary_key=True)
	name = db.Column('name', db.Unicode)
	address = db.Column('address', db.Unicode)
	phone_number = db.Column('phone_number', db.Integer)
	employer_info = db.Column('employer_info', db.Unicode)
	salary = db.Column('salary', db.Unicode)
	start_date=db.Column('start_date',db.DateTime)
	mortgage_value=db.Column('mortgage_value',db.Unicode)
	mortid=db.Column('mortid', db.Unicode)
	m1sid=db.Column('m1sid',db.Unicode)
	ins_value=db.Column('ins_value',db.Unicode)
	ded_value=db.Column('ded_value',db.Unicode)
	password = db.Column('password', db.Unicode)
	application_status = db.Column('application_status', db.Unicode)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = Mortgage_details()
    user.name = "test"
    user.password = "test"
    db.session.add(user)
    db.commit()
	if request.method == 'POST':
		userid = request.form['name']
		get_user = Mortgage_details.query.filter_by(name=userid).first()
		password = request.form['password']
        if get_user.password == password :
			if get_user.address is None or get_user.phone_number is None or get_user.employer_info is None or get_user.salary is None or get_user.mortgage_value is None or get_user.start_date is None or get_user.m1sid is None or get_user.ins_value is None or get_user.ded_value: 
				get_user.application_status='Complete'
				print(get_user.application_status)
			else: 
				get_user.application_status='Incomplete'
				print(get_user.application_status)
			
			return render_template('updatemessage2.html',mo=get_user)
		else:
			error = 'Employee ID and password do not match! Try again.'
			return render_template('login.html', error = error)

	return render_template('login.html')
