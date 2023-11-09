import requests
import re
from sys import stdin
from bs4 import BeautifulSoup  

print('Введите адрес сайта:')
addr = stdin.readline()
r = requests.get(addr)

soup = BeautifulSoup(r.content, 'html.parser')

long_number_pattern = r"[\s:\"]{1}[+]?[78][\s]?[-(]?[0-9]{3}[-)]?[\s]?[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}"
short_number_pattern = r"[\s:\"]{1}[0-9]{3}[-][0-9]{2}[-][0-9]{2}"

text = soup.prettify()

phone_numbers = set()
short_numbers = set()
for phone_number in re.findall(long_number_pattern, text):
    new_number = phone_number.replace('+', '')[2:].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
    if new_number not in phone_numbers:
        short_numbers.add(new_number[3:])
        phone_numbers.add('8' + new_number)
    
for phone_number in re.findall(short_number_pattern, text):
    new_number = phone_number[1:].replace(' ', '').replace('-', '')
    if new_number not in short_numbers:
        short_numbers.add(new_number)
        phone_numbers.add('8495' + new_number)

print('\nНайдены следующие телефонные номера:')
for number in phone_numbers:
    print(number)