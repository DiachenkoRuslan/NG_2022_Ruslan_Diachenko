# Input seconds
second = int(input("Enter second:"))

# border = int(input("Border value: "))

#while second <= border:
   # second+=1

minutes = second / 60%60
hours = second / 60/60 % 24
days = second / 60/ 60 / 24 % 365

seconds = second % 60

print("Days: " + str(int(days)) + " : " + "Hours: " + str(int(hours)) + " : " + "Minutes: " + str(int(minutes)) + " : " + "Seconds: " + str(int(seconds)))
