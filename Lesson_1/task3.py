# Variables start value.
days = 0
hours = 0
minutes = 0
seconds = 0

# Input seconds who comes for 01.01.1970.
seconds = int(input("Enter seconds: "))

# Algorithm
if seconds > 60:                # if seconds > 60,
    minutes = seconds/60        # minutes = seconds/60(60 - second in 1 minute)
    seconds = seconds%60        # cout seconds without overflow (Example: seconds = 100, then seconds = 40)

    if minutes > 60:            # if minutes > 60,
        hours = minutes/60      # hours = minutes/60(60 - minutes in 1 hour)
        minutes = minutes%60    # cout minutes without overflow (Example: minutes = 70, then minutes = 10)

        if hours > 24:          # if hours > 60, 
            days = hours/24     # days = hours/24(24 - hours in 1 day)
            hours = hours%24    # cout hours without overflow (Example: hour = 27, then hour = 3)


# Graphic
print("================================================================")


print("Time flow with 01.01.1970:")
# days:hours:minutes:seconds. Therefor str(int()), this doing because 1.6 -> 1 > "1". Very bigger number after comma...
print("Days: " + str(int(days)) + " : " + "Hours: " + str(int(hours)) + " : " + "Minutes: " + str(int(minutes)) + " : " + "Seconds: " + str(int(seconds)))

# Graphic
print("================================================================")
