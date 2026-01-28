Student = {}
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Favorite_Subject = input("Enter your favorite subject: ")
Student['Name'] = Name
Student['Age'] = Age
Student['Favorite subject'] = Favorite_Subject
print("Student Record:")
for key, value in Student.items():
    print(f"{key}: {value}")