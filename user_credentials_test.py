from user import User
from user import Credential
import unittest



class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            'paul', 'pal', 'wasongapaul5@gmail.com', '0791555693', '12081998')

    def test__init__(self):
        self.assertEqual(self.new_user.first_name, 'paul')
        self.assertEqual(self.new_user.last_name, 'pal')
        self.assertEqual(self.new_user.email, 'wasongapaul5@gmail.com')
        self.assertEqual(self.new_user.phone_number, '0791555693')
        self.assertEqual(self.new_user.password, '12081998')

    def tearDown(self):
        Credential.credential_list = []
        User.users_list = []

    def test_save_user(self):
        '''
        Method to test if we can save the user details
        '''
        self.new_user.save_user()
        test_user = User('paul', 'pal', 'wasongapaul51998@gmail.com',
                         '0791555693', '12081998')
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)

    def test_delete_user(self):
        '''
        Method to test if we can delete a user
        '''
        self.new_user.save_user()
        test_user = User('paull', 'pal', 'wasongapaul5@gmail.com',
                         '0791555693', '12081998')
        test_user.save_user()
        test_user.delete_user()
        self.assertEqual(len(User.users_list), 1)


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential(
            'paul', 'twitter', 'wasongapaul5', '120819985')

    def test__init__(self):
        self.assertEqual(self.new_credential.user_name, 'paul')
        self.assertEqual(self.new_credential.site_name, 'twitter')
        self.assertEqual(self.new_credential.account_name, 'wasongapaul5')
        self.assertEqual(self.new_credential.password, '120819985')
# Testing credentials

    def tearDown(self):
        Credential.credential_list = []
        User.users_list = []

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential('paul', 'twitter', 'wasongapaul5', '120819985')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        twitter = Credential('paul', 'twitter', 'wasongapaul5', '120819985')
        twitter.save_credentials()
        twitter.delete_credentials()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_account_type method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('paul', 'twitter', 'wasongapaul5', '120819985')
        twitter.save_credentials()
        credential_found = Credential.find_by_site_name('twitter')
        self.assertEqual(credential_found.password, twitter.password)


if __name__ == '__main__':
    unittest.main()