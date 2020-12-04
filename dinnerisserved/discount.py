# Student: Xiran Dong 400346507
class Discount:


    def calculated_discount(self, num_orders, set_value):
        if num_orders >= 5 :
            num_orders = num_orders - 5
            return 0.1 + set_value
        else:
            return set_value

