# Heaps

<details>
<summary> Heaps </summary>

---
- Find the top k longest string (each node represents length of a string)
---

```cpp
vector<string> TopK (int k, vector<string>::const_iterator stream_begin,
					 const vector<string>::const_iterator& stream_end) 
{
	priority_queue<string, vector<string>, function<bool(string, string)>>
	min_heap([](const straing& a, const string& b) 
	{
		return size(a) >= size(b);
	});

	while (stream_begin != stream_end) 
	{
		min_heap.emplace(*stream_begin);
			if (size(min_heap) > k) 
			{
				min_heap.pop();
			}

			stream_begin = next(stream_begin);
	}

	vector<string> result;
	while (!empty(min_heap))
	{
		result.emplace_back(min_heap.top());
		min_heap.pop();
	}

	return result;
}

```

---
- Time complexity: Lookup O(1), string process O(logK), total process O(nlogK)

---
</details>


<details>
<summary> Merge Sorted Files (need to review) </summary>

---
- Given a set of sorted sequences
- Find the union of them in sorted sequence.
- EX: <3,5,7>, <0,6>, <0,6,28> -> <0,0,3,5,6,6,7,28>

---

```cpp
// overwrite operator >
struct IteratorCurrentAndEnd {
	bool operator>(const IteratorCurrentAndEnd& that) const {
		return *current > *that.current;
	}

	vector<int>::const_iterator current;
	vector<int>::const_iterator end;
}

vector<int> MergeSortedArrays (const vector<vector<int>>& sorted_arrays) {
	priority_queue<IteratorCurrentAndEnd, vector<IteratorCurrentAndEnd>, greater<>> min_heap;

	for (const vector<int>& sorted_array: sorted_arrays) {
		if (!empty(sorted_array)) {
			min_heap.emplace(
				IteratorCurrentAndEnd{cbegin(sorted_array), cend(sorted_array)});
		}
	}

	vector<int> result;
	while (!empty(min_heap)) {
		IteratorCurrentAndEnd smallest_array = min_heap.top();
		min_heap.pop();
		result.emplace_back(*smallest_array.current);
		if (next(smallest_array.current) != smallest_array.end) {
			min_heap.emplace(IteratorCurrentAndEnd{next(smallest_array.current), smallest_array.end});
		}
	}
	return result;
}
```

---
- Time complexity: O(nlogk)

---
</details>


<details>
<summary> Sort an Increasing-Decreasing Array </summary>

---
- Given an array that is increasing and decreasing k times
- Sort the array
- Note: regular sorting takes O(nlogn) without taking advantage of k-inc-dec property 

---

```cpp
vector<int > SortKIncreasingDecreasingArray(const vector<int>& A) {
	vector<vector<int>> sorted_subarrays;
	typedef enum { kIncreasing, kDecreasing } SubarrayType;
	SubarrayType subarray_type = kIncreasing;

	int start_idx = 0;
	for (int i = 1; i <= size(A); ++i) {
		if (i == size(A) || // add the last subarray
			(A[i - 1] < A[i] && subarray_type == kDecreasing) ||
			(A[i - 1] >= A[i] subarray_type == kIncreasing)) 
		{
			
			if (subarray_type == kIncreasing)
			{
				sorted_subarrays.emplace_back(cbegin(A) + start_idx, cbegin(A) + i);
			} else {
				sorted_subarrays.emplace_back(crbegin(A) + size(A) - i, crbegin(A) + size(A) - start_idx);
			}

			start_idx = i;
			subarray_type = subarray_type == kIncreasing ? kDecreasing : kIncreasing;
		}
	}

	return MergeSortedArrays(sorted_subarrays);
}
```

---
- Time complexity: O(nlogK)
- Space complexity: O(n)

- Create subarrays of increasing array (reverse the decreasing array)
- Use merge sort function from above

---
</details>


<details>
<summary> Sort an Almost Sorted Array </summary>

---
- Each number is at most k away from its corrected position

---

```cpp
vector<int> SortApproximatelySortedData (vector<int>::const_iterator sequence_begin,
										const vector<int>::const_iterator& sequence_end, int k) {
	priority_queue<int, vector<int>, greater<>> min_heap;

	for (int i = 0; i < k && sequence_begin != sequence_end; ++i) {
		min_heap.push(*sequence_begin++);
	}

	vector<int> result;

	while (sequence_begin != sequence_end) {
		min_heap.push(*sequence_begin++);
		result.push_back(min_heap.top());
		min_heap.pop();
	}

	while (!empty(min_heap)) {
		result.push_back(min_heap.top());
		min_heap.pop();
	}

	return result;
}
```

---
- Time complexity: O(nlogk)
- Space complexity: O(k)

---
</details>


<details>
<summary> Compute the K Closest Stars</summary>

---
- Given 10^12 stars and Earth is at (0, 0, 0)
- Find the k stars that are closest to earth.

---

```cpp
struct Star {
	book operator<(const Star& that) const {
		return Distance() < that.Distance();
	}

	double Distance() const {return sqrt(x * x + y * y + z * z); }
	double x, y, z;
};

vector<Star> FindClosestKStars(vector<Star>::const_iterator stars_begin,
							   const vector<Star>::const_iterator& stars_end,
							   int k) {
	priority_queue<Star> max_heap;

	while (stars_begin != stars_end) {
		max_heap.emplace(*stars_begin++);
		if ( size(max_heap) == k + 1) {
			max_heap.pop();
		}
	}

	vector<Star> closest_stars;
	while (!empty(max_heap)) {
		closest_stars.emplace_back(max_heap.top());
		max_heap.pop();
	}

	return {rbegin(closest_stars), rend(closest_stars)};
}
```

---
- Time complexity: O(nlogk)
- Space complexity: O(k)

- Note: Keep top min k on the heap as you read in
---
</details>