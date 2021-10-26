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

 def setUp(self):
        '''
        This method is responsible for setting up an intialy state before each test begin
        '''
        self.user = User("Nancy", "12345", "n@mail.com")        

    def tearDown(self):
        '''
        This method is responsible for resetting the test env back to intial state by destroying the listed properties
        '''
        User.user_list = [] 

         def test_init(self):
        '''
        A test to check if the class is beign intialized correctly
        '''
        self.assertEqual(self.user.username,"Nancy")
        self.assertEqual(self.user.password,"12345")
        self.assertEqual(self.user.email,"n@mail.com")

  def test_save_user(self):
        '''
        A test to check if the the save method saves the values
        '''
        self.user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        A test to check if the delete method works 
        '''
        self.user.save_user()
        self.new_user = User("nancy","4312", "nancy@mail.com")
        self.new_user_2 = User("muriithin","4262", "muriithin@mail.com")
        self.new_user_2.save_user()
        self.new_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),2)

          def test_find_by_username(self):
        '''
        A test to check if we can retrive a user using a username
        '''
        self.user.save_user()
        new_user = User("Nancy","4312", "nancy@mail.com")
        new_user.save_user()
        found_contact = User.find_by_username("nancy")
        self.assertEqual(found_contact.email,new_user.email)

    def test_user_exists(self):
        '''
        test to check if a User  actually exits
        '''
        self.user.save_user()
        new_user = User("muriithi","6262","muriithi.gmail.com")
        new_user.save_user()
        user_exists = User.user_exists("njeri")
        self.assertTrue(user_exists)

    def test_display_user(self):
        '''
        test to check display stored users
        '''
        self.assertEqual(User.user_list,User.display_user())
        
        