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

<details>
<summary> Advance Through an Array</summary>

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

<details>
<summary> Advance Through an Array</summary>

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

<details>
<summary> Delete duplicates from a Sorted Array</summary>

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

<details>
<summary> Buy and Sell Stock Once</summary>

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

<details>
<summary> Buy and Sell Stock Twice</summary>

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

- can solve with O(n) time, O(1) space
---
</details>

<details>
<summary> Rearrange Alternation </summary>

---
- Takes an array A of n numbers, and rearranges A's elements to get a new array B  
- B[0] <= B[1] >= B[2] <= B[3] >= B[4] ...  

---

```cpp
void Rearrange(vector<int>* A_ptr) {
	vector<int>& A = *A_ptr;

	for (size_t i = 1; i < size(A); ++i) {
		if (!(i%2) && A[i-1] < A[i] || ((i%2) && A[i-1] > A[i])){
			swap(A[i-1], A[i]);
		}
	}
}
```

---
Note:  
Time complexity: O(n)  
Space complexity: O(1)  

- This works since each elements will either be > or < regardless of being sorted  
- Better than sort and swap O(nlog(n))  
- similar to median finging  
---
</details>


<details>
<summary> Generate Primes </summary>

```cpp
vector<int> GeneratePrimes(int n) {
	 if (n < 2) {
	 	return {};
	 }

	 const int size = floor(0.5 * (n - 3) ) + 1;
	 vector<int> primes;
	 primes.emplace_back(2);

	 deque<bool> is_prime(size, true);
	 for(long i = 0; i < sizes; ++i) {
	 	if (is_prime[i]) {
	 		long p = (i * 2) + 3;
	 		primes.emplace_back(p);

	 		for (long j = (i * i) * 2 + 6 * i + 3; j < size; j += p) {
	 			is_prime[j] = false;
	 		}
	 	}
	 }
	 return primes;
}
```

---
- O(n/2 + n/3 + n/4 ...) ~ O(nloglogn)  
- note: for trivial divion approach bound is O(n^(3/2)/(logn)^2)  
- Optimized runtime by sieving p's multiples from p^2 instead of p  

---
</details>

<details>
<summary> Apply Permutation </summary>

---
- Given array A and permutation array P, apply P to A  
- Ex. P = < 2,0,1,3 >, A = < a,b,c,d > => A_new = < b, c, a, d >  

---

```cpp
void ApplyPermutation(vector<int>* perm_ptr, vector<int>* A_ptr) {
	vector<int>&perm = *perm_ptr, &A = *A_ptr;
	
	for (int i = 0; i < size(A); ++i) {
		int next = i;
		
		while (perm[next] >= 0) {
			swap(A[i], A[perm[next]]);
			int temp = perm[next];

			perm[next] = size(perm);
			next = temp;
		}
	}

	// Restore perm
	for_each(begin(perm), end(perm), [&perm](int& x) { x += size(perm); });
}

```

---
- Time: O(n), Space: O(1)  
- Swap with permuted next element, keep track by subtracting -size(P) (add them later)  
- Two loops: 1. loop over each array, 2. loop over next permuted element  

---
</details>


<details>
<summary> Compute Next Permutation </summary>

---
- takes a permutation and returns next permutation under dictionary order  
- ex: < 6, 2, 1, 5, 4, 3, 0> -> < 6, 2, 3, 0, 1, 4, 5 >  

---

```cpp
vector<int> NextPermutation(vector<int> perm) {
	auto inversion_point = is_sorted_until(rbegin(), rend(perm)); // reverse iterator

	// last permutation
	if (inversion_point == rend(perm)) {
		return {};
	}

	auto least_upper_bound = upper_bound(rbegin(perm), inversion_point, *inversion_point);
	iter_swap(inversion_point, least_upper_bound);

	reverse(rbegin(perm), inversion_point);
	return perm;
} 

```

---
- Time: O(n), Space: O(1)  
- General algorithm  
1. Find the first decreasing number (k) from back to start order
2. Find the next smallest number than k 
3. Swap the two numbers
4. Reverse the sequence after position k

---
</details>


<details>
<summary> Random Sampling </summary>

---
- Given array A, create random subarray of size k

---

```cpp
void RandomSampling(int k, vector<int>* A_ptr) {
	vector<int>& A = *A_ptr;
	default_random_engine seed((random_device())()) // random num generator

	for (int i = 0; i < k; ++i) {
		swap(A[i], A[uniform_int_distribution<int>{i, static_cast<int>(A.size() - 1)}(seed)]);
	}
}

```

---
- Time: O(n), Space: O(1)  

---
</details>


<details>
<summary> Online Random Sampling</summary>

---
- Take input size k and packets
- Continuously maintain uniform random subset S of size k of the read packets
---

```cpp
vector<int> OnlineRandomSample(vector<int>::const_iterator stream_begin, 
								const vector<int>::const_iterator stream_end, 
								int k) {
	vector<int> running_sample;

	for (int i = 0; i < k; ++i) {
		running.sample.emplace_back(*stream_begin++);
	}

	int num_seen_so_far = k;
	while (stream_begin != stream_end) {
		int x = *stream_begin++;
		++num_seen_so_far;

		if (const int idx_to_replace = 
					uniform_int_distribution<int>{0, num_seen_so_far - 1}(seed);
					idx_to_replace < k) {
			running_sample[idx_to_replace] = x;
		}
	}
	return running_sample;
}
```

---
Note:
- if (CThing thing {}; thing.is_good()) {} -> C++17 format
- Time: O(1)/element, Space: O(k)

1. For every new packet, find random number between 0 - new_stream_size
2. If new_stream_size < k, replace S[new_stream_size] to the new packet - P(k/stream_size)

---
</details>



<details>
<summary> Compute Random Permutation </summary>

---
- create uniformly random permutations of {0, 1, ..., n-1}

---

```cpp
vector<int> ComputeRandomPermutation(int n) {
	vector<int> permutation(n);

	iota(begin(permutation), end(permutation), 0); // initialize permutation 0, 1, ..., n-1
	RandomSampling(n, &permutation);
	return permutation;
}
```

---
- Time: O(n), no extra spaces

---
</details>