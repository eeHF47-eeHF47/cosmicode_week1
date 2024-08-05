# Task 5: Create a program that converts a given time in seconds to hours, minutes, and seconds.

def convert_seconds(total_seconds):
    hours=total_seconds//3600
    minutes = (total_seconds%3600)//60
    seconds = total_seconds%60
    return hours, minutes ,seconds

# now,take input from the user
total_seconds=int(input("Enter the time in seconds: "))

# conversion
hours, minutes ,seconds= convert_seconds(total_seconds)

# result
print(f"{total_seconds} seconds is equivalent to {hours} hours,{minutes} minutes, and {seconds} seconds.")