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