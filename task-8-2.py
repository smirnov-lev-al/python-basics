from math import nan, inf;

class ZeroDivisionException(Exception):
    def __init__(self, dividend, errorstr = 'Error :: Dvision by zero.'):
        self.quotient = nan if dividend == 0 else inf;
        self.errorstr = errorstr;
    def __str__(self):
        return self.errorstr;

def division(dividend, divisor):
    try:
        if divisor == 0:
            raise ZeroDivisionException(dividend);
        quotient = dividend / divisor;
    except ZeroDivisionException as err:
        quotient = err.quotient;
        print(err);
    return quotient;

while True:
    print('Enter two numbers to find their quotient:');
    try:
        nums = list(map(float, input().split()));
        if len(nums) == 1:  nums.append(float(input()));
        result = division(nums[0], nums[1]);
        print(f'The result of dividing {nums[0]} by {nums[1]} is {result}.\n');
    except ValueError:  print('Something is wrong. Please, try again.');
    qanswer = input('Press "Enter" to continue, or type "Q" to finish.\n');
    if qanswer.upper() == 'Q':  break;
