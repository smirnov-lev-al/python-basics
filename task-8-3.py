class IntFloatValueError(Exception):
    def __init__(self, errorstr = 'Warning :: Invalid string to convert to number.'):
        self.errorstr = errorstr;
    def __str__(self):
        return self.errorstr;
    
def exception_detector(ylist):
    if len(ylist) > 2:
        raise IntFloatValueError();
    else:
        for y in ylist:
            if not y.isdigit():
                raise IntFloatValueError();

qexit = lambda xlist: list(filter(lambda x: x.upper() == 'Q', xlist));

print('Enter numbers, or type "Q" to finish:')
numbers = [];
while True:
    xlist = list(map(lambda x: x.lower(), input().split()));
    if 'q' in xlist:  break;
    for x in xlist:
        try:
            ylist = x.lstrip('-').lstrip('+').split('.');
            exception_detector(ylist);
            numbers.append(x);
        except IntFloatValueError as err:
            print(err);
print(*numbers);