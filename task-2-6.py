def isint(istr):
    try:
        int(istr);
        return True;
    except ValueError:
        return False;
def isfloat(fstr):
    try:
        float(fstr);
        return True;
    except ValueError:
        return False;

dict_statistics = {};
print('Enter product characteristics:');
while True:
    dict_keys = input().split();
    if dict_keys == []:   break;
    for key in dict_keys:
        dict_statistics[key] = None;
print(dict_statistics);

n, products_info = 0, [];
while True:
    answer = input('Do you want to enter a new product information? (yes/no)\n');
    if answer == 'yes':
        n += 1;
        for key in dict_statistics.keys():
            val = input(f'{key}: ');
            if isint(val):
                dict_statistics[key] = int(val);
            elif isfloat(val):
                dict_statistics[key] = float(val);
            else:
                dict_statistics[key] = val;
        products_info.append((n, dict_statistics.copy()));
    elif answer == 'no':
        for key in dict_statistics.keys():
            dict_statistics[key] = [];
        break;
    else:
        print('Please, try again to answer the question.');
print(products_info);

for i in range(n):
    for key, val in products_info[i][1].items():
        dict_statistics[key].append(val);
print(dict_statistics);
