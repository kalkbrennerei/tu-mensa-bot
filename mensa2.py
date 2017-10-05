import requests
from lxml import html

def food():

	# specify user-agent
	headers = {'User-Agent': 'https://github.com/lydl28/tu-mensa-bot'}

	# make request and check status code
	page = requests.get('https://www.stw.berlin/mensen/mensa-tu-hardenbergstra%C3%9Fe.html', headers=headers)
	if(page.status_code != 200):
		return None

	page = page.content
	tree = html.fromstring(page)

	# define path
	type_path = '//div[@class="container-fluid splGroupWrapper"][{}]//div[@class="col-md-12 splGroup"]/text()'
	entry_path = '//div[@class="container-fluid splGroupWrapper"][{}]//span/text()'

	# define food dict
	food = {}
	for n in range (1,8):
		type = tree.xpath(type_path.format(str(n)))[0]
		entries = tree.xpath(entry_path.format(str(n)))
		food[type] = entries

	return food