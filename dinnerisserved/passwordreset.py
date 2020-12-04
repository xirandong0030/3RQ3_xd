# Student: Xiran Dong 400346507
class Password_reset:


    def security_answer_confirm(self, username, security_answer):
        valid_user = {
            username: "john0030",
            security_answer: "B"
        }

        if username == valid_user[username]:
            pass
        else:
            return "Invalid Username."

        if security_answer == valid_user[security_answer]:
            return True
        else:
            return "Your answer is wrong"