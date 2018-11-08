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


<details>
<summary> Computing H-Index</summary>

---
- Given an array of positive integers
- Find the largest h such that there are at least h entries in the array that are greater than or equal to h.

---

```cpp
int HIndex(vector<int> citations) {
	sort(begin(citations), end(citations));
	const int n = citations.size();

	for (int i = 0; i < citations.size(); ++i) {
		if (citations[i] > n - i) {
			return n - i;
		}
	}

	return 0;
}
```

---
- Time complexity: O(nlogn)
- Space complexity: O(1)

- Example cases:
- [1] -> 0
- [3, 0, 6, 1, 5] -> [0, 1, 3, 5, 6] -> 3

---
</details>


<details>
<summary> Remove First-Name Duplicates </summary>

---
- Design an efficient algorithm for removing all first-name duplicates from an array.

---

```cpp
struct Name {
	bool operator==(const Name& that) const {
		return first_name == that.first_name;
	}

	bool operator<(const Name& that) const {
		return first_name != that.first_name ? first_name < that.first_name : last_name < that.last_name;
	}

	string first_name, last_name;
}

void ElliminateDuplicate(vector<Name>* names) {
	sort(begin(*names), end(*names));

	names->erase(unique(begin(*names), end(*names)), end(*names));
}
```

---
- Time complexity: O(nlogn)
- Space complexity: O(1)

- Explanation to line ```names->erase(unique(begin(*names), end(*names)), end(*names)); ```:
- unique(v.begin(), v.end()) removes all following duplicates from each element ([10, 10, 20, 20, 10] -> [10, 20, 10, ?, ?]) returns the pointer to last element
- vector::erase(v.begin(), v.end()) removes elements from begin to end. ([10, 20, 10, ?, ?] -> [10, 20, 10])

---
</details>


<details>
<summary> Smallest Nonconstructible Value </summary>

---
- Given an array of positive integers
- Return the smallest number which is not the sum of a subset of elements of the array

---

```cpp
int SmallestNonconstructibleValue(vector<int> A) {
	sort(begin(A), end(A));

	int max_constructible_value = 0;
	for (int a : A) {
		if (a > max_constructible_value + 1) {
			break;
		}

		max_constructible_value += a;
	}

	return max_constructible_value + 1;
}
```

---
- Time complexity: O(nlogn)
- Space complexity: O(1)

---
</details>


<details>
<summary> Render a Calendar </summary>

---
- Given a set of event times
- Find the maximum number of events that takes place concurrently

---

```cpp
struct Event {
	int start, finish;
};

struct Endpoint {
	int time;
	bool is_start;
};

int FindMaxSimultaneousEvents(const vector<Event>& A) {
	vector<Endpoint> E;
	for (const Event& event: A) {
		E.emplace_back(Enpoint{event.start, true});
		E.emplace_back(Endpoint{event.finish, false});
	}

	sort(begin(E), end(E), [](const Endpoint& a, const Endpoint& b) {
		return a.time != b.time ? a.time < b.time : (a.is_start && !b.is_start);
	});

	int max_num_simultaneous_events = 0, num_simultaneous_events = 0;
	for (const Endpoint& endpoint : E) {
		if (endpoint.is_start) {
			++num_simultaneous_events;
			max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events);
		} else {
			--num_simultaneous_events;
		}
	}

	return max_num_simultaneous_events;
}
```

---
- Time complexity: O(nlogn)
- Space complexity: O(n)

---
</details>


<details>
<summary> Merging Intervals </summary>

---
- Given an array of disjoint intervals with integer endpoints (sorted by increasing order) and an interval to be added.
- Return the union of the interval array and added interval

---

```cpp
struct Interval {
	int left, right;
};

vector<Interval> AddInterval(const vector<Interval>& disjoint_intervals, Interval new_interval) {
	size_t i = 0;
	vector<Interval> result;

	while (i < size(disjoint_intervals) &&
		new_interval.left > disjoint_intervals[i].right) {
		result.emplace_back(disjoint_intervals[i++]);
	}

	while (i < size(disjoint_intervals) && new_interval.right >= disjoint_intervals[i].left) {
		new_interval = {min(new_interval.left, disjoint_intervals[i].left),
						max(new_interval.right, disjoint_intervals[i].right)};
		++i;
	}

	result.emplace_back(new_interval);
	result.insert(end(result), begin(disjoint_intervals) + i, end(disjoint_intervals));
	return result;
}
```

---
- Time complexity: O(n)

---
</details>


<details>
<summary> Compute the Union of Intervals </summary>

---
- Given a set of intervals
- Output their union expressed as set of disjoint intervals

- Note: endpoints can be open or closed
---

```cpp
struct Interval {
	struct Endpoint {
		bool is_closed;
		int val;
	};

	Endpoint left, right;
}

vector<Interval> UnionOfIntervals(vector<Interval> intervals) {
	if (empty(intervals)) {
		return {};
	}

	// sort intervals according to left endpoints
	sort(begin(intervals), end(intervals), [](const Interval& a, const Interval& b){
		if (a.left.val < b.left.val) {
			return a.left.val < b.left.val;
		}

		return a.left.is_closed && !b.left.is_closed;
		});

	vector<Interval> result;
	for (Interval i : intervals) {
		// checks if left of the new interval intersects with the last interval's right
		// if both values are equal, they only intersect when both are closed
		if (!empty(result) &&
			(i.left.val < result.back().right.val ||
			(i.left.val == result.back().right.val &&
			(i.left.is_closed || result.back().right.is_closed)))) {

			if (i.right.val > result.back().right.val ||
				(i.right.val == result.back().right.val && i.right.is_closed)) {
				result.back().right = i.right;
			}
		}
		else {
			result.emplace_back(i);
		}
	}

	return result;
}
```

---
- Time complexity: O(nlogn)

---
</details>


<details>
<summary> Partitioning and Sorting an Array with Many Repeated Entries </summary>

---
- Given an array of student objects with integer-valued age as key
- Rearrange the elements of the array so that the students of equal age appear together (does not have to be age ordered)
---

```cpp
struct Person {
	int age;
	string name;
};

void GroupByAge(vector<Person>* person) {
	unordered_map<int, int> age_to_count;
	for (const Person& p : *people) {
		++age_to_count[p.age];
	}

	unordered_map<int, int> age_to_offset;
	int offset = 0;

	for (const auto& [age, count] : age_to_count) {
		age_to_offset[age] = offset;
		offset += count;
	}

	while (!empty(age_to_offset)) {
		auto from = begin(age_to_offset); // get the first object
		auto to = age_to_offset.find((*people)[from->second].age); // find an object
		swap((*people)[from->second], (*people)[to->second]);

		--age_to_count[to->first];
		if (age_to_count[to->first] > 0) {
			++to->second;
		} else {
			age_to_offset.erase(to);
		}
	}
}
```

---
- Time complexity: O(n)
- Space complexity: O(m), where m is number of distinct ages

- Avoided O(n) space by performing in-place

---
</details>


<details>
<summary> Team Photo Day 1 </summary>

---
- Given 2 rows of arrays of same size,
- Check if it is possible to arrange each arrays s.t. each elements in row 1 is bigger than the row 2 (of same column)

---

```cpp
class Team {
public:
	explicit Team(const vector<int>& height) {
		transform(begin(height), end(height), back_inserter(players_), [](int h) { return Player{h}; });
	}


	static bool ValidPlacementExists(const Team& team0, const Team& team1) {
		vector<Player> team0_sorted(team0.SortPlayersByHeight());
		vector<Player> team1_sorted(team1.SortPlayersByHeight());

		for (int i = 0; i < size(team0_sorted) && i < size(team1_sorted); ++i) {
			if (!(team0_sorted[i] < team1_sorted[i])) {
				return false;
			}
		}

		return true;
	}

private:
	struct Player {
		bool operator<(const Player& that) const { return height < that.height; }

		int height;
	};

	vector<Player> SortPlayersByHeight() const {
		vector<Player> sorted_players(players_);
		sort(begin(sorted_players), end(sorted_players));
		return sorted_players;
	}

	vector<Players> players_;
};
```

---
- Time complexity: O(nlogn)

---
</details>


<details>
<summary> Implement Fast Sorting Algorithm For Lists - Insertion Sort (need to review) </summary>

---
- Implement a routine which sorts lists efficiently

- Must be a stable sort
---

```cpp
// Insertion sort
shared_ptr<ListNode<int>> InsertionSort(const shared_ptr<ListNode<int>>& L) {
	auto dummy_head = make_shared<ListNode<int>>(ListNode<int>{0, L});
	auto iter = L;

	while (iter && iter->next) {
		if (iter->data > iter->next->data) {
			auto target = iter->next, pre = dummy_head;
			while (pre->next->data < target->data) {
				pre = pre->next;
			}

			auto temp = pre->next; // need to draw and check
			pre->next = target;
			iter->next = target->next;
			target->next = temp;
		} else {
			iter = iter->next;
		}
	}
	return dummy_head->next;
}
```

---
- Time complexity: O(n^2)
- Space complexity: O(1)

---
</details>


<details>
<summary> Implement Fast Sorting Algorithm For Lists - Merge Sort </summary>

```cpp
shared_ptr<ListNode<int>> StableSortList(shared_ptr<ListNode<int>> L) {
	if (L == nullptr || L->next == nullptr) {
		return L;
	}

	// find midpoint
	shared_ptr<ListNode<int>> pre_slow = nullptr, slow = L, fast = L;

	while (fast && fast->next) {
		pre_slow = slow;
		fast = fast->next->next, slow = slow->next;
	}

	// split into two lists
	pre_slow->next = nullptr;

	return MergeTwoSortedLists(StableSortList(L), StableSortList(slow));
}
```

---
- Time complexity: O(nlogn)
- Space complexity: O(logn) - max function call stack depth

---
</details>


<details>
<summary> Compute Salary Threshold </summary>

---
- Given an array of salaries and target payroll sum
- Compute salary cap such that salary sum equals the target payroll

---

```cpp
double FindSalaryCap(int target_payroll, vector<int> current_salaries) {
	sort(begin(current_salaries), end(current_salaries));

	double unadjusted_salary_sum = 0.0;

	for (int i = 0; i < size(current_salaries); ++i ) {
		const int adjusted_people = size(current_salaries) - i;
		const double adjusted_salary_sum = current_salaries[i] * adjusted_people;

		if (unadjusted_salary_sum + adjusted_salary_sum >= target_payroll) {
			return (target_payroll - unadjusted_salary_sum) / adjusted_people;
		}

		unadjusted_salary_sum += current_salaries[i];
	}

	return -1.0;
}
```

---
- Time complexity: O(nlogn)

---
</details>
