# -*- coding: utf-8 -*-
from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
	user = {'login' : 'Allan'}
	posts = [
		{
			'autor' : {'login' : u'joão'},
			'body' : 'O filme e muito bom'
		},
		{
			'autor' : {'login' : 'maria'},
			'body' : 'gostei muito do filme'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							posts=posts)