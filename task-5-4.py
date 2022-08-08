splitstr = ' - ';
infilename = 'text_4.txt';
#infilename = 'text_4_en.txt';
outfilename = 'text_4_ru.txt';

enru_cardinal_numerals = \
    {0: ['zerro', 'ноль'], 1: ['one', 'один'], 2: ['two', 'два'], \
     3: ['three', 'три'], 4: ['four', 'четыре'], 5: ['five', 'пять'], \
     6: ['six', 'шесть'], 7: ['seven', 'семь'], 8: ['eight', 'восемь'], \
     9: ['nine', 'девять'], 10: ['ten', 'десять'], 11: ['eleven', 'одиннадцать'], \
     12: ['twelve', 'двенадцать'], 13: ['thirteen', 'тринадцать'], 14: ['fourteen', 'четырнадцать'], \
     15: ['fifteen', 'пятнадцать'], 16: ['sixteen', 'дцать'], 17: ['seventeen', 'семнадцать'], \
     18: ['eightteen', 'восемнадцать'], 19: ['nineteen', 'девятнадцать'], 20: ['twenty', 'двадцать']};

enru_ordinal_numerals = \
    {0: ['zero', 'нулевой'], 1: ['first', 'первый'], 2: ['second', 'второй'],
     3: ['third', 'третий'], 4: ['fourth', 'четвертый'], 5: ['fifth', 'пятый'], \
     6: ['sixth', 'шестой'], 7: ['seventh', 'седьмой'], 8: ['eighth', 'восьмой'], \
     9: ['ninth', 'девятый'], 10: ['tenth', 'десятый'], 11: ['eleventh', 'одиннадцатый'], \
     12: ['twelfth', 'двенадцатый'], 13: ['thirteenth', 'тринадцатый'], 14: ['fourteenth', 'четырнадцатый'], \
     15: ['fifteenth', 'пятнадцатый'], 16: ['sixteenth', 'шестнадцатый'], 17: ['seventeenth', 'семнадцатый'], \
     18: ['eightteenth', 'восемнадцатый'], 19: ['nineteenth', 'девятнадцатый'], 20: ['twentieth', 'дванадцатый']};

try:
    with open(infilename, 'r', encoding = 'utf-8') as finput:
         enrudict = [[*enru_cardinal_numerals[int(a.strip('\n').split(splitstr)[1])], a.strip('\n').split(splitstr)[1]] \
                     for a in finput if a.split(splitstr)[0].lower() == enru_cardinal_numerals[int(a.strip('\n').split(splitstr)[1])][0]];
    with open(outfilename, 'w', encoding = 'utf-8') as foutput:
        for numeral in enrudict:
            print(numeral[0].capitalize(), numeral[1].capitalize(), numeral[2], sep = ' - ');
            print(numeral[1].capitalize(), numeral[2], sep = ' - ', file = foutput);
except IOError:
    print('Errorr :: Some problem occurs while trying to work with files.');
except ValueError:
    print('Error :: At least one of the input employee salary values is not in a float format.');
