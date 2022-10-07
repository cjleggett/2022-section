def count_a(s):
    total = 0
    for letter in s:
        if letter == "a" or letter == "A":
            total += 1
    return total

def count_a_2(s):
    return sum([1 for letter in s if letter in {"a", "A"}])

def main():
    s = input("Phrase: ")
    print(count_a(s))
    print(count_a_2(s))

main()