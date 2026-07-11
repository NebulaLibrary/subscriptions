import requests
import yaml
import os


url = "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/refs/heads/main/output/clash.yaml"

output = "clash/clash.yaml"
temp = "clash/clash_temp.yaml"


try:

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    data = yaml.safe_load(r.text)


    if "proxies" in data and len(data["proxies"]) > 0:

        for proxy in data["proxies"]:
            proxy["name"] = "@SystemNebula"


        os.makedirs("clash", exist_ok=True)


        with open(temp, "w", encoding="utf-8") as f:
            yaml.dump(
                data,
                f,
                allow_unicode=True,
                sort_keys=False
            )


        os.replace(temp, output)

        print("Clash updated:", len(data["proxies"]))


    else:

        print("Clash failed. Old file kept.")


except Exception as e:

    print("Clash error:", e)
    print("Old file kept.")
