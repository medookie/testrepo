# A program which doesn't get a user's input is a deaf program.
# the result of the input() function is a string

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
print("----------------------------------------------------------------------")

anything = input("Tell me anything...") # displays a message to console before input received
print("Hmm...", anything, "...Really?")
print("----------------------------------------------------------------------")

# Testing TypeError message.

# anything = input("Enter a number: ")
# something = anything ** 2.0 # causes an errer here because input can only be a string and cannot be used with math operators
# print(anything, "to the power of 2 is", something)
# ----------------------------------------------------------------------------

anything = float(input("Enter a number: ")) # input function within float function forces (type casting) string input into float value if possible
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
print("----------------------------------------------------------------------")

# another example of type casting input

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# results are same as above, but assigns calculation to hypo variable
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# type casting to a string
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
print("----------------------------------------------------------------------")

# Concatenation (+) - both arguments must be strings

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".") # concatenation of strings

# Replication operator (*)

print("+" + 10 * "-" + "+") # takes string value and repeats it the number of times specified in the number
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
print("----------------------------------------------------------------------")

# Lab 2.6.1.9 - simple input and output

var_a = float(input("Input a value: ")) # input a float value for variable a here
var_b = float(input("Input a second value: ")) # input a float value for variable b here

print(var_a + var_b) # output the result of addition here
print(var_a - var_b) # output the result of subtraction here
print(var_a * var_b) # output the result of multiplication here
print(var_a / var_b) # output the result of division here

print("\nThat's all, folks!")
print("----------------------------------------------------------------------")

# Lab 2.6.1.10 - operators and expressions

# Your task is to complete the code in order to evaluate the following expression:
# 1 / (x + (1 / (x + (1 / (x + 1/x)))))

x = float(input("Enter value for x: "))

y = 1/(x + (1 / (x + (1 / (x + (1 / x))))))

print("y =", y)

# Lab 2.6.1.11 - operators and expressions

# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of 
# minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). 
# The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
# Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important 
# thing is that the code produce valid results for valid input data.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = (hour * 60) + mins + dura

hour = total_mins // 60
mins = total_mins % 60

hour = hour % 24

print(hour, ":", mins, sep='')

# Key Takeaways

#