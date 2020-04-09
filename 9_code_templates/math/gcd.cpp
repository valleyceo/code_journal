// time complexity - O(logx + logy)
long long Gcd(long long x, long long y) {
	if (x > y){
		return Gcd(y, x);
	} else if (x == 0) {
		return y;
	} else if (!(x & 1) && !(y & 1)) { // both are even
		return Gcd(x >> 1, y >> 1) << 1;
	} else if (!(x & 1) && y & 1) {
		return Gcd(x >> 1, y);
	} else if (x & 1 && !(y & 1)) {
		return Gcd(x, y >> 1);
	}

	return Gcd(x, y - x);
}

// euclidean algorithm - O(log max(x, y)), or O(n) where n is number of bits in input
long long Gcd(long long x, long long y) { return y == 0 ? x : Gcd(y, x % y); }