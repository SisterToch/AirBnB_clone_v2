#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestCreateCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.console.reset_output()
        storage.reload()

    def test_create_with_params(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel name=\"My little house\" number=42 price=10.5")
            output = mock_stdout.getvalue().strip()

        self.assertTrue(len(output) == 36)
        created_instance = storage.all()['BaseModel.' + output]
        self.assertEqual(created_instance.name, "My little house")
        self.assertEqual(created_instance.number, 42)
        self.assertEqual(created_instance.price, 10.5)

    # Add more tests as needed

