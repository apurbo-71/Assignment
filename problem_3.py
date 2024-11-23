# finding the number of total digit
stringInput=str(input('Enter a string: '))
digits="0123456789"
Ct_digit=0
for n in stringInput:
    if n  in digits:
        Ct_digit=Ct_digit+1
print(f"Total digits are: {Ct_digit}")