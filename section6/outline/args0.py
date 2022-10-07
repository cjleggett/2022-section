import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Correct Usage: python args.py [arg1] [arg2]")
    result = add(sys.argv[1], sys.argv[2])
    print(result)

def add(x, y):
    return x + y

main()