# Greedy Algorithms and Invariants

<details>
<summary> Compute an Optimum Assignment of Tasks </summary>

---
- Given a list of tasks with duration time, and each worker must take two tasks
- Return the optimum duration to complete all

---

```cpp
struct PairedTasks {
	int task_1, task_2;
};

vector<PairedTasks> OptimumTaskAssignment(vector<int> task_durations) {
	sort(begin(task_durations), end(task_durations));
	vector<PairedTasks> optimum_assignments;

	for (int i=0, j=size(task_durations); i < j; ++i, --j) {
		optimum_assignments.emplace_back(PairedTasks{task_durations[i], task_durations[j]});
	}

	return optimum_assignments;
}
```

---
- Time complexity: O(nlogn)

---
</details>


<details>
<summary> Schedule to Minimize Waiting Time (need to review) </summary>

---
- Given a set of query waiting time
- Create schedule for a minimal processing time

- Example: <2,5,1,3> -> 10 (optimal when 0 + (1) + (1+2) + (1+2+3))

---

```cpp
int MinimumTotalWaitingTime(vector<int> service_times) {
	sort(begin(service_times), end(service_times));

	int total_waiting_time = 0;
	for (int i = 0; i < size(service_times); ++i) {
		int num_remaining_queries = size(service_times) - (i + 1);
		total_waiting_time += service_times[i] * num_remaining_queries;
	}

	return total_waiting_time;
}
```

---
- Time complexity: O(nlogn)

---
</details>


<details>
<summary> Interval Covering Problem </summary>

---
- Given a set of closed intervals
- Find minimum sized set of numbers that covers all intervals

---

```cpp
struct Interval {
	int left, right;
};

int FindMinimumVisits(vector<Interval> intervals) {
	sort(begin(intervals), end(intervals), [](const Interval& a, const Interval& b){ return a.right < b.right; });

	int last_visit_time = numeric_limits<int>::min(), num_visits = 0;

	for (const Interval& interval : intervals) {
		if (interval.left > last_visit_time) {
			last_visit_time = interval.right;
			++num_visits;
		}
	}

	return num_visits;
}
```

---
- Time complexity: O(nlogn)

- Idea:
	1. Sort by right  
	2. Iterate through item  
	3. keep a pointer from -inf, and whenever a new interval.left is bigger, set it to the interval.right (this creates new interval)

---
</details>


<details>
<summary> Invariants Boot Camp </summary>

---
- Given a sorted array and a target value
- Return if there are two values that add up to target value

---

```cpp
bool HasTwoSum(const vector<int>& A, int t) {
	int i = 0, j = size(A) - 1;

	while (i <= j) {
		if (A[i] + A[j] == t) {
			return true;
		} else if (A[i] + A[j] < t) {
			++i;
		} else {
			--j;
		}
	}
	return false;
}
```

---
- Time complexity: O(n)
- Space complexity: O(1)

- Observation: there can never be a same sum pair in the order of {a,b,a,b}
- Same sum pair occurs in {a,b,b,a} order, so you can follow the above's algorithm

---
</details>


<details>
<summary> The 3-Sum Problem </summary>

---
- Given an array and a target number
- Determine if there are three entries that add up to the target number

---

```cpp
bool hasThreeSum(vector<int> A, int t) {
	sort(begin(A), end(A));

	return any_of(begin(A), end(A), [&](int a) {return HasTwoSum(A, t-a); });
}
```

---
- Time complexity: O(n^2 overall)
- Space complexity: O(1)

- any_of: checks if any of the elements in array given a function meets true
- ```std::any_of(foo.begin(), foo.end(), [](int i){return i<0;})```

---
</details>


<details>
<summary> Find the Majority Element </summary>

---
- Given a sequence of strings, where more than half the strings are repetitions of a single string
- Find the majority element

---

```cpp
string MajoritySearch(vector<string>::const_iterator stream_begin, const vector<string>::const_iterator stream_end) {
	string candidate;
	int candidate_count = 0;

	while (stream_begin != stream_end) {
		string it = *stream_begin++;

		if (candidate_count == 0) {
			candidate = it;
			candidate_count = 1;
		} else if (candidate == it) {
			++candidate_count;
		} else {
			--candidate_count;
		}
	}

	return candidate;
}
```

---
- Time complexity: O(n)

- Justification: if m/n > 1/2, then m/(n-2) > 1/2 and (m-1)/(n-2)
- (Explanation) Majority of elements will stay 1/2 or above even if majority or non-majority element is added/discarded. As a result, the majority element will always be left at the end.

---
</details>


<details>
<summary> The Gasup Problem </summary>

---
- Given circular cities with x gallons to fill and their distance
- Return the city (index) that is 'ample' (can make a full circle without getting empty)

- Assumes there always is an ample city
---

```cpp
const int kMPG = 20;

int FindAmpleCity(const vector<int>& gallons, const vector<int>& distances) {
	int remaining_gallons = 0;
	struct CityAndRemainingGas {
		int city = 0, remaining_gallons = 0;
	};

	CityAndRemainingGas city_remaining_gallons_pair;
	const int num_cities = size(gallons);

	for (int i = 1; i < num_cities; ++i) {
		remaining_gallons += gallons[i-1] - distances[i-1] / kMPG;

		if (remaining_gallons < city_remaining_gallons_pair.remaining_gallons) {
			city_remaining_gallons_pair = {i, remaining_gallons};
		}
	}

	return city_remaining_gallons_pair.city;
}
```

---
- Time complexity: O(n)
- Space complexity: O(1)

---
</details>


<details>
<summary> Compute The Maximum Water Trapped by Pair of Vertical Lines </summary>

---
- Given an integer array
- Return the pair which traps the maximum amount of water

---

```cpp
int GetMaxTrappedWater(const vector<int>& heights) {
	int i = 0, j = size(heights) - 1, max_water = 0;

	while (i < j) {
		int width = j-i;
		max_water = max(max_water, width * min(heights[i], heights[j]));

		if (heights[i] > heights[j]) {
			--j;
		} else {
			++i;
		}
	}

	return max_water;
}
```

---
- Time complexity: O(n)
- Space complexity: O(1)

---
</details>


<details>
<summary> Compute the Largest Rectangle Under the Skyline (need to review) </summary>

---
- Given array representing heights of adjacent buildings of unit width
- Compute area of largest rectangle contained in the skyline

---

```cpp
int CalculateLargestRectangle(const vector<int>& heights) {
	stack<int> pillar_indices;
	int max_rectangle_area = 0;

	for (int i = 0; i <= size(heights); ++i) {
		while (!empty(pillar_indices) && IsNewPillarOrReachEnd(heights, i, pillar_indices.top())) {
			int height = heights[pillar_indices.top()];
			pillar_indices.pop();
			int width = empty(pillar_indices) ? i : i-pillar_indices.top() - 1;
			max_rectangle_area = max(max_rectangle_area, height * width);
		}
		pillar_indices.emplace(i);
	}

	return max_rectangle_area;
}

bool IsNewPillarOrReachEnd(const vector<int>& heights, int curr_idx, int last_pillar_idx) {
	return curr_idx < size(heights) ? heights[curr_idx] <= heights[last_pillar_idx] : true;
}
```

---
- Time complexity: O(n)
- Space complexity: O(n)
---
</details>