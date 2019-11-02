N = list(map(int,input()))
target = ''.join(map(str,N))
if N[0]*111 < int(target):
	print((N[0]+1)*111)
else:
	print(N[0]*111)