#numbers = [1, 2, 3, 4]
#print(numbers)

#mixed = ["hello", 5, True, None]
#print(mixed)

#print(mixed[-1])

#numbers[1] = "apple"
#numbers.append(6)
#print(numbers)

#print(mixed.insert(1, False))
#print(mixed)

#numbers.remove(3)
#print(numbers)

#numbers.pop()
#print(numbers)

#for num in numbers:
 #   print(num)

#nums = [1, 2, 3, 4, 5]
#sub_num = nums[1:4]
#print(sub_num)

#list = [12, 14, 16, 18, 22]
#print(list[::2])

#print(list[1:4:2])

#nums = [10, 20, 30, 40, 50, 60]
#print
bugs = {"ants": ["black", "fire"],
        "spiders": ["black widow", "tarantula"],
        "flys": ["horse", "house"]
        }
bugs["bees"] = ["honey", "queen"]# adds an item
bugs.values()# the things in a key
bugs.items() # everything
bugs.keys() # the titles of teh categories
# .del, .clear(), .update(), .setdefault(), .exists()
#for key in bugs.keys():
    #print(key)

#list1 = list(range(0,11))
#list2 = list1[0:5]
#print(list2)
#list3 = list1[0:11:2]
#print(list3)
#list4 = list1[::-1]
#print(list4)

#nested_list = [[2, 4, 6],
               #[8, 10, 12],
               #[14, 16, 18]
               #]
#print(nested_list[2][1])

stars_data = {
    "name":["Sirius", "Vega", "Altair"],
    "magnitude":[-1.46, 0.03, 0.77],
    "distance_ly":[8.6, 25.0, 16.7],
    "constellation":["Canis Major", "Lyra", "Aquila"]
}
for name in stars_data.keys():
    for "name" in stars_data.values():
        print(name)