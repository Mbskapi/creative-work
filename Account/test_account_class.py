import unittest

from Account.account import Account


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        self.assertEqual(0, self.acc.balance)

    def test_that_account_has_a_name(self):
        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_money_can_be_deposited_into_my_account_successfully(self):
        self.acc.deposit(100)
        self.assertEqual(100, self.acc.balance)

    def test_that_i_can_withdraw_form_current_balance(self):
        self.acc.balance(50)
        self.assertEqual(50,self.acc.balance)


if __name__ == '__main__':
    unittest.main()
