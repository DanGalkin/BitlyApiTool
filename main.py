import requests
import json
import sys
import os
from dotenv import load_dotenv
import argparse

API_ENDPOINT = 'https://api-ssl.bitly.com/v4/{method}'

def create_parser():
  parser = argparse.ArgumentParser(description='Программа сокращает ссылку в битлинк или выдает статистику по вашему битлинку')
  parser.add_argument('link', help='Ваша ссылка')
  return parser

def make_oauth_headers(token):
  oauth_header = 'Bearer {}'.format(token)
  headers = {
    'Authorization': oauth_header
  }
  return headers

def shorten_link(long_url, headers):
  data_to_shorten = {'long_url': long_url}
  short_link_response = requests.post(API_ENDPOINT.format(method='shorten'), headers=headers, json=data_to_shorten)
  if short_link_response.ok:
    return short_link_response.json()['link']

def get_link_statistics(url, headers):
  method = 'bitlinks/{}/clicks/summary'.format(url)
  link_statistics_response = requests.get(API_ENDPOINT.format(method=method), headers=headers)
  if link_statistics_response.ok:
    return link_statistics_response.json()['total_clicks']

def check_if_bitlink(url, headers):
  method = 'bitlinks/{}'.format(url)
  bitlink_response = requests.get(API_ENDPOINT.format(method=method), headers=headers)
  return bitlink_response.ok

def main():
  token = os.getenv("BITLY_API_TOKEN")
  headers = make_oauth_headers(token)
  bitly_user_response = requests.get(API_ENDPOINT.format(method='user'), headers=headers)
  parser = create_parser()
  link = parser.parse_args().link
  if check_if_bitlink(link, headers):
    print('Вы ввели битлинк, сейчас выгрузим статистику по нему')
    link_statistics = get_link_statistics(link, headers)
    if not link_statistics:
      sys.exit('Что-то пошло не так. Программа завершит работу')
    print('Статистика переходов по ссылке: {}'.format(link_statistics))
  else:
    print('Это явно не ваш битлинк, попробуем сократить эту ссылку')
    bitly_link = shorten_link(link, headers)
    if not bitly_link:
      sys.exit('Bitly не может сократить ссылку, проверьте, что она правильная. Программа завершит работу')
    print('Сокращенная ссылка: {}'.format(bitly_link))

if __name__ == '__main__':
  load_dotenv()
  main()