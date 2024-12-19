number = int(input("Enter a number to see its multiplication table: "))

for i in range(11):
    ans = number * i
    print(number, "*", i, "=", ans)
