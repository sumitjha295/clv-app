import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/src/includes')

from clv_utils import CLVUtils

def predict_and_import():
    clv_utils = CLVUtils()
    clv_resource_path = current_path + '/src/resource/orders.csv'
    clv_model_filename = current_path + '/src/resource/model.dill'
    clv_export_filename = current_path + '/output/prediction.csv'

    try:
        df = clv_utils.import_from_csv(clv_resource_path, num_rows=100)
        df = clv_utils.transform(df)
        df = clv_utils.predict(df, clv_model_filename)
        clv_utils.export_to_csv(df, clv_export_filename)
        clv_utils.save_to_database(df)
    except Exception as e:
        print('Error : %s' % e)


if __name__ == '__main__':
    predict_and_import()