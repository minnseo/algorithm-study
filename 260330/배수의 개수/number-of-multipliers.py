three_s = 0
five_s = 0

for _ in range(10):
    num = int(input())
    if num % 3 == 0:
        three_s += 1
    if num % 5 == 0:
        five_s += 1

print(three_s, five_s)
