# Print Functions

def say_goodbye(name):
    # prints the given goodbye and then the given name
    return("Goodbye", name)

print(say_goodbye("Evan"))

def area_circle (radius):
    # prints the area of a circle with a given radius
    return(3.14*(radius**2))

print(area_circle(9))

# Return Functions

def subtract(a, b):
    # Prints the output of the first given number subtracted by the second given number
    return(a - b)

print(subtract(15, 4))

def multiply(c, d):
    # Prints the output of the first given number multiplied by the second number
    return(c * d)

print(multiply(5, 7))

def divide(e, f):
    # Prints the output of the first given number divided by the second given number
    return(e / f)

print(divide(84, 7))

# Conditionals
readings = [15, 14, 17, 20, 23, 28, 20]
def what_to_wear():
    # Determines the highest and lowest given temperatures
    return max(readings), min(readings)

print(what_to_wear())

monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7
def day_of_the_week (day):
    # determines whether the day is a weekend or not based on a given number reoresenting a day
    if day == 6 or day == 7:
        return("It's the weekend!")
    else:
        return("It's not the weekend")

print(day_of_the_week(4))

def fuel_efficiency (distance, fuel):
    # determines how efficient the drive will be based on it's distance and gallons of fuel
    return("the fuel efficiency is :", distance / fuel, "miles per gallon")

print(fuel_efficiency(63, 22))


def code (data):
    # replaces the first digit of a number with the last digit and moves all other digits back a decimal space
    last_number = data%10
    remainding_numbers = data//10
    return (remainding_numbers + last_number*(10**(len(str(remainding_numbers)))))

print(code(2549601))

# Loops

def power (x, y):
    #  find x raised to the power of y by using a for loop
    result = 1
    for i in range (y):
        result *= x
    return (result)

print(power(2, 3))


for_list_max = [43, 2, 6, 71, 16, 39, 659, 74]
def extremes_of_numbers1(data_list):
    # Finds the max number for the given list of numbers
    max = data_list[0]
    for i in data_list:
        if i > max:
            max = i
    return(max)
print(extremes_of_numbers1(for_list_max))

for_list_min = [43, 2, 6, 71, 16, 39, 659, 74]
def extremes_of_numbers2(data_list):
    # Finds the min number for the given list of numbers
    min = data_list[0]
    for i in data_list:
        if i < min:
            min = i
    return(min)
print(extremes_of_numbers2(for_list_min))

while_list_max = [43, 2, 6, 71, 16, 39, 659, 74]
def extremes_of_numbers3(data_list):
    # Find the max number filtering smaller numbers through an if function through a while loop
    max = data_list[0]
    i = 0
    while i < len(data_list):
        if data_list[i] > max:
            max = data_list[i]

        i += 1
    return(max)
print(extremes_of_numbers3(while_list_max))

while_list_min = [43, 2, 6, 71, 16, 39, 659, 74]
def extremes_of_numbers4(data_list):
    # Find the min number filtering larger numbers through an if function through a while loop
    min = data_list[0]
    i = 0
    while i < len(data_list):
        if data_list[i] < min:
            min = data_list[i]

        i += 1
    return(min)
print(extremes_of_numbers4(while_list_min))

def sum(numbers):
    # Finds the sum of the indiviual numbers within a larger number by by turning the number into a string to find the numbers' placs and then turning it back into an integer to find the sum
    result = 0
    for i in str(numbers):
        result += int(i)
    return(result)
print(sum(3418))
