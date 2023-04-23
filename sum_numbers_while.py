target_sum = int(input("Enter target sum: "))
current_sum = 0

while current_sum < target_sum:
    number = int(input("Enter a number: "))
    current_sum += number

print("Sum of entered numbers:", current_sum)
