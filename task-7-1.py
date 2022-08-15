from json import dumps;
from random import randint;

class Matrix:
    __matrix_types = {0: 'zeros', 1: 'ones', 2: 'identity', 3: 'random'};

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.type = 'common';
            self.size = [len(args[0]), len(args[0][0])];
            self.matrix = args[0];
        elif 'matrix' in kwargs:
            self.type = 'common';
            self.size = [len(kwargs['matrix']), \
                         len(kwargs['matrix'][0])];
            self.matrix = kwargs['matrix'];
        else:
            if 'type' in kwargs:
                self.type = kwargs['type'];
            else:
                message = dumps(Matrix.__matrix_types).strip('{').strip('}');
                message = message.replace('"', '').replace(':', ' ' + chr(8680));
                print('Select the matrix type.\nMake a choice from the',
                      f'following supported matrix types:\n{message}');
                answer = input();
                if answer.isdigit() and int(answer) in Matrix.__matrix_types.keys():
                    self.type = Matrix.__matrix_types[int(answer)];
                elif answer in Matrix.__matrix_types.values():
                    self.type = answer;
                else:
                    print('Warning :: The choice does not match',
                          'with any supported matrix types.');
                    print('The matrix will be filled with random integer numbers.');
                    self.type = 'random';
            if 'size' in kwargs:
                self.size = list(kwargs['size']);
            else:
                try:
                    print('\nEnter two integers to determine the matrix size:');
                    self.size = list(map(int, input().split()));
                except ValueError:
                    print('Error :: At least one of the input',
                          'values is not in an integer format.');
                    print('The matrix 2x2 will be generated.');
                    self.size = [2, 2];
            if self.type == 'zeros':
                self.matrix = [[0] * self.size[1]] * self.size[0];
            elif self.type == 'ones':
                self.matrix = [[1] * self.size[1]] * self.size[0];
            elif self.type == 'identity':
                if self.size[0] < self.size[1]:
                    self.size[1] = self.size[0];
                else:
                    self.size[0] = self.size[1];
                self.matrix = [[0] * self.size[1]] * self.size[0];
                for i in range(self.size[0]):
                    self.matrix[i][i] = 1;
            elif self.type == 'random':
                try:
                    if 'randrange' in kwargs:
                        rmin, rmax = kwargs['randrange'];
                    else:
                        print('\nEnter three integers to determine',
                              'the range of possible random values.');
                        rmin, rmax = map(int, input().split());
                    if rmin > rmax:  rmin, rmax = rmax, rmin;
                except ValueError or TypeError:
                    print('Error :: At least one of the input',
                          'values is not in an integer format.');
                    rmin, rmax = -10, +10;
                self.matrix = [[randint(rmin, rmax) for _ in range(self.size[1])]\
                                                    for _ in range(self.size[0])];
            else:  pass;
    
    def __str__(self):
        strmatrix = '';
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                strmatrix += f'{self.matrix[i][j]:6}';
            strmatrix += '\n';
        return strmatrix;

    def __add__(self, other):
        if type(other) is int:
            matrix =[[other + element for element in row] for row in self.matrix];
        else:
            if self.size != other.size:
                print('Error :: Matrices have different sizes',
                      'and cannot be summed element-wise.');
                return ArithmeticError;
            else:
                matrix =[[self.matrix[i][j] + other.matrix[i][j]\
                          for j in range(self.size[1])] for i in range(self.size[0])];
        return Matrix(matrix);
    
    def __mul__(self, other):
        if type(other) is int:
            matrix =[[other * element for element in row] for row in self.matrix];
        else:
            if self.size != other.size:
                print('Error :: Matrices have different sizes',
                      'and cannot be multiplied element-wise.');
                return ArithmeticError;
            else:
                matrix =[[self.matrix[i][j] * other.matrix[i][j]\
                          for j in range(self.size[1])] for i in range(self.size[0])];
        return Matrix(matrix);
    
    def __radd__(self, a : int):
        matrix =[[a + element for element in row] for row in self.matrix];
        return Matrix(matrix);

    def __rmul__(self, a : int):
        matrix =[[a * element for element in row] for row in self.matrix];
        return Matrix(matrix);


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]);
    m2 = Matrix(size = (4, 3), type = 'ones');
    m3 = 3 * m2;
    m4 = Matrix(size = (4, 3), type = 'random', randrange = (-20, 20));

    for n, m in enumerate([m1, m2, m3, m4]):
        print(f'{m.type} matrix {n}:\n{m}');

    print(f'sum of matrix 1 and martix 4:\n{m1 + m2}');
else:
    print('Matrix Module.');
