class Employee:
    grade = "Very Good"
    def __init__(self, first, last, salary):
        self.FirstName = first
        self.LastName = last
        self.Salary = salary
        self.Email = first+'.'+last+'@company.com'

    def profit(self,years):
        netpay = self.Salary*int(years)
        return netpay

khamis = Employee("Mohamed", "Khamis", "40k USD")
print(khamis.Email)
sofy = Employee("Ahmed","Sofy",50000)
share = sofy.profit(3)
print(share)

print ("new commit")
print ("new push")