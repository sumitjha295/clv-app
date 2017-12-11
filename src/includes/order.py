from db_controller import DbController


class CLVPrediction:

    def __init__(self, customer_id, order_id, order_item_id, num_items, revenue, created_at_date):
        self.id = -1
        self.customer_id = customer_id
        self.order_id = order_id
        self.order_item_id = order_item_id
        self.num_items = num_items
        self.revenue = revenue
        self.created_at_date = created_at_date

    def save(self):
        try:
            db = DbController()
            query = "INSERT INTO tbl_orders (" \
                    "id, " \
                    "customer_id, " \
                    "order_id," \
                    "order_item_id," \
                    "num_items, revenue," \
                    "created_at_date" \
                    ")" \
                    " VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            data = (self.customer_id, self.order_id, self.order_item_id,
                    self.num_items, self.revenue, self.created_at_date)
            db.execute(query, data)
            self.id = db.lastInsertedId
        except Exception as e:
            raise e

    def update(self):
        try:
            pass
        except Exception as e:
            raise e

        return False

    def find_by_id(self, id):
        try:
            db = DbController()
            query = "SELECT * FROM tbl_orders where id = %s"
            return db.executeSelect(query, [id])
        except Exception as e:
            raise e

    def find_by_customer_id(self, customer_id):
        try:
            db = DbController()
            query = "SELECT * FROM tbl_orders where customer_id = %s"
            return db.executeSelect(query, [customer_id])
        except Exception as e:
            raise e

    def delete_by_id(self, id):
        try:
            db = DbController()
            query = "DELETE FROM tbl_orders where id = %s"
            db.execute(query, [id])
        except Exception as e:
            raise e

if __name__ == "__main__":
    print(__name__)
