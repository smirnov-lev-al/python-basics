time_in_seconds = int(input('Enter the time in seconds:'));
hours = time_in_seconds // 3600;
minutes = time_in_seconds // 60 - hours * 60;
seconds = time_in_seconds % 60;
print(f'{hours:02}:{minutes:02}:{seconds:02}');