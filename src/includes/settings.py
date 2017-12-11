import json
import os

config_filename = os.path.dirname(os.path.abspath(__file__)) + "/../config.json"


def db_config():   # return Fibonacci series up to n
    try:
        with open(config_filename) as json_data_file:
            data = json.load(json_data_file)
            return data["mysql"]
    except Exception as e:
        raise e


if __name__ == "__main__":
    print(db_config())
