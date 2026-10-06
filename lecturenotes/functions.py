#def say_hello(name):
    #print ("hello", name)

#def add(a, b):
    #return(a + b)

#print(add(7, 8))

#def check_num(x):
    #if x > 0:
        #return("positive")
    #elif x < 0:
        #return("negative")
    #else:
        #return "zero"
#print(check_num(42))

#def can_vote(age, is_citizen):
 #   if age >= 18 and is_citizen:
  #      print("you can vote")
   # else:
    #    print("you cannot vote")

#can_vote(20, True)

#def is_weekend(day):
    #if day == "saturday" or day == "sunday":
   #  else:
 #       return("it is not the weekend")

#print(is_weekend("sunday"))

#for i in range(10):
 #   print(i)

#fruit_basket = ["lychee", "mango", "nectarines"]
#for fruit in fruit_basket:
 #   print(fruit)

#def countdown(start):
    #while start > 0:
   #     print("T-", start)
  #      start -= 1
 #   print("liftoff")

#countdown(10)

#def weather(temp):
    #if temp >= 65 and temp <= 80:
    #    return("It's warm today")
   # elif temp > 85:
 #       return("It's hot today")
  #  else:
 #       return("It's cold today")

#print(weather(40))

data_list = [40, 80, 10, 30, 50, 20]
def min_num(num):
    minimum = min(num)
    return(minimum)
print(min_num(data_list))

data_list = [40, 80, 10, 30, 50, 20]
def max_num(num):
    maximum = max(num)
    return(maximum)
print(max_num(data_list))

# create a function to determine if a positive integer is prime

def prime(num):
    if num <= 0 or type(num) != int:
        return("Choose a new number")
    else:
        if num == 1:
            return("neither")
        elif num == 2:
            return("is a prime number")
        else:
            if num % 2 == 0:
                return("Not a prime number")
            else:
                for i in range(2, num):
                    if num % i == 0:
                        return("Not a prime number")
                    else:
                        return("This is a prime number")

print(prime(439847))
readings = [15, 14, 17, 20, 23, 28, 20]
min = 100
max = 0
def readings ():
    for i in readings:
        if i < min:
            min = i
        else