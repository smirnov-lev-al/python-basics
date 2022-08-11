class Road:
    def __init__(self, length, width):
        self._length = length;
        self._width = width;

    def profit_calc(self, weight, thickeness):
        res = self._length * self._width * weight * thickeness / 1000;
        return res;
    
    def profit_print(self, weight, thickeness):
        res = self.profit_calc(weight, thickeness);
        print(f'\n{self._length}(m) * {self._width}(m) *',
              f'{weight}(kg/(m*m*cm)) * {thickeness}(cm) = {res}(ton)');


try:
    rlength, rwidth = map(float, input('Enter length and width of the road in meter:\n').split());
    aweight, athickeness = map(float, input('Enter asphalt consumption parameters:\n').split());
except:
    print('Error :: At least one of the input values is not in a float format.');
    print('The default parameters are used in the calculations.');
    rlength, rwidth, aweight, athickeness = 20, 5000, 25, 5;

road = Road(rlength, rwidth);
road.profit_print(aweight, athickeness);