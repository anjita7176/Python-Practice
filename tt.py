# from h import H
# class Vehicle(H):
#     def star(self):
#         pass
#     def stop(self):
#         pass
# class Car(Vehicle):  
#     def star(self):
#         print("car is started")
#     def stop(self):
#         print("car is stopped")  
# vc=Car()
# vc.star()
# vc.stop()    


# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def star(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def star(self):
#         print("car is started")
#     def stop(self):
#         print("car is stopped")

# cr=Car()
# cr.star()
# cr.stop()   

# def food():
# print("Start point")
# try:
#     a=10
#     b=0
#     c=a/b
# except:
#     print(c) 
#     print("hello")
#     print("End point")   
# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result) 
except ZeroDivisionError:
    print("0 se divide nahi kar sakte")
except ValueError:
    print("Please valid number enter karo")
finally:
    print("Program end ho gaya")  