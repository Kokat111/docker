from app.forms import MiastoForm
from flask import render_template,redirect,url_for,request
from app import app
import requests

city = ''
data = 0


@app.route('/', methods=['GET','POST'])
def home():


	form = MiastoForm()
	if form.validate_on_submit():
		global city
		city = request.form.get('miasto')
		responce = requests.post('http://dataservice.accuweather.com/locations/v1/cities/search?apikey=wPAADHiPqogW497qyheQpEGimLAhTHsj&q='+city+'').json()
		global data
		data = responce[0]['Key']
		print(data)
		print(city)
		return redirect(url_for('forcast'))

	return render_template('search.html',title='Search',form=form)

@app.route('/pogoda', methods=['GET','POST'])
def forcast():
	form = MiastoForm()
	forcast_info = requests.post('http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+data+'?apikey=%20%09wPAADHiPqogW497qyheQpEGimLAhTHsj%20&metric=true').json()

	day1 = forcast_info['DailyForecasts'][0]['Date'],str(forcast_info['DailyForecasts'][0])

	
	day2 = forcast_info['DailyForecasts'][1]['Date']

	day3 = forcast_info['DailyForecasts'][2]['Date']

	day4 = forcast_info['DailyForecasts'][3]['Date']

	day5 = forcast_info['DailyForecasts'][4]['Date']


	print(day1,day2,day3,day4,day5)
	return render_template('search.html',title='Search',form=form)