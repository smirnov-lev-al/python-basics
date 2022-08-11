class Car:
    _directions = {'unknown': 8597,\
                   'north': 8593, 'northeast': 8599, 'east': 8594, 'southeast': 8600,\
                   'south': 8595, 'southwest': 8601, 'west': 8592, 'northwest': 8598};
    
    def __init__(self, name, color, speed, direction, police_lable = False):
        self.name = name;
        self.color = color;
        self.speed = speed;
        self.is_police = police_lable;
        if self.speed  == 0:
            self.direction = ['at rest', chr(8596)];
        else:
            self.set_direction(direction);
    
    def set_direction(self, direction):
        if direction in Car._directions.values():
            dd = list(filter(lambda d: d[1] == 8593, Car._directions.items()))[0];
            self.direction = [dd[0], chr(dd[1])];
        elif direction.lower() in Car._directions.keys():
            self.direction = [direction.lower(), chr(Car._directions[direction])];
        else:
            self.direction = ['unknown', chr(8597)];
        return self.direction;
    
    def stop(self):
        self.speed = 0;
        self.direction = ['at rest', chr(8596)];
        print(f'{self.name} is at rest. \033[1m\033[35m  {self.direction[1]}  \033[0m');
        return self.speed, self.direction;
    
    def go(self, speed = None, direction = None):
        if speed is not None:
            self.speed = speed;
        if self.speed == 0:
            self.stop();
        else:
            if direction is not None:
                self.set_direction(direction);
            print(f'{self.name} is moving at the speed {self.speed}(km/h).');
            print(f'The motion direction is {self.direction[0]}.',
                  f'\033[1m\033[35m  {self.direction[1]}  \033[0m');
        return self.speed, self.direction;
    
    def turn(self, direction):
        if self.speed  == 0:
            self.stop();
        else:
            d = self.direction.copy();
            self.set_direction(direction);
            print(f'{self.name} turns from {d[0]} to {self.direction[0]}.',
                  f'\033[1m\033[36m  {d[1]} \033[1m\033[35m {self.direction[1]}  \033[0m');
        return self.direction;

    def show_speed(self):
        print(f'The seep of {self.name} is {self.speed}(km/h).');
        return self.speed;

class TownCar(Car):
    __max_speed = 60;
    
    def show_speed(self):
        if super().show_speed() > TownCar.__max_speed:
            message = 'Attention :: This car have to move at the seed less then {TownCar.__max_speed}(km/h).';
        else:
            message = 'The speed of this car is within acceptable limits.';
        return message;

class WorkCar(Car):
    __max_speed = 40;

    def show_speed(self):
        if super().show_speed() > WorkCar.__max_speed:
            message = 'Attention :: This car have to move at the seed less then {WorkCar.__max_speed}(km/h).';
        else:
            message = 'The speed of this car is within acceptable limits.';
        return message;

class SportCar(Car):
    pass;

class PoliceCar(Car):
    def __init__(self, name, color, speed, direction):
        police_lable = True;
        super().__init__(name, color, speed, direction, police_lable);


policecar = PoliceCar('Volkswagen', 'red', 60, 'northeast');
policecar.turn('southeast');

print();
towncar = TownCar('Volvo', 'green', 55, 'north');
towncar.go();
print(towncar.show_speed());

print();
workcar = WorkCar('Kia', 'blue', 50, 'northwest');
print(workcar.show_speed());
towncar.stop();
