number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    ans = number * i
    multiplication_table = number, "*", i, "=", ans
    print(multiplication_table)
