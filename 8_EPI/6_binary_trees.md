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