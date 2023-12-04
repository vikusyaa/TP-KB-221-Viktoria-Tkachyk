import unittest
import io
from unittest.mock import patch
from lab2 import load_data, saveData, addStudent, deleteUser

class TestLab2Script(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_lab2.csv"
        self.test_data = [
            {"name": "Alice", "phone": "9675643454", "age": "21", "gender": "man"},
            {"name": "John","phone": "734586290", "age": "19", "gender": "woman"},
        ]


    def test_load_data(self):
        with open(self.test_file, "w") as file:
            file.write("name,phone,age,gender\nJohn,1234567890,25,male\nAlice,9876543210,22,female")

        data = load_data(self.test_file)
        self.assertEqual(data, [
            {"name": "John", "phone": "1234567890", "age": "25", "gender": "male"},
            {"name": "Alice", "phone": "9876543210", "age": "22", "gender": "female"}
        ])

    def test_saveData(self):
        saveData(self.test_file, self.test_data)
        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_addStudent(self):
        with patch('builtins.input', side_effect=["Bob", "1234567890", "25", "male"]):
            addStudent(self.test_data)
            self.assertEqual(len(self.test_data), 3)

    def test_deleteElement(self):
        with patch('builtins.input', return_value="John"):
            deleteUser(self.test_data)
            self.assertEqual(len(self.test_data), 1)

if __name__ == '__main__':
    unittest.main()