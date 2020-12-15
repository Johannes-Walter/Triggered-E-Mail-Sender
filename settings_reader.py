import json
from typing import Any

__DEFAULT_FILE_NAME: str = "settings.json"


def get_pin_to_read() -> int:
    return __getSettings("GPIO_Pin")


def get_E_Mail_data() -> dict:
    return __getSettings("E_Mail_Daten")


def __getSettings(data_name: str = "") -> Any:
    # liest die settings.json
    with open(__DEFAULT_FILE_NAME) as read_file:
        data = json.load(read_file)

    # Entscheidet ob alles, nur ein Teil, oder nichts aus der settings.json zurückgegeben wird.
    if data_name == "":
        return data

    elif data_name in data:
        return data[data_name]

    else:
        return ""