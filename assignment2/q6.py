print("Enter the sides of the triangle you want to check")
side_one=float(input())
side_two=float(input())
side_three=float(input())
if (((int(side_one)+int(side_two))>int(side_three))) and ((int(side_two)+int(side_three))>side_one) and ((int(side_three)+int(side_one))>side_two):
    print("yes")
else:
    print("No")