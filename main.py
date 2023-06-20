import requests
from cep import BuscaEndereco

cep = '22261040'
objeto = BuscaEndereco(cep)
bairro, cidade, uf = objeto.acessa_cep()
print(bairro, cidade,uf)


#link = f'http://viacep.com.br/ws/{cep}/json/'
#r = requests.get(link)
#print(r.text)
