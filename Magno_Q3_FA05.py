hours_of_screen_time = [ 
    [1, 2, 3, 4, 5], # Me 
    [2, 3, 4, 5, 6], # Chanelle 
    [3, 4, 5, 6, 7], # Heshei 
] 
#Rows: Me, Chanelle, Heshei 
#Columns: Monday, Tuesday, Wednesday, Thursday, Friday

# Store totals in a list to compare later
daily_totals = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Calculate and print total for each day using a loop
for day_index in range(len(weekdays)):
    total = hours_of_screen_time[0][day_index] + hours_of_screen_time[1][day_index] + hours_of_screen_time[2][day_index]
    daily_totals.append(total)
    print(f"Total Steps on {weekdays[day_index]}: {total}")

# Identify the most active day overall
most_active_steps = max(daily_totals)
most_active_day_index = daily_totals.index(most_active_steps)
most_active_day_name = weekdays[most_active_day_index]

print(f"Most Active Day Overall (in steps): {most_active_day_name} ({most_active_steps})")

