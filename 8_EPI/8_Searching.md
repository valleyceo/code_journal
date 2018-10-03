# Searching

<details>
<summary> Binary Search </summary>

```cpp
int bsearch(int t, const vector<int>& A) {
	int L = 0, U = size(A) - 1;
	while (L <= U) {
		int M = L + (U - L) / 2;
		if (A[M] < t) {
			L = M + 1;
		} else if (A[M] == t) {
			return M;
		} else {
			U = M - 1;
		}
	}

	return -1;
}
```

---
- Time complexity: O(logn), or O(nlogn) for sorting

---
</details>


<details>
<summary> Binary Search Bootcamp </summary>

```cpp
struct Student {
	string name;
	double grade_point_average;
};

const static function<bool(const Student&, const Student&)> CompGPA = [](const Student& a, const Student& b) {
	if (a.grade_point_average != b.grade_point_average) {
		return a.grade_point_average > b.grade_point_average;
	}

	return a.name < b.name;
};

bool SearchStudent(
				const vector<Student>& students, const Student& target, 
				const function<bool(const Student&, const Student&)>& comp_GPA) {
	return binary_search(begin(students), end(students), target, comp_GPA);
}
```

---
- Time complexity: O(logn), with O(1) access time
---
</details>


<details>
<summary> Search a Sorted Array for first occurence of K </summary>

```cpp
int SearchFirstOfK(const vector<int>>& A, int k) {
	int left = 0, right = size(A) - 1, result = -1;
	while (left <= right) {
		if (int mid = left + ((right - left) / 2); A[mid] > k) {
			right = mid - 1;
		} else if (A[mid] == k) {
			result = mid;
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}

	return result;
}
```

---
- Time complexity: O(logn)

---
</details>


<details>
<summary> Search a Sorted Array for Entry Equal to its Index </summary>

---

---

```cpp
in SearchEntryEqualToItsIndex(const vector<int>& A) {
	int left = 0, right = size(A) - 1;

	while (left <= right) {
		int mid = left + ((right - left) / 2);

		if (int differences = A[mid] - mid; difference == 0) {
			return mid;
		} else if (difference > 0) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}

	return -1;
}
```

---
- Time complexity: O(logn)

---
</details>


<details>
<summary> Search a Cyclically Sorted Array </summary>

---
- Given a cyclically sorted array
- Find the smallest element and return the index

---

```cpp
int SearchSmallest(const vector<int>& A) {
	int left = 0, right = size(A) - 1;

	while (left < right) {
		if (int mid = left ((right - left) / 2); A[mid] > A[right]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left; // loop ends when left == right
}
```

---
- Time complexity: O(logn)

---
</details>