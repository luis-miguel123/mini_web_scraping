import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import timeit

requisicao = requests.get('https://g1.globo.com/')
conteudo = requisicao.content
site = BeautifulSoup(conteudo, 'html.parser')
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

start = time.time()

for noticia in noticias:
	
	titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
	print('conexao com o site: ', urllib.request.urlopen('https://g1.globo.com/').getcode())
	print('tempo da requisicao', requisicao.elapsed)
	print('titulo: ', titulo.text)
	subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
	if (subtitulo):
		print('subtitulo: ', subtitulo.text)
	noticia_relacionada = noticia.find('div', attrs={'class': 'bstn-fd-relatedtext'})
	if (noticia_relacionada):
		print('veja tbm: ', noticia_relacionada.text)
	
	print()
	decisao = int(input("cada requisicao leva 20 minutos para ser finalizada, continuar esperando?(0= nao, 1=sim:  "))
	if decisao == 1:
		time.sleep(1200)
	elif decisao == 0:    
	    break
	else:
		print('stop, get some help')
		break
		
	


end = time.time()
print(f'todas as requisicoes levaram: {end - start} para serem concluidas!')
	
	
