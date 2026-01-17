def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    sorted_data_list = []
    for data in data_list:
        if data["state"] == state:
            sorted_data_list.append(data)
        else:
            continue
    return sorted_data_list


data_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(data_list))


def sort_by_date(client_data: list, direction: bool = True) -> list:
    """Функция сортирует входящий список по дате (date) и возвращает новый отсортированный список."""

    sorted_client_data = sorted(client_data, key=lambda x: x["date"], reverse=direction)
    return sorted_client_data


client_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.241689"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.241689"},
]
print(sort_by_date(client_data, False))
