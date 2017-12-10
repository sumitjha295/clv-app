import unittest
from order import Order
from dbController import DbController

class TestOrder(unittest.TestCase):
    """
    Test the db controller
    """
    #37d67f5feef4cb754056a54841e43ad9,4662083,21257304,1,24.79,2017-09-01

   

    def setUp(self):
        """
        Clean tbl_orders 
        """  
        db = DbController()
        query = "DELETE FROM tbl_orders"
        db.execute(query)
        """
        create object
        """      
        self.customer_id = "37d67f5feef4cb754056a54841e43ad9"
        self.order_id = 4662083 
        self.order_item_id = 21257304
        self.num_items = 1
        self.revenue = 24.79
        self.created_at_date = "2017-09-01"
        self.orderObject = Order(self.customer_id,self.order_id,self.order_item_id,self.num_items,self.revenue,self.created_at_date)


    def test_constructor(self):
        """
        Test db controller
        """
        self.assertEqual(self.orderObject.customer_id, self.customer_id)
        self.assertEqual(self.orderObject.order_id, self.order_id)
        self.assertEqual(self.orderObject.order_item_id, self.order_item_id)
        self.assertEqual(self.orderObject.num_items, self.num_items)
        self.assertEqual(self.orderObject.revenue, self.revenue)
        self.assertEqual(self.orderObject.created_at_date, self.created_at_date)


    def test_order(self):
        """
        Test order save
        """
        self.orderObject.save()
        self.assertNotEqual(self.orderObject.id, -1)
        
        """
        Test findById
        """
        data = self.orderObject.findById(self.orderObject.id)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["customer_id"], self.customer_id)
        self.assertEqual(data[0]["order_id"], self.order_id)
        self.assertEqual(data[0]["order_item_id"], self.order_item_id)
        self.assertEqual(data[0]["num_items"], self.num_items)
        self.assertEqual(data[0]["revenue"], self.revenue)
        self.assertEqual(data[0]["created_at_date"].strftime("%Y-%m-%d"), self.created_at_date)

        
        """
        Test findByCustomerId
        """

        data = self.orderObject.findByCustomerId(self.orderObject.customer_id)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], self.orderObject.id)
        self.assertEqual(data[0]["order_id"], self.order_id)
        self.assertEqual(data[0]["order_item_id"], self.order_item_id)
        self.assertEqual(data[0]["num_items"], self.num_items)
        self.assertEqual(data[0]["revenue"], self.revenue)
        self.assertEqual(data[0]["created_at_date"].strftime("%Y-%m-%d"), self.created_at_date)


        self.orderObject.deleteById(self.id)
        data = self.orderObject.findById(self.orderObject.id)
        print (data)
        self.assertEqual(len(data), 0)







if __name__ == '__main__':
    unittest.main()
