from app.forms import MiastoForm
from flask import render_template,redirect,url_for
from app import app
import requests

responce=requests.get('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=wPAADHiPqogW497qyheQpEGimLAhTHsj&q=krakow').json()
data = {
		responce[0]['Key'],
	}
print(data)

def get_key():
	url = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=wPAADHiPqogW497qyheQpEGimLAhTHsj&q={}'
	
	r = requests.get(url.format(city)).json()
	data = {
		'key':r[0]['Key'],
	}
	return data

@app.route('/', methods=["GET"])
def home():
	form = MiastoForm()



	return render_template('search.html',title='Search',form=form)

