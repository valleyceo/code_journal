# Sorting

<details>
<summary> Compute the Intersection of the Sorted Arrays </summary>

---
- Given two sorted arrays
- Return a new array that are present in both input arrays

---

```cpp
vector<int> IntersectTwoSortedArrays(const vector<int>& A,
									 const vector<int>& B) {
	vector<int> intersection_A_B;

	int i = 0, j = 0;
	while (i < size(A) && j < size(B)) {
		if (A[i] == B[j] && (i == 0 || A[i] != A[i-1])) {
			intersection_A_B.emplace_back(A[i]);
			++i, ++j;
		} else if (A[i] < B[j]) {
			++i;
		} else { // A[i] >= B[j]
			++j;
		}
	}

	return intersection_A_B;
}
```

---
- Time complexity: O(m + n)

---
</details>


<details>
<summary> Merge Two Sorted Arrays </summary>

---
- Given two sorted arrays of integers
- Update the first array to the combined entries of two arrays in sorted order

- Assume spare space at end of first array
---

```cpp
void MergeTwoSortedArrays(vector<int>& A, int m, const vector<int>& B, int n) {
	int a = m - 1, b = n - 1, write_idx = m + n - 1;
	while (a >= 0 && b >= 0) {
		A[write_idx--] = A[a] > B[b] ? A[a--] : B[b--];
	}

	while (b >= 0) {
		A[write_idx--] = B[b--];
	}
}
```

---

---
</details>