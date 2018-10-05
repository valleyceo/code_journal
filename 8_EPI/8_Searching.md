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


<details>
<summary> Compute the Integer Square Root </summary>

```cpp
int SquareRoot(int k) {
	int left = 0, right = k;

	while (left <= right) {
		long mid = left + ((right - left) / 2);
		if (long mid_squared = mid * mid; mid_squared <= k) {
			left = mid + 1;
		} else if (mid_squared > k) {
			right = mid - 1;
		}
	}

	return left - 1;
}
```

---
- Time complexity: O(logn)

---
</details>


<details>
<summary> Compute the Real Square Root </summary>

```cpp
typedef enum { kSmaller, kEqual, kLarger} Ordering;

double SquareRoot (double x) {
	double left, right;

	if (x < 1.0) {
		left = x, right = 1.0;
	} else { // x >= 1.0
		left = 1.0, right. = x;
	}

	while (Compare(left, right) != kEqual) {
		double mid = left + 0.5 * (right - left);
		if (double mid_squared = mid * mid; Compare(mid_squared, x) == kLarger) {
			right = mid;
		} else {
			left = mid;
		}
	}

	return left;
}

Ordering Compare(double a, double b) {
	double diff = (a-b) / max(abs(a), abs(b));
	return diff < -numeric_limits<double>::epsilon() ? 
		   kSmaller : 
		   diff > numeric_limits<double>::epsilon() ? kLarger : kEqual;
}
```

---
- Time complexity: O(log(x/s))

---
</details>


<details>
<summary> Search in a 2D Sorted Array </summary>

---
- Given an integer and 2D array where its rows and columns are sorted in nondecreaing order.
- Check whether the number appears in the array.

---

```cpp
bool MatrixSearch(const vector<vector<int>>& A, int x) {
	int row = 0, col = size(A[0]) - 1;

	while (row < size(A) && col >= 0) {
		if (A[row][col] == x) {
			return true;
		} else if (A[row][col] < x) {
			++row;
		} else {
			--col;
		}
	}

	return false;
}
```

---
- Time complexity: O(m+n)

- Starting from wither top-right(or bottom-left), go down if value is bigger, or go left if smaller.
- This will weave through all values close to the seached number to guarantee crossover.

---
</details>


<details>
<summary> Find the Min and Max Simultaneously </summary>

---

---

```cpp
struct MinMax {
	int smallest, largest;
}

MinMax FindMinMax(const vector<int>& A) {
	if (size(A) <= 1) {
		return {A.front(), A.front()};
	}

	int global_min, global_max;
	tie(global_min, global_max) = minmax(A[0], A[1]);

	for (int i = 2; i + 1 < size(A); i += 2) {
		const auto& [local_min, local_max] = minmax(A[i], A[i + 1]);
		global_min = min(global_min, local_min);
		global_max = max(global_max, local_max);
	}

	if (size(A) % 2) {
		global_min = min(global_min, A.back());
		global_max = max(global_max, A.back());
	}

	return {global_min, global_max};
}
```

---
- Time complexity: O(3n/2 - 2), which is the sum of smallest O(n/2-1), largest O(n/2-1), and comparison computation O(n/2)

- minmax() function returns [smaller, larger] of the given array

---
</details>