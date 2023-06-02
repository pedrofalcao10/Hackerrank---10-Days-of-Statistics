# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rank_X = [sorted(X).index(i) for i in X]
rank_Y = [sorted(Y).index(i) for i in Y]

r_XY = 1 - 6*sum([(rank_X[i] - rank_Y[i])**2 for i in range(n)])/(n*(n**2 -1))

print(round(r_XY, 3))