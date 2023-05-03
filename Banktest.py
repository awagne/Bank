import unittest
from unittest import mock
import Bank

class Banktest(unittest.TestCase):

    @mock.patch('builtins.input', create=True)
    def test_create(self, mocked_input):
        bank = Bank.Bank([])
        mocked_input.side_effect = ['Alan']
        bank.createAccount()

        self.assertEqual(len(bank.accounts), 1)
        self.assertEqual(bank.accounts[0].getOwner(), "Alan")

    @mock.patch('builtins.input', create=True)
    def test_delete(self, mocked_input):
        bank = Bank.Bank([])
        mocked_input.side_effect = ['Alan']
        bank.createAccount()

        self.assertEqual(len(bank.accounts), 1)
        bank.deleteAccount(bank.accounts[0].getNum())
        self.assertEqual(len(bank.accounts), 0)

    @mock.patch('builtins.input', create=True)
    def test_get(self, mocked_input):
        bank = Bank.Bank([])
        mocked_input.side_effect = ['Alan']
        bank.createAccount()

        account = bank.getAccount("Alan", bank.accounts[0].getNum())
        self.assertEqual(account.getOwner(), "Alan")
        self.assertEqual(account.getNum(), bank.accounts[0].getNum())
    

if __name__ == '__main__':
    unittest.main()