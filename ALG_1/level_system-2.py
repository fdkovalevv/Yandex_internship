def solve_linear_system(a, b, c, d, e, f):
    # Calculate the determinant of the coefficient matrix
    det_A = a * d - b * c

    # Check for singular matrix (determinant is zero)
    if det_A == 0:
        # Check for infinitely many solutions or no solution
        if e == 0 and f == 0:
            # Infinitely many solutions of the form y = kx + b
            k = -c / d
            b = f / d
            return 1, k, b
        elif a == 0 and b == 0:
            # Infinitely many solutions of the form x = x0, y - any
            x0 = e / a
            return 3, x0
        elif c == 0 and d == 0:
            # Infinitely many solutions of the form y = y0, x - any
            y0 = f / d
            return 4, y0
        else:
            # No solution
            return 0
    else:
        # Unique solution
        x = (e * d - b * f) / det_A
        y = (a * f - e * c) / det_A
        return 2, x, y

# Example usage:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
result = solve_linear_system(a, b, c, d, e, f)
print(result)