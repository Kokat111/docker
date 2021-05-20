from app.forms import MiastoForm
from flask import render_template,redirect,url_for
from app import app
import requests

city=''

def get_key():
	url = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=wPAADHiPqogW497qyheQpEGimLAhTHsj&q={}'
	
	r = requests.get(url.format(city)).json()
	data = {
		'key':r[0]['Key'],
	}
	return data

@app.route('/')
def home():
	form = MiastoForm()
	city = form.miasto.data
	print(city)
	if form.validate_on_submit():
		r = get_weather_data([0])
		print(r)

	return render_template('search.html',title='Search',form=form)

