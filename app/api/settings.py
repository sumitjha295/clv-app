import yaml
import os

config_filename = os.path.dirname(os.path.abspath(__file__)) \
    + "/../config/config.yaml"


def db_config():
    try:
        with open(config_filename) as file:
            cfg = yaml.load(file)
            return cfg["mysql"]
    except Exception as e:
        raise e


if __name__ == "__main__":
    try:
        print(db_config())
    except Exception as e:
        print(e)
