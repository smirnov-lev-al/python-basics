from sys import argv;

def salary_calc(hours, rate_per_hour, award):
    salary = hours * rate_per_hour + award;
    return salary;

if len(argv) < 4:
    print("\nError :: There is not enough data to ",
          "calculate the employee's salary.\n", sep = '');
else:       
    try:
        h, r, a = map(float, argv[1:4]);
        s = salary_calc(h, r, a);
        print(f"\nThe employee's salary is {s}.\n");
    except:
        print("\nError :: At least one of the first three script ",
              "input parameters is not in a numeric format.\n", sep = '');