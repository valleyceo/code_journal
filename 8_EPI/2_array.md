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

<details>
<summary> Multiply two arbitrary-precision integers </summary>

---
Positive value <1, 9, 3>
Negative value <-7, 6, 1>

---

```cpp
vector<int> Multiply(vector<int> num1, vector<int> num2) {
	const int sign = num1.front() < 0 ^ num2.front() < 0 ? -1 : 1;
	num1.front() = abs(num1.front());
	num2.front() = abs(num2.front());

	vector<int> result(size(num1) +  size(num2), 0);

	for (int i = size(num1) - 1; i >= 0; --i) {
		for (int j = size(num2) - 1; j >= 0; --j) {
			result[i + j + 1] += num1[i] * num2[j];
			result[i + j] += result[i + j + 1] / 10;
			result[i + j + 1] %= 10;
		}
	}

	result = {
		find_if_not(begin(result), end(result), [](int a) {return a == 0;})
	}
}
```

---
Note:
Time complexity: O(n)

---
</details>

<details>Advance Through an Array</summary>

---
- Array of n integers
- A[i] denotes the maximum you can advance from index i
- return whether it is possible to advance to the last index starting from beginning of array

---

```cpp
bool CanReachEnd(const vector<int>>& max_advance_steps) {
	int furthest_reach = 0;
	int last_idx = size(max_advance_steps) - 1;

	for (int i = 0; i < furthest_reach && furthest_reach < last_idx; ++i) {
		furthest_reach = max(furthest_reach, max_advance_steps[i] + i);
	}

	return furthest_reach >= last_idx;
}
```

---
Note:
Time complexity: O(n)
Space complexity: O(1)

---
</details>

<details>Advance Through an Array</summary>

---
- Array of n integers
- A[i] denotes the maximum you can advance from index i
- return whether it is possible to advance to the last index starting from beginning of array

---

```cpp
bool CanReachEnd(const vector<int>>& max_advance_steps) {
	int furthest_reach = 0;
	int last_idx = size(max_advance_steps) - 1;

	for (int i = 0; i < furthest_reach && furthest_reach < last_idx; ++i) {
		furthest_reach = max(furthest_reach, max_advance_steps[i] + i);
	}

	return furthest_reach >= last_idx;
}
```

---
Note:
Time complexity: O(n)
Space complexity: O(1)

---
</details>

<details>Delete duplicates from a Sorted Array</summary>

---
- Return count of remaining elements

---

```cpp
int DeleteDuplicates(vector<int>* A_ptr) {
	vector<int>& A = *A_ptr;

	if (empty(A)) {
		return 0;
	}

	int write_index = 1;

	for (int i = 1; i < size(A); ++i) {
		if (A[write_index - 1] != A[i]) {
			A[write_index++] = A[i];
		}
	}

	return write_index;
}

```

---
Note:
Time complexity: O(n)
Space complexity: O(1)

---
</details>

<details>Buy and Sell Stock Once</summary>

---
- Return max profit

---

```cpp
double BuyAndSellStockOnce(const vector<double>& prices) {
	double min_price_so_far = numeric_limits<double>::max(), max_profits = 0;

	for (double price : prices) {
		double max_profit_sell_today = price - min_price_so_far;
		max_profit = max(max_profit, max_profit_sell_today);
		min_price_so_far = min(min_price_so_far, price);		
	}

	return max_profit;
}

```

---
Note:
Time complexity: O(n)
Space complexity: O(1)

---
</details>

<details>Buy and Sell Stock Twice</summary>

---
- Return max profit

---

```cpp
double BuyAndSellStockTwice(const vector<int>& prices) {
	double max_total_profit = 0;
	vector<double> sell_profits(size(prices), 0);
	double min_price_so_far = numeric_limits<double>::max();

	// Forward phase. For each day, record maximum profit we can make up to that day
	for (int i = 0; i < size(prices); ++i) {
		min_price_so_far = min(min_price_so_far, prices[i]);
		max_total_profit = max(max_total_profit, prices[i] - min_price_so_far);
		sell_profits[i] = max_total_profit;
	}

	double max_price_so_far = numeric_limits<double>::min();
	// Backward phase. Record maximum profit we can make on the second day, and add it to the array
	for (int i = size(prices)-1; i > 0; --i) {
		max_price_so_far = max(max_price_so_far, prices[i]);
		max_total_profit = max(max_total_profit, max_price_so_far - prices[i] +
							   sell_profits[i-1]);
	}

	return max_total_profit;
}
```

---
Note:
Time complexity: O(n)
Space complexity: O(n)

- can solve with O(1) space
---
</details>