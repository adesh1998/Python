#Task 1

import random
number = random.randint(1, 100)

print("Welcome to the guessing game !")
print("The number is between 1 and 100")

number_of_tries = 0

while number_of_tries < 3:
    guess = int(input("Please enter your guess: "))
    number_of_tries += 1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
if guess == number:
    print("Congratulations! You guessed the number in " + str(number_of_tries) + " tries!")
else:
    print("End of the game! You did not guess the number, The number was " + str(number))






#Task 2

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for i in range(0,len(charList)):
    print(f"{i}:{charList[i]}")

    

#Task 3

cDict = {'Name': 'Adesh', 'Address': 'pune', 'Language': 'English'}
for key, value in cDict.items():
    print(value," belong to ",key)



#Task 4
    
#else  invoked
    
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("The number cannot be less than 2")
    
#else not being invoked
    
i = 1
while i < 2:
    print(i)
    i += 1
    if i == 2:
      break
else:
    print("The number cannot be less than 2")

#Task 5

print("\n Function to return sum")
def add(num1,num2):
    print("Type of argument is ",str(type(num1)))
    return num1+num2
print(add(5,10),"\n")

#Task 6
print('\nFunction for Multiple Arguments \n')
def arguments(*args):
    for item in args:
        print(item)
arguments(10,20,30,40,50)

#Task 7
print('\nFunction for Multiple KwArgs \n')
def kwarguments(**kwargs):
    count=1
    for key, value in kwargs.items():
     print(value , ' -> ', key)
     print(" you passed ",count, "args ")
     count +=1
kwarguments(FirstName="Adesh",LastName="Bhosale")

#Task 8
print('\nFunction to find the count of Args and KwArgs \n')

def both_count(*args, **kwargs):
    print(f'There are {len(args)} Arg elements and {len(kwargs)} KwArgs elements')

both_count(1,2,3,4,5,name="Mr.ABC",email="abc@gmail.com",phoneNo="1234567890")

#Task 9

avg = lambda t,c : t/c
print(avg(10,2))

#Task10
total=int(input("Enter the total : "))
count=int(input("Enter the count : "))
avg = lambda total, count : total /count
print("Average  = ", avg(total,count))




