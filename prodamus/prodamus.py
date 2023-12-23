import requests
from data.config import prodamus as prodamusConf

def prodamus_create_url(product: dict, user_id: int):
    data = {
        "do": "pay",
        "order_id": user_id,
        "demo_mode": prodamusConf["demo_mode"],
        # "callbackType": "json",
        "customer_email": "kologermit@gmail.com",
        "customer_extra": "extra",
        "currency": "rub",
        "payments_limit": 1,
        "_param_user_tg_id": user_id,
        # "callbackType": "json",
        "payments_limit": "1",
    }
    for key, value in product.items():
        data[f"products[0][{key}]"] = value
    return requests.get(prodamusConf["url"], data).text
