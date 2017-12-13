import pandas as pd
import numpy
import dill
import datetime
from clv_prediction import CLVPrediction


class CLVUtils:

    def __init__(self):
        pass

    @staticmethod
    def import_from_csv(filename, num_rows=None):
        try:
            columns = ['order_id', 'order_item_id', 'num_items', 'revenue',
                       'created_at_date']
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
            for customer_id, customer_df in grouped_customer_df:
                grouped_order_df = customer_df.groupby('order_id')
                longest_interval = -1
                for order_id, order_df in grouped_order_df:
                    if order_df.shape[0] > 1:
                        longest_interval = \
                            order_df['created_at_date'].diff().max().days
                    else:
                        longest_interval = numpy.nan

                transformed_data_frame.loc[customer_id] = [
                    grouped_order_df.num_items.sum().max(),
                    grouped_order_df.revenue.sum().max(),
                    customer_df.revenue.sum(),
                    customer_df.num_items.sum(),
                    (last_order_date - customer_df.created_at_date.max()).days,
                    longest_interval

                ]

            mean_longest_interval = \
                transformed_data_frame.longest_interval.mean()

            transformed_data_frame = \
                transformed_data_frame.apply(
                    lambda x: x.fillna(
                        value=transformed_data_frame['days_since_last_order'] +
                        mean_longest_interval)
                        )

            transformed_data_frame.index.name = 'customer_id'

            return transformed_data_frame

        except Exception as transform_exception:
            raise transform_exception

    @staticmethod
    def predict(data_frame, model_filename):
        with open(model_filename, 'rb') as file:
            model = dill.load(file)
            data_frame['predicted_clv'] = model.predict(data_frame.values)

        return data_frame

    @staticmethod
    def export_to_csv(data_frame, filename):
        try:
            data_frame.to_csv(filename)
        except Exception as export_exception:
            raise export_exception

    @staticmethod
    def save_to_database(data_frame):
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
