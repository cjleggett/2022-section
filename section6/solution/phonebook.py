import csv
import sys

def main():
    # Read in phone numbers
    people = []
    with open("numbers.csv", "r") as f:
        for row in csv.DictReader(f):
            people.append(row)

    # Print out data
    for person in people:
        name = person["name"]
        number = person["number"]
        print(f"{name}'s phone number is {convert_number(number)}.")


def convert_number(phone_number):
    area_code = phone_number[:3]
    first_3 = phone_number[3:6]
    last_4 = phone_number[6:]
    return f"({area_code}) {first_3}-{last_4}"

main()