from app.forms import MiastoForm
from flask import render_template,redirect,url_for,request
from app import app
import requests




@app.route('/', methods=['GET','POST'])
def home():


	form = MiastoForm()
	if form.validate_on_submit():
		global city
		city = request.form.get('miasto')
		responce = requests.post('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=wPAADHiPqogW497qyheQpEGimLAhTHsj&q='+city+'').json()
		global data
		data = responce[0]['Key'],
	print(data)
	print(city)
	return redirect(url_for('forcast'))

	return render_template('search.html',title='Search',form=form)

@app.route('/pogoda', methods=['GET','POST'])
def forcast():
	
	return print(data)