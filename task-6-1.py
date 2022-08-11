from time import sleep;
from itertools import cycle;

class TrafficLight:
    __color = [[('red',    '\033[1m\033[34m\033[41m'), 7],\
               [('yellow', '\033[1m\033[34m\033[43m'), 2],\
               [('green',  '\033[1m\033[34m\033[42m'), 7],
               [('yellow', '\033[1m\033[34m\033[43m'), 2]];
    
    def running(self, max_num_switching = None):
        switchoff_style = '\033[1m\033[30m\033[40m';
        num_switching = 0;
        for color_lag in cycle(TrafficLight.__color):
            rstyle = color_lag[0][1] if color_lag[0][0] == 'red' else switchoff_style;
            gstyle = color_lag[0][1] if color_lag[0][0] == 'green' else switchoff_style;
            ystyle = color_lag[0][1] if color_lag[0][0] == 'yellow' else switchoff_style;
            print(f'\r{rstyle}(  red  )\033[0m',
                  f' {ystyle}( yellow )\033[0m',
                  f' {gstyle}( green )\033[0m', end = ' ');
            sleep(color_lag[1]);
            num_switching += 1;
            if max_num_switching is not None and num_switching > max_num_switching:  break;


traffictight = TrafficLight();
traffictight.running(50);
