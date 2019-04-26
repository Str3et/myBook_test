import os


AUTH_URL = 'https://mybook.ru/api/auth/'
BOOK_LIST_URL = 'https://mybook.ru/api/bookuserlist/'
HEADERS = {'Accept': 'application/json; version=5'}


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
