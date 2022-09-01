class Date:
    __months = {'january': [1, 31], 'february': [2, 28], 'march': [3, 31],
                'april': [4, 30], 'may': [5, 31], 'june': [6, 30],
                'july': [7, 31], 'august': [8, 31], 'september': [9, 30],
                'october': [10, 31], 'november': [11, 30], 'december': [12, 31]};
    __starting_date = '01-01-000';
    __clsdate = __starting_date;
    
    def __init__(self, date : str):
        self.__objdate = Date.__starting_date;
        self.date = date;
    
    @property
    def date(self):
        return [self.__objdate, Date.__clsdate];
    @date.setter
    def date(self, date : str):
        date_format, date_range = Date.validation(date);
        dints = Date.extraction(date, console_output = False);
        if dints is not None:
            day = str(dints[0]) if dints[0] > 9 else ('0' + str(dints[0]));
            month = str(dints[1]) if dints[1] > 9 else ('0' + str(dints[1]));
            year = str(dints[2]);
            self.__objdate = day + '-' + month + '-' + year;
            if date_range:  Date.__clsdate = self.__objdate;
        else:
            print('Error :: Invalid date format. The current date does not change.');
    
    @classmethod
    def extraction(cls, *args, console_output = True):
        date = args[0] if len(args) > 0 else cls.__clsdate;
        date_format, date_range = cls.validation(date);
        if type(date) == str and date_format:
            dstrs = date.split('-');
            if dstrs[1] in Date.__months.keys():
                dstrs[1] = Date.__months[dstrs[1]][0];
            dints = list(map(int, dstrs));
            if console_output and date_range == False:
                print('Warning :: At least one of the integers',
                          'defining the date is out of range.');
            return dints;
        else:
            if console_output:
                print('Error :: The date format is incorrect.');
            return None;
    
    @staticmethod
    def validation(*args):
        date = args[0] if len(args) > 0 else Date.__clsdate;
        if type(date) == str and len(date.split('-')) == 3:
            dlist = date.split('-');
        elif type(date) == list and len(date) == 3:
            dlist = date.copy();
        else:
            return False, False;
        if dlist[1] in Date.__months.keys():
            dlist[1] = Date.__months[dlist[1]][0];
        try:
            dints = list(map(int, dlist));
            if dints[2] > 0 and dints[0] > 0 and\
               dints[1] > 0 and dints[1] < 13:
                numdays = [d[1] for d in Date.__months.values()][dints[1] - 1];
                if numdays == 28 and dints[2] % 4 == 0:  numdays += 1;
                if dints[0] < numdays + 1:
                    return True, True;
                else:
                    return True, False;
            else:
                return True, False;
        except ValueError:
            return False, False;

if __name__ == '__main__':
    dates = ['15-10:1987', '25a10-1987', '12-may-2000', '29-02-2008',
             [21, 4, 2024], '02-15-2017', '45-august-1997'];
    for date in dates:
        print(f'{date}:');
        print('Validation:', Date.validation(date));
        print('Extraction:', Date.extraction(date), end = '\n\n');
    
    objdate = Date('04-may-2000');
    print(f'Object date is {objdate.date[0]}.');
    print('Validation:', objdate.validation(objdate.date[0]));
    print('Extraction:', objdate.extraction(objdate.date[0]));
    print(f'Class date is {objdate.date[1]}.');
    print('Validation:', objdate.validation());
    print('Extraction:', objdate.extraction(), end = '\n\n');
    
    dates = ['15-10:1987', '25a10-1987', '5-05-1985',
             '35-14-2021', '02-15-2017', '45-august-1997'];
    for date in dates:
        objdate.date = date;
        print(f'Object date is {objdate.date[0]}.');
        print('Validation:', objdate.validation(objdate.date[0]));
        print('Extraction:', objdate.extraction(objdate.date[0]));
        print(f'Class date is {objdate.date[1]}.');
        print('Validation:', objdate.validation());
        print('Extraction:', objdate.extraction(), end = '\n\n');
else:
    print('Date Module.');
