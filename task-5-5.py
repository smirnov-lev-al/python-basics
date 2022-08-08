def isequence_generator(fname = 'sequence-of-integers.txt'):
    print('Enter a sequence of integers, or type "rand" to generate',
          'such a sequence using the built-in random number generator:');
    answer = input();
    try:
        if answer.lower() == 'rand':
            from random import randint;
            print('\nEnter three integers to determine the number and range',
                  'of possible random values in the sequence of integers.');
            rnum, rmin, rmax = map(int, input().split());
            if rmin > rmax:  rmin, rmax = rmax, rmin;
            isequence = [randint(rmin, rmax) for _ in range(rnum)];
        else:
            isequence = list(map(int, answer.split()));
    except ValueError:
        print('\nError :: At least one of the input values is not in an integer format.');
        print('The sequence of integers cannot be formed and stored in a file.');
        return [], '';
    print('\nTo save the data to a file, enter your preferred file name,',
          'or press the "Space" button to apply a predefined file name.');
    answer = input().strip();
    filename = fname if len(answer) == 0 else answer;
    try:
        with open(filename, 'w', encoding = 'utf-8') as foutput:
            print(*isequence, file = foutput);
    except IOError:
        print('Errorr :: Some problem occurs while trying to wirte',
              f'the sequence of integers to the file "{filename}".');
        filename = '';
    return isequence, filename;


a, filename = isequence_generator();
try:
    with open(filename, 'r', encoding = 'utf-8') as finput:
        bstr = finput.readline().strip('\n');
        b = list(map(int, bstr.split()));
        print(f'sum = {sum(b)} ({sum(a)})');
except IOError or ValueError:
    print('Errorr :: Some problem occurs while trying to read',
          f'the sequence of integers from the file "{filename}".\n');
    print(f'sum = ? ({sum(a)})');
