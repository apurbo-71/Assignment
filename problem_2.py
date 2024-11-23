#Multiplication table
Number=int(input("Enter a number for multiplication table: "))
for i in range(1,11):
    T_multi= i*Number
    print(f"{Number}*{i}={T_multi}")
    i=i+1