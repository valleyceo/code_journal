
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
