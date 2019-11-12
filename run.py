#!/usr/bin/env python3.6
from sec import User

def create_user(fname,lname,phone,email,password):
    '''
    Function to create a new user
    '''

    new_user = User(fname,lname,phone,email,password)
    return new_user

def save_users(User):
    '''
    Function to save user
    '''
    user.save_user()
    

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
     
  


def find_user(user):
    '''
    Function that finds a user by number and returns the user
    '''

    return User.find_by_number(number)
   
def check_existing_users(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your user list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cu - create a new user, du - display users, fc -find a user, ex -exit the usert list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("password...")
                            password = input()


                            save_users(create_user(f_name,l_name,p_number,e_address,password)) 
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_users(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()