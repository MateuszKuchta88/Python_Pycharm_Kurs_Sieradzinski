# Find who didn't go on a trip

# You have a set of students going to class and a set of those going to
# trip. Prepare a collection of students who stay in school.

# Declare set of students
students = {
                    ("Piotr", "Kowalczyk"),
                    ("Katarzyna", "Mazur"),
                    ("Tomasz", "Adamski"),
                    ("Agnieszka", "Kaczmarek"),
                    ("Krzysztof", "Krawczyk")
           }

# Declare who goes on a trip
going_on_trip = {
                    ("Katarzyna", "Mazur"),
                    ("Tomasz", "Adamski"),
                    ("Krzysztof", "Krawczyk")
                }

# Check who stays in school
who_stays_in_school = students - going_on_trip

# Print an output
print(f'In school stay: {who_stays_in_school}.')
