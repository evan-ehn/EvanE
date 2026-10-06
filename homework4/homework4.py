# List Operations

fav_food = ["miso soup", "soba", "mapo tofu", "fried Rice", "ramen"]
print(fav_food[1])
print(fav_food[-1])
fav_food.append("sukiyaki")
print(fav_food)
fav_food.insert(0, "apple")
print(fav_food)
fav_food.remove("mapo tofu")
print(fav_food)
print(len(fav_food))
for i in fav_food:
    i = i.upper()
    print(i)

fav_food1 = fav_food[0::4]
print(fav_food1)

if fav_food.count("potato") > 0:
    print("A potato!")
else:
    print("No potato!")

# slicing and striding
numbers = list(range(0, 21))
def get_first_15(numbers):
    return numbers[0:15:]
def get_every_5th(lst):
    return lst[::5]
def reverse_and_stride(lst):
    return lst[::-1]
first_15 = get_first_15(numbers)
every_5th = get_every_5th(first_15)
final_result = reverse_and_stride(every_5th)
print(final_result)

# Nested lists
numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
print(numbers)
def sum(total):
    result = 0
    for i in total:
        for num in i:
            result += num
    return(result)
print(sum(numbers))

# create a 5x5 list

def five_x_five():
    number = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        number.append(row)
    return(number)
fivebyfive = five_x_five()
print(fivebyfive)

def multiple_of_3(fivebyfive):
    new_fivebyfive = []
    for i in fivebyfive:
        new_row = []
        for num in i:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_fivebyfive.append(new_row)
    return(new_fivebyfive)
print(multiple_of_3(fivebyfive))

new_fivebyfive = multiple_of_3(fivebyfive)
def total(new_fivebyfive):
    result = 0
    for i in new_fivebyfive:
        for num in i:
            if num != "?":
                result += num
            else:
                result += 0
    return(result)
print(total(new_fivebyfive))

# Dictionaries

# dictionary operations

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")
for key, value in ages.items():
    print(f"{key}: {value}")

