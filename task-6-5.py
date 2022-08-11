class Stationery:
    def __init__(self, title = ''):
       self.title = title;
       
    def draw(self):
        print(f'Start drawing with {self.title} stationery.');
    
class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title } pen.');

class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title } pencil.');

class Marker(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title } marker.');

stationery = Stationery('Unknown');
pen = Pen('Parker');
pencil = Pencil('Koh-i-Noor');
marker = Marker('Faber-Castell');

office_tools = [stationery, pen, pencil, marker];

for tool in office_tools:
    tool.draw();