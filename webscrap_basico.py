from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# fazer um scrap da primeira pagina de teclados gamers na newegg.
my_url = 'https://www.newegg.com/Gaming-Keyboards/SubCategory/ID-3523?Tid=160908'

# abrindo a conexao e retornando a pagina!
uClient = uReq(my_url)
page_html = uClient.read()

# fechando a conexao.
uClient.close()

# html parsing com o bs4 (sopa de html :9)
page_soup = soup(page_html, "html.parser")

# dentro da pagina na newegg, pego a div de de produtos (procurar no html
# a div referente aos produtos!)
containers = page_soup.findAll("div", {"class": "item-container"})

# salvaremos esses dados dentro de um arquivo csv, abrindo o arquivo csv...
filename = "produtos.csv"
f = open(filename, "w")
headers = "MARCA, NOME PRODUTO, FRETE"
f.write(headers)

# pegando os dados dos produtos <3
for container in containers:
    # pegando a marca do item
    brand = container.div.div.a.img["title"]

    # pegando titulo do item
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    # pegando dados do frete
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("Marca: " + brand)
    print("Nome do produto: " + product_name)
    print("Frete: " + shipping)
    print("----")

    # inserindo o item dentro do csv
    f.write(brand + "," + product_name.replace(",", " |") + "," + shipping + "\n")


# fechando e salvando o arquivo csv
f.close()
