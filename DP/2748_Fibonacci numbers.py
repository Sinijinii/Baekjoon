num = int(input())
arr = [0 for _ in range(num+1)]
arr[1] = 1
for i in range(2,num+1):
    arr[i] = arr[i-1]+arr[i-2]
print(arr[-1])