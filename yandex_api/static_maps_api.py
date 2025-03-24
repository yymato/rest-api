import requests

from yandex_api.geocoder_api import get_coords_from_geocoder


def selection_size(toponym):
    toponym_dictionary_size = toponym['boundedBy']['Envelope']
    delta_x = float(toponym_dictionary_size['upperCorner'].split()[0]) - float(
        toponym_dictionary_size['lowerCorner'].split()[0])
    delta_y = float(toponym_dictionary_size['upperCorner'].split()[1]) - float(
        toponym_dictionary_size['lowerCorner'].split()[1])

    return ",".join(map(str, (delta_x, delta_y)))



def get_picture(city):
    geocoder_response = get_coords_from_geocoder(city)
    size = selection_size(geocoder_response[1])
    map_apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": geocoder_response[0],
        "spn": size,
        "apikey": map_apikey,
    }

    map_api_server = "https://static-maps.yandex.ru/v1"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response

