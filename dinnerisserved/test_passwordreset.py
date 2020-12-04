# Student: Xiran Dong 400346507
from dinnerisserved.passwordreset import Password_reset


# Requirement: Cannot reset password when enter invalid username
def test_passwordreset_invalid_username():
    passwordreset = Password_reset()
    security_answer_confirm = passwordreset.security_answer_confirm("a", "B")

    assert security_answer_confirm == "Invalid Username." , "Username is invalid"


# Requirement: Cannot reset password when enter invalid security answer
def test_passwordreset_invalid_security_answer():
    passwordreset = Password_reset()
    security_answer_confirm = passwordreset.security_answer_confirm("john0030", "AB")

    assert security_answer_confirm == "Your answer is wrong" , "Your answer is wrong"

# Requirement: Reset password when enter correct username and security answer
def test_passwordreset():
    passwordreset = Password_reset()
    security_answer_confirm = passwordreset.security_answer_confirm("john0030", "B")

    assert security_answer_confirm == True , "Security answer is correct."
