import os
import numpy
from clv_utils import CLVUtils


def predict_and_import(num_rows=None):
    current_path = os.path.dirname(os.path.abspath(__file__))
    clv_utils = CLVUtils()
    clv_resource_path = current_path + '/../resource/orders.csv'
    clv_model_filename = current_path + '/../resource/model.dill'
    clv_export_filename = current_path + '/../output/prediction.csv'

    try:
        df = clv_utils.import_from_csv(clv_resource_path, num_rows=num_rows)
        df = clv_utils.transform(df)
        df = clv_utils.predict(df, clv_model_filename)
        clv_utils.export_to_csv(df, clv_export_filename)
        clv_utils.save_to_database(df)
    except Exception as e:
        print('Error : %s' % e)


if __name__ == '__main__':
    num_rows = os.getenv('NUM_ROWS', -1)
    if int(num_rows) > 0:
        predict_and_import(int(num_rows))
    else:
        predict_and_import()
