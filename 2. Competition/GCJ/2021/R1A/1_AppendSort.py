T = int(input())

for t in range(1, T + 1):
	N = int(input())
	X = input().strip().split()
	res = 0
	curr = list(X[0])

	for i in range(1, len(X)):
		prev = curr
		curr = list(X[i])

		if len(curr) > len(prev):
			continue

		digit_diff = len(prev) - len(curr)
		min_len = len(curr)
		res += digit_diff

		if curr[:min_len] < prev[:min_len]:
			curr.append([0] * (digit_diff + 1))
		elif curr[:min_len] > prev[:min_len]:
			curr.append([0] * (digit_diff))
		else:
			if digit_diff != 0 and int("".join(prev[len(curr):])) + 1 < 10**(digit_diff):
				print(str(int("".join(prev[len(curr):])) + 1))
				curr.extend(list(str(int("".join(prev[len(curr):])) + 1)))
			else:
				curr.extend([0]*digit_diff)
				res += 1

	print("Case #{}: {}".format(t, res))
