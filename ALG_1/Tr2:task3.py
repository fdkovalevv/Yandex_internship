n = int(input())
arr = list(map(int, input().split()))
k = int(input())
diff = 10**9
closest = 0
for i in arr:
    if diff > abs(i-k):
        diff = abs(i-k)
        closest = i
print(closest, diff)