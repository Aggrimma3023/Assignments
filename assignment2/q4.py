print("Enter three numbers")
first_no=int(input())
second_no=int(input())
third_no=int(input())
if first_no==second_no:
    if second_no==third_no:
        print("The entered numbers are equal with value",first_no)
if first_no>second_no:
    if first_no>third_no:
        print("First number",first_no, "is the greatest")
    else:
        print("Third number",third_no,"is the greatest")
elif second_no>third_no:
    print("Second number",second_no,"is the greatest")
else:
    print("Third number ",third_no,"is the greatest")























