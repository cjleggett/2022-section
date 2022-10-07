def remove_a(s):
    new_s = ""
    for letter in s:
        if letter != "a" and letter != "A":
            new_s += letter
    return new_s

def remove_a_2(s):
    return "".join([letter for letter in s if letter not in {"a", "A"}])

def main():
    s = input("Phrase: ")
    print(remove_a(s))
    print(remove_a_2(s))

main()