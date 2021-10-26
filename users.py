class User:
    '''
    Class that creates a new instance of a user
    '''
    user_list = [] #store the users
    def __init__(self, username, password, email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user username.
            password : New user password.
            email : New user email.
        '''

        self.username = username
        self.password = password
        self.email = email
