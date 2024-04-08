import unittest
import json
import os
from unittest.mock import patch
from main import LoadData, SaveData, AddTransaction, ViewTransactions


class TestFinanceHelper(unittest.TestCase):
    def setUp(self):
        self.TestData = {'food': {'income': 0, 'expense': 0},
                         'entertainment': {'income': 0, 'expense': 0}}
        self.FileName = 'testdata.json'

    def tearDown(self):
        if os.path.exists(self.FileName):
            os.remove(self.FileName)

    def test_load_data(self):
        with open(self.FileName, 'w') as f:
            json.dump(self.TestData, f)
        loaded_data = LoadData(self.FileName)
        self.assertEqual(loaded_data, self.TestData)

    def test_save_data(self):
        SaveData(self.TestData, self.FileName)
        with open(self.FileName, 'r') as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data, self.TestData)

    def test_add_transaction(self):
        test_input = [
            '20', 'dinner', 'expense',
            '50', 'movie theater', 'expense',
            '200', 'job', 'income',
            '30', 'entertainment', 'expense',
        ]
        expected_data = {
            'food': {'expense': 20},
            'movie theater': {'expense': 50},
            'job': {'income': 200},
            'entertainment': {'expense': 30}
        }
        with patch('builtins.input', side_effect=test_input):
            AddTransaction(self.TestData)
        self.assertEqual(self.TestData, expected_data)

    def test_view_transactions(self):
        with patch('sys.stdout', new=unittest.mock.MagicMock()) as mock_stdout:
            ViewTransactions(self.TestData)
            expected_output = 'Category\tIncome\tExpense\tBalance\nfood\t0\t0\t0\nentertainment\t0\t0\t0\n'
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
