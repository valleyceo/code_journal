# Rectangle Mania

'''
Given a list of cartesian coordinate, return how many 4-points can from a rectangle
'''
def rectangleMania(coords):
	cache = set()
	res = 0
	
	for coord in coords:
		cache.add((coord[0], coord[1]))
	
	for i in range(len(coords)):
		for j in range(i + 1, len(coords)):
			if hasSameAxis(coords[i], coords[j]):
				continue
			
			if coords[i][0] < coords[j][0]:
				p1 = coords[i]
				p2 = coords[j]
			else:
				p1 = coords[j]
				p2 = coords[i]
			
			if p1[1] > p2[1]:
				continue
			
			if (coords[i][0], coords[j][1]) in cache and (coords[j][0], coords[i][1]) in cache:
				res += 1

	return res

def hasSameAxis(point1, point2):
	return point1[0] == point2[0] or point1[1] == point2[1]