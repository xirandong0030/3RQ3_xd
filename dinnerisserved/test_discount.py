# Student: Xiran Dong 400346507
from dinnerisserved.discount import Discount


# Requirement: No discount applied when customers have placed less than 5 orders and set discount is 0.
def test_discount_zero_percent():
    discount = Discount()
    calculated_discount = discount.calculated_discount(3, 0)

    assert calculated_discount == 0, "discount should be 0%!"


# Requirement: No discount applied when customers have placed less than 5 orders and set discount is 5%.
def test_discount_five_percent():
    discount = Discount()
    calculated_discount = discount.calculated_discount(3, 0.05)

    assert calculated_discount == 0.05, "discount should be 5%!"


# Requirement: discount of 10% is applied when customers have placed 5 orders and set discount is 5%.
def test_discount_ten_percent():
    discount = Discount()
    calculated_discount = discount.calculated_discount(5, 0)

    assert calculated_discount == 0.1, "discount should be 10%!"


# Requirement: discount of 15% is applied when customers have placed 5 orders and set discount is 5%.
def test_discount_fifteen_percent():
    discount = Discount()
    calculated_discount = discount.calculated_discount(5, 0.05)

    assert calculated_discount == 0.15000000000000002, "discount should be 15%!"
