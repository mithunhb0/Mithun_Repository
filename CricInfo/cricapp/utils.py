import json

def is_valid_json_data(data):
    try:
        real_dict_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False 
    return valid
