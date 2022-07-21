example = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55];

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

b = [a[i] for i in range(1, len(a)) if a[i] > a[i - 1]];
print(f'\nThe list befor transformation is as follows:\n{a}');
print(f'\nThe list after transformation is as follows:\n{b}');
