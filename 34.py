arr=list(map(int, input().split()))
data1=[i for i in arr if i>0]
print(sum(data1), len(arr)-len(data1))
