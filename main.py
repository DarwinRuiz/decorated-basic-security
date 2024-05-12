

from models.user import User


try:
    user = User("darwinruiz", "darwinTest1234$")
    print(user.say_hello())
    print(user.show_password())


    # This should change the password
    print(user.change_password("darwinTest1234*"))

    # This should raise an exception
    print(user.change_password("darwin1"))

except Exception as exception:
    print(exception)


