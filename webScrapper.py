from bs4 import BeautifulSoup
from pylint.reporters import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import requests


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
  browser = webdriver.Chrome("C:\\Projetos\\Hardware Scrapping\\hs-webapp\\chromedriver.exe")
  browser.get("https://www.terabyteshop.com.br/promocoes")
  while True:
    try:
      time.sleep(3)
      botao_mais_produtos = browser.find_element_by_link_text("VER MAIS PRODUTOS")
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
    link_produto = "https://www.terabyteshop.com.br" + href
    response = requests.get(link_produto)
    if response.status_code is 200:
      response = requests.get(link_produto)
      soup = BeautifulSoup(response.content, 'lxml')
      if soup.find("del") is not None:
        preço_antigo = soup.find("del").get_text()
        preço_vista = soup.find(id="valVista").get_text()
        preço_novo = soup.find(id="valParc").get_text()
        img_produto = (soup.find(id="p0"))['src']
        titulo_produto = (soup.select("h1.tit-prod > strong")[0]).get_text()
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
    else:
      print("Not found")
    time.sleep(5)
  listaProdutos = {
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
  print(listaProdutos)
  with open('listaProdutos.json', 'w') as outfile:
    json.dump(listaProdutos, outfile)
