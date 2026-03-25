string = input()
str_lst = list(string)

str_lst[1] = 'a'
str_lst[-2] = 'a'

string = ''.join(str_lst)

print(string)