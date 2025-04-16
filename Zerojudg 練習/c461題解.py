a, b, c = map(int, input().split())

a = a % 2
b = b % 2

if c == 0:
    if a == 0 and b == 0:
        print("AND")
        print("OR")
        print("XOR")
    elif a == 0 and b != 0:
        print("AND")
    elif a != 0 and b == 0:
        print("AND")
    elif a != 0 and b != 0:
        print("XOR")

elif c == 1:
    if a == 0 and b == 0:
        print("IMPOSSIBLE")
    elif a == 0 and b != 0:
        print("OR")
        print("XOR")
    elif a != 0 and b == 0:
        print("OR")
        print("XOR")
    elif a != 0 and b != 0:
        print("AND")
        print("OR")
