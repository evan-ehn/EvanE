# Homework 1 + 2 review
# 2.1 Vocabulary Review

#Git vs. GitHub
# Git is the actual version control system, responsible for tracking changes and looking at the history of a project, 
# while github is a platform for hosting Git repositories.

# Terminal vs. Command Line
# A terminal is a text input and output area. and a command line is where a user enters commands and data to navigate directories

# Local vs. Remote Repository
# A local repository is a repository that is centralized on a local system, while a remote repository can be accessed anywhere.

# Version Control
# A version control is a system used to track and monitor projects and collaborations

# Staging Area
# The stageing area is the place you put your documents that you want to send to a remote repository

# git add
# This is how you put something onto the staging area

# git commit
# this is how you save you work locally

# git push
# This is how you push your documents to a remote repository

# git status
# This tell you the status of your repository

# git pull
# this pulls changes from a remote repository into your local repository 

# pwd
# This displays your current directory

# ls
# This displays all the sub directories within your current directory

# cd
# This moves you to a specified directory

# nano
# This launches a specified text file

# touch
# This craetes a new file in your current repository

# mv
# This moves a specified file into a specified repository

# rm
# This removes a specified file from a directory

# cat
# This displays the contents of a file

# 2.2 directory Tree

# You have been plopped into Judy’s directory system. What command will tell you what your 
# #current working directory is?
# pwd

# The terminal responds by saying you are in ∼/python decal/judy decal. What command
# will list all the files in your current working directory?
# ls

# Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
# You will need to pull the brianna repo repository to find the updated file. What command(s)
# will let you move to the correct repository and pull the latest changes?
# cd python_decal/brianna_repo/
# git pull

# How would you move this new homework.py to the homework/ folder in your personal repository?
#mv homework.py/brianna_repo/python_decal/judy_decal/homework/

# How would you move yourself to the same repository as homework.py?
# cd brianna_repo/python_decal/judy_decal/homework/

# You want to see the contents of homework.py in your terminal, how would you do this?
# python3 homework.py

# Great job! You just finished the homework for this week. What command(s) allow you to
# save the changes and push from your local repository to your remote repository?
# git add .
# git commit -m "done with homework"
# git push origin main

# Oh no! Git gave you the following error. What commands should you call to resolve this
# error and push your homework properly? What does the error mean? (i.e. what did “Judy”
# do wrong when trying to push?
# They didn't do it in the correct order. They tried to push without adding an updated repository

# What absolute path will allow you to move to Recents/?
# cd ~/recents

# 3 Homework review
# 3.1 Data types:
def checkDataType(input):
    if type(input) == int:
        return("int")
    elif type(input) == float:
        return("float")
    elif type(input) == complex:
        return("complex")
    elif type(input) == str:
        return("string")
    elif type(input) == list:
        return("list")
    elif type(input) == dict:
        return("dict")
    elif type(input) == tuple:
        return("tuple")
    elif type(input) == bool:
        return("boolean")
    else:
        return("NoneType")
print(checkDataType(True))

# 3.2 conditionals
def evenorodd(num):
    if (num % 2) == 0:
        return("even")
    else:
        return("odd")
print(evenorodd(13))

# 4 Loops
numbers = [1, 2, 3, 4, 5]
def summation(input):
    result = 0
    for i in input:
        result += i
    return(result)
print(summation(numbers))

# 5 Lists
# 5.1 lists
letters = ["a", "b", "c"]
def duplicatelist(letters):
    final_result = []
    for i in letters:
        final_result.append(i)
        final_result.append(i)
    return(final_result)
print(duplicatelist(letters))


# 5.2 debugging
def square(num): # this function didn't have a colon
    return num * num
print(square(5))