import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from firebase import firebase
def criarProduto(tipo, preçoAntigo, preçoNovo, preçoVista, srcImg, nomeProduto):
  produto = {
    'nomeProduto': nomeProduto,
    'preçoAntigo': preçoAntigo,
    'preçoNovo': preçoNovo,
    'preçoVista': preçoVista,
    'linkImg': srcImg,
    'categoria': tipo
  }
  return produto


if __name__ == '__main__':
  options = Options()
  options.headless = True
  browser = webdriver.Chrome("C:\\Projetos\\hswebapp\\chromedriver.exe", options=options)
  browser.get("https://www.terabyteshop.com.br/promocoes")
  config = {
    "apiKey": "AIzaSyCySoEZDSBpVGXpWM55dCZjJ3tSlw2vl5M",
    "authDomain": "hswebapp-33c2a.firebaseapp.com",
    "databaseURL": "https://hswebapp-33c2a.firebaseio.com",
    "projectId": "hswebapp-33c2a",
    "storageBucket": "hswebapp-33c2a.appspot.com",
    "messagingSenderId": "459313121026",
    "appId": "1:459313121026:web:f2071d2fe799d93434641b",
    "measurementId": "G-GPR1BEPY32"
  }

  while True:
    try:
      time.sleep(3)
      botao_mais_produtos = browser.find_element_by_id("pdmore")
      botao_mais_produtos.click()

    except NoSuchElementException:
      break
  html = browser.page_source
  soup = BeautifulSoup(html, 'lxml')
  links_produtos = [a['href'] for a in soup.find_all('a', href=True, class_="prod-name")]
  browser.close()
  kits_upgrades = []
  gpus = []
  pc_gamers = []
  memorias = []
  monitores = []
  gabinetes = []
  teclados = []
  cpus = []
  mouses = []
  headsets = []
  coolers = []
  watercoolers = []
  placas_mães = []
  ssds = []
  hds = []
  combos = []
  fontes = []
  outros = []
  for href in links_produtos:
    browser = webdriver.Chrome("C:\\Projetos\\hswebapp\\chromedriver.exe", options=options)
    link_produto = "https://www.terabyteshop.com.br" + href
    browser.get(link_produto)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    browser.close()
    if soup.find('del') is not None:
      preço_antigo = soup.find('del').get_text()
      preço_vista = soup.find(id="valVista").get_text()
      preço_novo = soup.find(id="valParc").get_text()
      #img_produto = (soup.find(id="p0"))['src']
      img_produto = (soup.select(' div.fotorama__stage__frame.fotorama__loaded.fotorama__active > div > div > img:nth-child(1)')[0])['src']
      titulo_produto = (soup.find_all('h1', class_='tit-prod')[0]).get_text()
      if titulo_produto.startswith("Kit Upgrade"):
        kits_upgrades.append(
          criarProduto("Kit Upgrade", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Pc Gamer"):
        pc_gamers.append(criarProduto("Pc Gamer", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Memória"):
        memorias.append(criarProduto("Memória", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Placa de Vídeo"):
        gpus.append(
          criarProduto("Placa de Vídeo", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Monitor"):
        monitores.append(criarProduto("Monitor", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Gabinte"):
        gabinetes.append(criarProduto("Gabinte", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Teclado"):
        teclados.append(criarProduto("Teclado", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Mouse"):
        mouses.append(criarProduto("Mouse", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Headset"):
        headsets.append(criarProduto("Headset", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Combo"):
        combos.append(criarProduto("Combo", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Water Cooler"):
        watercoolers.append(
          criarProduto("Water Cooler", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Cooler"):
        coolers.append(criarProduto("Cooler", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Processador"):
        cpus.append(criarProduto("Processador", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Placa Mãe"):
        placas_mães.append(
          criarProduto("Placa Mãe", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("Fonte"):
        fontes.append(criarProduto("Fonte", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("SSD"):
        ssds.append(criarProduto("SSD", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      elif titulo_produto.startswith("HD"):
        hds.append(criarProduto("HD", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
      else:
        # Isso aqui é para colocar como outros a categoria
        outros.append(criarProduto("Outros", preço_antigo, preço_novo, preço_vista, img_produto, titulo_produto))
    else:
      pass
    time.sleep(5)
  else:
    print("Not found")
  listaProdutos = {
    "diaPromoções": datetime.today().strftime('%Y-%m-%d'),
    "kits_upgrades": kits_upgrades,
    "pc_games": pc_gamers,
    "gpus": gpus,
    "fontes": fontes,
    "placas mães": placas_mães,
    "teclados": teclados,
    "memorias": memorias,
    "mouses": mouses,
    "headsets": headsets,
    "coolers": coolers,
    "watercoolers": watercoolers,
    "ssds": ssds,
    "combos": combos,
    "processadores": cpus,
    "hds": hds,
    "outros": outros
  }
  firebase = firebase.FirebaseApplication('https://hswebapp-33c2a.firebaseio.com/', None)
  firebase.post('/users', data={"whatever":"data"})

