import csv
import re


DATA_PATH = 'data/users.csv'

def get_users(file_dir):
    with open(file_dir, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def authenticate(username, password):
    user = {
        'username': username,
        'password': password	
    }
    
    users = get_users(DATA_PATH)
    if user in users:
        return True
    

def validate_secure_password(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}"
    return bool(re.match(pattern, password))


def change_password(username,  new_password):


    users = get_users(DATA_PATH)
    for user in users:
        if user['username'] == username:
            user['password'] = new_password
            break
    
    with open(DATA_PATH, 'w', newline='') as file:
        fields = ['username', 'password']
        csv_writer = csv.DictWriter(file, fieldnames=fields)

        csv_writer.writeheader()
        csv_writer.writerows(users)