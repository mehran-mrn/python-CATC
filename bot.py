import requests
import time

TOKEN = "1351458999:KcCVT7Ve7EWCt-g_6r7pHgflYzOVDdmkuFs"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"

offset = 0
MAX_RUNTIME = 1 * 60  # 10 دقیقه به ثانیه
start_time = time.time()

while True:
    # بررسی زمان
    if time.time() - start_time > MAX_RUNTIME:
        print("Max runtime reached, exiting...")
        break

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
