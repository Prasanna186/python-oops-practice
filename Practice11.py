class Payment :
    def pay(self, amount):
        pass
class CreditCard(Payment):
    def __init__(self, card_number):
        super().__init__()
        self.card_number = card_number
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card: {self.card_number}")
class UPI(Payment):
    def __init__(self, upi_id):
        super().__init__()
        self.upi_id = upi_id
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI: {self.upi_id}")
class Cash(Payment):
    def __init__(self):
        super().__init__()
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")
credit = CreditCard("1234-5678-9012-3456")
upi = UPI("prasanna@upi")
cash = Cash()
payments = [credit, upi, cash]
for payment in payments :
    payment.pay(5000)
