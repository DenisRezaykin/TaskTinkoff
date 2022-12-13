# Тебе нужно с помощью цикла отфильтровать массив JSON, чтобы получить только рублевые договоры.
# Как ты это сделаешь? Решение можно прислать в виде блок-схемы или в любом другом формате


def get_rub_contracts(contracts_list: list):
    rub_contracts = []
    for item in contracts_list:
        if item["currency"] == "RUB":
            rub_contracts.append(item)
    return rub_contracts


if __name__ == '__main__':
    A = [
        {
            "balance": -10324.54,
            "currency": "RUB",
            "status": "NORM",
            "productType": "Тариф "
        },
        {
            "balance": 0,
            "currency": "EUR",
            "status": "CLBL",
            "productType": "Текущий счет"
        },
        {
            "balance": 0,
            "currency": "RUB",
            "status": "CLBL",
            "productType": "Тариф"
        },
        {
            "balance": 9424.63,
            "currency": "USD",
            "status": "NORM",
            "productType": "Текущий счет"
        },
        {
            "balance": 2345.23,
            "currency": "RUB",
            "status": "NORM",
            "productType": "Текущий счет"
        }
    ]

    rub_contracts = get_rub_contracts(A)
    print(rub_contracts)
