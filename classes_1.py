'''
Classes ,OOP and inheriatance
    1.Instance variables and methods
    2.Class variables and methods
    3.Inheritance and Resolution Order 
    https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
    '''

class Employee:
    no_of_employees=0
    annual_increament =3
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        Employee.no_of_employees +=1

    def fullname(self):
        return '{} {}'.format(self.last,self.first)

    def apply_raise(self):
        self.pay=int(self.pay * Employee.annual_increament)

    @classmethod
    def from_string(cls,cls_string):
        first,last,pay=cls_string.split('-')
        return cls(first,last,pay)

    def __repr__(self):
        return f'{self.fullname()}..{self.no_of_employees} th instancce'



# print('No of Employees= {}'.format(Employee.no_of_employees))
emp1=Employee('karani','pranavi',60000)
# print('No of Employees ={}'.format(Employee.no_of_employees))
emp2=Employee('karani','ganesh',50000)
# print('No of Employees= {}'.format(Employee.no_of_employees))

#
# print(emp1.email)
# print(emp2.email)
# print(emp1.fullname())
# print(Employee.fullname(emp2))


# Cehck the instance variables how it will be behaved
# print(emp1.pay)
# # emp1.annual_increament=2      Instance variables wont be affect , as it is using the class variable
# emp1.apply_raise()
# print(emp1.pay)
# print(emp2.pay)
# emp2.apply_raise()
# print(emp2.pay)




#Chgeck the namespace variables and methods  for instances and classes

# print(emp1.__dict__)
# print(Employee.__dict__)

# regular methods , class methods (alternative constructors), static methods (utility methods if it doesn't belong to any instance or classes varibles then it should be static method)

# new_emp1_str='siva-karani-100000'
# new_emp2_str='rathna-karani-120000'
# new_emp1=Employee.from_string(new_emp1_str)
# new_emp2=Employee.from_string(new_emp2_str)
#
# print(new_emp1.fullname())
# print(new_emp2.fullname())
#
# print(emp1.no_of_employees)
# print(Employee.__dict__)


###INHERITANCE
    # All the varivle and methods will be inherited to the chaild classes

class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

    def __repr__(self):
        return f'{self.fullname()} is {self.prog_lang} Developer'

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if emp in self.employees:
            print('-->',emp.fullname())

    def __repr__(self):
        return f'{self.fullname()} has {len(self.employees)} employees.({self.employees})'



dev1=Developer('dev-prani','k',1000,'Python')
dev2=Developer('dev-gani','k',5000,'Database')
# dev_str='dev_siva-karani-12000-python'
# dev3=Developer(Developer.from_string(dev_str.split('-')))

# print(dev1.__dict__)
# print(Developer.__dict__)
# print(Employee.__dict__)
# print(dev2.no_of_employees)


# print(dev1.fullname())
# print(dev1.prog_lang)
# print(help(dev1))?            Check the order resolution order


mgr1=Manager('karani','padma',10000)
print(mgr1)  # get the more info by implementing the __repr__ method
# print(f'{mgr1.employees})
mgr1.add_emp(dev1)
print(mgr1)

mgr1.add_emp(emp1)
print(mgr1)

mgr2=Manager('karani','venky',3000)
print(mgr2)

mgr2.add_emp(mgr1)
print(mgr2)

print(isinstance(mgr2,Manager))   # to check the instance of the class
