# from h import h


# print("hello")
# n=100
# print(n)
# print(type(n))
# a="rahul"
# print(a)
# print(type(a))
# m=14.28
# print(m)
# print(type(m))
# b=True
# print(b)
# print(type(b))
# a=20
# b=30
# c=145
# d=a+b+c
# print(d)
# print(type(d))
# z=[1,2,3,4,12,14,25,27,28,29]
# print(z)
# print(type(z))
# print(z[0])
# print(z[1])
# print(h)
# l=eval(input("enter a number"))
# print(l)
#age=int(input("enter your age"))
#if age>=18:
    #print("you are eligible for voting")
#else:
    #print("you are not eligible for voting")
# marks=int(input("enter your marks"))
# if marks>=80 and  marks<=100:
#     print("you got A grade")
# elif marks>=60 and marks<80:
#     print("you got B grade")
# elif marks>=40 and marks<60:
#     print("you got C grade")
# elif marks>=0 and marks<40:
#     print("you got D grade")
# else:    print("fail")
# O=int(input("enter a O"))
# for O in range(1,11):
#     print(O)   
# P=int(input("enter a P"))
# for P in range(1,11):
#     print(P)
#     P=P+1
# I=2
# while I<=20:
#     print(I)
#     I=I+2    
# U=int(input("enter a U"))
# for U in range(2,41,2):
#     print(U)    
# def cool():
#     print("this is a function")
#     a=10
#     b=20
#     c=a+b
#     print(c)
#     for i in range(1,11):
#         print(i)
# cool()        
# def eat(a,b,c):
#     print("this is a function")
#     d=a+b+c
#     print(d)
# eat(10,20,30)
# def show(name,age):
#     return f"my name is {name} and my age is {age}"
# print(show("rahul",25))
# print
# (show("sachin",30))
# n=int(input("enter a number"))
# if n>0:
#     print("positive number")
# if n<0:
#     print("negative number")
# if n==0:
#     print("zero")
# a1=int(input("enter a first subject number")) 
# a2=int(input("enter a second subject number"))
# a3=int(input("enter a third subject number"))
# percentage=(a1+a2+a3)*100/150
# if percentage>=40:
#     print("pass")
# else:
#     print("fail") 
# run=int(input("enter a number of runs")) 
# if run>=100:
#     print("century")
# elif run>=200:
#     print("double century")
# elif run>=300:
#     print("triple century")  
# elif run>=70:  
# #     print("half century")     
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# z=int(input("enter a number"))
# if x>y:
#     if x>z:
#         print("x is greatest")
#     else:
#         print("z is greatest")        
# k=2+3j
# print(k)
# # print(type(k))
# l=2+3j
# print(l)
# # print(type(l))
# ch=input("enter a alphabet")
# if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
#     print("vowel")
# else:    print("consonant")    
# a=12
# while a<=20:
#     print(a)
#     a=a+2
# print("loop is ended")    
# jk=input("enter a name")
# s=1
# while s<=10:
#     print(jk)
#     s=s+1
# text="programming"
# print(text[1:5])
# print(text[2:6])
# print(text[3:7])
# print(text[4:8])
# print(text[0:4])
# print(text[1:5])
# print(text[2:6])
# print(text[3:7])
# print(text[4:8])
# print(text[0:4])
# class xyz:
#     def __init__(self, n, m):
#         print(n)
#         print(m)
#         print(n+m)
# ss=xyz(10,20)
# class abc:
#     def __init__(self):
#         print("hello")
#         print("this is a class")
# ss=abc()        
# class show:
#     def food(self):
#         print("this is a function")
#         print("this is a class")
# class eat(show):
#     def drink(self):
#         print("this is a function")
#         print("this is a class")        
# se=eat()
# se.drink() 
# # se.food()           
# class xyz:
#     def fire(self):
#         print("Hi this is a function")
#     def fire(self,a,b):
#         print(a)
#         print(b)
#         print(a+b)
# fc=xyz()
# # fc.fire
# fc.fire(30,20)
# class zoo:
#     def __init__(self):
#         print("Hi this is a function")
        
# class zooo(zoo):        
#     def __init__(self,a,b):
#         super().__init__()
#         print(a)
#         print(b)
# yzz=zooo(10,20)
# class cow:
#     def add(self,a,b,c=0):
#         print(a)
#         print(b)
#         print(c)
#         print(a+b+c)
# Aa=cow()
# Aa.add(10,20)
# Aa.add(10,20,30)
# # Aa.add(10,20,50)
# class anime:
#     def __init__(self):
#         self.age=""
#     def setage(self,b):
#         self.age=b
#     def getage(self):
#         return self.age
# ae=anime()
# ae.setage(25)
# print(ae.getage())    
from h import H
class Vehicle(H):
    def star(self):
        pass
    def stop(self):
        pass
class Car(Vehicle):  
    def star(self):
        print("car is started")
    def stop(self):
        print("car is stopped")
vh=Vehicle()
vh.star()    
vh.stop()    
vc=Car()
vc.star()
vc.stop()                  