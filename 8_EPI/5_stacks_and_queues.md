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
		return empty(element_with_cached_max);
	}

	int Max() const {
		if (Empty()) {
			throw length_error("Max(): empty stack");
		}

		return element_with_cached_max_.top().max;
	}

	int Pop() {
		if (Empty()) {
			throw  length_error("Pop(): empty stack");
		}

		int pop_element = element_with_cached_max_.top().element;
		element_with_cached_max_.pop();
		return pop_element;
	}

	void Push(int x) {
		// cache the maximum stored at or below that entry
		element_with_cached_max_.emplace(ElementWithCachedMax{x, max(x, Empty() ? x : Max())});
	}

private:
	struct ElementWithCachedMax {
		int element, max;
	};

	stack<ElementWithCachedMax> element_with_cached_max_;
}
```

---
- Time Complexity: O(1)
- Space Complexity: O(n)

---
</details>