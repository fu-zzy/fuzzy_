import string
N = int(input())
S = list(str(input()))
alpha = list(ascii_uppercase)
L = list()
for i in range(len(S)):
	L.append(alpha[(alpha.index(S[i])+N)%26])
print(''.join(L))