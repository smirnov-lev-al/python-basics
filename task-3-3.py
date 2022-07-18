def my_func(num1, num2, num3):
    s = num1 + num2 if num1 + num2 > num2 + num3 else \
        num2 + num3 if num2 + num3 > num1 + num3 else num1 + num3;
    return s;

a, b, c = map(float, input('Enter tree numbers:\n').split());
print('The sum of the two largest numbers you entered is', my_func(a, b, c));