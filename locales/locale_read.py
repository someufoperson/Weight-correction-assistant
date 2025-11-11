import json

def locale_read(language: str, func_name: str):
    with open (file=f"locales/locale.json", mode="r", encoding="UTF-8") as file:
        locale = json.load(file)[func_name]
        if func_name == "start_register":
            return locale
        else:
            return locale[language]