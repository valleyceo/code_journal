#  Binary Search Tree

<details>
<summary> BST Prototype </summary>

---
- Similar to sorted arrays, but efficient in adding and deleting elements
- Look up time of O(logn)

- Avoid mutating objects in BST, always first remove from tree then add

---

```cpp
// structure
template<typename T>
struct BstNode {
	T data;
	unique_ptr<BstNode<T>> left, right;
}

// search
BstNode<int>* SearchBST(const unique_ptr<BstNode<int>>& tree, int key) {
	if (tree == nullptr) {
		return nullptr;
	}

	return tree->data == key ? tree.get() : key < tree->data ? SearchBST(tree->left, key) : SearchBST(tree->right, key);
}
```

---
- Search time complexity: O(h), h is height of tree

---

</details>


<details>
<summary> Test If A Binary Tree Satisfies The BST Property </summary>

---
- Given a binary tree
- Check if the tree satisfies BST property

---

```cpp
bool IsBinaryTreeBST(const unique_ptr<BinaryTreeNode<int>>& tree) {
	return AreKeysInRange(tree, numeric_limits<int>::min(), numeric_limits<int>::max());
}

bool AreKeysInRange(const unique_ptr<BinaryTreeNode<int>>& tree, int low_range, int high_range) {
	if (tree == nullptr) {
		return tree;
	} else if (tree->data < low_range || tree->data > high_range) {
		return false;
	}

	return AreKeysInRange(tree->left, low_range, tree->data) && AreKeysInRange(tree->right, tree->data, high_range);
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Test If A Binary Tree Satisfies The BST Property (Using Queue) </summary>

```cpp
struct QueueEntry {
	const unique_ptr<BinaryTreeNode<int>>& tree_node;
	int lower_bound, upper_bound;
};

bool IsBinaryTreeBST(const unique_ptr<BinaryTreeNode<int>>& tree) {
	queue<QueueEntry> bfs_queue;
	bfs_queue.emplace(QueueEntry{tree, numeric_limits<int>::min(), numeric_limits<int>::max()});

	while (!empty(bfs_queue)) {
		if (bfs_queue.front().tree_node.get()) {
			if (bfs_queue.front().tree_node->data < bfs_queue.front().lower_bound ||
				bfs_queue.front().tree_node->data > bfs_queue.front().upper_bound) {
				return false;
			}

			bfs_queue.emplace(QueueEntry{bfs_queue.front().tree_node->left,
										bfs_queue.front().lower_bound,
										bfs_queue.front().tree_node->data});

			bfs_queue.emplace(QueueEntry{bfs_queue.front().tree_node->right,
										bfs_queue.front().tree_node->data,
										bfs_queue.front().upper_bound});
		}
		bfs_queue.pop();
	}

	return true;
}
```

---
- Time complexity: O(n)
- Space complexity: O(n)

---
</details>


<details>
<summary> Find The First Key Greater Than Given Value in a BST </summary>

---
- Given a BST and a value
- Find the first key that appears in an in-order traversal which is greater than the input value

---

```cpp
BstNode<int>* FindFirstGreaterThanK(const unique_ptr<BstNode<int>>& tree, int k) {
	BstNode<int>*subree = tree.get(), *first_so_far = nullptr;
	while (subtree) {
		if (subtree->data > k) {
			first_so_far = subtree;
			subtree = subtree->left.get();
		} else {
			subtree = subtree->right.get();
		}
	}

	return first_so_far;
}
```

---
- Time complexity: O(h)
- Space complexity: O(1)

---
</details>


<details>
<summary> Find the K Largest Element in BST </summary>

---
- Given a BST and an integer K
- Return the k largest elements in the BST in decreasing order

---

```cpp
vector<int> FindKLargestInBST(const unique_ptr<BstNode<int>>& tree, int k) {
	vector<int> k_largest_element;
	FindKLargestInBSTHelper(tree, k, &k_largest_element);
	return k_largest_element;
}

void FindKLargestInBSTHelper(const unique_ptr<BstNode<int>>& tree, int k, vector<int>* k_largest_element) {
	if (tree && size(*k_largest_element) < k) {
		FindKLargestInBSTHelper(tree->right, k, k_largest_element);
		if (size(*) < k) {
			k_largest_element->emplace_back(tree->data);
			FindKLargestIk_largest_elementnBSTHelper(tree->left, k, k_largest_element);
		}
	}
}
```

---
- Time complexity: O(h + k)

---
</details>


<details>
<summary> Compute the LCA in BST </summary>

---
- Given a BST and two nodes
- Return the LCA of the two nodes

---

```cpp
BstNode<int>* FindLCA(const unique_ptr<BstNode<int>>& tree,
					const unique_ptr<BstNode<int>>& s,
					const unique_ptr<BstNode>>& b) { // node s <= node b
	auto* p = tree.get();
	while (p->data < s->data || p->data > b->data) {
		// both are bigger than the current node
		while (p->data < s->data) {
			p = p->right.get();
		}

		// both are smaller than the current node
		while (p->data > b->data) {
			p = p->left.get();
		}
	}

	return p;
}
```

---
- Time complexity: O(h)
- Space complexity: O(1)

---
</details>


<details>
<summary> Reconstruct a BST from Traversal Data (need to review) </summary>

---
- Given a sequance
- Reconstruct BST

- Note: a sequence <1,2,3> can have five distinct BST
---

```cpp
unique_ptr<BstNode<int>> RebuildBSTFromPreorder(const vector<int>& preorder_sequence) {
	return RebuildBSTFromPreorderHelper(preorder_sequence, 0, size(preorder_sequence));
}

unique_ptr<BstNode<int>> RebuildBSTFromPreorderHelper(const vector<int>& preorder_sequence, int start, int end) {
	if (start >= end) {
		return nullptr;
	}

	int transition_point = distance(cbegin(preorder_sequence), find_if_not(cbegin(preorder_sequence) + start, cend(preorder_sequence),
									[&](int a) { return a <= preorder_sequence[start]; }));

	return make_unique<BstNode<int>> (BstNode<int>{preorder_sequence[start],
										RebuildBSTFromPreorderHelper(preorder_sequence, start + 1, transition_point),
										RebuildBSTFromPreorderHelper(preorder_sequence, transition_point, end)});
}
```

---
- Time complexity: O(n^2) worst case

- find_if_not: returns an iterator to the first element in range which returns 0 (false)
- Example: ```std::find_if_not (foo.begin(), foo.end(), [](int i){return i%2;} );```
---
</details>


<details>
<summary> Rebuild a BST from Traversal Data - Improved (need to review) </summary>

```cpp
unique_ptr<BstNode<int>> RebuildBSTFromPreorder(const vector<int>& preorder_sequence) {
	return RebuildBSTFromPreorderOnValueRange(preorder_sequence, numeric_limits<int>::min(), numeric_limits<int>::max(), make_unique<int>(0).get());
}

unique_ptr<BstNode<int>> RebuildBSTFromPreorderOnValueRange(const vector<int>& preorder_sequence, int lower_bound, int upper_bound, int* root_idx_ptr) {
	int& root_idx = *root_idx_ptr;
	if (root_idx == size(preorder_sequence)) {
		return nullptr;
	}

	int root = preorder_sequence[root_idx];
	if (root < lower_bound || root > upper_bound) {
		return nullptr;
	}

	++root_idx;

	auto left_subtree = RebuildBSTFromPreorderOnValueRange(preorder_sequence, lower_bound, root, root_idx_ptr);
	auto right_subtree = RebuildBSTFromPreorderOnValueRange(preorder_sequence, root, upper_bound, root_idx_ptr);

	return make_unique<BstNode<int>>(BstNode<int>{root, move(left_subtree), move(right_subtree)});
}
```

---
- Time complexity: O(n)

---
</details>


<details>
<summary> Find The Closest Entries in Three Sorted Arrays </summary>

---
- Given three sorted arrays
- Return one minimal interval that contains elements from each arrays

---

```cpp
int FinddClosestElementsInSortedArrays(const vector<vector<int>>& sorted_arrays) {
	int min_distance_so_far = numeric_limits<int>::max();

	struct IterTail {
		vector<int>::const_iterator iter, tail;
	};

	multimap<int, IterTail> iter_and_tail;
	for (const vector<int>& sorted_arrays : sorted_arrays) {
		iter_and_tail.emplace(sorted_arrays.front(), IterTail{cbegin(sorted_arrays), cend(sorted_arrays)});
	}

	while (true) {
		int min_value = cbeing(iter_and_tail)->first;
		int max_value = crbegin(iter_and_tail)->first;

		min_distance_so_far = min(max_value - min_value, min_distance_so_far);

		const auto next_min = next(cbegin(iter_and_tail)->second.iter); // move to the next value
		const auto next_end = cbegin(iter_and_tail)->second.tail; // to check if current element is the last in array

		if (next_min == next_end) {
			return min_distance_so_far;
		}

		iter_and_tail.emplace(*next_min, IterTail{next_min, next_end}); // can emplace to the current since multimap is sorted
		iter_and_tail.erase(cbegin(iter_and_tail));
	}
}
```

---
- Time complexity: O(nlogk)

- next(c++11): returns next pointer of the vector iterator (or more ```auto nx = std::next(it, 2); ```)
- multimap is a map that allows duplicate keys

---
</details>


<details>
<summary> Enumerate Numbers Of the Form a + b * sqrt(2) (need to review) </summary>

---

---

```cpp
struct Number {
	Number(int a, int b) : a(a), b(b), val(a + b * sqrt(2)){}

	int a, b;
	double val;
};

vector<double> GenerateFirstKABSqrt2(int k) {
	vector<Number> cand;
	cand.emplace_back(0, 0);
	int i = 0, j = 0;

	for (int n = 1; n < k; ++n) {
		Number cand_i_plus_1(cand[i].a + 1, cand[i].b);
		Number cand_j_plus_sqrt2(cand[j].a, cand[j].b + 1);
		cand.emplace_back(
			min(cand_i_plus_1, cand_j_plus_sqrt2, [](const Number &a, const &b) { return a.val < b.val; }));
		if (cand_i_plus_1.val == cand.back().val) {
			++i;
		}

		if (cand_j_plus_sqrt2.val == cand.back().val) {
			++j;
		}
	}

	vector<double> result;
	transform(begin(cand), end(cand), back_inserter(result), [](const Number &c) { return c.val; });
	return result;
}
```

---
- Time complexity: O(n)

---
</details>


<details>
<summary> Build a Minimum Height BST From a Sorted Array </summary>

---
- Given a sorted array
- Build a BST of minimum height

---

```cpp
unique_ptr<BstNode<int>> BuildMinHeightBSTFromSortedArray(const vector<int>& A) {
	return BuildMinHeightBSTFromSortedSubArray(A, 0, size(A));
}

unique_ptr<BstNode<int>> BuildMinHeightBSTFromSortedSubArray(const vector<int>& A, int start, int end) {
	if (start >= end) {
		return nullptr;
	}

	int mid = start + ((end - start) / 2);
	return make_unique<BstNode<int>>(BstNode<int> {A[mid], BuildMinHeightBSTFromSortedSubArray(A, start, mid),
															BuildMinHeightBSTFromSortedSubArray(A, mid + 1, end)});
}
```

---
- Time complexity: O(n) - T(n)=2T(n/2)+O(1) -> T(n)=O(n), or in another words, we call O(1) for each elements
- Space complexity: O(h)

---
</details>


<details>
<summary> Test if Three BST Nodes are Totally Ordered (need to review) </summary>

---
- Given two nodes and a middle node in a BST
- Return true if middle node is ordered such that one of the two node is a proper ancester or proper descendant
- Proper means it is not equal to the middle

---

```cpp
bool PairIncludesAncestorAndDescendantOfM(
	const unique_ptr<BstNode<int>>& possible_anc_or_desc_0,
	const unique_ptr<BstNode<int>>& possible_anc_or_desc_1,
	const unique_ptr<BstNode<int>>& middle) {
	auto* search_0 = possible_anc_or_desc_0.get();
	auto* search_1 = possible_anc_or_desc_1.get();

	while (search_0 != possible_anc_or_desc_1.get() && search_0 != middle.get() &&
		   search_1 != possible_anc_or_desc_0.get() && search_1 != middle.get() &&
		   (search_0 || search_1)) {

		if (seach_0) {
			search_0 = search_0->data > middle->data ? search_0->left.get() : search_0->right.get();
		}

		if (search_1) {
			search_1 = search_1->data > middle->data ? search_1->left.get() : search_1->right.get();
		}
	}

	// check if both nodes did not meet middle node or if
	if ((search_0 != middle.get() && search_1 != middle.get()) ||
		search_0 == possible_anc_or_desc_1.get() ||
		search_1 == possible_anc_or_desc_0.get()) {
		return false;
	}

	return SearchTarget(middle, search_0 == middle.get() ? possible_anc_or_desc_1 : possible_anc_or_desc_0)
}

bool SearchTarget(const unique_ptr<BstNode<int>>& from, const unique_ptr<BstNode<int>>& target) {
	auto* iter = from.get();
	while (iter && iter != target.get()) {
		iter = iter->data > target->data ? iter->left.get() : iter->right.get();
	}
	return iter == target.get();
}
```

---
- Time complexity: O(d), d is the difference btw depth of ancestor and descendant

- Process:
	1. Move each nodes to middle until one node equals middle (this will be the ancestor)
	2. Check if there is path to other (descendant)

---
</details>


<details>
<summary> The Range Lookup Problem </summary>

---
- Given a BST and interval
- Return the BST keys that lie in the interval

---

```cpp
struct Interval {
	int left, right;
};

vector<int> RangeLookupInPST(const unique_ptr<BstNode<int>>& tree, const Interval& interval) {
	vector<int> result;
	RangeLookupInBSTHelper(tree, interval, &result);
	return result;
}

void RangeLookupInBSTHelper(const unique_ptr<BstNode<int>>& tree, const Interval& interval, vector<int>* result) {
	if (tree == nullptr) {
		return;
	}

	if (interval.left <= tree->data && tree->data <= interval.right) {
		RangeLookupInBSTHelper(tree->left, interval, result);
		result->emplace_back(tree->data);
		RangeLookupInBSTHelper(tree->right, interval, result);
	} else if (interval.left > tree->data) {
		RangeLookupInBSTHelper(tree->right, interval, result);
	} else {
		RangeLookupInBSTHelper(tree->left, interval, result);
	}
}
```

---
- Time complexity: O(m + h)
- In-order traversal, but skips if the node is not in range of the interval

---
</details>


<details>
<summary> Add Credits (Augmented BST)</summary>

---
- Given a large number of clients to connect to, and each client has a credit (non-negative integer)
- Design a data structure that implements the following methods:
	- Insert, Remove, Lookup, Add-to-all, Max

---

```cpp
class ClientsCreditsInfo {
public:
	void Insert(const string& client_id, int c) {
		Remove(client_id);
		client_to_credit_.emplace(client_id, c - offset_);
		credit_to_clients_[c - offset_].emplace(client_id);
	}

	bool Remove(const string& client_id) {
		if (auto credit_iter = client_to_credit_.find(client_id);
			credit_iter != end(client_to_credit_)) {
			credit_to_clients_[credit_iter->second].erase(client_id);

			if (empty(credit_to_clients_[credit_iter->second])) {
				credit_to_clients_.erase(credit_iter->second);
			}

			client_to_credit_.erase(credit_iter);
			return true;
		}
		return false;
	}

	int Lookup(const string& client_id) const {
		auto credit_iter = client_to_credit_.find(client_id);
		return credit_iter == cend(client_to_credit_) ? -1 : credit_iter->second + offset_;
	}

	void AddAll(int C) {
		offset_ += C;
	}

	string Max() const {
		auto iter = crbegin(credit_to_clients_);
		return iter == crend(credit_to_clients_) || empty(iter->second) ? "" : *cbegin(iter->second);
	}

private:
	int offset_ = 0;
	unordered_map<string, int> client_to_credit_;
	map<int, unordered_set<string>> credit_to_clients_;
}
```

---
- Time complexity: O(logn) insert/remove, O(1) lookup and add-to-all

- Library BST implementations uses caching to perform max O(1) in time
---
</details>
