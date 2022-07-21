from functools import reduce;

amin, amax = 100, 1000;
agen = (i for i in range(amin, amax + 1) if i % 2 == 0);
p = reduce(lambda x, y: x * y, agen);
print(f'the product of all even elements from {amin} to {amax} is\n{p}.')

