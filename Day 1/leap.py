year = int(input("Enter year\n"))

if year % 100 != 0 and year % 4 == 0:
    print("Leap Year")

elif year % 400 == 0:
    print("Leap Year")


else:
    print("Non leap year")