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