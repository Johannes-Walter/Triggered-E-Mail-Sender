import json

__default_file_name = "settings.json"


def get_pin_to_read() -> int:
    return __getSettings("GPIO_Pin")

def get_E_Mail_daten() -> dict:
    return __getSettings("E_Mail_Daten")



def __getSettings(data_name: str = ""):
    with open(default_file_name) as read_file:
        data = json.load(read_file)

    if data_name == "":
        return data
    elif (data_name in data):
        return data[data_name]
    else:
        return ""