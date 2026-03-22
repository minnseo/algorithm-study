a, b, c = map(int, input().split())

if a > b:
    if c > a:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else:   # b > a
    if c > b:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)


# nums = list(map(int, input().split()))

# nums.sort()

# print(nums[1])