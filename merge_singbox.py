import requests
import json
import os


url = "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/refs/heads/main/output/singbox.json"

output = "singbox/singbox.json"


try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()

    data = r.json()


    # تغییر tag همه outbound ها
    if "outbounds" in data:

        for outbound in data["outbounds"]:

            if "tag" in outbound:
                outbound["tag"] = "@SystemNebula"


    # ساخت پوشه singbox
    os.makedirs("singbox", exist_ok=True)


    with open(output, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


    print("Sing-box updated successfully")


except Exception as e:
    print("Error:", e)
