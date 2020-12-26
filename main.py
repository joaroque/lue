from modules.bootstrapy import Strapy
from modules.banner import banner
from modules.weather import Clima
from os import system

apikey = "4d92040f1145cd22658acc99bc25d33a"  #get apikey http://api.openweathermap.org

def clear():
	clear = system('clear || cls')

def main():
	clear()
	print(banner())
	city_term = Strapy.RED + "\nInsire uma cidade (exemplo: Namibe): " + Strapy.END
	city = input(city_term)
	clima = Clima(city, apikey)
	clima.get_info()
	print(clima.show_info())
main()