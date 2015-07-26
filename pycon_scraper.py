import urllib
from bs4 import *

def strcmp(str1,str2):
	if(str1 == str2):
		return 0
	if(str1 > str2):
		return 1
	if(str1 < str2):
		return -1

def scrap_and_save():
	debug = 0

	soup = BeautifulSoup(urllib.urlopen("http://www.accuweather.com/en/de/braunschweig/38100/weather-forecast/169823"))
	title = soup.title.text
	file = open('result.txt', 'w')
	if(debug):
		print(title)
	
	#scrap date of today
	date_list = soup.find_all(attrs = {"class":"info city-fcast-text"})
	for date in date_list:
		if(strcmp(date.h3.contents[0], 'Today') == 0):
			print(date.h4.contents[0])

			#scrap today's weather condition
			condition_list = date.find(attrs = {"class":"cond"})
			if(debug):
				print "Today's weather condition = ", condition_list.contents[0]
			else:
				print(condition_list.contents[0])
				file.write(condition_list.contents[0])
				file.write('\n')

			#scrap today's highest temperature
			high_temperature_list = date.find(attrs = {"class":"temp"})
			if(high_temperature_list):
				high_temperature = high_temperature_list.contents
				if(debug):
					print "high_temperature = ", high_temperature[0]
				else:
					print(high_temperature[0])
					file.write('Hi')
					file.write(high_temperature[0])
					file.write(' ')
		elif(strcmp(date.h3.contents[0], 'Tonight') == 0):
			print(date.h4.contents[0])
			#scrap today's lowest temperature
			low_temperature_list = date.find(attrs = {"class":"temp"})
			if(low_temperature_list):
				low_temperature = low_temperature_list.contents
				#low_temperature[1] = low_temperature[1].replace(" ","")
				if(debug):
					print "low_temperature = ", low_temperature[0]
				else:
					print(low_temperature[0])
					file.write('Low')
					file.write(low_temperature[0])
					file.write(' ')

	current_list = soup.find(attrs = {"class":"info"})
	if(current_list):
		current_temperature = current_list.find(attrs = {"class":"temp"})
		if(current_temperature):
			if(debug):
				print "current_temperature = ", current_temperature.contents[0]
			else:
				print(current_temperature.contents[0])
				file.write('Now')
				file.write(current_temperature.contents[0])
				#file.write(' ')

	#close file result.txt
	file.close()

#scrap_and_save()
