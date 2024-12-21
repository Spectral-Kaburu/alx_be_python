size = int(input("Enter the size of the pattern: "))
x = size

while x:
    for _ in range(size):
        print("*", end="")
    x -= 1    
    print()

