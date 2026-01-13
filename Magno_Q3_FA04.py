hours_of_screen_time = [
    [1, 2, 3, 4, 5],  # Me
    [2, 3, 4, 5, 6],  # Chanelle
    [3, 4, 5, 6, 7],  # Heshei
]

person_totals = []
for person_hours in hours_of_screen_time:
    current_person_total = sum(person_hours)
    person_totals.append(current_person_total)
    print(f"Total Hours for one person in loop: {current_person_total}")

max_hours = max(person_totals)
min_hours = min(person_totals)
print(f"Max Hours for one person: {max_hours}")
print(f"Min Hours for one person: {min_hours}")

range_hours = max_hours - min_hours
print(f"Difference between Max and Min Hours: {range_hours}")
