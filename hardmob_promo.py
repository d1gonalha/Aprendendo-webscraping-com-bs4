from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

header = {'User-Agent': 'Mozilla/5.0'}
my_url = 'http://www.hardmob.com.br/promocoes/'

req = Request(my_url, headers=header)

# salvando a página
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class": "threadinfo"})

count = 0
print("HARDMOB PROMOCOES by digonalha")
for container in containers:
	count+=1

	if(count > 3):
	    print("")
	    print(container.div.h3.a.text)
	    print("Link: " + str(container.div.h3.a["href"]))
	    print("")
	    print("---------")
