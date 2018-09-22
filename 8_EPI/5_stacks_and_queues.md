# Stacks and Queues

<details>
<summary> Implement a Stack with MAX API </summary>

---
- Design a stack that includes max operation

---

```cpp
class Stack {
public:
	bool Empty() const {
		return empty(element_);
	}

	int Max() const {
		if (Empty()) {
			throw length_error("Max(): empty stack");
		}

		return cached_max_with_count_.top().max;
	}

	int Pop() {
		if (Empty()) {
			throw  length_error("Pop(): empty stack");
		}

		int pop_element = element_.top();
		element_.pop();
		const int current_max = cached_max_with_count_.top().max;
		if (pop_element == current_max) {
			int& max_frequency = cached_max_with_count_.top().count;
			--max_frequency;

			if (max_frequency == 0) {
				cached_max_with_count_.pop();
			}
		}

		return pop_element;
	}

	void Push(int x) {
		element_.emplace(x);
		if (empty(cached_max_with_count_)) {
			cached_max_with_count_.emplace(MaxWidthCount{x, 1});
		} else {
			const int current_max = cached_max_with_count_.top().max;
			if (x == current_max) {
				int& max_frequency = cached_max_with_count_.top().count;
				++max_frequency;
			} else if (x > current_max) {
				cached_max_with_count_.emplace(MaxWidthCount{x, 1});
			}
		}
	}

private:
	stack<int> element_;

	struct MaxWidthCount {
		int max, count;
	};

	stack<MaxWidthCount> cached_max_with_count_;
}
```

---
- Time Complexity: O(1)
- Space Complexity: O(n)

---
</details>


<details>
<summary> Evaluate Reverse Polish Notation (RPN) Expressions </summary>

---
- Compute the arithmetic expression string (in RPN).
- Example:
"1,1,+,-2,x" -> "(1+1)x-2" -> "-4"  
"3,4,+,2,x,1,+" -> "(3+4)x2+1" -> 15

---

```cpp
int Evaluate(const string& expression) {
	stack<int> intermediate_results;
	stringstream ss(expression);
	string token;

	const char kDelimeter = ',';
	const unordered_map<string, function<int(int, int)>> kOperators = {
		{"+", [](int x, int y) -> int { return x + y; }},
		{"-", [](int x, int y) -> int { return x - y; }},
		{"*", [](int x, int y) -> int { return x * y; }},
		{"/", [](int x, int y) -> int { return x / y; }}};

	while (getline(ss, token, kDelimeter)) {
		if (kOperators.count(token)) {
			const int y = intermediate_results.top();
			intermediate_results.pop();
			const int x = intermediate_results.top();
			intermediate_results.pop();
			intermediate_results.emplace(kOperators.at(token)(x, y));
		} else {
			intermediate_results.emplace(stoi(token));
		}
	}

	return intermediate_results.top();
}
```

---
- Time Complexity: O(n)

---
</details>


<details>
<summary> Brackets Well-Formedness </summary>

---
- Given a string with brackets "{,},(,),[,]"
- Check if brackets are all correctly closed.

---

```cpp
bool isWellFormed(const string& s) {
	stack<char> left_chars;
	const unordered_map<char, char> kLookup = {{'(', ')'}, {'{', '}'}, {'[', ']'}};

	for (int i = 0; i < size(s); ++i) {
		if (kLookup.count(s[i])) {
			left_chars.emplace(s[i]);
		} else {
			if (empty(left_chars) || kLookup.at(left_chars.top()) != s[i]) {
				return false;
			}
			left_chars.pop();
		}
	}
	return empty(left_chars);
}
```

---
- Time Complexity: O(n)

---
</details>


<details>
<summary> Normalize Pathnames </summary>

---
- Given a path string
- Return the shortest path
Ex:
- Input: "sc//./../tc/awk/././" -> <"tc", "ack">
- Output: "tc/ack/"
---

```cpp
string ShortestEquivalentPath (const string& path) {
	if (empty(path)) {
		throw invalid_argument("Empty string is not a valid path.");
	}

	vector<string> path_names;

	// starts with "/", which is an absolute path
	if (path.front() == '/') {
		path_names.emplace_back("/");
	}

	stringstream ss(path);
	string token;

	while (getline(ss, token, '/')) {
		if (token == "..") {
			if (empty(path_names) || path_names.back() == "..") {
				path_names.emplace_back(token);
			} else {
				if (path_names.back() == "/") { // "//.." actually works?
					throw invalid_argument("Path error");
				}
				path_names.pop_back();
			}
		} else if (token != "." && token != "") {
			path_names.emplace_back(token);
		}
	}

	string result;
	if (!empty(path_names)) {
		result = path_names.front();
		for (int i = 1; i < size(path_names); ++i) {
			if (i == 1 && result == "/") {
				result += path_names[i];
			} else {
				result += "/" + path_names[i];
			}
		}
	}

	return result;
}
```

---
- Time Complexity: O(n)
- Edge cases: 
1. "/" at the beginning (special case)
2. ".."
	- "../.." and "/.." -> valid
	- {"/", ".."} -> invalid (results to "//..")
3. "///", "/./" is allowed (cd desktop///git works)

---
</details>


<details>
<summary> Compute Buildings with a Sunset View </summary>

---
- Given a sequence of buildings
- Return index of buildings that can see the sunset (east to west)
- Input: [3, 5, 3, 2, 4]
- Output: [1(5), 4(4)]
---

```cpp

vector<int> ExamineBuildingsWithSunset (vector<int>::const_iterator sequence_begin,
										const vector<int>::const_iterator& sequence_end) {
	int building_idx = 0;
	struct BuildingWithHeight {
		int id, height;
	};

	stack<BuildingWithHeight> candidates;
	while (sequence_begin != sequence_end) {
		int building_height = *sequence_begin++;
		while (!empty(candidates) && building_height >= candidates.top().height) {
			candidates.pop();
		}
		candidates.emplace(BuildingWithHeight{building_idx++, building_height});
	}

	vector<int> buildings_with_sunset;

	while (!empty(candidates)) {
		buildings_with_sunset.emplace_back(candidates.top().id);
		candidates.pop();
	}
	return buildings_with_sunset;
}
```

---
- Time complexity: O(n), each element pop and pushed at most once
- Space complexity: O(n)

---
</details>


## Queue

<details>
<summary> Queue Implementation (Using List) </summary>

```cpp
class Queue {
public:
	void Enqueue(int x) { data_.emplace_back(x); }

	int Dequeue() {
		if (empty(data_)) {
			throw length_error("empty queue");
		}

		const int val = data_.front();
		data_.pop_front();
		return val;
	}

	int Max() const {
		if (empty(data_)) {
			throw length_error("cannot perform Max() on empty queue");
		}

		return *max_element(begin(data_), end(data_));
	}

private:
	list<int> data_;
}
```

</details>


<details>
<summary> Binary Tree Nodes in Order of Increasing Depth </summary>

---
- Given a binary tree
- Return arrays consisting keys at the same level

---

```cpp
vector<vector<int>> BinaryTreeDepthOrder (const unique_ptr<BinaryTreeNode<int>>& tree) {
	vector<vector<int>> result;
	if (!tree.get()) {
		return result;
	}

	queue<BinaryTreeNode<int>*> curr_depth_nodes({tree.get()});
	while (!empty(curr_depth_nodes)) {
		queue<BinaryTreeNode<int>*> next_depth_nodes;
		vector<int> this_level;

		while (!empty(curr_depth_nodes)) {
			auto curr = curr_depth_nodes.front();
			curr_depth_nodes.pop();
			this_level.emplace_back(curr->data);

			if (curr->left) {
				next_depth_nodes.emplace(curr->left.get());
			}
			if (curr->right) {
				next_depth_nodes.emplace(curr-right.get());
			}
		}

		result.emplace_back(this_level);
		curr_depth_nodes = next_depth_nodes;
	}

	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(m), m is the max number of nodes at any single depth

---
</details>


<details>
<summary> Circular Queue </summary>

---
- Implement a queue API using array for storing elements

---

```cpp
class Queue {
public:
	Queue(size_t capacity) {}
	explicit Queue(int capacity) : entries_(capacity) {}

	void Enqueue(int x) {
		if (num_queue_elements == size(entries_)) { // Needs to resize
			rotate(begin(entries_), begin(entries_) + head_, end(entries_)); // Makes queue appear consecutively
			head_ = 0, tail_ = num_queue_elements; // Resets head and tail
			entries_.resize(size(entries_) * kScaleFactor); // Doubles size
		}

		entries_[tail_] = x;
		tail_ = (tail_ + 1) % size(entries_); // Circulating index
		++num_queue_elements;
	}

	int Dequeue() {
		if (!num_queue_elements) {
			throw length_error("empty queue");
		}

		--num_queue_elements;
		int result = entries_[head_];
		head_ = (head_ + 1) % size(entries_);
		return result;
	}

	int Size() const {
		return num_queue_elements;
	}

private:
	const int kScaleFactor = 2;
	int head_ = 0, tail_ = 0, num_queue_elements = 0;
	vector<int> entries_;
}
```

---
- Time complexity: O(1) for dequeue, O(1) for enqueue (amortized time complexity)
---
</details>