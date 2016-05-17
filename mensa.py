import requests
import json
from lxml import html
import string

def food(type, date):
	#return('Salat')
	if date == 'today':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/index.html')
	elif date == 'tomorrow':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/01.html')
	elif date == 'day after tomorrow':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/02.html')
	tree = html.fromstring(page.content)	
	counter = 1
	typearr = []

	while True:
		name = tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]/text()')
		if name == []:
			break
		food = {'Name': None, 'Type': type, 'Price': None, 'Ampel': None}

		price = tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_preis"]/text()')
		food['Price'] = string.rstrip(price[0], None)

		if tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_rot"]') != []:
			ampel = 'rot'
		elif tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_orange"]') != []:
			ampel = 'orange'

		elif tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_gruen"]') != []:
			ampel = 'gruen'
		food['Ampel'] = ampel

		if name[1] == '        ':
			food['Name'] = string.rstrip(name[2], None)
		else:
			food['Name'] = string.strip(name[1], None)
		typearr.append(food)
		counter += 1	

	return typearr


#HP
print(food('food', 'today'))
#food2 = ''
#i = 0
#for n, val in enumerate(today):
#    food2 += today[n]['Name'] + today[n]['Price'] + '\n'
#    i += 1
#print(food2)
#usage: food('type', 'date'), prints all dishes and prices

#print(food('food', 'today')) #options: starters, salads, soups, special, food, side_dishes, desserts

