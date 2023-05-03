import unittest
import Account

class Accounttest(unittest.TestCase):

    def testDeposit(self):
        account = Account.Account("Alan")

        account.deposit(10, 'c')
        self.assertEqual(account.getCheckings(), 10)

        account.deposit(10, 's')
        self.assertEqual(account.getSavings(), 10)

        account.deposit(-10, 'c')
        self.assertEqual(account.getCheckings(), 10)

        account.deposit(-10, 's')
        self.assertEqual(account.getSavings(), 10)

    def testWithdraw(self):
        account = Account.Account("Alan")

        account.deposit(10, 'c')
        self.assertEqual(account.getCheckings(), 10)

        account.deposit(10, 's')
        self.assertEqual(account.getSavings(), 10)

        account.withdraw(10, 'c')
        self.assertEqual(account.getCheckings(), 0)

        account.withdraw(10, 's')
        self.assertEqual(account.getSavings(), 0)

        account.withdraw(-10, 'c')
        self.assertEqual(account.getCheckings(), 0)

        account.withdraw(-10, 's')
        self.assertEqual(account.getSavings(), 0)

if __name__ == '__main__':
    unittest.main()