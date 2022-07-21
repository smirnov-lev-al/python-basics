from sys import exit;
from itertools import count, cycle;


print('Enter two numbers to determine the first and',
       'last elements of a sequence of integers:');
try:
    cmin, cmax = map(int, input().split());
    if cmin > cmax:  cmin, cmax = cmax, cmin;
except ValueError:
    exit('Error :: At least one of the input values is not in an integer format.');

print(f'The sequence of integers from {cmin} to {cmax} is:');
for el in count(cmin):
    if el > cmax:  break;
    print(el, end = ' ');
print('\n');

progr_lang_list = ['c/c++', 'fortran', 'java', 'javascript', 'python'];
progr_lang_iter = cycle(progr_lang_list);
print('Cycle sequence of programming languages:');
c = cmin;
for el in progr_lang_iter:
    if c > cmax:  break;
    print(el);
    c += 1;