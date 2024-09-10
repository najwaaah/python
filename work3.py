# leap year

a = int(input("Enter a YEAR: "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :

    print("its a leap year")
else:
    print("not a leap year")