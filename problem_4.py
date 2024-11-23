#checking string is palindrome or not
stringInput= input("Enter a string: ")
rv_string = ""
for char in stringInput:
    rv_string = char + rv_string
if stringInput == rv_string:
    print("True")
else:
    print("False")