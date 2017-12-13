from db_controller import DbController


class CLVPrediction:

    def __init__(self,
                 customer_id="",
                 max_number_item=0,
                 max_revenue=0,
                 total_revenue=0,
                 total_orders=0,
                 days_since_last_order=0,
                 longest_interval=0,
                 predicted_clv=0
                 ):
        self.id = -1
        self.customer_id = customer_id
        self.max_number_item = max_number_item
        self.max_revenue = max_revenue
        self.total_revenue = total_revenue
        self.total_orders = total_orders
        self.days_since_last_order = days_since_last_order
        self.longest_interval = longest_interval,
        self.predicted_clv = predicted_clv

    def save(self):
        try:
            db = DbController()
            query = "INSERT INTO tbl_clv_prediction (" \
                    "id, " \
                    "customer_id, " \
                    "max_number_item," \
                    "max_revenue," \
                    "total_revenue, " \
                    "total_orders," \
                    "days_since_last_order," \
                    "longest_interval," \
                    "predicted_clv" \
                    ")" \
                    " VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (self.customer_id,
                    self.max_number_item,
                    self.max_revenue,
                    self.total_revenue,
                    self.total_orders,
                    self.days_since_last_order,
                    self.longest_interval,
                    self.predicted_clv
                    )

            db.execute(query, data)
            self.id = db.last_inserted_id
        except Exception as e:
            raise e

    def load(self):
        data = self.find_by_customer_id(self.customer_id)
        if len(data) == 0:
            raise ValueError('customer %s does not exist' % self.customer_id)
        else:
            self.id = data[0].id
            self.max_number_item = data[0].max_number_item
            self.max_revenue = data[0].max_revenue
            self.total_revenue = data[0].total_revenue
            self.total_orders = data[0].total_orders
            self.days_since_last_order = data[0].days_since_last_order
            self.longest_interval = data[0].longest_interval,
            self.predicted_clv = data[0].predicted_clv

    @staticmethod
    def clean_table():
        try:
            db = DbController()
            query = "DELETE FROM tbl_clv_prediction"
            db.execute(query)
        except Exception as e:
            raise e

    @staticmethod
    def find_by_customer_id(customer_id):
        try:
            db = DbController()
            query = "SELECT * FROM tbl_clv_prediction where customer_id = %s"
            return db.execute_select(query, [customer_id])
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(clv_id):
        try:
            db = DbController()
            query = "DELETE FROM tbl_clv_prediction where id = %s"
            db.execute(query, [clv_id])
        except Exception as e:
            raise e

    def delete(self):
        try:
            self.load()
            self.delete_by_id(self.id)
        except Exception as e:
            raise e


if __name__ == "__main__":
    print(__name__)
