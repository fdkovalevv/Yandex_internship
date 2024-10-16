left = 30.0
right = 4000.0
n = int(input())
prev = float(input())
for i in range(1, n):
    f, s = input().strip().split()
    current = float(f)
    middle = (prev+current)/2.0
    diff = current-prev
    if abs(diff) < 10**-6:
        continue
    if s == 'closer':
        if diff > 0:
            left = max(left, middle)
        else:
            right = min(right, middle)
    elif s == 'further':
        if diff < 0:
            left = max(left, middle)

        else:
            right = min(right, middle)
    prev = current
print(f"{left:.1f} {right:.1f}")
