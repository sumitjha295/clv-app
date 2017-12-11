from twisted.trial import unittest
from db_controller import DbController
from settings import db_config


class TestDbController(unittest.TestCase):
    """
    Test the db controller
    """

    def test_constructor(self):
        """
        Test db controller
        """
        db_object = DbController()
        cfg = db_config()
        self.assertEqual(db_object.host, cfg["host"])
        self.assertEqual(db_object.user, cfg["user"])
        self.assertEqual(db_object.password, cfg["password"])
        self.assertEqual(db_object.db, cfg["db"])

    def test_execute_select(self):
        """
        Test db execute
        """
        db_object = DbController();
        cfg = db_config()
        query = 'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s'
        results = db_object.execute_select(query, [cfg["db"]])
        self.assertEqual(db_object.row_count, 1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['SCHEMA_NAME'], cfg["db"])


if __name__ == '__main__':
    unittest.main()
