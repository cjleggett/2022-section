word = "but"

def count_buts(s):
    total = 0
    for i in range(len(s) - len(word)):
        if s[i:i + len(word)] == word:
            total += 1
    return total

def main():
    s = input("Sentence: ")
    print(count_buts(s))

main()