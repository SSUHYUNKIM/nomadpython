#1.0
# a_string = "like this"
# a_number = 3
# a_float = 3.12
# a_boolean = False


#1.1
#days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
#print(days[3])
#days.append("Sat")
#print(days)

#1.2
# #nico = {
#   "name": "Nico",
#   "age": 29,
#   "korean": True,
#   "fav_food" :["Kimchi", "Bulgogi"]
# }

# print(nico)
# nico["handsome"] = True
# print(nico)

#1.3
# age = "18"
# print(age)
# print(type(age))
# n_age = int(age)
# print(n_age)
# print(type(n_age))

#1.4
# def say_hello():
#   print("bye")
#   print("hello")

# say_hello()

#1.5
# def say_hello(who):
#   print("hello", who)

# say_hello("Nico")

# def plus(a, b):
#   print(a + b)

# def minus(a, b):
#   print(a - b)

# plus(2, 5)
# minus(2, 5)

#1.6
# def plus(a, b):
#   return a + b

# result = plus(2, 4)
# print(result)

#1.7
# def say_hello(name, age):
#   return f"Hello {name} you are {age} years old"

# hello = say_hello(age="12", name="nico")
# print(hello)

#1.8
# a = int(input())
# b = int(input())
# def calculator(a, b):
#   return a+b, a-b, a*b, a/b, -a, a**b, a%b

# print(calculator(a,b))

#1.9
# def plus(a,b):
#   if type(b) is int or type(b) is float:
#     return a + b
#   else:
#     return None

# print(plus(12, 1.2))

#1.10
# def age_check(age):
#   print(f"you are {age}")
#   if age < 18:
#     print("you cant drink")
#   elif age ==18 or age == 19:
#     print("you are new to this!")
#   elif age > 20 and age < 25:
#     print("you are still king of young")
#   else:
#     print("enjoy tour drink")

# age_check(19)

#1.11
# days =("Mon", "Tue", "Wed", "Thu", "Fri")

# for day in days:
#   if day is "Wed":
#     break
#   else:
#     print(day)

#1.12
# from calculator import plus, minus

# print(plus(1,2), minus(1,2))

#2.2
import requests

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

print(indeed_result)
