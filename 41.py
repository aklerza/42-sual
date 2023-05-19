arr=list(map(int, input().split()))
cem = 0
for i in arr:
    for j in str(i):
        cem+=int(j)
print(cem/3)