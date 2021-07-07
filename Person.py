import random

class Person:
   # private variables
   __name: str
   __age: int
   __likes: list

   # constructor
   def __init__(self, name: str, age: int, likes: list):
      self.__name = name
      self.__age = age
      self.__likes = likes

   # functions
   def greet(self):
      print("Hi, I am " + self.__name + "!")
      print("I am " + str(self.__age) + " years old.")

   def doSomething(self):
      rand_num = random.randint(0, len(self.__likes) - 1)
      print("I will do " + str(self.__likes[rand_num]))

