import pandas as pd
import numpy as np
import dill as pickle
import datetime


class CLVUtils:

    def __init__(self):
        pass

    @staticmethod
    def import_from_csv(filename, num_rows=None):
        try:
            return pd.read_csv(
                filename,
                parse_dates=['created_at_date'],
                nrows=num_rows
            )
        except Exception as import_exception:
            raise import_exception

    @staticmethod
    def transform(data_frame):
        try:
            grouped_customer_df = data_frame.groupby(["customer_id"])
            last_order_date = datetime.datetime(2017, 10, 17)
            clv_columns = [
                'max_number_item',
                'max_revenue',
                'total_revenue',
                'total_orders',
                'days_since_last_order',
                'longest_interval'
            ]
            transformed_data_frame = pd.DataFrame(columns=clv_columns)
            for customer_id, customer_df in grouped_customer_df:
                grouped_order_df = customer_df.groupby('order_id')
                transformed_data_frame.loc[customer_id] = [
                    grouped_order_df.num_items.sum().max(),
                    grouped_order_df.revenue.sum().max(),
                    customer_df.revenue.sum(),
                    customer_df.num_items.sum(),
                    (last_order_date - customer_df.created_at_date.max()).days,
                    5
                ]
            transformed_data_frame.index.name = 'customer_id'
            return transformed_data_frame
        except Exception as transform_exception:
            raise transform_exception

    @staticmethod
    def predict(data_frame, model_filename):
        try:
            with open(model_filename,'rb') as file:
                model = pickle.load(file)
                #print(data_frame.apply(lambda x: model.predict(np.array([[x]])), axis=1))
        except Exception as predict_exception:
            raise predict_exception

    def export_to_mysql(self):
        pass


if __name__ == '__main__':
    clv_utils = CLVUtils()
    clv_resource_path = '../resource/orders.csv'
    clv_model_filename = '../resource/model.dill'

    try:
        df = clv_utils.import_from_csv(clv_resource_path, 4500)
        df = clv_utils.transform(df)
        df = clv_utils.predict(df,clv_model_filename)
        print(df.head())
    except Exception as e:
        print(e)
