""" python crash course notes (Oxford Brookes): """

"""Basic Infomration:"""

# commenting (single line)

""" commenting (multiple lines)"""

# printing to the terminal:

print("Python Crash Course")

# Variables / Simple Data Types:

string_example = "first_name"

# Variables Showcased (pg.16)

message = "Hello Python World!"
print(message)

# if a variable is assigned in one place and then later within the same code it is assigned a value.

# the latest version assigned will be the final assigned value

# example:

message = "MoneyManMikey"
print(message)

# Chapter 2 Activities:

# 2.1: assign a message to a variable, and then print that message

message = "hello world"
print(message)

# 2.2: assign a message to a variable, and print that message then cvhange the value of the variable to a new message and print the new message

message = "goodbye world"

# Data Types:

# strings: series of characters, anything inside quotes

string = "this is a string"

# changing case in a string with methods:

name = "ada lovelace"
print(name.title())

# output: Ada Lovelace

print(name.upper())

# output: ADA LOVELACE

print(name.lower())

# output ada lovelace

# using variables in strings:

# its good to break down the information you are looking to present

# the 'f' characcter is used to indicate when a variable is being printed in a sentance

first_name = "ada"
second_name = "lovelace"
full_name = f"{first_name} {second_name}"
print(f"Hello, {full_name.title()}!")

# adding whitespace to strings with tabs or newlines:

# normal print ccall

print("Python")

# print with a tab. before it (indicated by the '\t')

print("\tPython")

# printing on a new line

print("Langugages:\nPython\nC++\nPowershell")



# stripping whitespace:

# whitespace is very important when comparing two values

# eg: 'hello' vs 'hello ' // in most instances you will be comparing two variable values

# eg: an email, password, username

username = "MoneyManMikey "
print(f"\n{username}".lower())

# will print: 'moneymanmikey '

username.rstrip()

# will print: 'moneymanmikey'

# changing the variable

current_username = 'moneymanmikey '
current_username = current_username.rstrip()
current_username

# strip():

username = ' moneymanmikey '
username.rstrip()
username.lstrip()
username.strip()



# avoiding syntax errors with strings (apostrophies)

message = "That is michael's"

# notice a key piece of information here the apostrophies are not the same at all. if you wish to use double quotations you use then demark the string with a single quotation

print(message)
message = 'I think she said "I hate you"'
print(message)

# Questions: PG.25

# Use a variable to represent a person's name and print a simple message.

name = "Eric"
message = f"Hello {name}, would you like to learn some Python this week?"
print(message)

# Print a person's name in uppercase, lowercase, and title case.

name = "MiChAeL"
print(name.upper())
print(name.lower())
print(name.title())

# Print a quote and its author's name.

quote = '"You have to love it more than it loves you"'
print(f"\nJean Dawson once said, {quote}")

# Use a variable to represent the author's name.

famous_person = "Jean Dawson"
print(f"\n{famous_person} once said, {quote}")

# Include tabs and newlines at the beginning and end of a name.

persons_name = "\t\nMichael Jones\n\t"

# Print the original name, then remove whitespace from each side.

print(persons_name)
print(persons_name.lstrip())
print(persons_name.rstrip())
print(persons_name.strip())




# Numbers:
# numbers are a frequently used data type and there are different type of numbers which must be treated differently 

# Integers (essentially whole numbers)
# they can make use of all basic operators

sum = 2 + 3 
print(sum)
# 5

sum = 3 - 2
print(sum)
# 1

sum = 2 * 3
print(sum)
# 6 


sum = 6 / 2
print(sum)
# 3


# if you are wanting to use exponenets you can make use of double multiplication/ellipsis
sum = 3 ** 2
print(sum) 
# 9


# python directly supports the order of operations too, so you can use multiple operations in one expression. additionally you can make use of parentheses to modify the order of operations so Python can evaluate your ecpression in the order you specifc
# eg:
sum = 2 + 3*4
print(sum)
# 14
sum = (2 + 3) * 4
print(sum)
# 20


# Floats:

# any number containing a decimal point is considered a float value
# for the majority of scenarios: you can use decimals freely (simply enter the numbers and they should act accordingly)

# eg:
sum = 0.1 + 0.1
print(sum)
# 0.2


# but its often you will recieve an arbitrary number of deicimal places
sum = 0.2 + 0.1 
print(sum)
# eg: 0.30000000000000004

# this is due to python trying to represent the value as accurately as possible



# Integars & Floats
# when dividing numbers of any kind you will get a float value back
# eg:
sum = 4/2
print (sum)
# 2.0

# when mixing an integar and a float in any operation you will get a float... python defaults toa. float, even if the output is a whole number.


# Underscores In Numbers:
# when writing long numbers you can use _ to group / make your digits more readible
# eg:
universe_age = 14_000_000_000
print(universe_age)
# will output 14000000000



# Multiple Assignment:
# you can assign multiple values to multiple correlating variables:
x, y, z = 0, 0, 0 
# xyz values are all 0


# Constants:
# a constant is a variable which its value doenst change throughout the program and is required to stay consistent
# it is best practice to always make use of all capital letters when naming constants
# eg:
MAX_CONNECTIONS = 5000



# Questions: PG.29
# write addtiion, subtraction, multiplcation, and dividsion lperations that each result in the number 8 (enclose all operations in print())
print(5+3)
print(10-2)
print(16/2)
print(4*2)




# Introduction To Lists: PG.33
# a list is a collection of values (in a specific order) which do not have to be related in anyway.. its good practice to 
# lists are indicated in python via the [] characters, values are seperated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# lists do not have to hold strings, they can hold all forms of data types

# if you ask python to print the list as a whole it will print the full [,,,] layout of the list in its entirety
print(bicycles)


# Acessing Elements In A List:

# to access specific elements in a list we make use of indexes which start at zero 0 ie the first items index is alwasy 0
# therefor when accessing items at the badck of the list we make use of a negative index (-1)
print(bicycles[0])
# would output 'trek'

# functions can also be called when accessing elements on from a list
# EG:
print(bicycles[0].title())

# Accessing elements using their position relative to the end of the list:
print(bicycles[-1])


# Using Individual Values From A List:
# to do we use a similiar format as accessing an individual item from a list it just depends on the method in which we are displaying / processing said item within our program
# EG:
message = f"\nMy first bicycle was a {bicycles[0].title()}"
print(message)



# Questions: (PG. 36)
# store the names of a few of your friends in a list called names. print each persons name by accessing each element in the list
friends = ['luke freitag', 'jordan zwart', 'quincy mabs', 'james weekes']

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

# start with the list you used in the first question. instead of just printing each person's name print a message to each of them
# they should all have the same text / personalized with the persons name

print(f"\nHi {friends[0].title()}!")
print(f"\nHi {friends[1].title()}!")
print(f"\nHi {friends[2].title()}!")
print(f"\nHi {friends[3].title()}!")

# make a list which stores several examples of your favourite mode of transport.. use your list to print a series of statements about these items, such as "i would like to own a honda motorcycle"

cars = ['ferrari', 'lambo', 'audi', 'bmw', 'bugati']

# i would like to own a honda motorcycle

print(f"\nI would like to own a {cars[0]} car")
print(f"\nI would like to own a {cars[1]} car")
print(f"\nI would like to own a {cars[2]} car")
print(f"\nI would like to own a {cars[3]} car")
print(f"\nI would like to own a {cars[4]} car")



# Changing, Adding, and Removing Elements:
# Modifying Elements Directly

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# this would output both the original list and then the augmented list which contains
# ducati where honda is, any item can be changed as long as the index is specified


# Adding Elements To A List:

# the easiest way to do so is to make use of the .append() function
# when making use of the .append() function items will get added ot the end of the list

motorcycles.append('ducati')
print(motorcycles)

# this allows us to easily build lists dynamically
# EG:

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)


# Inserting Elements Into A List
# you can add a new element at any position in your list by using the insert() method
# both index and value need to specified 

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing Elements From A List:
# in python, you are able to remove an item or a set of items from a list

# Using The del Statement To Remove An Item:
motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

# using del you need to know / specify the index of the item you wish to remove 
# this removes the item and moves all items left in terms of index
# you will no longer be able to access the removed item


# Removing An Item Using The pop() Method:

# this allows you to store / work with the value of the removed item freely / easily
# pop() - removes the last item from a list but lets you work with that item after removing it

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# when popping a list its essentially that that value is saved to a variable in order to be able to be worked with
# example of how this could be useful:
print(f"The last motorcycle I owned was a {popped_motorcycles}")


# Popping Items From Any Position In A List
# to do so the index of the specifc item just needs to be specified
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned_vehicle = motorcycles.pop(0) # 0 being the first item in the list (index)
print(f"The first motorcycle I owned was a {first_owned_vehicle}")

# once an item is popped you can no longer access it from the list itself only the variable associated with the popped item
# whenever you are wanting to remove a set item and use it , make use of pop()


# Removing An Item By Value:

# often you wont know the position of the item you are wishing to remove from a list.
# here is where we make use of the remove() method

motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# important: the remove() method deletes only the first occurence of the value you specify
# if there are several occurances make use of a loop to remove all instances


# Questions: PG.42
# if you could invite anyone to dinner who would you invite. make a list of those people
# then make a custom message inviting each of them
guest_list = ['michael jackson', 'jean dawson', 'chow lee', 'bianca censori']
print(f"\nWelcome {guest_list[0].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[1].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[2].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[3].title()}! You have been invited to join us for dinner!")



# you just heard that one of your guests cant make dinner so you send new invitations
# add a print() call at the end of the program stating the person who cant come)
# modify your list replacing the name of the guest who cant make it with a new one you are inviting
cannot_make_it = guest_list.pop()
new_guest = 'kim kardashian'
print(f"\nUnfortunately {cannot_make_it.title()} is unable to attend dinner.{new_guest.title()} will be attending in their place.")
guest_list.append(new_guest)

# print the second set of invitation messages, one for each person who is still in your list
print(f"\nWelcome {guest_list[0].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[1].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[2].title()}! You have been invited to join us for dinner!")
print(f"\nWelcome {guest_list[3].title()}! You have been invited to join us for dinner!")


# you just found out that your new dinner table wont arrive in time for the dinner, and you have space for only two guests
# add a new line that prints a message saying that you can invite only two people for dinner
# use pop() to remove guests from your list one at a time until only two names remain in your list
# each time you pop a name from your list print a message letting them know you cant invite them
# print a message to each of the two people still on the list letting them know they they're still invited
# use del to remove the last two names from your list, so you just have an empty list, print your list to make sure you actually have an empty list at the end of your program
print("\nI can actually only invite 2 guests to dinner!")
guest_list.pop()
guest_list.pop()

print(f"You guys are still invited! {guest_list[0]}, {guest_list[1]}")

del guest_list[0]
del guest_list[0]

print(guest_list)