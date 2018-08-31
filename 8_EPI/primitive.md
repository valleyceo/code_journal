# Primitive

<details>
<summary> Count 1s in bit </summary>

```cpp
while (x) {
	ct += x & 1;
	x >> = 1;
}
// complexity O(n)
```
</details>
<details>
<summary> Parity of number </summary>
Refers to whether it contains odd or even number of 1-bits  
ex1. 1101 -> 3 1's -> parity = 0 (odd)  
ex2. 1100 -> 2 1's -> parity = 1 (even)  

```cpp
while (x) {
	result ^= 1;
	x &= (x-1);
}
// complexity (O(k), k = number of 1's)

short Parity(unsigned long x) {
	x ^= x >> 32;
	x ^= x >> 16;
	x ^= x >> 8;
	x ^= x >> 4;
	x ^= x >> 2;
	x ^= x >> 1;
	return x & 0x1;
}
// complexity O(log(n))
```
</details>
<details>
<summary> Swap bits </summary>

```cpp
long SwapBits(long x, int i, int j) {
	// check if x[i] and x[j] is different (if equal, swap is not needed)
	if (((x >> i) & 1) != ((x >> j) & 1)) {
		unsigned long bit_mask = (1L << i) | (1L << j);
		x ^= bit_mask;
	}

	return x;
}
// complexity O(1)
```
</details>
<details>
<summary> Reverse bits </summary>

```cpp
unsigned long ReverseBits(unsigned long x) {
	const int kMaskSize = 16;
	const int kbitMask = 0xFFFF;

	return precomputed_reverse[ x 					& kBitMask] << (3 * kMaskSize) |
		   precomputed_reverse[(x >> 	 kMaskSize) & kBitMask] << (2 * kMaskSize) |
		   precomputed_reverse[(x >> 2 * kMaskSize) & kBitMask] << ( 	kMaskSize) |
		   precomputed_reverse[(x >> 3 * kMaskSize) & kBitMask];
		   
}
// used lookup table (precomputed_reverse), hard coded
// complexity O(n/L)
```
</details>
<details>
<summary> Closest integer with same weight (number of 1's) </summary>

```cpp
// ex1. 10 -> 01
// ex2. 1011 -> 111
// ex3. 111 -> 1011
unsigned long ClosestIntSameBitCount(unsigned long x) {
	const static int kNumUnsignedBit = 64;
	// loop through from LSB (least significant binary, right side)
	for (int i = 0; i < kNumUnsignedBit - 1; ++i) {
		// check if current and next are not equal
		if (((x >> i) & 1) != ((x >> (i + 1)) & 1)) {
			x ^= (1UL << i) | (1UL << (i + 1)); // swap using bitmask
			return x;
		}
	}

	throw invalid_argument("All bits are 0 or 1");
}
// complexity O(n)
```
</details>
<details>
<summary> Multiply(need to review) </summary>

```cpp
unsigned long Multiply(unsigned long x, unsigned long y) {
	unsigned long sum = 0;

	while (x) {
		// examines each bit of x
		if (x & 1) {
			sum = Add(sum, y);
		}

		x >>= 1, y <<= 1;
	}

	return sum;
}

unsigned long Add(unsigned long a, unsigned long b) {
	unsigned long sum = 0, carryin = 0, k = 1, temp_a, temp_b = b;

	while (temp_a || temp_b) {
		unsigned long ak = a & k, bk = b & k;
		unsigned long carryout = (ak & bk) | (ak & carryin) | (bk & carryin);
		sum |= (ak ^ bk ^ carryin);
		carryin = carryout << 1, k <<= 1, temp_a >>= 1, temp_b >>= 1;
	}

	return sum | carryin;
}
```
</details>

<details>
<summary> Divide x/y (need to review) </summary>

```cpp
it Divide(int x, int y) {
	int result = 0;
	int power = 32;

	unsigned long long y_power = static_cast<unsigned long long>(y) << power;

	while (x >= y) {
		while (y_power > x) {
			y_power >>= 1;
			--power;
		}

		result += 1 << power;
		x -= y_power;
	}

	return result;
}
```
</details>

<details>
<summary> Compute x^y </summary>

```cpp
double Power(double x, int y) {
	double result = 1.0;
	long long power = y;
	
	if (y < 0) {
		power = -power;
		x = 1.0 / x;
	}

	while (power) {
		if (power & 1) {
			result *= x;
		}

		x *= x;
		power >>= 1;
	}

	return result;
}
// complexity O(n)
```
</details>

<details>
<summary> Reverse digits </summary>

---

Example:  
42 -> 24  
-314 -> -413

---

```cpp
long reverse(int x) {
	long res = 0, x_rem = abs(x);

	while (x_rem) {
		res = res * 10 + x_rem % 10;
		x_rem /= 10;
	}

	return x < 0 ? -result : result;
}
```
</details>


<details>
<summary> Is palindrome </summary>

---

Write a program that takes an integer and determines if that integer's representation as a decimal string is a palindrome.

hint: extract least significant digit and most significant digit.

---

```cpp
bool IsPalindromeNumber(int x) {
	if (x <= 0) {
		return x == 0;
	}

	const int num_digits = static_cast<int>(floor(log10(x))) + 1;
	int msd_mask = static_cast<int> (pow(10, num_digits - 1));
	
	for (int i = 0; i < (num_digits / 2); ++i) {
		if (x / msd_mask != x % 10) {
			return false;
		}

		x %= msd_mask;
		x /= 10;
		msd_mask /= 100;
	}
}
```
</details>


<details>
<summary> Generate Uniform Random Numbers </summary>

---

Implement a random number generator that generates a random integer i (btw a - b inclusive), given a random number generator that produces zero or one with equal probability?

Hint: how would you mimic a 3-side coin with 2-side coin?

---

```cpp
int UniformRandom (int lower_bound, int upper_bound) {
	int number_of_outcomes = upper_bound - lower_bound + 1, res;

	do {
		result = 0;
		for (int i = 0; (1 << i) < number_of_outcomes; ++i) {
			// ZeroOneRandom() is the provided random number generator.
			result = (result << 1) | ZeroOneRandom();
		}
	} while (result >= number_of_outcomes);

	return result + lower_bound;
}
```

---
Note:
- This is equivalent to random int btw 0 - b-a (add a at end).  
- Find the smallest number form of 2^i - 1 that is greater than b-a.  
- Create until a number below b-a is made (all numbers will have equal chance).  

Time complexity: O(log(b-a+1)), each try is O(1)

---
</details>

<details>
<summary> Rectangle Intersection </summary>

---

Write a program which test if two rectangles have a nonempty intersection. If the intersection is nonempty, return the rectangle formed by the intersection

---

```cpp
struct Rectangle {
	int x, y, width, height;
};

bool IsIntersect (const Rectangle& R1, const Rectangle& R2) {
	return R1.x <= R2.x + R2.width && R1.x + R1.width >= R2.x &&
		   R1.y <= R2.y + R2.height && R1.y + R1.height >= R2.y;
}

Rectangle IntersectRectangle(const Rectagle& R1, const Rectangle& R2) {
	if (!IsIntersect(R1, R2))
		return {0, 0, -1, -1};

	return {max(R1.x, R2.x), max(R1.y, R2.y),
			min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
			min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)};
}
```

---
Note:
Time complexity: O(1), space: O(1)

---
</details>