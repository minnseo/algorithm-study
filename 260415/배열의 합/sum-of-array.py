arr = [map(int, input().split()) for _ in range(4)]

for row in arr:
    s = 0
    for i in row:
        s += i
    print(s)