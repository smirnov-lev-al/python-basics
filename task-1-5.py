revenue = float(input('Enter revenue: '));
costs = float(input('Enter costs: '));
dif = revenue - costs;

if dif > 0:
    print(f'The is {dif}.');
    print(f'The profitability is {100 * dif / costs:.2f}%.');
    n = int(input('Enter number of staff: '));
    print(f'The profit per staff is {dif / n:.2f}.');
elif dif < 0:
    print(f'The loss is {- dif}.');
else:
    print('The revenue and costs are equal.');