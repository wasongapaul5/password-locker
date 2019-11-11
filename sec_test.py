import unittest
from sec import User

class TestUser(unittest.TestCase):

    '''
    Test  class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase:TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''

        self.new_user = User("Paul","Wasonga","0758669657","wasongapaul5@gmail.com","1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''

        self.assertEqual(self.new_user.first_name,"Paul")
        self.assertEqual(self.new_user.last_name,"Wasonga")
        self.assertEqual(self.new_user.phone_number,"0758669657")
        self.assertEqual(self.new_user.email,"wasongapaul5@gmail.com")
        self.assertEqual(self.new_user.password,"1234")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_uset(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user list
        '''

        self.new_user.save_user()
        test_user = User("Oketch","Paul","0703921156","oketchpaul@gmail.com","1111")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User("Oketch","Paul","0703921156","oketchpaul@gmail.com","1111")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_user.save_user()
            test_user = User("Oketch","Paul","0703921156","oketchpaul@gmail.com","1111")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)
        
    def test_find_user_by_number(self):
            '''
            test to check if we can find a user by phone number and display information
            '''
            self.new_user.save_user()
            test_user = User("Oketch","Paul","0703921156","oketchpaul@gmail.com","1111")
            test_user.save_user()

            found_user = User.find_by_number("0712345678")
            self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
       '''
       test to check if we can return a Boolean if we cannot find then the user
       '''
       self.new_user.save_user()
       test_user = User("Oketch","Paul","0703921156","oketchpaul@gmail.com","1111")
       test_user.save_user()
       user_exist = User.user_exist("Oketch")
       self.assertTrue(user_exist)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

            
if __name__ == '__main__':
    unittest.main()