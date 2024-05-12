import functools

from utils.users import authenticate, validate_secure_password


def authenticate_class(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if authenticate(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception("Not autenticated")
    return wrapper


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            password = args[1]
        except IndexError:
            raise Exception("Password is required")
        
        if validate_secure_password(password):
            return func(*args, **kwargs)
        else:
            raise Exception('The password must contain at least 8 characters, including at least one letter, one number, and one special character such as @$!%*?&.')
    return wrapper