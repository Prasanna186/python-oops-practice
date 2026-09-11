class Address:
    def __init__(self, city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def display_address(self):
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Pincode: {self.pincode}")


class Student:
    def __init__(self, name, roll_number, address):
        self.name = name
        self.roll_number = roll_number
        self.address = address

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        self.address.display_address()

address1 = Address("Bangalore", "Karnataka", 560001)

student1 = Student("Prasanna", 101, address1)

student1.display_details()