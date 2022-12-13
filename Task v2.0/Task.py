# Тебе нужно с помощью цикла отфильтровать массив JSON, чтобы получить только рублевые договоры.
# Как ты это сделаешь? Решение можно прислать в виде блок-схемы или в любом другом формате

import json


def get_rub_contracts(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.loads(file.read())
    rub_contracts = []
    for item in data["data"]:
        if item["currency"] == "RUB":
            rub_contracts.append(item)
    return rub_contracts


if __name__ == '__main__':
    rub_contracts = get_rub_contracts("VO.json")
    print(rub_contracts)
