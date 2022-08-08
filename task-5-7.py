import json;

infilename = 'text_7.txt';
outfilename = 'company-profit-analysis.json';

try:
    with open(infilename,  'r', encoding = 'utf-8') as finput, \
         open(outfilename, 'w', encoding = 'utf-8') as foutput:
        cprofit = {fline.split()[0]: float(fline.split()[2]) - \
                   float(fline.split()[3]) for fline in finput};
        positive_profit = [val for val in cprofit.values() if val > 0];
        aprofit = sum(positive_profit) / len(positive_profit);
        fprofit = [cprofit, {'average_profit': round(aprofit, 4)}];
        json.dump(fprofit, foutput, indent = 4, ensure_ascii = False);
except IOError:
    print('Errorr :: Some problem occurs while trying to work with one',
          f'of the following files: "{infilename}" and "{outfilename}".');
except ValueError:
    print('Error :: At least one of the input values is not in a float format.');
