# File: homework1.py

# --- Variables and Data Types ---
a = 10
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawberry"}
g = (1, 2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

print(type(a)) # a is an integer which is a whole number with no decimals or fracations
print(type(b)) # b is a float which is number that can contain a decimal or fraction
print(type(c)) # c is a complex value which treats j as an imaginary number
print(type(d)) # d is a string which just treats it as letters
print(type(e)) # e is a list which is just an ordered collection of values
print(type(f)) # f is a dict which stores items into a variable which is indicated by the first value
print(type(g)) # g is a tuple which is an immutable, ordered collection that can store elements of different data types.
print(type(h)) # h is a list which is just an ordered collection of values
print(type(i)) # is a bool which deterimines if something is true
print(type(j)) # j doesn't have a data type
print(type(k)) # j is a list which is just an ordered collection of values
print(type(l)) # l is a string string which just treats it as letters
print(type(m)) # m is a float which is number that can contain a decimal or fraction

"""
1. How many different data types did you find?
I found 9 different data types

2. List all the data types you found.
int, float, complex, str, list, dict, tuple, bool, nonetype

3. What variables have the same data types?
b and m have the same type, d and l have the same type, k, h, and e have the same type

4. What was the data type of l? Why is it not an integer? What does str() do?
The data dype of l was a string. It isn't an integer because it is enclosed in parenthesss
with str in front of it. str() makes it so anything in it's parentheses is a string

5. Look up one more data type not given above. Repeat the same procedure.
"""
s = {10, 50, 20}
print(s)
print(type(s))

# Booleans

print(10 > 9) # true
print(10 == 9) # flase
print(10 <= 9)# false
print(bool("abc")) # true
print(bool(123)) # true
print(bool(["apple", "cherry", "banana"])) # true
print(bool(True)) # true
print(bool(False)) # false
print(bool(0)) # false
print(bool("")) # false
print(bool(" ")) # true
print(bool(())) # false
print(bool([])) # false
print(bool({})) # false
print(bool(True and False)) # false
print(bool(True and True)) # true
print(bool(False and False)) # false
print(bool(True or False))# true
print(bool(True or True)) # true
print(bool(False or False)) # false
print(bool(not(False))) # true
print(bool(not(True))) # false
"""
Questions:
What pattern do you notice about expressions returning True or False?
When I ran it multiple times it would always return true

Which expression surprised you about its result?
bool(["apple", "cherry", "banana"]) confused me the most.

Create an expression, not given above, that will return True. Why is it True?
(15 == 15) It will return true becuase 15 is in fact equal to 15

Create an expression, not given above, that will return False. Why is it False?
(15 == 14) This is false because 15 doesn't equal 14
"""

# Operators

print(10 + 5) # 15. Adds 10 and 5 to get 15
print(10 - 5) # 5. Subtracts 5 from 10 to get 5
print(2 * 4) # 8. Puts 2 to the power of 4 getting 8
print(6 / 3) # 2.0. Divides 6 by 3 to get 2.0
print(5 % 2) # 1. Gives the number of deciaml places in the remainder
print(3 ** 2) # 9. Puts 3 to the power of 2
print(15 // 2) # 7 Divides 15 by 2 with no remainder
print(5 == 2) # false. Checks if 5 is equal to 2
print(10 != 10) # false. Checks if 10 doesn't equal 10
print(2 < 5) # true. Checks if 2 is less than 5
print(12 > 5) # true. Checks if 12 is greater than 5
print(5 <= 6) # true. Checks if 5 is less than or equal to 6
print(1 >= 10) # false/ Checks if 1 is greater than or equal to 10
x = 5 
x += 5
print(x) # 10. Takes x and adds 5 and then returns it to the variable x
x -= 4
print(x) # 6. Takes x and subtracts 4 from it and returns it to x
x *= 3
print(x) # 18. Takes x and multiplies it by 3 and rerturns the value to x

"""
Answer the following questions as comments:
1. What does the operator and do? Write an expression that results in True. Write an expression
that results in False.
The and operator returns true if both things its reffring to are true. If one is false it will return as false.
True: 7 > 3 and 10 < 21
False: 3 > 7 and 10 < 21

2. What does the operator or do? Write an expression that results in True. Write an expression
that results in False.
The or operator returns true if either of the things it is reffering to is true. It returns false if both are fals
True: 3 > 7 or 10 < 21
False: 3 > 7 or 21 < 10

3. What does the operator not do? Write an expression that results in True. Write an expression
that results in False.
The not operator just reverses the result of a true/false question
True: not False
False: not true
"""

"""
More Questions:
1. What is the difference between / and //?
/ will divide the two numbers and // will also divide but not inclde the decimal.

2. What is the difference between % and //?
// will divide the two numbers and not include the decimal and % will just return the number of decimal places

3. What operator would you use to calculate the remainder when dividing two numbers? Give
an example.
I would use the % operator
19%9 = 1

4. How do assignment operators work?
Assignment operators takes the variable on the left and operates on the value corresponding to whatever operator is
before the equals sign. Then it returns the result back to the variable.
"""

# Strings

my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints the first letter in hello
print(my_string[1]) # prints the 2nd letter in hello
print(my_string[2]) # prints the 3rd letter in hello
print(my_string[3]) # prints the 4th letter in hello
print(my_string[4]) # prints the 5th letter in hello
print(my_string[-1]) # prints the last letter in hello
print(my_string[1:3]) # prints the 2nd and 3rd letters in hello
print(my_string[0:5:2]) # prints the 1st letter, then the 6th letter then the 3rd letter
print(len(my_string)) # prints the length of hello which is 5 letters
print (my_string + "goodbye") # prints hello then goodbye
print (7*my_string) # prints hello 7 times

"""
Questions:
1. Define the term slicing. For which of the manipulations did you slice your string?
Slicing takes speciic values in the string by seperating with a colon. (my_string[1:3]) and (my_string[0:5:2])
use slicing

2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
"""
name = "Oski"
print("Hello, my name is", name) # the result displays the phrase "Hello, my name is" then displays the string attached to name
"""
3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
"""
name = "Oski"
print(f"Hello, my name is {name}") # the result displays the phrase "Hello, my name is" then displays the string attached to name
"""
4. What is the difference between the two last print statements?
The first one sepeartes the two outouts with a comma and the second one sepeartes the two outputs with a f string and {}
"""

# Terminal Commands
"""
cd: means change directory. After the command write a pathway to follow to change to that path.
example: cd astro_decal_fa26

ls: Means list of the directory contents. Use it by typing ls in the terminal
example: ls

ls -a: means list pf the directory contents including hidden files. Use it by typing ls in the terminal
Example: ls -a

mkdir: Make a new directory. Use it by typing mkdir and then the name of the directory you want to make
example: mkdir astro_decal_fa26

cat: Displays the file contents. Use it by typing cat and the name of the file
example: cat astro_decal.txt

pwd: Shows the current directory. Use it by typing pwd in the terminal
Example: pwd
cd ..: Change the directory to the file above. Use it by typing cd .. to get to the file above
example: cd ..

cd .: Change the directory to the current directory. Use it by typing cd .
example: cd .

cd ∼: Changes the directory to the home directory. Use it by typing cd ~ in the terminal
example: cd ~

cp: Copy the directory. Use it by typing cp and then the naame of the directory you want to copy
example: cp astro_decal_fa26

mv: Move the files in a directory. Type mv and then the name of the source and then the name of the path
example: mv old_astro_decal_fa26.txt new_astro_deacl_fa26.txt

rm (be careful with this one): Deletes the current directory. Type rm adn then the directory you want to delete
example: rm not_astro_decal_fa26

clear: Clears the terminal screen. Type clear into the ternmianl
example: clear

grep: Searchs the text for a given character or characters. Type grep then the searched characters then the file.
example: grep homeowerk1 astro_decal_fa26.txt
"""

"""
Questions:
1. Look up 3 other commands not present. Define and explain how to use them on the command
line.

rmdir: removes an empty directory. Type rmdir and the the direcotry you want to remove
example: rmdir empty_astro_decal_fa26

cls: used to clear the screen of all previously entered commands and other text. Type cls into the terminal
example: cls

date: Used to show or change the current date. Type date into the terminal
example: date

2. What is the difference between ls and ls -a?
ls -a also displays hidden files and directories

3. What is a hidden file?
A hidden file is any file that has been toggled to appear hidden. Making it so you can't see it while scrolling files.

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.

cd ~{username}: Brings you to the home of the specfied user. Use it y typing cd ~{} and then the username you wish to go to
example: cd ~{Evane}

cd -: Brings you to the previous directory. Use it by typing cd - into the ternminal
example: cd -

cd \ : brings you to the root directory. use it by typing cd \ .
example: cd \
"""

