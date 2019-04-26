import requests
import pprint

from config import AUTH_URL, BOOK_LIST_URL, HEADERS


def mybook(user_email, user_password):
    session = requests.Session()
    # post_result = session.post(AUTH_URL, json={'email': 'str3ett@yandex.ru', 'password': '456Street456'})
    post_result = session.post(AUTH_URL, json={'email': user_email, 'password': user_password})
    book_list = session.get(BOOK_LIST_URL, data=post_result, headers=HEADERS)
    book = book_list.json()
    data_book = book['objects']

    pprint.pprint(data_book)

    return data_book
