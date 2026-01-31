hours_of_screen_time = [
    me:= [1, 2, 3, 4, 5],  # Me
    chanelle:= [2, 3, 4, 5, 6],  # Chanelle
    heshei:= [3, 4, 5, 6, 7],  # Heshei
    ]

"""
Print each row of the array clearly (e.g., scores per student or daily steps per person).
Calculate and display:
    The total for each row (e.g., total score, total views, total steps)
    The average for each row (if applicable)
    Optionally: Find the maximum or minimum value in the entire dataset
"""

print("hours_of_screen_time:")
for i in range(len(hours_of_screen_time)):
    print(hours_of_screen_time[i])

for i in range(len(hours_of_screen_time)):
    total = sum(hours_of_screen_time[i])
    average = total / len(hours_of_screen_time[i])
    maximum = max(hours_of_screen_time[i])
    minimum = min(hours_of_screen_time[i])
    print(f"Person {i+1} - Total Hours: {total} | Average Hours: {average:.2f} | Max: {maximum} | Min: {minimum}")

"""
Reflection: Using an array helps you find the data easily since it is organized. 
The most difficult was the loops since I am not familiar with it yet.
Overall, it was a nice experience.

"""