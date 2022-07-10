array = list(map(int, input('Enter a list with integer numbers:\n').split()));
array.sort(reverse = True);
print('We have the following rating structure:');
print(*array, sep = ', ', end = '\n\n');

print('Enter a new item to include in the rating structure:');
a = int(input());

if a > array[0]:
    array.insert(0, a);
else:
    array.append(a);
    for n in range(-1, - (len(array) + 1), -1):
        if array[n] > array[n - 1]:
            array[n], array[n - 1] = array[n - 1], array[n];
        else:  break;
print('Updated rating structure:');
print(*array, sep = ', ', end = '\n');
