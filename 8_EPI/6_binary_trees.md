# Binary Trees

<details>
<summary> Binary Tree Template</summary>

```cpp
template <typename T>
struct BinaryTreeNode {
	T data;
	unique_ptr<BinaryTreeNode<T>> left, right;
}
```

</details>


<details>
<summary> Check Binary Tree is Height Balanced </summary>

---
- Given a root of binary tree
- Check whether the tree is height-balanced

---

```cpp
struct BalancedStatusWithHeight {
	bool balanced;
	int height;
};

bool IsBalanced(const unique_ptr<BinaryTreeNode<int>>& tree) {
	return CheckBalanced(tree).balanced;
}

BalancedStatusWithHeight CheckBalanced(const unique_ptr<BinaryTreeNode<int>>& tree) {
	if (tree == nullptr) {
		return {true, -1};
	}

	auto left_result = CheckBalanced(tree->left);
	if (!left_result.balanced) {
		return {false, 0};
	}

	auto right_result = CheckBalanced(tree->right);
	if (!right_result.balanced) {
		return {false, 0};
	}

	bool is_balanced = abs(left_result.height - right_result.height) <= 1;
	int height = max(left_result.height, right_result.height) + 1;

	return {is_balanced, height};
}
```

---
- Time complexity: O(n)
- Space complexity: O(h) - function call stack corresponds to a unique path from root to node, and therefore it is bounded by height

---
</details>


<details>
<summary> Test if Binary Tree is Symmetric </summary>

---
- The nodes has to be symmetric too

---

```cpp
bool IsSymmetric(const unique_ptr<BinaryTreeNode<int>>& tree) {
	return tree == nullptr || CheckSymmetric(tree->left, tree->right);
}

bool CheckSymmetric(const unique_ptr<BinaryTreeNode<int>& subtree_0,
					const unique_ptr<BinaryTreeNode<int>& subtree_1) {
	if (subtree_0 == nullptr && subtree_1 == nullptr) {
		return true;
	} else if (subtree_0 != nullptr && subtree_1 != nullptr) {
		return CheckSymmetric(subtree_0->left, subtree_1->right) &&
			   CheckSymmetric(subtree_0->right, subtree_1->left);
	}

	return false;
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Compute Lowest Common Ancestor in Binary Tree </summary>

---

---

```cpp
struct Status {
	int num_target_nodes;
	BinaryTreeNode<int>* ancestor;
};

BinaryTreeNode<int>* LCA(const unique_ptr<BinaryTreeNode<int>>& tree,
						 const unique_ptr<BinaryTreeNode<int>>& node0,
						 const unique_ptr<BinaryTreeNode<int>>& node1) {
	return LCAHelper(tree, node0, node1).ancestor;
}

Status LCAHelper(const unique_ptr<BinaryTreeNode<int>>& tree,
				 const unique_ptr<BinaryTreeNode<int>>& node0,
				 const unique_ptr<BinaryTreeNode<int>>& node1) {
	if (tree == nultpr) {
		return {0, nullptr};
	}

	auto left_result = LCAHelper(tree->left, node0, node1);
	if (left_result.num_target_nodes == 2) {
		return left_result;
	}

	auto right_result = LCAHelper(tree->right, node0, node1);
	if (right_result.num_target_nodes == 2) {
		return right_result;
	}

	// compute the number of found nodes (max is alwasy 2)
	int num_target_nodes = left_result.num_target_nodes +
							right_result.num_target_nodes + (tree == node0) +
							(tree == node1);

	return {num_target_nodes, num_target_nodes == 2 ? tree.get() : nullptr};
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Compute LCA when Nodes have Parent Pointers </summary>

```cpp
BinaryTreeNode<int>* LCA(const unique_ptr<BinaryTreeNode<int>>& node0,
						 const unique_ptr<BinaryTreeNode<int>>& node1) {
	BinaryTreeNode<int>*iter0 = node0.get(), *iter1 = node1.get();

	int depth0 = GetDepth(iter0), depth1 = GetDepth(iter1);

	if (depth1 > depth0) {
		swap(iter0, iter1);
	}

	int depth_diff = abs(depth0 - depth1);
	while (depth_diff--) {
		iter0 = iter0->parent;
	}

	while (iter0 != iter1) {
		iter0 = iter0->parent, iter1 = iter1->parent;
	}
	return iter0;
}

int GetDepth(const BinaryTreeNode<int>* node) {
	int depth = 0;
	while (node->parent) {
		++depth, node = node->parent;
	}

	return depth;
}
```

---
- Time complexity: O(h)
- Space complexity: O(1)

---
</details>


<details>
<summary> Sum Root to Leaf </summary>

---
- Given a binary tree with 1 and 0
- find the sum of all binary numbers available from root to leaves
- ex path sum: (11001)\_2

---

```cpp
int SumRootToLeaf(const unique_ptr<BinaryTreeNode<int>>& tree) {
	return SumRootToLeafHelper(tree, 0);
}

int SumRootToLeafHelper(const unique_ptr<BinaryTreeNode<int>>& tree,
						int partial_path_sum) {
	if (tree == nullptr) {
		return 0;
	}

	partial_path_sum = partial_path_sum * 2 + tree->data;
	if (tree->left == nullptr && tree->right == nullptr) {
		return partial_path_sum;
	}

	return SumRootToLeafHelper(tree->left, partial_path_sum) +
		   SumRootToLeafHelper(tree->left, partial_path_sum);
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Find Root to Leaf Path with Specified Sum</summary>

---
- Given a binary tree and an integer value
- return if there exist a path to node where the sum equals to the desired value

---

```cpp
bool HasPathSum(const unique_ptr<BinaryTreeNode<int>>& tree,
				int remaining_weight) {
	if (tree == nullptr) {
		return false;
	} else if (tree->left == nullptr && tree->right == nullptr) {
		return remaining_weight == tree->data;
	}

	return HasPathSum(tree->left, remaining_weight - tree->data) ||
		   HasPathSum(tree->right, remaining_weight - tree->data);
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Design an In-Order-Traversal without Recursion </summary>


```cpp
vector<int> InOrderTraversal(const unique_ptr<BinaryTreeNode<int>>& tree) {
	stack<const BinaryTreeNode<int>*> s;
	const auto* curr = tree.get();
	vector<int> result;

	while (!empty(s) || curr) {
		if (curr) {
			s.push(curr);
			curr= curr->left.get();
		} else {
			curr = s.top();
			s.pop();
			result.emplace_back(curr->data);
			curr = curr->right.get();
		}
	}
	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Implement Pre-order Traversal without Recursion </summary>

```cpp
vector<int> PreorderTraversal(const unique_ptr<BinaryTreeNode<int>>& tree) {
	stack<BinaryTreeNode<int>*> path;
	path.emplace(tree.get());
	vector<int> result;

	while (!path.emtpy()) {
		auto curr = path.top();
		path.pop();

		if (curr != nullptr) {
			result.emplace_back(curr->data);
			path.emplace(curr->left.get());
			path.emplace(curr->right.get());
		}
	}

	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(h)

---
</details>


<details>
<summary> Find Kth Node in Binary Tree</summary>

---
- Given binary tree and integer k
- Find the kth node in the tree in inorder traversal
- Assume that each node stores the number of nodes in subtree

---

```cpp
const BinaryTreeNode<int>* FindKthNodeBinaryTree(const unique_ptr<BinaryTreeNode<int>*> tree, int k) {
	const auto* iter = tree.get();

	while (iter != tree.get()) {
		int left_size = iter->left ? iter->left->size : 0;

		if (left_size + 1 < k) {
			k -= (left_size + 1);
			iter = iter->right.get();
		} else if (left_size == k - 1) {
			return iter;
		} else {
			iter = iter->left.get();
		}

		return nullptr;
	}
}
```

---
- Time complexity: O(h) or O(logn), binary search

---
</details>


<details>
<summary> Compute the Successor </summary>

```cpp
BinaryTreeNode<int>* FindSuccessor(const unique_ptr<BinaryTreeNode<int>>& node) {
	auto* iter = node.get();
	if (iter->right != nullptr) {
		iter = iter-right.get();
		while (iter->left) {
			iter = iter->left.get();
		}
		return iter;
	}

	while (iter->parent != nullptr && iter->parent->right.get() == iter) {
		iter = iter->parent;
	}

	return iter->parent;
}
```

---
- Time complexity: O(h)

---
</details>


<details>
<summary> Implement an Inorder Traversal with O(1) space </summary>

---
- Note that recursion has complexity of O(h)

---

```cpp
vector<int> InOrderTraversal(const unique_ptr<BinaryTreeNode<int>>& tree) {
	BinaryTreeNode<int>*prev = nullptr, *curr = tree.get();
	vector<int> result;

	while (curr != nullptr) {
		BinaryTreeNode<int>* next;

		if (curr->parent == prev) {
			if (curr->left != nullptr) {
				next = curr->left.get();
			} else {
				result.emplace_back(curr->data);
				next = (curr->right != nullptr) ? curr->right.get() : curr->parent;
			}
		} else if (curr->left.get() == prev) {
			result.emplace_back(curr->data);
			next = (curr->right != nullptr) ? curr->right.get() : curr->parent;
		} else {
			next = curr->parent;
		}

		prev = curr;
		curr = next;
	}

	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(1)

---
</details>