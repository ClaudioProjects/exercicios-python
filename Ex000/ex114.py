import requests
try:
    response = requests.get('http://www.pudim.com.br/')
except Exception as erro:
    print('\033[31mO site Pudim não esta disponível')
else:
    print('\033[32mO site Pudim esta disponível')
