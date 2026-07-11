import requests
import json
import os


url = "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/refs/heads/main/output/singbox.json"


output = "singbox/singbox.json"
temp = "singbox/singbox_temp.json"



try:

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    data = r.json()


    if "outbounds" in data and len(data["outbounds"]) > 0:


        for item in data["outbounds"]:

            if "tag" in item:
                item["tag"] = "@SystemNebula"



        os.makedirs("singbox", exist_ok=True)


        with open(temp, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


        os.replace(temp, output)


        print("Singbox updated:", len(data["outbounds"]))


    else:

        print("Singbox failed. Old file kept.")



except Exception as e:

    print("Singbox error:", e)
    print("Old file kept.")
