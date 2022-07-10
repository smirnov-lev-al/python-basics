print('Enter a list with integer numbers:');
array = list(map(int, input().split()));
while True:
    try:
        astr = input();
        if astr == '' or astr == ' ': break;
        anum = list(map(int, astr.split()));
    except ValueError: break;
    array.extend(anum);
print(array);

N = len(array) // 2;
for n in range(N):
    array[2 * n], array[2 * n + 1] = \
        array[2 * n + 1], array[2 * n];
print(array);
