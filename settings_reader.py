import json
from typing import Any

__DEFAULT_FILE_NAME: str = "settings.json"


def get_pin_to_read() -> int:
    return __getSettings("GPIO_Pin")

def get_batch_send_wait_time() -> int:
    return __getSettings("batch_send_wait_time")

def get_E_Mail_data() -> dict:
    return __getSettings("E_Mail_Daten")



def __getSettings(data_name: str = "") -> Any:
    with open(__DEFAULT_FILE_NAME) as read_file:
        data = json.load(read_file)

    if data_name == "":
        return data
    elif (data_name in data):
        return data[data_name]
    else:
        return ""