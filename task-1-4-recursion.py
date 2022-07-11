def greatest_digit(n):
    if n < 10:
        return n;
    else:
        r = n % 10;
        m = greatest_digit(n // 10);
        return m if m > r else r;

n = int(input('Enter an integer number: '));
max_digit = greatest_digit(n);
print(f'The greatest digit in the entered number is {max_digit}.');