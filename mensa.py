import requests
import json
from lxml import html
import string

def food(type, date):

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

		#init food dict
		food = {'Name': None, 'Type': type, 'Price': None, 'Ampel': None, 'Veg': None, 'Bio': None, 'Klimaessen': None}

		#get name
		if name[1] == '        ':
			food['Name'] = string.rstrip(name[2], None)
		else:
			food['Name'] = string.strip(name[1], None)


		price = tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_preis"]/text()')
		food['Price'] = string.rstrip(price[0], None)

		#get Ampel
		if tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_rot"]') != []:
			food['Ampel'] = 'rot'
		elif tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_orange"]') != []:
			food['Ampel'] = 'orange'
		elif tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//a[@href="#ampel_gruen"]') != []:
			food['Ampel'] = 'gruen'

		#Vegetarian/Vegan option
		if tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//img[@alt="Vegan"]') != []:
			food['Veg'] = 'vegan'
		elif tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//img[@alt="Vegetarisch"]') != []:
			food['Veg'] = 'vegetarisch'

		#Bio option
		if tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//img[@alt="Bio"]') != []:
			food['Bio'] = 'Bio'

		#Klimaessen
		if tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]//img[@alt="Klimaessen"]') != []:
			food['Klimaessen'] = 'Klimaessen'

		typearr.append(food)
		counter += 1	

	return typearr


#HP
#print(food('food', 'today'))

#usage: food('type', 'date'), all dishes and prices in an array of dicts
#print(food('food', 'today')) #options: starters, salads, soups, special, food, side_dishes, desserts

