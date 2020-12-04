# Student: Xiran Dong 400346507
import re
class Register:


    def verify_username_format(self, username):
        u = re.compile(r'[a-zA-Z0-9]*$')
        valid_username = ["john", "bob"]
        if len(username) > 5 and len(username) < 20:
            pass
        else:
            return "Wrong username length"

        if u.match(username):
            pass
        else:
            return "Wrong username format"

        if username in valid_username:
            return "This username exist"
        else:
            return True


    def verify_password_format(self, password):
        p = re.compile(r'[a-zA-Z0-9()$%_/.]*$')
        if len(password) > 7 and len(password) < 20:
            pass
        else:
            return "Wrong password length"

        if p.match(password):
            return True
        else:
            return"Wrong password format"
