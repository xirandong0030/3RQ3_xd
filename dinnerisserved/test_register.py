# Student: Xiran Dong 400346507
from dinnerisserved.register import Register



# Requirement: Username cannot be register when the username is not in correct length
def test_wrong_username_length():
    register = Register()
    verify_username_format = register.verify_username_format("john")

    assert verify_username_format == "Wrong username length", "Wrong username length"


# Requirement: Username cannot be register when the username does not only contain with letters and numbers.
def test_wrong_username_format():
    register = Register()
    verify_username_format = register.verify_username_format("johng!!!!")

    assert verify_username_format == "Wrong username format", "Wrong username format"


# Requirement: password cannot be register when the password is not in correct length
def test_wrong_password_length():
    register = Register()
    verify_password_format = register.verify_password_format("16511")

    assert verify_password_format == "Wrong password length", "Wrong password length"
    

# Requirement: password cannot be register when the password does not only contain with letters and numbers.
def test_wrong_password_format():
    register = Register()
    verify_password_format = register.verify_password_format("16511!^&*:;")

    assert verify_password_format == "Wrong password format", "Wrong password format"

