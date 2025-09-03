def is_valid_phone_number(number):
    return len(str(number)) == 5 and str(number)[0] != '0'
n = int(input())
y = int(input())
total_bill = n * y
if is_valid_phone_number(total_bill):
    print(f"The total bill {total_bill} is a valid phone number.")
else:
    print(f"The total bill {total_bill} is not a valid phone number.")