example = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11];

print('Enter a list of integer numbers, or type "rand" to generate',
       'such a list using the built-in random number generator:');
answer = input();

if answer.lower() == 'rand':
    from random import randint;
    print('Enter three integers to determine the number',
             'and range of possible random values.');
    try:
        rnum, rmin, rmax = map(int, input().split());
        if rmin > rmax:  rmin, rmax = rmax, rmin;
        a = [randint(rmin, rmax) for n in range(rnum)];
    except ValueError:
        print('Error :: At least one of the input values is not in an integer format.');
        print('The predefined array from the example is taken as the input list.');
        a = example;
else:
    try:
        a = list(map(int, answer.split()));
    except ValueError:
        print('Error :: At least one of the input values is not in an integer format.');
        print('The predefined array from the example is taken as the intial list.');
        a = example;

b = {a[i] : i for i in range(len(a))};
c = [key for key in b.keys() if b[key] == a.index(key)];

print(f'\nThe initial list is as follows:\n{a}');
print(f'\nThe list of  non-duplicate values is as follows:\n{c}');
