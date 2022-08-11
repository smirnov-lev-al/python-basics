class Worker:
    def __init__(self, name, surname, position, wage, bonus):
       self.name, self.surname, self.position = name, surname, position;
       self._income = {'wage': wage, 'bonus': bonus};

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}';
    
    def get_total_income(self):
        return sum(self._income.values());

developers = [];
developers.append(Position('Michael', 'Thoennessen', 'junior developer', 60000, 20000));
developers.append(Position('Jessica', 'Thomas', 'middle developer', 90000, 30000));

for n, d in enumerate(developers):
    print(f'\n\033[4m\033[35mDeveloper {n+1}\033[0m');
    print('Full Name:', d.get_full_name());
    print('Total Income:', d.get_total_income());
