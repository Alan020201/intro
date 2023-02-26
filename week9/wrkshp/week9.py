total = 0

while True:
    num = int(input("Enter a positive integer (enter -1 to exit): "))
    if num == -1:
        break
    if num > 100:
        print("Number greater than 100, not included in the sum.")
        continue
    total += num

print("The sum of the integers entered is:", total)
