hours_of_screen_time = [
    me:= [1, 2, 3, 4, 5],  # Me
    chanelle:= [2, 3, 4, 5, 6],  # Chanelle
    heshei:= [3, 4, 5, 6, 7],  # Heshei
    ]

#Rows: Me, Chanelle, Heshei
#Columns: Monday, Tuesday, Wednesday, Thursday, Friday

#Print or access a specific value
#Update a specific value
#Or summarize the dataset (e.g., total, average, max)

# Example: Print the screen time for Chanelle on Wednesday
print("Chanelle's screen time on Wednesday:", hours_of_screen_time[1][2], "hours")

# Example: Update Heshei's screen time on Friday to 8 hours
hours_of_screen_time[2][4] = 8
print("Updated Heshei's screen time on Friday:", hours_of_screen_time[2][4], "hours")

# Example: Calculate total screen time for Me over the week
total_hours_me = sum(hours_of_screen_time[0])
print("Total screen time for Me over the week:", total_hours_me, "hours")

#Average screen time for wednesday
average_wednesday = (hours_of_screen_time[0][2] + hours_of_screen_time[1][2] + hours_of_screen_time[2][2]) / 3
print("Average screen time on Wednesday:", average_wednesday, "hours")

"""
Reflection: I chose this dataset since a lot of people have been using their phones everyday, 
and tracking screen time is a good way to know how much time we spent on our devices. 
This can help us find the problem why we can't focus/manage our time well.

"""
