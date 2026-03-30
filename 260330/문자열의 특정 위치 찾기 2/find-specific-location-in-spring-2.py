string = ['apple', 'banana', 'grape', 'blueberry', 'orange']


a = input()

cnt = 0

for item in string:
    if item[2] == a or item[3] == a:
        cnt += 1
        print(item)
        
print(cnt)