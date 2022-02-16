import sys

def CountNum(n: int, n2: int):
	curr = n
	new = n2
	count = 0
	tens = 1

	while curr >= new:
		count += 1
		tens *= 10
		new = n2 * tens + n % tens

		if (curr == new and n % 10 < 9):
			new += 1
		elif (curr == new and n % 10 == 9):
			new = n2 * (tens * 10)
			count += 1
			
	if curr < (n2 * tens):
		return [n2 * tens, count]
	else: 
		return [new, count]

T = int(input())

for t in range(1, T + 1):
	X = int(input())
	NC = [int(x) for x in input().strip().split(" ")]
	res = 0
	prev = NC[0]

	for i in range(1, len(NC)):
		[new, count] = CountNum(prev, NC[i])
		prev = new
		res += count
		print(new, count)

	print("Case #{}: {}".format(t, res))