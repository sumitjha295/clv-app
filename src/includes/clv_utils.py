import pandas as pd
import numpy as np
import dill
import datetime
from clv_prediction import CLVPrediction
import inspect


class CLVUtils:

    def __init__(self):
        pass

    @staticmethod
    def import_from_csv(filename, num_rows=None):
        try:
            columns = ['order_id', 'order_item_id', 'num_items', 'revenue', 'created_at_date']
            imported_df = pd.read_csv(
                filename,
                index_col='customer_id',
                parse_dates=['created_at_date'],
                nrows=num_rows
            )
            for column in columns:
                if column not in imported_df.columns:
                    raise ValueError('column %s does not exist.' % column)
            return imported_df

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
            iteration = 0
            for customer_id, customer_df in grouped_customer_df:
                iteration += customer_df.shape[0]
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
            with open(model_filename, 'rb') as file:
                model = dill.load(file)
                data = np.array([[1,2,4,5,6,6],[1,2,4,5,6,6]])
                print(model.predict(data))
                # dummy prediction
                #data_frame['predicted_clv'] = pd.Series(np.random.randn(len(data_frame.index)), index=data_frame.index)
                return data_frame
        except Exception as predict_exception:
            raise predict_exception

    @staticmethod
    def export_to_csv(data_frame, filename):
        try:
            data_frame.to_csv(filename)
        except Exception as export_exception:
            raise export_exception

    @staticmethod
    def save_to_database(data_frame):
        print("save_to_database")
        try:
            CLVPrediction.clean_table()
            for index, row in data_frame.iterrows():
                clv_object = CLVPrediction(
                    customer_id=index,
                    max_number_item=row.max_number_item.item(),
                    max_revenue=row.max_revenue.item(),
                    total_revenue=row.total_revenue.item(),
                    total_orders=row.total_orders.item(),
                    days_since_last_order=row.days_since_last_order.item(),
                    longest_interval=row.longest_interval.item(),
                    predicted_clv=row.predicted_clv.item()
                )
                clv_object.save()
        except Exception as e:
            raise e


if __name__ == '__main__':
    print(__name__)
