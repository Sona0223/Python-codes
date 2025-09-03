a='NH-24, Delhi Hapur By pass vijay nagar 201009'
alpha=0
digit=0
for val in a:
    if val.isalpha():
        alpha=alpha+1
    if val.isdigit():
        digit=digit+1
print(f"Total number of alphabets={alpha}")
print(f"Total number of digits={digit}")  