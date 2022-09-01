from math import sqrt, atan2, nan, inf;

class Complex:
    def __init__(self, re, im):
        self.__c = [re, im];
    
    @property
    def real(self):    return self.__c[0];
    @real.setter
    def real(self, re):  self.__c[0] = re;
    
    @property
    def imag(self):    return self.__c[1];
    @imag.setter
    def imag(self, im):  self.__c[1] = im;
    
    @property
    def norm(self):
        return self.real**2 + self.imag**2;
    @property
    def abs(self):  return sqrt(self.norm);
    @property
    def angle(self):
        return atan2(self.imag, self.real);
    
    def conj(self):
        return Complex(self.real, -self.imag);
    
    def __str__(self):
        signstr = [-1, '-'] if self.imag < 0 else [+1, '+'];
        return f'({round(self.real, 5)}{signstr[1]}{round(signstr[0]*self.imag, 5)}j)';
    
    def __add__(self, other):
        if type(other) is int or type(other) is float:
            re, im = self.real + other, self.imag;
        else:
            re = self.real + other.real;
            im = self.imag + other.imag;
        return Complex(re, im);
    def __radd__(self, re):
        re, im = self.real + re, self.imag;
        return Complex(re, im);
    
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            re, im = self.real * other, self.imag * other;
        else:
            re = self.real * other.real - self.imag * other.imag;
            im = self.real * other.imag - self.imag * other.real;
        return Complex(re, im);
        return Matrix(matrix);
    def __rmul__(self, re):
        re, im = self.real * re, self.imag * re;
        return Complex(re, im);
    
    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            re, im = self.real - other, self.imag;
        else:
            re = self.real - other.real;
            im = self.imag - other.imag;
        return Complex(re, im);
    def __rsub__(self, re):
        re, im = re - self.real, -self.imag;
        return Complex(re, im);
    
    def __truediv__(self, other):
        try:
            if type(other) is int or type(other) is float:
                re, im = self.real / other, self.imag / other;
            else:
                re = (self.real * other.real + self.imag * other.imag) / other.norm;
                im = (self.imag * other.real - self.real * other.imag) / other.norm;
            return Complex(re, im);
        except ZeroDivisionError:
            mesage = 'The result of the calculation cannot be correctly determined.';
            print('Error :: Division by zero.\n', mesage, sep ='');
            if self.norm == 0:
                return Complex(nan, nan);
            else:
                return Complex(inf, inf);

if __name__ == '__main__':
    from random import randint;
    rnum, rmin, rmax = 5, -100, 100;
    c = [Complex(randint(rmin, rmax), randint(rmin, rmax)) for _ in range(rnum)];
    print(f'{rnum} random complex numbers:\n', *c, sep =' ', end = '\n\n');
    
    a = [c[0].real, c[1].imag, c[2].abs, c[3].angle, c[4].conj()];
    print('Results of "real", "imag", "abs", "angle", and',
          '"conj" functions:\n', *a, sep =' ', end = '\n\n');
    
    cc = c[0] + c[1];
    print(f'{c[0]} + {c[1]} =', cc);
    cc = c[2] + c[3];
    print(f'{c[2]} * {c[3]} =', cc);
    cc = c[0] - c[2];
    print(f'{c[0]} - {c[2]} =', cc);
    cc = c[1] / c[3];
    print(f'{c[1]} / {c[3]} =', cc);
    
    r = randint(rmin, rmax);
    cc = r + c[4];
    print(f'{r} + {c[4]} =', cc);
    r = randint(rmin, rmax);
    cc = r * c[4];
    print(f'{r} * {c[4]} =', cc);
else:
    print('"Complex Numbers" Module.');
