# 2. Median Sort
import logging
import sys

#utputFileName = "7_GCJ/2021/R0/4_0out.txt"

(T, N, Q) = [int(i) for i in input().strip().split(" ")]
#file_object = open(OutputFileName, 'w')

for t in range(1, T + 1):
	
	def binarySearch(L:list, newVal:int):
		start = 0
		end = len(L)-1
		mid = -1

		#file_object.write(str(L) + "\n")
		while(start < end):
			mid = (end + start)//2
			
			# interact
			print("{} {} {}".format(L[mid], L[mid+1], newVal) , flush=True)
			n = int(input())

			#file_object.write(str(L) +"{} {} {} {}".format(L[mid], L[mid+1], newVal, n) + "\n")
			if mid == 0 and n == L[0]:
				#file_object.write("A" + str(L) + str(mid) + str(n) + "\n")
				L.insert(start, newVal)
				return
			elif mid == len(L)-2 and n == L[-1]:
				#file_object.write("B" + str(L) + str(mid) + str(n) + "\n")
				L.insert(len(L), newVal)
				return

			if n == newVal:
				#file_object.write("C" + str(L) + str(mid) + str(n) + "\n")
				L.insert(mid+1, newVal)
				return
			elif n == L[mid]:
				end = mid
			else:
				start = mid + 1

		#file_object.write("D" + str(L) + str(n) + "\n")
		L.insert(mid, newVal)
		return

	print("1 2 3", flush=True)
	n = int(input())
	
	if n == 1:
		order = [2, 1, 3]
	elif n == 2:
		order = [1, 2, 3]
	else:
		order = [1, 3, 2]

	#file_object.write(str(order) + "\n")
	#print("1 2 3", flush=True)
	#n = int(input())
	#file_object.write(str(n) + "\n")

	for i in range(4, N+1):
		#print("HELLO"+str(n), file=sys.stderr)
		binarySearch(order, i)

	#file_object.write(str(order) + "\n")
	x = " ".join([str(i) for i in order])
	

	print(x, flush=True)
	n = int(input())

#file_object.close()