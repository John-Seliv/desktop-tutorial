import json
import os
import requests
import sys
from dotenv import load_dotenv

def short_url(long_url):
	def_url = 'https://api-ssl.bitly.com/v4/shorten'
	headers = {'Authorization' : my_token}
	params = {'long_url': long_url}
	response = requests.post(def_url, headers=headers, json=params)
	if response.status_code != 200:
		print('Некорректный ввод!!!')
		sys.exit(0)
	bitlink = response.json().get('id')
	return(bitlink)

def count_clicks(sh_url):
	def_url = 'https://api-ssl.bitly.com/v4/bitlinks/' + sh_url + '/clicks/summary'
	headers = {'Authorization' : my_token}
	payload = {"unit": "day", "units" : 5, "size" : 10}
	try:
		response = requests.get(def_url, params=payload, headers=headers)
		response.raise_for_status()
		answer_text = response.text
		answer_dict = json.loads(answer_text)
		count = answer_dict.get("total_clicks")
	except requests.exceptions.HTTPError as err:
		print('Извините, ошибка сервера')
		count = 'подсчитать не удалось.'
	return(count)

def is_bitlink(bitlink):
    def_url = 'https://api-ssl.bitly.com/v4/bitlinks/' + bitlink
    headers = {'Authorization' : my_token}
    try:
        response = requests.get(def_url, headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as err:
    	return False

from config import token
my_token = token

print('Введите HTTP (Пример - https://dvmn.org)')
url = input()

if __name__ == '__main__':
	if is_bitlink(url):
		count = count_clicks(url)
		print('Количество кликов за 1 день - ', count)
		sys.exit(0)
	bitlink = short_url(url)
	print('Короткая ссылка -', bitlink)