import unittest
import os
import sys
import numpy
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../api')
from clv_utils import CLVUtils


class TestCLVUtils(unittest.TestCase):

    def setUp(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.clv_utils = CLVUtils()
        self.clv_resource_path = self.current_path + \
            '/../resource/test_orders/test_orders.csv'
        self.clv_model_path = self.current_path + \
            '/../resource/model.dill'
        self.clv_export_path = self.current_path + \
            '/../output/prediction.csv'

    def test_clv_import(self):

        self.assertRaises(Exception,
                          self.clv_utils.import_from_csv, 'invalid_path.csv')

        self.assertRaises(ValueError,
                          self.clv_utils.import_from_csv, self.current_path +
                          '/../resource/test_orders/invalid.csv')

        df = self.clv_utils.import_from_csv(self.clv_resource_path)
        columns = ['order_id', 'order_item_id', 'num_items', 'revenue',
                   'created_at_date']
        self.assertCountEqual(df.columns, columns)
        for column in columns:
            self.assertEqual(column in df.columns, True)

        self.assertEqual(df.shape[1], 5)
        self.assertEqual(df.shape[0], 9)

    def test_clv_transform(self):
        df = self.clv_utils.import_from_csv(self.clv_resource_path)
        df = self.clv_utils.transform(df)
        clv_columns = [
            'max_number_item',
            'max_revenue',
            'total_revenue',
            'total_orders',
            'days_since_last_order',
            'longest_interval'
        ]

        for column in clv_columns:
            self.assertEqual(column in df.columns, True)

        self.assertEqual(df.index.name, 'customer_id')
        self.assertEqual(df.shape[0], 2)
        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].max_number_item, 8)

        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].max_revenue, 57.54)

        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].total_orders, 9)

        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].total_revenue, 64.91)

        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].days_since_last_order,
            16)

        self.assertEqual(
            df.loc['37d67f5feef4cb754056a54841e43ad9'].longest_interval, 0)

    def test_clv_predict(self):
        df = self.clv_utils.import_from_csv(self.clv_resource_path)
        df = self.clv_utils.transform(df)
        # df = self.clv_utils.predict(df, self.clv_model_path)
        # self.assertEqual('predicted_clv' in df.columns, True)

    def test_clv_export(self):
        pass
        # df = self.clv_utils.import_from_csv(self.clv_resource_path)
        # df = self.clv_utils.transform(df)
        # df = self.clv_utils.predict(df, self.clv_model_path)

        # if os.path.isfile(self.clv_export_path):
        #    os.remove(self.clv_export_path)

        # self.assertEqual(os.path.isfile(self.clv_export_path), False)
        # self.clv_utils.export_to_csv(df, self.clv_export_path)
        # self.assertEqual(os.path.isfile(self.clv_export_path), True)

    def test_clv_save_to_db(self):
        pass


if __name__ == '__main__':
    unittest.main()
