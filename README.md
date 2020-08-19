RedLinks - пакет, предназначенный для взаимодействия ссылок с базой данных Redis в формате json

Установка (в ):
    pip install -e redlinks

Использование:
    redlinks.logic.post(request) - добавляет сайт или список сайтов в базу данных
    redlinks.logic.post(request) - печатает список сайтов, добавленных в указанный промежуток времени

Привер для post: request = {"address": ["ya.ru", "google.com"]}
Пример для get: request = {"from": 1231242342343, "to": 1331242342345}