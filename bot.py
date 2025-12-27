import requests
import time

TOKEN = "1351458999:KcCVT7Ve7EWCt-g_6r7pHgflYzOVDdmkuFs"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"

offset = 0

while True:
    resp = requests.get(
        f"{BASE_URL}/getUpdates",
        params={"offset": offset, "timeout": 30}
    ).json()

    if not resp.get("ok"):
        time.sleep(2)
        continue

    for update in resp["result"]:
        offset = update["update_id"] + 1

        message = update.get("message")
        if not message:
            continue

        chat_id = message["chat"]["id"]
        text = message.get("text")

        if not text:
            continue

        requests.post(
            f"{BASE_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": text
            }
        )

    time.sleep(1)
