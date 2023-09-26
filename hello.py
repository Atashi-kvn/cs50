
print("Hello, Stranger!")

#In pyhton the input function only deals with strings

name = input("What's your name? ") .strip().title()

#Remove whitespace from str

#  name = name.strip()

#capitalize input (user's 1st name)

#  name = name.capitalize

#capitalize input (user's 1st & other name)

#  name = name.title()

#split user's name into first name & last name

name.split(" ")

#concatenate

print("Welcome, "+ name)

#Using sep = , for a couple of arguments

print("Feel at home,", name)

#overriding "\n" preset for every print function

print('You are going to like it here ', end="")
print(name)

#using the f string

print(f"I can't beleive your name is {name}") 