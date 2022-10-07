i = 0
while i < 3:
    print(i)
    i += 1
print()


for i in range(0, 3, 1):
    print(i)
print()


for i in range(3):
    print(i)
print()


name = "Connor"
for letter in name:
    print(letter)
print()


my_list = ["hey", 2, 7.5]
for element in my_list:
    print(element)
print()

ages = {
    "connor": 22,
    "sophie": 20,
    "sam": 18
}

for name, age in ages.items():
    print(f"{name}: {age}")