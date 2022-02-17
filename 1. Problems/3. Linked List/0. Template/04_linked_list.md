

<details>
<summary> Remove the Kth Last Element From List </summary>

---
- Given a singly linked list and integer k
- Remove the Kth last element from the list

---

```cpp
// Assumes L has at least k nodes, deletes the k-th last node in L
shared_ptr<ListNode<int>> RemoveKthLast(const shared_ptr<ListNode<int>>& L, int k) {
	auto dummy_head = make_shared<ListNode<int>>(ListNode<int>{0, L});
	auto first = dummy_head->next;

	while (k--) {
		first = first->next;
	}

	auto second = dummy_head->next;
	while (first) {
		second = second->next;
		first = first->next;
	}

	// remove node
	second->next = second->next->next;
	return dummy_head->next;
}
```

---
- Time complexity: O(n)
- Space complexity: O(1)

---
</details>


<details>
<summary> Remove Duplicates from a Sorted List</summary>


```cpp
shared_ptr<ListNode<int>> RemoveDuplicates (const shared_ptr<ListNode<int>>& L) {
	auto iter = L;

	while (iter) {
		auto next_distinct = iter->next;

		while (next_distinct && next_distinct->data == iter->data) {
			next_distinct = next_distinct->next;
		}

		iter->next = next_distinct;
		iter = next_distinct;
	}
}
```

---
- Time Complexity: O(n)
- Space Complexity: O(1)

---
</details>


<details>
<summary> Cyclic Shift </summary>

---
- Given singly linked list and nonnegative integer k
- Return the list cyclically shifted to the right by k

- Can assume k < n since k = k % n
---

```cpp
shared_ptr<ListNode<int>> CyclicallyRightShiftList(const shared_ptr<ListNode<int>> L, int k) {
	if (L == nullptr) {
		return L;
	}

	// Computes the length of L and the tail
	auto tail = L;
	int n = 1;
	while (tail->next) {
		++n, tail = tail->next;
	}

	k %= n;
	if (k == 0) {
		return L;
	}

	tail->next = L; // makes a cycle by connecting the tail to the head
	int steps_to_new_head = n - k;
	auto new_tail = tail;
	while (steps_to_new_head--) {
		new_tail = new_tail->next;
	}

	auto new_head = new_tail->next;
	new_tail->next = nullptr;
	return new_head;
}
```

---
- Time Complexity: O(n)
- Space Complexity: O(1)

---
</details>


<details>
<summary> Even-Odd Merge </summary>

---
- Given a singly linked list
- Reorder the list such that the list is ordered in following:

Input:
L -> L0 -> L1 -> L2 -> L3 -> L4

Output:
L -> L0 -> L2 -> L4 -> L1 -> L3

---

```cpp
shared_ptr<ListNode<int>> EvenOddMerge(cons shared_ptr<ListNode<int>>& L) {
	if (L == nullptr) {
		return L;
	}

	auto even_dummy_head = make_shared<ListNode<int>>{0, nullptr};
	auto odd_dummy_head = make_shared<ListNode<int>>{0, nullptr};
	array<shared_ptr<ListNode<int>>, 2> tails = {even_dummy_head, odd_dummy_head};

	int turn = 0;

	for (auto iter = L; iter; iter = iter->next) {
		tails[turn]->next = iter;
		tails[turn] = tails[turn]->next;
		turn ^= 1;
	}

	tails[1]->next = nullptr;
	tails[0]->next = odd_dummy_head->next;
	return even_dummy_head->next;
}
```

---
- Time Complexity: O(n)
- Space Complexity: O(1)

---
</details>


<details>
<summary> Check if Singly List is Palindromic </summary>

---

---

```cpp
bool IsLinkedListAPalindrome(shared_ptr<ListNode<int>> L) {
	shared_ptr<ListNode<int>> slow = L, fast = L;

	while (fast && fast->next) {
		fast = fast->next->next;
		slow = slow->next;
	}

	auto first_half_iter = L;
	auto second_half_iter = ReverseLinkedList(slow);

	while (second_half_iter && first_half_iter) {
		if (second_half_iter->data != first_half_iter->data) {
			return false;
		}

		first_half_iter = first_half_iter->next;
		second_half_iter = second_half_iter->next;
	}

	return true;
}
```

---
- Time Complexity: O(n)
- Space Complexity: O(1)

---
</details>


<details>
<summary> List Pivoting </summary>

---
- Given a singly linked list and a node within list with value k
- Pivot the list such that all nodes smaller than k are on left and larger than k on the right.
- Ex:
Input:
L->3->2->2->11->7->5->11
Output:
L->3->2->2->5->7->11->11

---

```cpp
shared_ptr<ListNode<int>> ListPivoting(const shared_ptr<ListNode<int>>& L, int x) {

	shared_ptr<ListNode<int>> less_head(new ListNode<int>),
							  equal_head(new ListNode<int>),
							  greater_head(new ListNode<int>);
	shared_ptr<ListNode<int>> less_iter = less_head,
							  equal_iter = equal_head,
							  greater_head = greater_head;

	shared_ptr<ListNode<int>> iter = 1;

	while(iter) {
		AppendNode(&iter, iter->data < x ? &less_iter : iter->data == x ? &equal_iter : &greater_iter);
	}

	greater_iter->next = nullptr;
	equal_iter->next = greater_head->next;
	less_iter->next = equal_head->next;

	return less_head->next;
}
```

---
- Time Complexity: O(n)
- Space Complexity: O(1)

---
</details>


<details>
<summary> Add List-Based Integers </summary>

---
- Given two singly linked list representing digits (least significant digit comes first)
- Return list of sum
- Ex:

Input
L1->3->1->4
L2->7->0->9

Output
L->0->2->3->1

---

```cpp
shared_ptr<ListNode<int>> AddTwoNumbers(shared_ptr<ListNode<int>>L1,
										shared_ptr<ListNode<int>>L2) {
	shared_ptr<ListNode<int>> dummy_head(new ListNode<int>);
	auto place_iter = dummy_head;
	int carry = 0;

	while (L1 || L2 || carry) {
		int val = carry + (L1 ? L1->data : 0) + (L2 ? L2->data : 0);
		L1 = L1 ? L1->next : nullptr;
		L2 = L2 ? L2->next : nullptr;

		place_iter->next = make_shared<ListNode<int>>(ListNode<int>(val % 10, nullptr));
		carry /= 10;
		place_iter = place_iter->next;
	}

	return dummy_head->next;
}

```

---
- Time Complexity: O(n+m)
- Space Complexity: O(max(n, m))

---
</details>
