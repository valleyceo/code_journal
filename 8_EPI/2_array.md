# Array

<details>
<summary> Dutch National Flag Problem (Quicksort) </summary>

---
Hint: quicksort

---

```cpp
typedef enum {kRed, kWhite, kBlue} Color;

void DutchFlagPartition(int pivot_index, vector<Color>* A_ptr) {
	vector<Color>& A =*A_ptr;
	Color pivot = A[pivot_index];

	int smaller = 0;
	int equal = 0;
	int larger = size(A);

	while (equal < larger) {
		if (A[equal] < pivot) {
			swap(A[smaller++], A[equal++]);
		} else if (A[equal] == pivot) {
			++equal;
		} else {
			swap(A[equal], A[--larger]);
		}
	}
}
```

---
Note:
Time complexity: O(n), space: O(1)

---
</details>

<details>
<summary> Increment a Non-negative Number </summary>

```cpp
vector<int> PlusOne(vector<int> A) {
	++A.back();

	for (int i = size(A) - 1; i > 0 && A[i] == 10; --i) {
		A[i] = 0;
		++A[i-1];
	}

	if (A[0] == 10) {
		A[0] = 1;
		A.emplace_back(0) // place 0 on the end since value will be 100...0
	}
}
```

---
Note:
Time complexity: O(n)

---
</details>