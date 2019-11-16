import sys
N = int(input())
# S = list(map(str,input().split()))
S = list(input())
if N % 2 == 0:
	T_1 = S[:int(len(S)/2)]
	T_2 = S[int(len(S)/2):]
	print(T_1)
	print(T_2)
	for i in range(len(T_1)):
		if T_1[i] != T_2[i]:
			print("No")
			sys.exit()	
	print("Yes")
	sys.exit()
else:
	print("No")