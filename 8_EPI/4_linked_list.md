# Linked List

<details>
<summary> Linked List Manipulation </summary>

```cpp
// init
template <typename T>
struct ListNode {
	T data;
	shared_ptr<ListNode<T>> next;
}

// search
shared_ptr<ListNode<int>> SearchList(shared_ptr<ListNode<int>> L, int key) {
	while (L && L->data != key) {
		L = L->key;
	}

	return L;
}

// insert a node
void InsertAfter(const shared_ptr<ListNode<int>>& node,
				 const shared_ptr<ListNode<int>>& new_node) {
	new_node->next = node->next;
	node->next = new_node;
}

// delete a node
void DeleteAfter(const shared_ptr<ListNode<int>>& node) {
	node->next = node->next->next;
}

```

</details>


<details>
<summary> Merge Two Sorted Lists </summary>

```cpp
shared_ptr<ListNode<int>> MergeTwoSortedLists(shared_ptr<ListNode<int>> L1,
											  shared_ptr<ListNode<int>> L2) {
	shared_ptr<ListNode<int>> dummy_head(new ListNode<int>);
	auto tail = dummy_head;

	while (L1 && L2) {
		AppendNode(L1->data <= L2->data ? &L1 : &L2, &tail);
	}

	tail->next = L1 ? L1 : L2;
	return dummy_head->next;
}

void AppendNode(shared_ptr<ListNode<int>> *node,
				shared_ptr<ListNode<int>> *tail) {
	(*tail)->next = *node;
	*tail = *node;
	*node = (*node)->next;
}

```

---
- time: O(n)
---
</details>


<details>
<summary> Reverse Single Sublist (need to review) </summary>

---
- given a singly linked list L, and two integers s and f
- reverse order from sth node to fth node

---

```cpp
shared_ptr<ListNode<int>> ReverseSublist(shared_ptr<ListNode<int>> L,
										 int start, int finish) {
	auto dummy_head = make_shared<ListNode<int>>(ListNode<int>{0, L});
	auto sublist_head = dummy_head;

	int k = 1;
	while (k++ < start) {
		sublist_head = sublist_head->next;
	}

	auto sublist_iter = sublist_head->next;
	while (start++ < finish) {
		auto temp = sublist_iter->next;
		sublist_iter->next = temp->next;
		temp->next = sublist_head->next;
		sublist_head->next = temp;
	}

	return dummy_head->next;
}
```

---
- time: O(f)

---
</details>


<details>
<summary> Test Cyclicity </summary>

```cpp
shared_ptr<ListNode<int>> HasCycle(const shared_ptr<ListNode<int>>& head) {
	shared_ptr<ListNode<int>> fast = head, slow = head;

	while (fast && fast->next) {
		slow = slow->next, fast = fast->next->next;

		if (slow == fast) {
			int cycle_len = 0; // n

			do {
				++cycle_len;
				fast = fast->next;
			} while (slow != fast);

			auto cycle_len_advanced_iter = head;
			while (cycle_len--) {
				cycle_len_advanced_iter = cycle_len_advanced_iter->next;
			}

			auto iter = head;

			while (iter != cycle_len_advanced_iter) {
				iter = iter->next;
				cycle_len_advanced_iter = cycle_len_advanced_iter->next;
			}

			return iter;
		}
	}

	return nullptr; // no cycle
}

// using Floyd's algorithm
shared_ptr<ListNode<int>> HasCycle(const shared_ptr<ListNode<int>>& head) {
	shared_ptr<ListNode<int>> fast = head, slow = head;

	while (fast && fast->next && fast->next->next) {
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast) {
			slow = head;

			while (slow != fast) {
				slow = slow->next;
				fast = fast->next;
			}

			return slow;
		}
	}

	return nullptr;
}
```

---
- Floyd's algorithm (https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work)
- full equation: i = m + p*n + k
- after derivation: m + k = q * n -> m = q*n - k
- time: O(n)

---
</details>