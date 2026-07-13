import os

INPUT = "v2ray/all.txt"
OUTPUT_DIR = "v2ray/parts"

PART_SIZE = 30

os.makedirs(OUTPUT_DIR, exist_ok=True)


with open(INPUT, "r", encoding="utf-8") as f:
    configs = [
        line.strip()
        for line in f
        if line.strip()
    ]


print("Total:", len(configs))


# پاک کردن پارت‌های قبلی
for file in os.listdir(OUTPUT_DIR):
    os.remove(
        os.path.join(OUTPUT_DIR, file)
    )


part = 1


for i in range(0, len(configs), PART_SIZE):

    chunk = configs[i:i+PART_SIZE]

    filename = f"v2ray-{part:03}.txt"

    path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(chunk))

    print(filename, len(chunk))

    part += 1


print("Done")
