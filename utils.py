import requests

from config import AUTH_URL, BOOK_LIST_URL, HEADERS


def mybook(user_email, user_password):

    session = requests.Session()
    #  отправляем POSTом данные пользователя на API для логина
    post_result = session.post(AUTH_URL, json={'email': user_email, 'password': user_password})
    #  получаем данные о книгах пользователя
    book_list = session.get(BOOK_LIST_URL, data=post_result, headers=HEADERS)
    book = book_list.json()
    data_book = book['objects']

    return data_book
