import requests
from lxml import html

def food():

	# specify user-agent
	headers = {'User-Agent': 'curl/7.43.0'}

	type_path = '//div[@class="container-fluid splGroupWrapper"][{}]//div[@class="col-md-12 splGroup"]/text()'
	entry_path = '//div[@class="container-fluid splGroupWrapper"][{}]//span/text()'

	page = requests.get('https://www.stw.berlin/mensen/mensa-tu-hardenbergstra%C3%9Fe.html', headers=headers)
	page = page.content
	tree = html.fromstring(page)

	# define food dict
	food = {}
	counter = 1
	while(counter < 8):
		typ = tree.xpath(type_path.format(str(counter)))[0]
		entries = tree.xpath(entry_path.format(str(counter)))
		food[typ] = entries
		counter+=1

	return food