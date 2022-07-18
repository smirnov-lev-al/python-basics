def my_func(x, y):
    m, n = (1. / x, -y) if y < 0 else (x, y) if y > 0 else (1., 0);
    p = 1.;
    for i in range(n // 2):  p *= m;
    p *= p if n % 2 == 0 else p * m;
    return p;

x = float(input('Enter a numbers to raise a number to a power:\n'));
y = int(input('Enter the corresponding power value:\n'));
print('\nThe result returned by the python operator "**":\n', x**y);
print('\nThe answer obtained by using the function "my_func":\n', my_func(x, y));