from decorators.users import authenticate_class, validate_password
from utils.users import change_password

@authenticate_class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def say_hello(self):
        return f"Hello, {self.username}!"
    
    def show_password(self):
        return f"Your password is {self.password[:4]}{len(self.password[4:])*'*'}!"
    
    @validate_password
    def change_password(self, new_password):
        self.password = new_password
        change_password(self.username, new_password)
        return f"Your new password is {self.password[:4]}{len(self.password[4:])*'*'}!"
    