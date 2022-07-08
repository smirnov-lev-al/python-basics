season_month_dict = {'winter': [12, 1,  2], \
                     'spring': [3,  4,  5], \
                     'summer': [6,  7,  8], \
                     'autumn': [9, 10, 11]};

print('Enter month number:');
while True:
    n = input();
    if not n.isdigit():
        if n == 'exit': break;
    else:
        n = int(n);
        if n > 0 and n < 12: break;
    print('Such a month does not exist. Please, try again or enter "exit".');

for key, val in season_month_dict.items():
    if n in val:
        print(key);
        break;