n = int(input())
arr = list(map(int, input().split()))

even = []

for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])

even.reverse()
for j in even:
    print(j, end = ' ')