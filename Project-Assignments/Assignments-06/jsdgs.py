# class Student:
#     def __init__(self, name, engMarks , mathMarks, phyMarks):
#         self.name = name
#         self.engMarks = engMarks
#         self.mathMarks = mathMarks
#         self.phyMarks = phyMarks


#     def display(self):
#         print(f"Name: {self.name}, English Marks: {self.engMarks}, Math Marks: {self.mathMarks}, Physics Marks: {self.phyMarks}")

# st1 = Student("John", 85, 90, 95)
# st2 = Student("Jane", 80, 85, 90)
# st1.display()
# st2.display()


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


acc1 = Account("123456", 1000)
acc2 = Account("654321", 2000)
acc1.debit(200)
acc1.credit(500)
acc1.display_balance()