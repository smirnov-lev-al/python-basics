while True:
    days = 1;
    initial_res = float(input('Enter an initial result: '))
    final_res = float(input('Enter a final result: '));
    if initial_res <= 0 or final_res <= 0:
        print('The results should be positive. Please, try again');
    else:
        while initial_res < final_res:
            initial_res *= 1.1;
            days += 1;
        print(f'It takes {days} days to achieve the final result.')
        break;