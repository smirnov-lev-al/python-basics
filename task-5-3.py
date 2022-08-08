filename = 'text_3.txt';
salary_border = 20000.0;

try:
    with open(filename, 'r', encoding = 'utf-8') as finput:
         salary = {fline.split()[0] : float(fline.strip('\n').split()[1]) for fline in finput};
    names = [key for key, val in salary.items() if val < salary_border];
    print(f'The following employees have a salary of less than {salary_border}:');
    print(*names, sep = ', ', end = '.\n\n');
    average_salary = round(sum(salary.values()) / len(salary.values()), 4);
    print(f'The average employee salary if {average_salary}.')
except IOError:
    print(f'Errorr :: Some problem occurs while trying to read the file "{filename}".');
except ValueError:
    print('Error :: At least one of the input employee salary values is not in a float format.');
except ZeroDivisionError:
    print('Error :: Division by zero.');
