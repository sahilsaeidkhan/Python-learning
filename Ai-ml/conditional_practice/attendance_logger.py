# 1. The Smart Attendance Logger
# The Goal: Manage a classroom attendance list and ensure no duplicate entries are recorded if a student taps their ID
# card twice.
# Concepts: set , function , while .
# The Problem: Create a function mark_attendance() that keeps asking for student names until the user
# types "STOP". Store names in a Set to automatically prevent duplicates.
# Input: Multiple strings (names) entered one by one.
# Output: The final count of unique students and the set itself.


def mark_attendance():
    names_list = set()

    while True:
     
     name = input("Enter your name ( or STOP ): ")

     if name == "STOP":
        break
     
     names_list.add(name)


    print(len(names_list))
    print(names_list)


mark_attendance()