my_name = input("plz enter ur full name")
my_age = input("how old r u?")

print(f"my name is {my_name} and i am {my_age} yrs old ")

first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
operation = input("enter operation type: ")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
  print(first_number / second_number)
else:
  print("the operation isn't valid")

bus_capacity = 50
inside_bus = int(input("people inside: "))
want_bus = int(input("people want in: "))
empty_seats = bus_capacity - inside_bus
if empty_seats>= want_bus:
    print("there is space inside")
else:
   print("the bus is full")
   



