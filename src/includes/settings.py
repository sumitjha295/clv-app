import json

config_filepath = "../config.json"


def dbConfig():   # return Fibonacci series up to n
    try:
        with open(config_filepath) as json_data_file:
            data = json.load(json_data_file)
            return data["mysql"]
    except Exception as e:
        raise e


if __name__ == "__main__":
    dbConfig()
