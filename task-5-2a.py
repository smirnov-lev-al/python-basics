filename = 'info_in.txt';

try:
    finput = open(filename, 'r', encoding = 'utf-8');
    flines = finput.readlines();
    finput.close();
    if len(flines) == 0:
        print(f'The file "{filename}" is empty.')
    else:
        print(f'There are {len(flines)} lines in the file "{filename}".')
        print('Each single line in this file contains the following number of words:');
        for nline, fline in enumerate(flines):
            fline = fline.strip('\n');
            numwords = len(fline.split());
            print(f'line {nline + 1} -> {numwords} words');
except IOError:
    print(f'Errorr :: Some problem occurs while trying to read the file "{filename}".');