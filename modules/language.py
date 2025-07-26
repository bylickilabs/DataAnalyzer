import json
import os

def load_language(code):
    path = os.path.join("i18n", f"{code}.json")
    if not os.path.exists(path):
        path = os.path.join("i18n", "en.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
