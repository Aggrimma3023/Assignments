print("Enter the number of seconds you want to convert to minutes and seconds")
seconds=int(input())
minutes=seconds//60
rem_sec=seconds%60
print("The number of minutes in entered number of seconds are " + str(minutes))
print ("The remaining seconds are " + str(rem_sec))