import requests
import base64
import os
from urllib.parse import quote


urls = [
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub1.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub2.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub4.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub9.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub10.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub11.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub12.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub13.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub14.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub15.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub16.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub17.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub18.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub19.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub20.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub21.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub23.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub24.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub25.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub26.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub27.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub29.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Subscriptions/Sub30.txt",
]


configs = []


def add_config(line):
    line = line.strip()

    if not line:
        return

    if "#" in line:
        line = line.split("#")[0]

    line += "#" + quote("@SystemNebula")

    configs.append(line)


for url in urls:
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()

        for line in r.text.splitlines():
            add_config(line)

    except Exception as e:
        print("Error:", e)


# Base64 source
try:
    url = "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/refs/heads/main/output/v2ray-base64.txt"

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    decoded = base64.b64decode(r.text).decode()

    for line in decoded.splitlines():
        add_config(line)

except Exception as e:
    print("Base64 error:", e)



output = "v2ray/all.txt"
temp = "v2ray/all_temp.txt"


if len(configs) > 20:

    os.makedirs("v2ray", exist_ok=True)

    with open(temp, "w", encoding="utf-8") as f:
        f.write("\n".join(configs))

    os.replace(temp, output)

    print("V2Ray updated:", len(configs))

else:
    print("V2Ray failed. Old file kept.")
