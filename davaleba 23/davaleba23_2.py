class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough amount")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount(100)
print("Initial balance:", account.get_balance())

account.deposit(50)
print("Balance after deposit:", account.get_balance())

account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())

account.withdraw(150)


class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("Incorrect score")

    def get_average(self):
        if len(self._scores) == 0:
            return 0
        return sum(self._scores) / len(self._scores)

    def get_scores(self):
        return self._scores


students = []

student1 = Student("Mari")
student1.add_score(85)
student1.add_score(90)

student2 = Student("Nino")
student2.add_score(75)
student2.add_score(95)

students.append(student1)
students.append(student2)

for student in students:
    print(f"{student._name} - Scores: {student.get_scores()} - Average: {student.get_average()}")

student3 = Student("Nika")
student3.add_score(67)
student3.add_score(100)

students.append(student3)

print(f"{student3._name} - Scores: {student3.get_scores()} - Average: {student3.get_average()}")