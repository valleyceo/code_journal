import sys
from itertools import permutations

def Nd2Deg(nd):
	return nd/12*1e-10

def Deg2Nd(deg):
	return deg*12*1e10

def IsValid(hr, m, sec):
	
	if m != (hr % Deg2Nd(30)) * 12:
		return False

	if sec != (m % Deg2Nd(6)) * 60:
		return False

	return True

def IsValidSecSearch(hr, m, sec):
	maxDeg = min(hr, m, sec)

	for i in range(0, 72000):
		hr2 = hr + Deg2Nd(i/1200) - maxDeg
		m2 = m + Deg2Nd(i/1200) - maxDeg
		sec2 = sec + Deg2Nd(i/1200) - maxDeg
		#print(hr2, m2, sec2)
		if IsValid(hr2, m2, sec2):
			return GetTime(hr2, m2, sec2)

	return []

def GetTime(hr, m, sec):
	hour = int(hr / Deg2Nd(30))
	minute = int(m / Deg2Nd(6))
	second = int(sec / Deg2Nd(6))
	nanosecond = int(sec % Deg2Nd(6))
	return (hour, minute, second, nanosecond)

T = int(input())

for t in range(1, T + 1):
	H = [int(x) for x in input().strip().split(" ")]
	res = []
	for p in permutations(H):
		if IsValid(p[0], p[1], p[2]):
			res = GetTime(p[0], p[1], p[2])

	if len(res) == 0:
		for p in permutations(H):
			res = IsValidSecSearch(p[0], p[1], p[2])
			if len(res) == 4:
				break

	if len(res) == 4:
		print("Case #{}: {} {} {} {}".format(t, res[0], res[1], res[2], res[3]))
	else:
		print("Case #{}: 0 0 0 -1".format(t))



"""
Note:
- 3 Hands in clock (hr, min, sec), you don't konw which is which
- Input: 3 integers, represent angles
- 1 tick equals 1/12*e-10 deg
- each nanosecond = 1 tick (hr) = 12 ticks (min) = 720 ticks (sec)

- Output: 
	- h(full hours since midnight)
	- m(full min since last full hr)
	- s(full sec since last full min)
	- n(full nanosec since last full second)
"""
