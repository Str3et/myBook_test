from flask import request
import json
import requests


from config import AUTH_URL, BOOK_LIST_URL


def test_mybook():
    post_result = requests.post(AUTH_URL, data={'email': 'str3ett@yandex.ru', 'password': '456Street456'})

    # result = post_result.json()
    print(post_result)
    # data_dict = json.loads(post_result)
    # print(data_dict)
    book_list = requests.get(BOOK_LIST_URL, data=post_result)
    book = book_list.json()
    print(book)
    return book

# data={'email': 'str3ett@yandex.ru', 'password': '456Street456'}
