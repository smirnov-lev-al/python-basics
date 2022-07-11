n = int(input('Enter an integer number: '));
m, max_digit = n, 0;

while m > 0:
    digit = m % 10;
    if digit > max_digit:
        max_digit = digit;
        if max_digit == 9:  break;
    m //= 10;

print(f'The greatest digit in the entered number is {max_digit}.');