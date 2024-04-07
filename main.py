import json
import os
# read from json


def LoadData(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    else:
        return {}

# save to json


def SaveData(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
