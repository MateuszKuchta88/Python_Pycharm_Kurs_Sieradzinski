# Module 9 - Meetings calendar (GPT generated, improved\fixed by me)

# TASK DESCRIPTION
# Prepare a program that will store all your meetings.
#  Store meeting information in the meetings.json file.
#  Requirements:
#  Each meeting always lasts an hour.
# Meetings can have different titles.
#  Only one meeting can be scheduled for a given day and time.
#  The calendar has methods that allow you to:
#  ● View all appointments
#  ● checking whether a given date (date and time) is available

# Import libraries
import json

class MeetingScheduler:
    def __init__(self, file_name="meetings.json"):
        self.meetings = None
        self.file_name = file_name
        self.load_meetings()

    def load_meetings(self):
        """Load meetings from the JSON file."""
        try:
            with open(self.file_name, "r") as file:
                self.meetings = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.meetings = {}

    def save_meetings(self):
        """Save meetings to the JSON file."""
        with open(self.file_name, "w") as file:
            json.dump(self.meetings, file, indent=4)

    def display_meetings(self):
        """Display all meetings."""
        if not self.meetings:
            print("No meetings scheduled.")
            return

        for meeting_date, slots in sorted(self.meetings.items()):
            print(f"Date: {meeting_date}")
            for meeting_time, meeting_title in sorted(slots.items()):
                print(f"  Time: {meeting_time}, Title: {meeting_title}")

    def is_slot_free(self, meeting_date, meeting_time):
        """Check if a specific date and time is free."""
        return not (meeting_date in self.meetings and meeting_time in self.meetings[meeting_date])

    def add_meeting(self, meeting_date, meeting_time, meeting_title):
        """Add a new meeting if the slot is free."""
        if not self.is_slot_free(meeting_date, meeting_time):
            print(f"The slot on {meeting_date} at {meeting_time} is already booked.")
            return False

        if meeting_date not in self.meetings:
            self.meetings[meeting_date] = {}

        self.meetings[meeting_date][meeting_time] = meeting_title
        self.save_meetings()
        print(f"Meeting '{meeting_title}' scheduled on {meeting_date} at {meeting_time}.")
        return True

# Example usage
if __name__ == "__main__":
    scheduler = MeetingScheduler()

    while True:
        print("\nMeeting Scheduler")
        print("1. Display all meetings")
        print("2. Check if a slot is free")
        print("3. Add a new meeting")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            scheduler.display_meetings()
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM, 24-hour format): ")
            if scheduler.is_slot_free(date, time):
                print(f"The slot on {date} at {time} is free.")
            else:
                print(f"The slot on {date} at {time} is occupied.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM, 24-hour format): ")
            title = input("Enter the title of the meeting: ")
            scheduler.add_meeting(date, time, title)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")