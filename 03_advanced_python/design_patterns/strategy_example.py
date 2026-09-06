class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} with card"

class CashPayment:
    def pay(self, amount):
        return f"Paid {amount} in cash"


class Payment:
    def __init__(self, payment_type):
        self.payment_type = payment_type

    def pay(self, amount):
        return self.payment_type.pay(amount)



payment = Payment(CashPayment())
print(payment.pay(100))

payment = Payment(CardPayment())
print(payment.pay(200))