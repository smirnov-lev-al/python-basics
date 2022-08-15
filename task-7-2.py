from abc import ABC, abstractmethod;

class Сlothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass;

class Coat(Сlothes):
    def __init__(self, csize):
        self.__size = csize;
        self.__fabric_consumption = 0;
    
    @property
    def size(self):
        return self.__size;
    @size.setter
    def size(self, csize):
        self.__size = csize;

    @property
    def fabric_consumption(self):
        self.__fabric_consumption = self.size / 6.5 + 0.5;
        return self.__fabric_consumption;
    @fabric_consumption.setter
    def fabric_consumption(self, cconsumption):
        self.__fabric_consumption = cconsumption;
        self.size = 6.5 * (cconsumption - 0.5);

class Suit(Сlothes):
    def __init__(self, sheight):
        self.__height = sheight;
        self.__fabric_consumption = 0;
    
    @property
    def height(self):
        return self.__height;
    @height.setter
    def height(self, cheight):
        self.__height = cheight;

    @property
    def fabric_consumption(self):
        self.__fabric_consumption = 2. * self.height + 0.3;
        return self.__fabric_consumption;
    @fabric_consumption.setter
    def fabric_consumption(self, sconsumption):
        self.__fabric_consumption = sconsumption;
        self.height = 0.5 * (sconsumption - 0.3);

try:
    size, height = map(float, input('Enter a coat size and a suit height:\n').split());
    coat = Coat(size);
    suit = Suit(height);
    print('The total fabric consumption is',
          f'{coat.fabric_consumption + suit.fabric_consumption}.');
except ValueError:
    print('Error :: At least one of the input values is not in a float format.');