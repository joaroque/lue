import requests
import json

class Clima():
	"""docstring for Clima"""
	def __init__(self, city, apikey):
		
		self.city = city
		self.apikey = apikey

	def get_info(self):
		# Request from link weather
		response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apikey}')
		self.res = response
	
	def show_info(self):
		data = self.res.json()

		#organize return
		return f'''
	RESULTADO:
	+ Cidade: {data['name']},
	+ Clima: {data['weather'][0]['main'].replace('Clear', 'Limpo').replace('Fog', 'Névoa')
	.replace('Mist', 'Névoa').replace('Rain', 'Chuva').replace('Clouds', 'Nuvens')
	.replace('Drizzle', 'Chuvisco').replace('Storm', 'Tempestade')},
	+ Humidade: {data['main']['humidity']}%,
	+ Vento: {(data['wind']['speed'] * 1.6):.1f} KM/H,
	+ Temperatura: {(data['main']['temp'] - 273.15):.1f}°

	Outras informações:
	• País: {data['sys']['country']},
	• Longitude {data['coord']['lon']},
	• Latitude {data['coord']['lat']}
		'''
	

