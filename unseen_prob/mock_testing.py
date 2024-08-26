import unittest
from unittest.mock import patch
import app

class TestApp(unittest.TestCase):

    @patch('app.items', [])
    def test_create_item(self):
        item = {'id': 1, 'name': 'Test Item', 'price': 10.0}
        result = app.create_item(item)
        self.assertEqual(result, item)
        self.assertEqual(app.items, [item])

    @patch('app.items', [{'id': 2, 'name': 'Test Item 2', 'price': 20.0}])
    def test_read_item(self):
        result = app.read_item(2)
        self.assertEqual(result, {'id': 2, 'name': 'Test Item 2', 'price': 20.0})

    @patch('app.items', [{'id': 3, 'name': 'Old Item', 'price': 30.0}])
    def test_update_item(self):
        updated_item = {'id': 3, 'name': 'Updated Item', 'price': 35.0}
        result = app.update_item(3, updated_item)
        self.assertEqual(result, updated_item)
        self.assertEqual(app.items, [updated_item])

    @patch('app.items', [{'id': 4, 'name': 'Item to Delete', 'price': 40.0}])
    def test_delete_item(self):
        result = app.delete_item(4)
        self.assertEqual(result, {'id': 4, 'name': 'Item to Delete', 'price': 40.0})
        self.assertEqual(app.items, [])

if __name__ == '__main__':
    unittest.main()
