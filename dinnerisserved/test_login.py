# Student: Xiran Dong 400346507
from dinnerisserved.login import Login


# Requirement: Cannot login when enter invalid username
def test_login_invalid_username():
    login = Login()
    verify_user = login.verify_user("a", "234567AB")

    assert verify_user == "Invalid Username." , "Username is invalid"


# Requirement: Cannot login when wrong password
def test_login_wrong_password():
    login = Login()
    verify_user = login.verify_user("john0030", "AB")

    assert verify_user == "Password Wrong, Please try again." , "Password is wrong."



# Requirement: Login with correct username and password
def test_login_login():
    login = Login()
    verify_user = login.verify_user("john0030", "234567AB")

    assert verify_user == True , "Login successfully"