class User:
    '''
    Class that generates new instances of users.
    '''

    user_list = []

    def __init__ (self,first_name,last_name,phone_number,email,password):



        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

       
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns  a user that matches that number.

        Args:
            number:Phone number to search for
        Returns:
            User of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exists(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number:phone number to search if it exists
        Returns:
            Boolean:True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return True