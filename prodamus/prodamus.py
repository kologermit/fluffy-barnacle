import requests
from data.config import prodamus as prodamusConf

def prodamus_create_url(product: dict, extra: str, user_id: int):
    data = {
        "do": "link",
        "order_id": user_id,
        "demo_mode": 0,
        "customer_extra": extra,
        "currency": "rub",
        "payments_limit": 1,
        "_param_user_tg_id": user_id,
        "payments_limit": "1",
    }
    for key, value in product.items():
        data[f"products[0][{key}]"] = value
    return requests.get(prodamusConf["url"], data).text
