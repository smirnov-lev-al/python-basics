#filename = 'info_in.txt';
filename = 'info_out.txt';
print(f'Enter an information that you want to store to the file "{filename}".');

try:
    with open(filename, 'a', encoding = 'utf-8') as foutput:
        while True:
            istr = input();
            if len(istr) == 0:  break;
            #foutput.write(istr + '\n');
            print(istr, file = foutput);
    print(f'This information was successfully added to the file named "{filename}".');
except IOError:
    print(f'Errorr :: Some problem occurs while trying to work with the file "{filename}".');
