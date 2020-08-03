n = int(input())
num = [0, 1, 1]
if n in [1, 2]:
    print(1)
else:
    for j in range(3, n+1):
        num.append(num[j-1]+num[j-2])
    print(num[n])
