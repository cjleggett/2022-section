from cs50 import get_string, SQL

# Connect to the database
db = SQL("sqlite:///school.db")

# Add new person
name = get_string("Name: ")

# TODO: Add the student as a person and get their ID
student_id = ...

# Prompt for courses to enroll in
while True:
    code = get_string("Course Code: ")

    # If no input, then stop adding courses
    if not code:
        break

    # TODO: Query for course
    results = ...

    # TODO: Check to make sure course exists

    # TODO: Enroll student by associating them with a course.

    print(f"Added {name} to {code}")

    # Testing hello lkj