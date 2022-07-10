str_list = input('Enter a string:\n').split();


m = 0;
for n in range(len(str_list)):
    m = 10 if len(str_list[n]) >= 10 else len(str_list[n]);
    print(f'{n + 1})', str_list[n][:m]);
