arr = list(map(int, input().split()))
arr.insert(0, 10**9)
arr.append(10**9)
count = 0
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1
print(count)