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
        delete_user method deletes a saved contact from our user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,email):
        '''
        Method that takes in an email and retuens a user that matches that email.
        
        Args:
            email:Email to search for
        Returns:
            User of person that matches the email.
        '''

        for user in cls.user_list:
            if user.email == email:
                return user

   @classmethod
   def user_exists = 
