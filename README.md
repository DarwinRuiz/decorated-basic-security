# Python Decorated Security

## Description

This Python project is a simple user authentication system. It includes a `User` class with methods for saying hello, showing the user's password (partially obscured), and changing the user's password. The `User` class and the `change_password` method are decorated with `authenticate_class` and `validate_password` decorators, respectively, to handle authentication and password validation.

## Features

- User instance creation with username and password
- Greeting the user with a hello message
- Displaying the user's password (partially obscured)
- Changing the user's password with validation

## Installation

To install the project, follow these steps:

1. Clone the repository: `git clone https://github.com/username/projectname.git`
2. Navigate into the project directory: `cd decorated-basic-security`

## Usage

To run the application, use the following command:

```bash
python main.py