import requests
from lxml import html

def food(type, date):
	if date == 'today':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/index.html')
	elif date == 'tomorrow':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/01.html')
	elif date == 'day after tomorrow':
		page = requests.get('http://www.studentenwerk-berlin.de/mensen/speiseplan/tu/02.html')
	tree = html.fromstring(page.content)	
	print(type + ":")
	counter = 1

	while True:
		food = tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_name"]/text()')
		if food == []:
			break
		price = tree.xpath('//div[@class="mensa_day mensa_day_speise ' + type +'"]//tr[@class="mensa_day_speise_row"][' + str(counter) + ']//td[@class="mensa_day_speise_preis"]/text()')
		if food[1] == '        ':
			print(food[2] + ":    " + price[0])
		else:
			print(food[1] + ":    " + price[0])
		counter = counter + 1	



#HP
#usage: food('type', 'date'), prints all dishes and prices
food('side_dishes', 'tomorrow') #options: starters, salads, soups, special, food, side_dishes, desserts
food('food','tomorrow')

