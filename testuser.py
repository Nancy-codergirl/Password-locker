import unittest
from user import  User

class UserTestCreate(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        This method is responsible for setting up an intialy state before each test begin
        '''
        self.user = User("Nancy", "12345", "n@mail.com")        
