filename = 'info_in.txt';

try:
    finput = open(filename, 'r', encoding = 'utf-8');
    for nline, fline in enumerate(finput):
        numwords = len(fline.strip('\n').split());
        print(f'line {nline + 1} -> {numwords} words');
    print(f'There are {nline + 1} lines in the file "{filename}".')
    print('Each single line in this file contains the shown above number of words.');
except IOError:
    print(f'Errorr :: Some problem occurs while trying to read the file "{filename}".');
except NameError:
    print(f'The file "{filename}" is empty.')
finally:
    finput.close();