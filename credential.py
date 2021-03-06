import pyperclip


class Credential:
    """
    a class that creates new credentials 
    """
    credential_list = []

    def __init__(self, account_name,username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            credential_name: New credential credential_name.
            password : New credential password.
            number: New contact phone number.
        '''
        self.account_name = account_name        
        self.username =username
        self.password = password

        
    def save_credential(self):
        '''
        save_credential method saves credential object into the credential_list
        '''
        Credential.credential_list.append(self)

     def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)
         @classmethod
    def find_credential_by_account_name(cls,account_name):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.
        Args:
        account_name:account_name to search for
        Returns:
        credential  that matches the account_name.
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential


    @classmethod
    def credential_exist(cls,account_name):
        '''
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        list = cls.credential_list
        for l in list:
            print(l.__dict__)

    @classmethod
    def copy_username(cls ,account_name):
        credentials_found = Credential.find_credential_by_account_name(account_name)
        pyperclip.copy(credentials_found.username)

    @classmethod
    def copy_password(cls ,account_name):
        credentials_found = Credential.find_credential_by_account_name(account_name)
        pyperclip.copy(credentials_found.password)