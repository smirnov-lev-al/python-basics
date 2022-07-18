from math import nan;

def division(dividend, divisor):
    if divisor == 0:
        quotient = nan;
        print('Error :: Dvision by zero.\nThe result of division by zero cannot be defined.');
    else:
        quotient = dividend / divisor;
    return quotient;

while True:
    print('Enter two numbers to find their quotient:');
    try:
        nums = list(map(float, input().split()));
        if len(nums) == 1:  nums.append(float(input()));
        result = division(nums[0], nums[1]);
        if result == result:
            print(f'The result of dividing {nums[0]} by {nums[1]} is {result}.\n');
    except ValueError:  print('Something is wrong. Please, try again.');
    qanswer = input('Press "Enter" to continue, or type "Q" to finish.\n');
    if qanswer.upper() == 'Q':  break;
