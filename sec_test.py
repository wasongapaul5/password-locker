import unittest
from sec import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase:TestCase class that in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Paul","Wasonga","0758669657","wasongapaul5@gmail.com","1234") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Paul")
        self.assertEqual(self.new_user.last_name,"Wasonga")
        self.assertEqual(self.new_user.phone_number,"0758669657")
        self.assertEqual(self.new_user.email,"wasongapaul5@gmail.com")


if __name__ == '__main__':
    unittest.main()