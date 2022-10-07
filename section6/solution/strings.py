phrase = "Hello, World!"

print("phrase[0]")
print(phrase[0])
print()

print("phrase[-1]")
print(phrase[-1])
print()

print("phrase[2:4]")
print(phrase[2:4])
print()

print("phrase[2:]")
print(phrase[2:])
print()

print("len(phrase)")
print(len(phrase))
print()

new_phrase = "     phrase    "
print("new_phrase.strip()")
print(new_phrase.strip())

# Formatted strings
name = input("Name: ")
phrase = f"Hello, {name}!"
print(phrase)
print()

age = 22
phrase = f"You are {age} years old."
print(phrase)
