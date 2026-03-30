string = ['apple', 'banana', 'grape', 'blueberry', 'orange']


a = input()

cnt = 0

for word in string:
    if word[2] == a or word[3] == a:
        cnt += 1
        print(word)

print(cnt)