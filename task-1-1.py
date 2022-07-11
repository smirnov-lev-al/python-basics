a_srt = 'This repository contains homework';
b_str = 'assignments for the lessons of the course';
c_str = 'named "Python Basics" from GeekBrains.';
print(a_srt, b_str, c_str, end = '\n\n');

array = list(map(float, input('Enter several numbers (at least two):\n').split()));
asum = 0;
for a in array:
    asum += a;
print(f'The sum of the entered numbers is equal to {asum}.');