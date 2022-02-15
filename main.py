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
a = int(input())
b = int(input())
def calculator(a, b):
  return a+b, a-b, a*b, a/b, -a, a**b, a%b

print(calculator(a,b))