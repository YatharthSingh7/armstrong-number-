def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    if total == num:
        return True
    else:
        return False
while True:
    try:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive number.")

if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

