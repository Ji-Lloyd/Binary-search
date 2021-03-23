# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = a + b

# ch = eval(input("Enter a char: "))
# print(c)
# print(ch)

# ---------------------------------------

# for i in range(1, 20, 1):
# import math as m
# if int(m.sqrt(i)) == float(m.sqrt(i)):
# print(i)
# ---------------------------------------

# num = int(input("Enter a prime number: "))

# for a in range (2,num):
#   if num % a == 0:
#      print("not prime")
#     break
# else:
#   print("prime")
# ------------------------------------------

# a = array('u',(input("Enter number: ")))

# vals = array(a.typecode, (b for b in a))

# for c in vals:
#   print(c)

# vals = array('i', [1,2,3,4,5])

# arr = array(vals.typecode, (a for a in vals))

# for b in arr:
#   print(b)
# ----------------------------------------------------

# arr = array('i', [])

# a = int(input("Enter the length of Array: "))

# for b in range (a):
#   c = int(input("Enter the value: "))
#  arr.append(c)

# print(arr)


# d = int(input("Enter the value of being search: "))
# print(arr.index(d))
# arr2 = arr
# arr[1] = 3
# print(arr2)
# print(id(arr))
# print(id(arr2))
# e = 0

# for f in arr:
# if d == f:
#   print(e)
# break
#  e+=1

# -----------------------------------------------------
# arr = arange(1,10,2)
# arr = logspace()

# arr = array([
#               [1,2,3,4,5,6],
#              [6,7,8,9,10,11],
#             [12,13,14,15,16,17]
#        ])

# arr2 = arr.flatten()
# arr3 = arr2.reshape(2,2,3)

# m1 = matrix("1 2 7 ; 3 4 7 ; 7 5 6")
# m2 = matrix("7 8 7 ; 9 10 7 ; 7 11 12")
# m3 = m1 * m2
# print(m3)
# ----------------------------------------------------
# frst = float(input("Enter first number: "))
# scnd = float(input("Enter second number: "))
# prtn = input("What operation: ")

# def add(x,y):
#   sm = x + y
#  print(sm)

# def sub(x,y):
#   sm = x - y
#  print(sm)

# if prtn == "+":
#   add(frst,scnd)
# elif prtn == "-":
#   sub(frst,scnd)
# elif prtn == "*":
#   res = frst * scnd
#  print(res)

# ----------------------------------------------------------

# def update(x):
#   print(id(x))
#  x = 5
# pass by value of lst
#  lst[1] = 2
# print(id(x))
# print("here ",x)
# pass by reference on id
# y = 10
# lst = [10, 20, 30]
# update(y)
# print(y)
# print(lst)
# print(id(y))

# -----------------------------------------------------------

# frst = input("Enter first name: ")
# lst = input("Enter last name: ")

# def name(first,last):
#   nm = first + " " + last
#  print(nm)

# name(frst,lst)

# frst = float(input("Enter first number: "))
# scnd = float(input("Enter second number: "))

# def sum(frst,*scnd):
#   frst = frst

#  for i in scnd:
#     frst = frst + i
# print(frst)

# def name():
#   print("Hello World")

# sum(frst,scnd)
# name()

# -----------------------------------------------------

# keyworded variable **data
# frst = input("Enter name: ")
# age = int(input("Enter age: "))
# location = input("Enter location: ")
# school = input("Enter school: ")
# print()

# def info(**data):
#   for k,v in data.items():
#     print(k,v)

# info(name= frst , age = age , Location = location, School= school)

# ------------------------------------------------------------------

# a = 10

# def num():
#   a = 3
#  b = globals()['a']
# print(id(b))
# print("function", a)
# globals()['a'] = 0

# num()
# print("global",a)
# print(id(a))

# ------------------------------------------------------------
# for i in range(1, 11, 1):
#   lst = input("Enter names: ")

# def count(c):
#   lst = 0
#  for g in c:
#     if len(g) >= 5:
#        lst += 1
# return lst

# lst = count(lst)
# print(lst)

# lst = []
# n = int(input('enter the size of the list'))
# for i in range(0,n):
#   x = input('enter the next string')
#  lst.append(x)
# print(lst)

# count = 0

# for i in lst:
#   x = len(i)
#  print(x)
# if(x>=5):
#    count +=1
# print('the no of inputs that have length of string more than 5 are :',count)

# --------------------------------------------------------------------------------
# FIBONACCI SEQUENCE
# def seq(x):
#   frst = 0
#   scnd = 1
#   if x <= 0:
#       print("Unacceptable")
#   elif x == 1:
#       print(scnd)
#   else:
#       print(frst)
#       print(scnd)
#       for num in range(2,x):
#           if x // 13:
#               break
#           else:
#               res = frst + scnd
#               frst = scnd
#               scnd = res
#               print(res)
# ui = int(input("Enter the number of sequence: "))
# seq(ui)
# ------------------------------------------------------------------------
# factoring using for loop
# def facto(x):
#   f = 1
#  for i in range(1, x + 1):
#      f = f * i
#  return f #return the value in x. Which means the value of x will be depend on the result

# ui = int(input("Enter factorial number: "))
# print(math.factorial(ui)) # simplest method when using factoring by using math.factorial
# res = facto(ui)
# print(res)
# -------------------------------------------------------------------------------------
# factoring by using recurssion
# def fact(x):
#   if x == 0:
#       return 1

#  return x * fact(x -1)

# ui = int(input("Enter factorial number: "))
# print(fact(ui))
# ------------------------------------------------------------------------------------------
# Lambda
# ui = float(input("Enter squareroot number: "))
# ui2 = float(input("Enter squareroot number: "))
# x = lambda ui : ui + ui2 #ANONYMOUS FUNCTION

# res = x(ui)
# print("The answer is ",res)
# --------------------------------------------------------------------------------------------
# using filter, map, reduce
# lst = []

# ui = int(input("Enter the length of List: ")) #taking how many the value the user will input

# for b in range(ui): #using for loop to repeatedly asking user for input
#    c = int(input("Enter the value: ")) #value from the user
#    lst.append(c) #the given by is being set for the list

# evens = list(filter(lambda x: x % 2 == 0, lst)) #filtering Evens using lambda from the list
# odds = list(filter(lambda x: x % 2 == 1, lst)) #filtering Odds using lambda from the list
# doubles = list(map(lambda x: x * 2, lst)) #double the value of the given list
# plus = reduce(lambda y, z: y + z, lst)  #summing up all the value

# print("This is the list: ", lst)
# print("This is evens: ", evens)
# print("This is odds: ", odds)
# print("This is product: ", doubles)
# print("This is sum: ", plus)
# ----------------------------------------------------------------------------------------------------
# determining even and odd using filter and lambda
# lst = []
# ui = int(input("Enter the length of list: ")) #asking the user for the length of list

# for i in range(ui): # looping the given length by the user until it is met
#    inp = int(input("Enter the value: ")) #asking the user on value for each list
#    lst.append(inp) #storing the value in list by appending

# Odd = tuple(filter(lambda x: x % 2 == 1, lst)) # filtering the values of list by Odd
# Even = tuple(filter(lambda x: x % 2 == 0, lst)) # filtering the values of list by Evens

# print("This is even: ", Even) # printing the Even values given by the user
# print("This is odd: ", Odd) # printing the Odd values given by the user

# ---------------------------------------------------------------------------------
# function within a function

# ui = float(input("Enter number: "))  # asking the user for 1st input
# ui2 = float(input("Enter number: "))  # asking the user for 2nd input


# def div(x, y):  # function for dividing the 2 values
#    print(x / y)


# def div_1(n):
#    def div_2(x, y):  # if the first given number is less than on the 2nd number the value will be swapped
#        if x < y:  # if the 1st given value is less than the 2nd it will swapped the two value
#            x, y = y, x
#        return n(x, y)  # the two value will return as div_1 'n'

#    return div_2  # if the conditions are met it will return the div_2 function


# print("The quotient is: ", end="")  # end="" is for deleting the second line
# res = div_1(div)  # reassigning the 2 function as 'res' variable
# res(ui, ui2)  # using the 'res' variable to compute the two given numbers

# -------------------------------------------------------------------------------------------------------
# This lesson is for importing the module python file to the main python file
# ui_1 = float(input("Enter 1st number: "))  # asking the user for a number value
# ui_2 = float(input("Enter 2nd number: "))  # asking the user for a number value

# ui_3 = input("Enter operator: ")  # asking the user for a operator value

# if ui_3 == "+":  # if the user enter the value '+' this statement will add the two given value
#    res = add(ui_1, ui_2)  # the add() function comes from the import python file which is the mod1.py
#    print(res)
# elif ui_3 == "-":  # if the user enter the value '-' this statement will subtract the two given value
#    res = sub(ui_1, ui_2)  # the sub() function comes from the import python file which is the mod1.py
#    print(res)
# elif ui_3 == "*":  # if the user enter the value '*' this statement will multiply the two given value
#    res = mul(ui_1, ui_2)  # the mul() function comes from the import python file which is the mod1.py
#    print(res)
# elif ui_3 == "/":  # if the user enter the value '/' this statement will divide the two given value
#   res = div(ui_1, ui_2)  # the div() function comes from the import python file which is the mod1.py
#    print(res)

# --------------------------------------------------------------------------------------------------------------
# from mod1 import *


# def mn():  # function for Welcoming the user
#    print("Hello World!")
#    print("Welcome to my system")


# ui = input("Enter 'OK' to proceed: ")  # The user shall type OK to proceed if not the program will quit

# if __name__ == "__main__":  # Only the main python file will show in this condition not the modules
#    if ui != "OK":  # If the user input 'OK' then the program will proceed
#        quit()  # However if not, then the program will terminate itself
#    else:
#        "Welcome"
#    mn()  # After the user type the Correct right word the function will show

#  ---------------------------------------------------------------------------------------------------------
# from mod1 import frst # importing the 'frst' function from the module which mod1.py


# def fun1():
#    print("This is my 1st function, ", end="")
#    frst() # This is the imported function from the module 'frst'


# def fun2():
#    print("This is my 2nd function")


# def main(): # This is the main function that BINDS together all function
#    fun1()
#    fun2()


# main() # Calling the 'main' function

# ----------------------------------------------------------------------------------------------------------
# This is the introduction for 'class' and 'objects'

# class mn:  # This class encompasses all the method = function and objects

#    def con(self):  # Within a 'class' the function will be called as 'method'
#        frst = input("Enter something: ")  # The program will ask the user to input something
#        print(frst)  # Printing the input of user


# x = mn()  # This 'x' variable will take this argument of 'class mn' to use
# The 'x = mn()' can be also called Object Creation

# x.con()  # The 'x' variable will now called the 'con' method by using the argument of 'mn'

# -------------------------------------------------------------------------------------------------------
# class PC:

#    def __init__(self, cpu, ram, storage):  # This __init__ method is use to accepts argument to use for function
#        self.cpu = cpu  # This parameter is use for the cpu variable which will be use to store the data
#        self.ram = ram  # This parameter is use for the ram variable which will be use to store the data
#        self.storage = storage  # This parameter is use for the storage variable which will be use to store the data
# The top part is consider to be the parameters that will be use in the program

#    def build(self):  # This method is use to show the inputs of the user for the questions
#        print("The type of Processor is: ", self.cpu)  # The 'self.cpu' comes from the '__init__' method
#        print("The Gigabyte of RAM is: ", self.ram, "GB")  # Same as the 'self.cpu'
#        print("The space of storage is: ", self.storage, "GB")  # Same as the two
# Example the self.cpu can be replace with other name
# however the part '= cpu' is not because that is the name on the top 'def __init__(cpu,ram,storage)


# ui_1 = input("Enter the type of CPU: ")  # This will ask the user for an input
# ui_2 = input("Enter the GB of RAM: ")  # This will ask the user for an input
# ui_3 = input("Enter the space of storage: ")  # This will ask the user for an input
# print()  # Break line only

# res = PC(ui_1, ui_2, ui_3)  # This is syntax is a constructor
# This variable will act as the class executioner, the three variables are the user inputs

# res.build()  # This code will show the accumulations of the rest

# ---------------------------------------------------------------------------------------------------------------
# class mn:  # This is the class that ties all the method together

#    def __init__(self):  # This method is taking argument to use by other methods
#        self.name = "Lloyd"  # This is the value for the first variable
#        self.age = 19

#    def compare(self, other):  # This method is use to compare the two(2) objects below
#        if res.age == res_2.age:  # If the res.age is equal to value of res_2.age then this condition will be true
#            return True
#        else:  # If the condition is not met then this statement will return as False
#            return False


# res = mn()  # First object to name the 'mn' class
# res_2 = mn()  # Second object to name the 'nm' class

# res.age = int(input("Enter age: "))  # The user will be ask to give a his/her age

# if res.compare(res_2):  # If the method of 'compare' return as true then this statement will print same
#    print("Same")
# else:  # If the method 'compare' return as false then statement will print 'Different'
#    print("Different")

# print("Name:", res.name)  # This will print the 'name' variable of the 'mn()' class
# print("Age:", res.age, "- age should be 19")  # This will print the 'age' that the user gives

# --------------------------------------------------------------------------------------------------------------------
# THIS IS ALL ABOUT THE CLASS VARIABLE AND INSTANCE VARIABLE

# class PC:
#    Case = "Rakk Haliya"  # Those variable that is not within method/functions are class variables

#    def __init__(self):
#        self.Cpu = ui_1  # This is called INSTANCE variables
#        self.Ram = ui_2  # This ui_# comes from the user
#        self.Storage = ui_3  # This will be used to print the value

#    def Build(self):  # This method is used for printing the values that was given by the user
#        print("The brand of the CPU is", ui_1)  # Prints the 1st question that is popup on the user's UI
#        print("The brand of the Ram is", ui_2)  # Prints the 2nd question that is popup on the user's UI
#        print("The brand of the Storage is", ui_3) # Prints the 3rd question that is popup on the user's UI


# user = input("Enter username: ")  # This will ask the user for the specific username
# pas = input("Enter password: ")  # This will ask the user for the specific password

# if user == "Lloyd" and pas == "Agdan":  # If this two was inputted by the user then the program will proceed
#    ui_1 = input("Enter CPU brand: ")  # This will ask the user
#    ui_2 = input("Enter Ram brand: ")  # This will ask the user
#    ui_3 = input("Enter Storage brand: ")  # This will ask the user
#    print()  # Giving a 'enter' space

#    res = PC()  # The 'PC()' class will be assign to 'res' as an OBJECT
#    res.Build()  # The 'res' variable is calling from the class for 'Build()' method to execute
#    print("The case will be", res.Case)  # This syntax is calling the class variable 'Case' from class
#    print()  # Break

#    res_2 = PC()  # The 'PC()' class will be assign to 'res_2' as an object
#    res_2.Case = "The case InPlay"  # This gives the '.Case' a new value
#    res_2.Cpu = "The cpu is intel"  # This gives the '.Cpu' a new value
#    res_2.Ram = "The ram is g.skill"  # This gives the '.Ram' a new value
#    res_2.Storage = "The storage is samsung"  # This gives the '.Storage' a new value

#    print(res_2.Case, res_2.Cpu, res_2.Ram, res_2.Storage)  # This prints all the called variables

# else:  # If the user does not log in the correct username and pass this condition will be executed
#    print("Try Again")  # Prints
#    quit()  # This code will forcefully terminates the program

# ---------------------------------------------------------------------------------------------------------
# This program introduces the different kind of methods classmethod, staticmethod, self

# class grade:  # This class holds all the different methods that needs to run the program

#    def __init__(self, ui_1, ui_2, ui_3):  # this method will store the three instance variable to use by the user
#        self.math = ui_1  # This instance variable is used to hold the math input
#        self.computer = ui_2  # This instance variable is used to hold the computer input
#        self.communication = ui_3  # This instance variable is used to hold the communication input

#    def getting_avg(self):  # This method is used for getting the average that given by the user

#        result = (self.math + self.computer + self.communication) / 3  # This is the computation to see the result

#        if result >= 90:  # If the result of the given outputs is equal or above 90 this condition will be executed
#            print("Excellent")  # Print
#            print("The average is:", result)  # Prints the result of the given
#        elif result >= 80:  # If the result of the given outputs is equal or above 80 this condition will be executed
#            print("Satisfactory")  # Print
#            print("The average is:", result)  # Prints the result of the given
#        elif result >= 75:  # If the result of the given outputs is equal or above 75 this condition will be executed
#            print("Pass")  # Print
#            print("The average is:", result)  # Prints the result of the given
#        else:  # If the output of the user does not reach the conditions above then this will be the last resort
#            print("Failed")
#            print("The average is:", result)  # Prints the result of the given

#    @staticmethod  # If the user does not want either the classmethod or self this can be used
#    def student_name():  # This method holds the student name
#        print("Lloyd")

#    @classmethod  # If there are class variable this '@classmethod' can be used
#    def getSchool(cls):  # The user must replaced the word within the round bracket with the word 'cls' to work
#        print(grade.ui_4)  # This will print the given output for the specific question

#    ui_4 = input("Enter School: ")  # This syntax will ask the user to input their school


# ui_1 = int(input("Enter Math grade: "))  # This will ask the user for the grade
# ui_2 = int(input("Enter Computer grade: "))  # This will ask the user for the grade
# ui_3 = int(input("Enter Communication grade: "))  # This will ask the user for the grade
# print()  # break
# res = grade(ui_1, ui_2, ui_3)  # This is the object that will be used for holding the three inputs

# res.student_name()  # prints the student name
# res.getting_avg()  # print the method getting_avg
# res.getSchool()  # prints the getSchool method

# ------------------------------------------------------------------------------------------------------------------
# This program show the class method that is within a class i.e the 'inner class'
# class buyer:  # This class holds all the methods/functions that is needed by the program to work

#    def __init__(self, own, brand):  # This method will hold the 2 instance variable and 1 inner class
#        self.owner = own  # This instance variable will carry the 'owner' variable for the output
#       self.model = brand  # This instance variable will carry the 'brand'
#       self.inf = self.specs  # This syntax is the introduction of inner class and this is how inner class works

#    def info(self):  # This method is for the primary info that is given by the user
#        print("The owner is:", self.owner)  # Prints the output of the user for the 'owner'
#        print("The model of laptop is:", self.model)  # Prints the output of the user for the 'model'

#    class specs:  # This is called the inner class, the class contains another different type of method

#        def __init__(self, processor, module, capacity):  # This method holds the three instance variables
#            self.cpu = processor  # This hold the processor given by the user
#            self.ram = module  # This hold the ram given by the user
#            self.storage = capacity  # This hold the storage given by the user

#        def laptop(self):  # This method prints the given output by the user
#            print("The type of processor is:", self.cpu)  # prints the type of processor that given by the user
#            print("The type of ram is:", self.ram)  # prints the type of ram that given by the user
#            print("The type of storage is:", self.storage)  # prints the type of storage that given by the user


# customer = input("Enter the name of the buyer: ")  # This variable is for buyers name
# brand = input("Enter the brand of the laptop: ")  # This will ask the user for the brand of the laptop
# cpu = input("Enter the brand of processor: ")  # This will ask the user for the brand of processor
# ram = input("Enter the brand of ram: ")  # This will ask the user for the brand of ram
# store = input("Enter the brand of storage: ")  # This will ask the user for the brand of storage
# print() # break

# invoke = buyer(customer, brand)  # 'invoke' will be the object for the 'buyer' class
# spec_buy = buyer.specs(cpu, ram, store)  # 'spec_buy' will be the object for the 'buyer.spec' innerclass

# invoke.info()  # executes the invoke = buyer.info = method
# spec_buy.laptop()  # executes the spec_buy.laptop innerclass

# --------------------------------------------------------------------------------------------------------------------
# This program represent the inheritance of classes

# class log:  # This is the parent/super class that take gives the primary inheritance

#    def student(self):  # method that contains a value
#        print("Lloyd ", end="")  # 'end=""' is for breaking the line

#    @staticmethod
#    def student_2():  # static method that contains a value
#        print("JayAr ", end="")  # 'end=""' is for breaking the line

#    def student_3(self):  # method that contains a value
#        print("Agdan ", end="")  # 'end=""' is for breaking the line


# class gender(log):  # This is the child/sub class that inherits the 'log' class above

#    def gen_1(self):  # method that contains a value
#        print("Male_1")

#    def gen_2(self):  # method that contains a value
#        print("Male_2")

#    def gen_3(self):  # method that contains a value
#        print("Male_3")


# info = gender()  # assign an object to use instead of calling the name of specific class
# res = info.student(), info.gen_1()  # This object concatenates a two methods
# res_1 = info.student_2(), info.gen_2()  # This object concatenates a two methods
# res_2 = info.student_3(), info.gen_3()  # This object concatenates a two methods
# result = res, res_1, res_2  # This compiles all the objects into a single variable
# result  # Calls the objects to execute

# ---------------------------------------------------------------------------------------------------
# Inheritance of classes
# class variables:

#    def __init__(self, user, key):
#        self.name = user
#        self.password = key


# class info(variables):
#    def inform(self):
#        if self.name == "Lloyd" and self.password == "Agdan":
#            print("Welcome!")
#            print()
#            ui_1 = int(input("Enter 1st number: "))
#            ui_2 = int(input("Enter 2nd number: "))
#            print("The sum is: ", ui_1 + ui_2)
#        else:
#            print("Try again")
#            quit()


# username = input("Enter username: ")
# security = input("Enter key: ")
# print()

# res = info(username, security)
# res.inform()

# --------------------------------------------------------------------------------------------
# This program represents Duck Typing

# class specs: # class that is needed as foundation for duck typing

#    def info(self):  # This method contains the needed value for Duck typing
#        print("AMD Ryzen 3 3100")  # value
#        print("Corsair vengeance")  # value


# class specs_2:  # extra

#    def info_2(self):  # method
#        print("Intel i9")  # value
#        print("G. Skill")  # value


# class laptop:  # class that catching the method of 'specs' class by argument it within the 'name'

#    def brand(self, name):  # method , the argument needed to execute the duck typing
#        name.info()  # executes the 'info' method from 'specs' class a.k.a duck typing


# type = specs()  # object for 'specs()' class , this is also the syntax that responsible for referencing the class
# lap = laptop()  # object for 'laptop' class
# lap.brand(type)  # calling the 'lap' object variable that has 'brand' method, with 'info' method from 'specs' class

# ---------------------------------------------------------------------------------------------------------------------
# This program show the constructor in inheritance also the method resolution order 'MRO'
# class name:

#   def __init__(self):  # constructor of 'name' class
#        print("Lloyd")

#    def surname(self):  # method of 'name' class
#        print("Agdan - name")


# class year:

#    def __init__(self):  # constructor of 'year' class
#        print("1st year")

#    def school_year(self):  # method
#        print("Agdan - year")

# This class show the method resolution order that executes because the parent 'name' class is on the left
# class course(name, year):  # The execution of this class that inherits the parent is in order from left to right

#    def __init__(self):  # constructor of 'course' class
#        super().__init__()  # The constructor of 'name' class will be executed because it is on the left
#        print("BSIT")


# res = course()  # object that receives the 'course' class

# -------------------------------------------------------------------------------------------------------------------
# This program shows the operator overloading, means that the user can modify the predetermine syntax of operators

# class ask:  # class

#    def __init__(self, ui1, ui2):  # method that contains the user inputs
#        self.frst = ui1  # the instance variable is 'frst'
#        self.scnd = ui2  # the instance variable is 'scnd'

#    def __add__(self, other):  # This is the operator overloading, modifying the predefined operator
#        res_1 = self.frst + self.scnd  # This sums the 'self' variables 'i.e' ui_1 and ui_2
#        res_2 = other.frst + other.scnd  # This sums the 'other' variables 'i.e' ui_3 and ui_4
#        fin = res_1 + res_2  # After getting the total of the two, this syntax will combine them
#        print(fin)  # print the overall total

#    def __gt__(self, other):  # This is operator overloading for 'greater than'
#        res_1 = self.frst + self.scnd  # This sums the 'self' variables 'i.e' ui_1 and ui_2
#        res_2 = other.frst + other.scnd  # This sums the 'other' variables 'i.e' ui_3 and ui_4

#        if res_1 > res_2:  # This conditional statement will modify the 'greater than' function that is predetermined
#            return True  # returns true the condition
#        else:
#            return False  # returns false the condition

# ui_1 = int(input("Enter 1st number:"))  # user input
# ui_2 = int(input("Enter 2nd number:"))  # user input
# print()  # break
# ui_3 = int(input("Enter 3rd number:"))  # user input
# ui_4 = int(input("Enter 4th number:"))  # user input

# output_1 = ask(ui_1, ui_2)  # object for 'ask' method that contain the 'ui_1' and 'ui_2' variables
# output_2 = ask(ui_3, ui_4)  # another object for 'ask' method that contain the 'ui_3' and 'ui_4' variables

# if output_1 > output_2:  # This conditional statement will check if the object 'output_1' is greater than 'output_2'
#    print("Output 1 wins")  # if the condition is true, this syntax will print
# else:  # This will execute if the 'if' statement is false
#    print("Output 2 wins")  # prints if the conditional statement is false

# result = output_1 + output_2  # This variable contains the overall total of two objects

# ----------------------------------------------------------------------------------------------------------------------
# This program show the METHOD OVERLOADING
# class plus:  # class

#    def __init__(self, x, y):  # constructor that carries the values
#        self.frst = x  # carries the value of 'ui_1'
#        self.scnd = y  # carries the value of 'ui_2'

#    def sum(self, h1=None, h2=None, h3=None):  # If the one of the arguments is empty the 'sum' method still executed

#        if h1 != None and h2 != None and h3 != None:  # If the three instances had value this statement will execute
#            res = h1 + h2 + h3  # adding the three instance variable
#        elif h1 != None and h2 != None:  # If the only two is given by the user then this condition will execute
#            res = h1 + h2  # adding the two given instance variable
#        else:  # if only one is given by the user this condition will be executed
#            res = h1

#        return res  # this will return the outcome of the conditional statement above

#    def info(self):  # This method is for the user input and will be stored on constructor
#        print("My name is: ", self.frst)  # prints the input of the user
#        print("My age is: ", self.scnd)  # prints the input of the user


# ui_1 = input("Enter name:")  # This syntax will ask the user to enter name
# ui_2 = int(input("Enter age:"))  # This will ask the user to input his/her age

# result = plus(ui_1, ui_2)  # This object will carry the two user input, 'ui_1' and 'ui_2'
# result.info()  # Executes the 'info' method from the object 'result'
# print(result.sum(1,2,3))  # prints the sum given by the user inside the parenthesis

# ------------------------------------------------------------------------------------------------------
# This program shows the METHOD OVERRIDING, this has same method from different class
# class show_1:  # This class is the parent/super class

#    def __init__(self, frst, scnd):  # This constructor will be used for the child/sub class
#       self.one = frst  # Stores the given value by the user
#        self.two = scnd  # Stores the given value by the user

#    def figure_1(self):  # This method has the same syntax for another class and it will proved the method overriding
#        print(self.one)  # Takes the value of 'self.one' instance variable to print
#        print(self.two)  # Takes the value of 'self.two' instance variable to print
#        print("Hello from 'figure_1'")  # prints to prove that the method is from 'show_1' class


# class show_2(show_1):  # This is the child/sub class that executes outside to see whether it is overriding the method
#    def figure_1(self):  # This method will call the super/parent constructor for inheriting the instance variables
#        super().__init__(self.one, self.two)  # This is called constructor inheritance
#        print(self.one)  # Takes the value of 'self.one' instance variable to print
#        print(self.two)  # Takes the value of 'self.two' instance variable to print
#        print("Hello from 'figure_2'")  # prints to prove that the method is from 'show_1' class


# ui_1 = input("Name:")  # This will ask the user for 'name' input
# ui_2 = input("Lastname:")  # This will ask the user for 'Lastname' input
# result = show_2(ui_1, ui_2)  # This is the created object for 'show_2' class and take the two inputs from user
# result.figure_1()  # This is the syntax that shows whether the overriding is happening or not
# There are two same method that can be consider to be called out but if the child class has the same method this will
# override the program and replace the same method from parent class

# ----------------------------------------------------------------------------------------------------------------------
# This program shows the Abstract classes and method
# from abc import ABC, abstractmethod  # This is needed if the programmer want to use abstract classes or method
# An abstract class or method can be also consider as template for child/sub class to use


# class abst(ABC):  # This class is an abstract that  is a method which only has declaration and doesn't have definition

#   @abstractmethod  # This decoration is needed if the programmer wants to use an abstract on method
#    def student_name(self): pass  # This method does not have any value/definition only declaration for sub class
#    @abstractmethod  # This decoration is needed if the programmer wants to use an abstract on method
#    def student_gender(self): pass  # This method does not have any value/definition only declaration for sub class


# class student(abst):  # This sub/child class is the one who will override or gives the value for abstract class

#    def __init__(self, name, sex):  # This constructor will carry the user's input
#        self.frst_nm = name  # This instance variable will hold the 'name'
#        self.gender = sex  # This instance variable will hold the 'gender'

#    def student_name(self):  # This method will override the definition of abstract method from parent/super class
#        print("The name is:", self.frst_nm)  # prints the user input

#    def student_gender(self):  # This method will override the definition of abstract method from parent/super class
#        print("The gender is:", self.gender)  # prints the user input


# ui_1 = input("Enter name:")  # Asking the user for input
# ui_2 = input("Enter gender:")  # Asking the user for input

# show = student(ui_1, ui_2)  # This object will be use as medium for the constructor and use by the methods
# show.student_name()  # calls the 'student_name' to execute
# show.student_gender()  # calls the 'student_gender' to execute

# --------------------------------------------------------------------------------------------------------------------
# This program show the iteration and next overloading, the user can use it on his/her class
# class count:  # This class contain the 'iteration' and 'next' functions

#    def __init__(self, ask):  # This constructor holds the 'starting number' and the 'ending point'
#        self.num = 1  # This is the first number
#        self.num_2 = ask  # This will hold the user's input and the last number

#   def __iter__(self):  # This will modify the iteration function
#        return self

#    def __next__(self):  # This method will check if the input of the user is met or not
#        if self.num <= self.num_2:  # This condition checks if the user's input is met to finish the execution
#            frst = self.num  # instance variable that holds 'self.num'
#            self.num += 1  # This syntax will increment the arguments until it met the user's condition
#            return frst  # After the condition is achieved it will return the value of 'frst'

#        else:  # After the condition is met this 'else' statement will stop the looping of iteration
#            print("STOP")  # prints value
#            raise StopIteration  # This syntax is important to stop the iteration


# ui_1 = int(input("Enter end number:"))  # ask the user for number input
# count = count(ui_1)  # This object will hold the 'count' class

# for x in count:  # loops the 'ui_1' input until the argument 'self.num' is reached the user's input
#    print(x)  # prints the loop

# ----------------------------------------------------------------------------------------------------------
# This program shows the generator function that uses 'yield'
# def gen(x):  # This function contains the loop to iterate the for the square root

#    n = x  # This syntax is for user's input
#    u = 1  # This is the beginning for squaring

#    while u <= n:  # The looping statement will act as square root function for the program
#        res = u * u  # This is the statement that is needed to square root the numbers
#        yield res  # This 'yield' statement is used for generator function
#        u += 1  # Increments the existing number


# ui_1 = int(input("Enter end sequence:"))  # Ask the user for 'end sequence'

# result = gen(ui_1)  # Object that will carry the 'gen' function

# for i in result:  # This 'for loop' will repeat the 'result' object
#    print(i)  # prints the result values

# -----------------------------------------------------------------------------------------
# This program shows the Exception Handling or error handling

# try:  # This 'try' statement is to test the codes/syntax that has error and try to make them easily to find
#    print("Database Open")  # print a value
#    ui_1 = int(input("Enter 1st number:"))  # user input
#    ui_2 = int(input("Enter 2nd number"))  # user input

#    res = ui_1 / ui_2  # dividing the input of the user
#    print("The result is", res)  # prints the result of the divided input

# except ValueError as x:  # This except statement is only for value errors
#    print(x)  # prints the type of error

# except ZeroDivisionError as x:  # The 'except' statement handles the value when user inputs zero/0 in program
#    print("Invalid input by the user", x)  # prints the error

# except Exception as x:  # This is the general or basic syntax when handling an error
#    print(x)  # prints any error on the program

# finally:  # whether the program have error or not this 'finally' statement will execute
#    print("Database Closed")  # prints a value

# -----------------------------------------------------------------------------------------------------------------
# This program shows on how to used the Multithreading and its function on programs
# from time import *  # import the package that has the ability to delayed the execution of codes
# from threading import *  # This packaged is used when calling out the 'Thread' as parent/super class for classes


# class name(Thread):  # This class is a sub/child class for 'Thread' function

#    def run(self):  # This class is a sub/child class for 'Thread' function
#        for i in range(5):  # looping the given output of the user
#            print("Student name:", ui_1)  # prints the output of the user
#            sleep(1)  # delayed the execution of the method


# class age(Thread):  # This class is a sub/child class for 'Thread' function

#    def run(self):  # This class is a sub/child class for 'Thread' function
#        for i in range(5):  # looping the given output of the user
#            print("Age:", ui_2)  # prints the output of the user
#            sleep(1)  # delayed the execution of the method


# ui_1 = input("Enter student name:")  # ask the user for 'string' input
# ui_2 = int(input("Enter age:"))  # ask the user for 'integer' input

# show_1 = name()  # 'show_1' will be the 'object' for 'name()' class
# show_2 = age()  # 'show_2' will be the 'object' for 'age()' class

# show_1.start()  # Executing the object, the '.start()' syntax is used when calling out a 'Thread' class
# sleep(.5)  # 'sleep' is the syntax that comes from 'time' packaged that delays the execution for below statements
# show_2.start()  # Executing the object, the '.start()' syntax is used when calling out a 'Thread' class

# show_1.join()  # This syntax will execute after the show_1 object or 'Thread' classes is finished
# show_2.join()  # This syntax will execute after the show_2 object or 'Thread' classes is finished
# print()  # Break
# print("BYE")  # print

# ----------------------------------------------------------------------------------------------------------------------

# 'w' - write
# 'r' - read
# 'a' - append the input to an existing file
# 'rb' - read binary for pic
# 'wb' - write binary for pic
# show = open('demo', 'r')  # This syntax is to create/modify the existing file in project
# show_2 = open('test', 'w')  # This syntax is to create/modify the existing file in project

# print(show.read())
# print(show.readline(),end="")
# print(show.readline())

# for x in show:
#    show_2.write(x)

# show_pic = open('pic.png', 'rb')
# copy_file = open('copied.png', 'wb')

# for i in show_pic:
#    copy_file.write(i)

# -------------------------------------------------------------------------------------------
# This program shows the 'Linear search' in the values of list and its index number
# pos = -1  # This variable will determine the location in the list


# def search(list, n):  # This function carries two arguments that is needed for list

#    for x in range(len(list)):  # This 'loop' act as the finder for the given value by the user if there is one in list
#        if x == n:  # This condition compares if the input of user has similar value within the list
#            globals()['pos'] = list.index(n)  # 'globals' is used because the variable is outside the function
#            return True  # The syntax above is used for printing the location/ index value that is given by the user

#    return False  # returns 'false' after the conditional statement


# list = [28, 1, 2, 5, 79, 12]  # list of values

# n = int(input("Enter search number:"))  # This variable will ask the user for input

# if search(list, n):  # This conditional statement will hold the two variables as parameters for 'search' function
#    print("Found it!", pos+1)  # This will print if the given value by the user has been found within the list
# else:
#    print("Lost :(")  # Prints only if there are no similar value that is given by the user

# ----------------------------------------------------------------------------------------------------------------------
# This program shows the Binary Search when the user is finding the value and index number in the list
# loc = -1  # This variable is to locate the index number of the given value by the user within the list


# def search(list, n):  # This function act as the searching method if the user's input is within the given list

#    l = 0  # This variable signified as the 'lower bound'
#    u = len(list) - 1  # This variable assigned for the length of 'list'

#    while l <= u:  # If the lower bound is less than the upper bound or the length of the list, this loop will execute
#        mid = (l + u) // 2  # This is the formula when doing the binary search!!

#        if list[mid] == n:  # If the result of 'mid' variable is equals to the output of the user, this will execute
#            globals()['loc'] = mid  # The 'globals()' will get the specific variable from the outside
#            return True  # Returns true if this condition is met
#        else:
#            if list[mid] < n:  # If the 'mid' variable is less than the output of the user this condition will execute
#                l = mid + 1  # The 'l' variable or lower  bound will append if the 'mid' is less the 'n'
#            else:
#                u = mid - 1  # If 'mid' is greater the 'n' or user's input then the 'mid' value will decrease

#    return False  # returns false


# list = [41, 21, 54, 6, 8, 31, 13]  # predetermined unorganised list

# print("Original list:", list)  # prints the predetermined unorganised list
# list.sort()  # This will sort the list from least to greatest value
# print("Sorted list:", list)  # prints the predetermined 'sorted list'

# n = int(input("Enter number:"))  # This variable will ask the user for input, that may be on the given list

# if search(list, n):  # This condition is for the 'search' function that will find the user's input in the list
#    print('found at index number:', loc + 1)  # prints the location or index value of the given value by the user
# else:
#    print("lost")  # If the list does not have the user's output value this will be executed

# ----------------------------------------------------------------------------------------------------------------------
# This program shows how to sort a 'list' using a 'bubble sort' method

# def sort(num):  # This function is to sort the list using 'Bubble sort'

#    for x in range(len(num)-1,0,-1):  # This will loop the length of the 'list'
#        for i in range(x):  # Loops the 'x' variable that is assign for 'num' list
#            if num[i] > num[i+1]:  # This condition will execute if the 'list' within this loop is greater than itself
#                temp = num[i]  # This will swap the variable name of 'num[i]' to become 'temp'
#                num[i] = num[i+1]  # This will swap the variable name of 'num[i+1]' to become the 'num[i]'
#                num[i+1] = temp  # Last is for swapping the variable name of 'temp' to become 'num[i+1]'

# num = [41, 2, 3, 65, 12]  # This is predetermined list
# sort(num)  # The 'sort()' is the function from above

# print(num)  # prints 'num' list

# ---------------------------------------------------------------------------------------------------------------------
# This shows the efficient way to sort out the unorganised list using the 'selection sort' method

# def search(list):  # This function is used for sorting the given list

#    for i in range (5):  # This statement will loop the list until it was sort out
#        pos = i  # assigning the 'i' loop in 'pos' variable
#        for x in range (i,6):  # This will loop the list to see whether it was sorted out
#            if list[x] < list[pos]:  # This condition will check if the list of present is less than on the original
# list
#                pos = x  # re assigning the 'pos' variable for 'x' loop variable
# Example. temp = '' list[i] = 2, list[pos] = 3
#        temp = list[i]  # temp will take the value of 'list[i]' which is 2
#        list[i] = list[pos]  # 'list[i]' will take the value of 'list[pos]' which is 3
#        list[pos] = temp  # Last 'list[pos]' will take the value of 'temp' which 2
# Final value of the variables
# list[i] = 3
# list[pos] = 2
# THIS IS ALSO CALLED SWAPPING METHOD
#        list[i], list[pos] = list[pos], list[i]  # This method can also be used in 'swapping methods'/'sorting method'
#    print(list)  # prints the result of the sorted list

# list = [5,1,2,6,8,9]  # unsorted predetermined list
# search(list)  # This will call out the 'search' function for list

# print(list)  # prints the present list


# ---------------------------------------------------------------------------------------------------------------------
#import mysql.connector

#mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE testdatabase")


