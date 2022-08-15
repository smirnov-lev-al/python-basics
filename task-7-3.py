class Cell:
    def __init__(self, csize : int):
        self.__size = csize;

    @property
    def size(self):
        return self.__size;
    @size.setter
    def size(self, csize):
        self.__size = csize;
        
    def __add__(self, other):
        csize = self.size + other.size;
        return Cell(csize);
    def __sub__(self, other):
        if (self.size - other.size) > 0:
            csize = self.size - other.size;
            return Cell(csize);
        else:
            mesage = 'Warning : Operation with cells is not possible.\n' + \
                     'The size of the first cell is large than the size of the second cell.';
            return mesage;
    def __mul__(self, other):
        csize = self.size * other.size;
        return Cell(csize);
    def __truediv__(self, other):
        csize = self.size // other.size;
        return Cell(csize);
    
    def make_order(self, n : int):
        m, r = self.size // n, self.size % n;
        cellstr, k = '', m;
        while k > 0:
            cellstr += ('*' * n);
            k -= 1;
            if k == 0: break;
            cellstr += '\n';
        if r != 0:
            if m != 0: cellstr += '\n';
            cellstr += ('*' * r);
        return cellstr;

if __name__ == '__main__':
    nsplit = 5;
    cell_1 = Cell(15);
    cell_2 = Cell(18);
    cell_3 = Cell(4);
    print(f'First three initial cells splitted by {nsplit} units in a row:');
    for c in [cell_1, cell_2, cell_3]:
        print(f'Cell of size {c.size}:', c.make_order(nsplit), sep = '\n', end = '\n\n');

    nsplit = 7;
    cell_4 = cell_1 + cell_3;
    cell_5 = cell_2 - cell_3;
    cell_6 = cell_1 * cell_3;
    cell_7 = cell_2 / cell_3;
    print('Four cells obtained after cells operations and',
          f'splitted by {nsplit} units in a row:');
    for c in [cell_4, cell_5, cell_6, cell_7]:
        print(f'Cell of size {c.size}:', c.make_order(nsplit), sep = '\n', end = '\n\n');
else:
    print('Cell Module.');
