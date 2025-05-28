# PD9 2 - Read json

# TASK DESCRIPTION
# Write a class that handles the json file according to: pattern.
# It should load the contents of the json file into
# variable, and if the file does not exist the variable should
# contain an empty list. Additionally, she should have it
# ability to add a new object to a file

# Import libraries
import json

# Code
class JSONfile:
    def __init__(self, file_path: str):
        self.content = None
        self.file_path = file_path
        self._load_json_file()

    def _load_json_file(self):
        """Load meetings from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                self.content = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.content = {}

    def add_person_to_file(self, first_name: str, last_name: str):
        person = {'first_name': first_name, 'last_name': last_name}
        self.content.append(person)
        with open(self.file_path, "w") as file:
            json.dump(self.content, file, indent=4)

    def __repr__(self):
        return f"Content: {self.content}."


# Example usage
x = JSONfile("peoples.json")
print(x)
x.add_person_to_file("Andrzej", "Duda")
print(x)
x = JSONfile("people.json")
print(x)
x.add_person_to_file("Jan", "Kowalski")
print(x)

