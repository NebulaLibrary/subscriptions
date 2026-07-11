import requests

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

configs = set()

for url in urls:
    print("Downloading:", url)
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()

        for line in r.text.splitlines():
            line = line.strip()

            if line:
                configs.add(line)

    except Exception as e:
        print(e)

configs = sorted(configs)

with open("all.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(configs))

print("Done")
print("Configs:", len(configs))
