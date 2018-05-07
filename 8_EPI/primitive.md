# Primitive
--

<details>
<summary> count 1s in bit </summary>
```cpp
while (x) {
	ct += x & 1;
	x >> = 1;
}
// complexity O(n)
```
</details>
<details>
<summary> parity of number </summary>
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
<summary> swap bits </summary>

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
<summary> reverse bits </summary>

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
<summary> closest integer with same weight (number of 1's) </summary>

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
<summary> Multiply </summary>

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

}
```
</details>