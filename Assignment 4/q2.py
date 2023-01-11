print("Enter the year you want to check for leap year")
year=int(input())
if year%100==0:
    if year%400==0:
        print("the year",year,"is a leap year")
    else:print("The year is not a leap year")
elif year%4==0:
        print("The year is a leap year")
else:print("the year is not a leap year")

