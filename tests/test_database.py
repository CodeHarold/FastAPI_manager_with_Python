

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config
import helpers
import copy
import unittest
import database as db
import csv

class TestDatabase(unittest.TestCase):
    def setUp(self):
       db.Customers.list = [
           db.Customer  ('15J', "John", "Doe"),
           db.Customer  ('48H', "Jane", "Smith"),  
           db.Customer  ('28Z', "Alice", "Johnson")           
        ]        

        

    def test_search(self):
        existing_customer = db.Customers.search('15J')
        non_existing_customer = db.Customers.search('99X')
        self.assertIsNotNone(existing_customer)
        self.assertIsNone(non_existing_customer)

    def test_add(self):
        new_customer = db.Customers.add('40B', "Bob", "Brown")
        self.assertEqual(len(db.Customers.list), 4)
        self.assertEqual(new_customer.id, '40B')
        self.assertEqual(new_customer.name, "Bob")
        self.assertEqual(new_customer.last_name, "Brown")

    def test_remove(self):
        updated_to_be_customer = copy.copy (db.Customers.search('28Z'))
        updated_customer = db.Customers.remove('28Z', "Albert", "Cooper")
        self.assertEqual(updated_to_be_customer.name, "Alice")
        self.assertEqual(updated_customer.name, "Albert")

    def test_delete(self):
        deleted_customer = db.Customers.delete('48H')
        re_serch_customer = db.Customers.search('48H')
        self.assertEqual(deleted_customer.id, '48H')
        self.assertIsNone(re_serch_customer)

    def test_id_validation(self):
        self.assertTrue(helpers.validate_id('00A', db.Customers.list))
        self.assertFalse(helpers.validate_id('232323S', db.Customers.list))
        self.assertFalse(helpers.validate_id('F68', db.Customers.list))
        self.assertFalse(helpers.validate_id('1H', db.Customers.list))


    def test_csv_reading(self):
        # Correctly call the delete and remove methods
        db.Customers.delete = ('48H')
        db.Customers.delete = ('15J')
        db.Customers.remove = ('28Z', "Albert", "Cooper")  

        id, name, last_name = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            id, name, last_name = next(reader)
        
            self.assertEqual(id, '28Z')
            self.assertEqual(name, "Albert")
            self.assertEqual(last_name, "Cooper")

            
