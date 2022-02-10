import sys

class Solution:

	def FindBestAns(self, nv, l):
		TArr = [0] * l
		TArrDen = [0] * l
		FArr = [0] * l
		FArrDen = [0] * l

		for s, v in nv:
			print(s,v,nv)
			for i in range(l):
				if s[i] == 'T':
					TArr[i] += v
					FArr[i] += l-v
				else:
					FArr[i] += v
					TArr[i] += l-v

		for i in range(l):
			FArr[i] /= len(nv)
			FArrDen[i] /= len(nv)
			TArr[i] /= len(nv)
			TArrDen[i] /= len(nv)

		res = ""
		val = 0
		valDen = 0
		print(TArr)
		print(FArr)
		for i in range(l):
			if TArr[i] >= FArr[i]:
				res += 'T'
				val += FArr[i]/TArr[i]
				valDen += FArr[i]
			else:
				res += 'F'
				val += FArr[i]/TArr[i]

		return [res, val, valDen]

	

obj = Solution()
T = int(input())

for t in range(1, T + 1):
	NC = [int(x) for x in input().strip().split(" ")]
	Test = []
	for i in range(NC[0]):
		NV = [x for x in input().strip().split(" ")]
		Test.append([NV[0], int(NV[1])])

	[res, val, den] = obj.FindBestAns(Test, NC[1])
	print("Case #{}: {} {}/{}".format(t, res, val, den))