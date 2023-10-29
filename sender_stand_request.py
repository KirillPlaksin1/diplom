# Плаксин Кирилл, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import data
import requests

# Создаем заказ
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
# Получение заказа по треку
def get_order(track):
    order_url = configuration.URL_SERVICE + configuration.GET_ORDER + str(track)
    response = requests.get(order_url)
    return response

def test_get_order_data():
    response = create_order(data.order_body)
    track = response.json()["track"]

# Получение данных заказа по треку
    order_response = get_order(track)
    assert order_response.status_code == 200
    order_data = order_response.json()

    print("Трек заказа:", track)
    print("Данные заказа:", order_data)
