# 2. Median Sort
import logging
import sys

#OutputFileName = "7_GCJ/2021/R1B/3_0out.txt"


(T, N, B, P) = [int(i) for i in input().strip().split(" ")]
#file_object = open(OutputFileName, 'w')
for t in range(1, T + 1):

	Arr = [0] * N

	for i in range(N * B):
		n = int(input())
		#file_object.write("IN" + str(n) + "\n")
		if n > 7 or Arr[N-1] == B-1:
			i = 0
			while Arr[i] == B:
				i += 1
			Arr[i] += 1
			#file_object.write(str(i) + "\n")
			print(str(i+1), flush=True)
		else:
			i = 0
			while i < N-1 and Arr[i] >= B - 1:
				i += 1

			j = i
			while j < N-1 and Arr[j] > Arr[j + 1]:
				j += 1

			Arr[j] += 1
			print(str(j+1), flush=True)
			#file_object.write(str(j) + "\n")

			#file_object.write(str(midx) + "\n")
		#file_object.write(str(Arr) + "\n")

	#res = int(input())
	#file_object.write("Complete" + str(res) + "\n")
#file_object.close()

"""
Note:
- N towers, B cublic blocks
- Towers are build bottom-up
- i-th block placed in tower ends up as i-th from bottom
- once placed, blocks cannot be moved

- block faces are facing front
"""