from math import factorial;

def fact(N):
    n, f = 0, 1;
    while n < N +1:
        yield n, f;
        n += 1;
        f *= n;

M = int(input('Enter an integer number: '));
print(f'Factorials of integers from {0} to {M} are equal:')
for el in fact(M):
    print(f'{el[0]}! = {el[1]} ({factorial(el[0])})');