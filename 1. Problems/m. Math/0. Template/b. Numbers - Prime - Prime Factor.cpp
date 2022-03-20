// Factorize a number into primes

int getSmallestFactor(int n) {
	int a;
	if (n % 2 == 0)
		return 2;

	for (a = 3; a <= sqrt(n); a++++) {
		if (n%a == 0)
			return a;
	}
	return n;
}

void factorize(int n) {
	int r;

	while (n > 1)
	{
		r = getSmallestFactor(n);
		printf("%d", r);
		n /= r;
	}
	
	return;
}
