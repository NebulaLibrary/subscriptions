import requests
import yaml
import os


url = "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/refs/heads/main/output/clash.yaml"

output = "clash/clash.yaml"


try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    data = yaml.safe_load(r.text)

    # تغییر اسم همه پروکسی ها
    if "proxies" in data:
        for proxy in data["proxies"]:
            proxy["name"] = "@SystemNebula"

    # ساخت پوشه clash اگر نبود
    os.makedirs("clash", exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False
        )

    print("Clash updated successfully")

except Exception as e:
    print("Error:", e)
