filename = 'text_6.txt';

subjects = {};
try:
    with open(filename, 'r', encoding = 'utf-8') as finput:
        for fline in finput:
            sname, sinfo = fline.split(':');
            shours = ''.join([ichar for ichar in sinfo if ichar == ' ' or ichar.isdigit()]);
            subjects[sname] = sum(map(int, shours.split()));
    print(subjects);
except IOError or ValueError:
    print('Errorr :: Some problem occurs while trying to read the file "{filename}".\n');