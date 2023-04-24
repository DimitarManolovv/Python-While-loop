max_number = None

while True:
    num_input = input()

    if num_input == "Stop":
        break

    number = int(num_input)

    if max_number is None or number > max_number:
        max_number = number

print(max_number)
