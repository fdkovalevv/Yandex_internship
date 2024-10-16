def increasing(arr):
    for i in range(len(arr) - 1):
        if (arr[i] >= arr[i + 1]):
            return "NO"
    return "YES"

arr = list(map(int, input().split()))
print(increasing(arr))
