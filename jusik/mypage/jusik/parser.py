from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

def get_code(stock_code):
    url = 'https://finance.naver.com/item/main.nhn?code=' + stock_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, 'html.parser')
    return bs_obj

def get_price(stock_code):
    bs_obj = get_code(stock_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class":"blind"})
    now_price = blind.text
    return now_price

