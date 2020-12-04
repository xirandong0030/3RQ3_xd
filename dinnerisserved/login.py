# Student: Xiran Dong 400346507
class Login:


    def verify_user(self, username, password):
        valid_user = {
            username: "john0030",
            password: "234567AB"
        }
        if username == valid_user[username]:
            pass
        else:
            return "Invalid Username."

        if password == valid_user[password]:
            return True
        else:
            return "Password Wrong, Please try again."


