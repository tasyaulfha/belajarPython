def hint_username(username):
    if len(username) <3 :
        print("invalid username, Must be at least 3 characters long") 
    else:
        print("Valid username")
hint_username("tasya")

def is_even(number):
    if number % 2 ==0:
        return True
    return False
is_even(5)

def hint_username(username):
    if len(username) <3 :
        print("invalid username, Must be at least 3 characters long") 
    elif len(username)>15 :
            print("invalid username, must be at most 15 characters long")
    else:
        print("Valid username")
hint_username("tasya")
