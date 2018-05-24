c = 10
n = 5
w = [0,7,4,6,8]
v = [0,100,50,60,70]
m = [[0] * (c+1) for row in range(n)]
for i in range(n):
	for j in range(c+1):
		if j >= w[i]:
			m[i][j] = max(m[i-1][j], m[i-1][j-w[i]]+v[i])
		else:
			m[i][j] = m[i-1][j]

print(m)
