import requests

def retornaDadosCep(cep):
  response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep));
  dadosCep = response.json();

  print(response.status_code)
  print(response.text)

  print(dadosCep['logradouro'])
 
retornaDadosCep('89280151')