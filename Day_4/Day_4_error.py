# Task 6
try:
    inputValue1 = int(input("Enter a number : "))
    inputValue2 = input("Enter a string : ")
    print("Square root of Your number input is ", inputValue1*inputValue1)
    print("Upper case of your string is ", inputValue2.upper())
    print("Square root of Your number input is "+ inputValue1)
except ValueError:
    print("Your input was faulty")
except TypeError:
    print("Your Data Type was faulty")
