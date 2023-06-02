# Enter your code here. Read input from STDIN. Print output to STDOUT

n = 5
X_Y = [map(int, input().split()) for _ in range(n)]

sum_X, sum_Y, sum_X2, sum_XY = map(sum, zip(*[(x, y, x**2, x * y) for x, y in X_Y]))

b = (n*sum_XY - sum_X*sum_Y)/(n*sum_X2 - sum_X**2)
a = (sum_Y/n) - b*(sum_X/n)

print(round(a + b*80, 3))
