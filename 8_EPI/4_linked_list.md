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
	(*tail)->next = *node; // connect
	*tail = *node; // update tail to next node
	*node = (*node)->next; // update node to next node
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


<details>
<summary> Test for Overlapping List (no cycles) </summary>

---
Given two cycle-free singly linked list
Determine if there exists a node that is common to both lists.

---

```cpp
shared_ptr<ListNode<int>> OverlappingNoCycleLists(
	shared_ptr<ListNode<int>> l0, shared_ptr<ListNode<int>> l1) {
	int l0_len = Length(l0), l1_len = Length(l1);

	AdvanceListByK(abs(l0_len - 1l_len), l0_len > l1_len ? &l0 : &l1);

	while (l0 && l1 && l0 != l1) {
		l0 = l0->next, l1 = l1->next;
	}
}

int Length(shared_ptr<ListNode<int>> L) {
	int length = 0;
	while (L) {
		++length, L = L->next;
	}

	return length;
}

void AdvanceListByK(int k, shared_ptr<ListNode<int>>* L) {
	while (k--) {
		*L = (*L)->next;
	}
}

```

---
time complexity: O(n)
space complexity: O(1)

---
</details>


<details>
<summary> Test for Overlapping List 2 (may have cycles) </summary>

---
Given two cycle-free singly linked list
Determine if there exists a node that is common to both lists.

- each linked list may have cycles
- there can be multiple point of merge (another one after a cycle)
---

```cpp
shared_ptr<ListNode<int>> OverlappingLists(shared_ptr<ListNode<int>> l0,
										   shared_ptr<ListNode<int>> l1) {
	auto root0 = HasCycle(l0), root1 = HasCycle(l1);

	if (!root0 && !root1) {
		return OverlappingNoCycleLists(l0, l1);
	} else if ((root0) && !root1) || (!root0 && root1) {
		return nullptr;
	}

	auto temp = root1;
	do {
		temp = temp->next;
	} while (temp != root0 && temp != root1);

	if (temp != root0) {
		return nullptr;
	}

	int stem0_length = Distance(l0, root0), stem1_length = Distance(l1, root1);
	AdvanceListByK (abs(stem0_length - stem1_length),
					stem0_length > stem1_length ? &l0 : &l1);

	while (l0 != l1 && l0 != root0 && l1 != root1) {
		l0 = l0->next, l1 = l1->next;
	}

	return l0 == l1 ? l0 : root0;
}

// calculates distance between a and b
int Distance(shared_ptr<ListNode<int>> a, shared_ptr<ListNode<int>> b) {
	int dis = 0;
	while (a != b) {
		a = a->next, ++dis;
	}

	return dis;
}
```

---
Time complexity: O(n)
Space complexity: O(n)

- If one list is cyclic and overlaps, the other list must be cyclic.
- If they are cycle and overlap, both lists will have same root node.

---
</details>


<details>
<summary> Delete a Node from a Singly Linked List </summary>

```cpp
void DeletionFromList(const shared_ptr<ListNode<int>>& node_to_delete) {
	node_to_delete->data = node_to_delete->next->data;
	node_to_delete->next = node_to_delete->next->next;
}
```

---
Time complexity: O(1)

---
</details>


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