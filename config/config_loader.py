import json


def load_config(config_file: str) -> dict:
    with open(config_file, 'r') as json_file:
        config_dict = json.load(json_file)
    return config_dict
