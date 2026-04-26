month, date, year = map(int, input().split('-'))

if 1 <= year <= 2021 and 1 <= month <= 12 and 1 <= date <= 28: 
    print(year, month, date, sep = '.')