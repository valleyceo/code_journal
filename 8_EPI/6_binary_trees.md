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