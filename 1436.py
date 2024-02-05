N = int(input())
i = 666
count = 0
result = 0
while True:
    if '666' in str(i):
        count += 1
        result = i
        i+=1
    else: i+=1
    if count == N:
        break
print(result)