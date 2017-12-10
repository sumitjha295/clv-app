import unittest
from dbController import DbController
from settings import dbConfig


class TestDbController(unittest.TestCase):
    """
    Test the db controller
    """

    def test_constructor(self):
        """
        Test db controller
        """
        dbObject = DbController();
        cfg = dbConfig()
        self.assertEqual(dbObject.host, cfg["host"])
        self.assertEqual(dbObject.user, cfg["user"])
        self.assertEqual(dbObject.passwd, cfg["passwd"])
        self.assertEqual(dbObject.db, cfg["db"])

    def test_execute(self):
        """
        Test db execute
        """
        dbObject = DbController();
        cfg = dbConfig()
        query = 'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s'
        value = dbObject.execute(query, [cfg["db"]])
        self.assertEqual(dbObject.rowCount, 1)


if __name__ == '__main__':
    unittest.main()
