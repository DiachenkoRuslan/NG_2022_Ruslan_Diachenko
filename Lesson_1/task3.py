# Input seconds
seconds = int(input("Enter second:"))

minutes = seconds / 60%60
hours = seconds / 60/60 % 24
days = seconds / 60/ 60 / 24 % 365

seconds = seconds % 60

print("Days: " + str(int(days)) + " : " + "Hours: " + str(int(hours)) + " : " + "Minutes: " + str(int(minutes)) + " : " + "Seconds: " + str(int(seconds)))
