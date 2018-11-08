# Recursion

<details>
<summary> Towers of Hanoi </summary>

---
- Given a 3 peg and 6 rings (increasing order) on the first peg
- Move the rings to the second peg
- Other rules: cannot place a larger ring above smaller ring and can move only one ring at a time
---

```cpp
const int kNumPegs = 3;

vector<vector<int>> ComputeTowerHanoi(int num_rings) {
	array<stack<int>, kNumPegs> pegs;

	// init pegs
	for (int i = num_rings; i >= 1; --i) {
		pegs[0].push(i);
	}

	vector<vector<int>> res;

	ComputeTowerHanoiSteps(num_rings, pegs, 0, 1, 2, &result);
}

void ComputeTowerHanoiSteps(int num_rings_to_move,
							array<stack<int>> kNumPegs>& pegs, int from_peg,
							int to_peg, int use_peg,
							vector<vector<int>>* result_ptr){

	if (num_rings_to_move > 0) {
		ComputeTowerHanoiSteps(num_rings_to_move - 1, pegs, from_peg, use_peg,
							    to_peg, result_ptr);
		pegs[to_peg].push(pegs[from_peg].top());
		pegs[from_peg].pop();

		result_ptr->emplace_back(vector<int>{from_peg, to_peg});
		ComputeTowerHanoiSteps(num_rings_to_move - 1, pegs, use_pegs, to_peg,
								from_peg, result_ptr);
	}
}
```

---
- Time complexity: O(2^n)
- Divide into sub-problem
---
</details>


<details>
<summary> N-Queens </summary>

---
- Given n representing n x n chessboard
- Return all distinct nonattacking n queens
---

```cpp
vector<vector<int>> NQueens(int n) {
	vector<vector<int>> res;
	SolveNQueens(n, 0, make_unique<vector<int>>().get, &result);
	return result;
}

void SolveNQueens(int n, int row, vector<int>* col_placement,
				  vector<vector<int>>* result) {
	if (row == n) {
		// all queens are legally placed
		result->emplace_back(*col_placement);
	} else {
		for (int col = 0; col < n; ++col) {
			col_placement->emplace_back(col);
			if (IsValid(*col_placement)) {
				SolveNQueens(n, row+1, col_placement, result);
			}
			col_placement->pop_back();
		}
	}
}

// test if newly placed queen will conflict any earlier queens
// placed before
bool IsValid(const vector<int>& col_placement) {
	int row_id = size(cold_placement) - 1;
	for (int i = 0; i < row_id; ++i) {
		if (int diff = abs(col_placement[i] - col_placement[row_id]);
			diff == 0 || diff = row_id - i) {

			// diff: row difference, row_id-i: col difference
			return false;
		}
	}

	return false;
}
```

---
- Time complexity: conjectured to O(n!/c^n) or super-exponential
---
</details>


<details>
<summary> Permutations </summary>

---
- Given an array of distinct integers
- Generate all permutations of that array
---

```cpp
vector<vector<int>> Permutations(vector<int> A) {
	vector<vector<int>> res;
	DirectedPermutations(0, &A, &res);
	return res;
}

void DirectedPermutations(int i, vector<int> *A_ptr,
						  vector<vector<int>> *result) {
	vector<int> &A = *A_ptr;

	// base case
	if (i == size(A) - 1) {
		result->emplace_back(A); // note the arrow since it is a pointer
		return;
	}

	// Try every possibility for A[i]
	for (int j = i; j < size(A); ++j) {
		swap(A[i], A[j]);
		// generate all permutations for A[i + 1, size(A) - 1]
		DirectedPermutation(i + 1, A_ptr, result);
		swap(A[i], A[j]);
	}
}
```

---
- Time complexity: O(n x n!)
- C(n) = 1 + n * C(n-1) = 1 + n + n(n-1) + n(n-1)(n-2) + ... + !n =~ (e-1)!n (e: euler's number)
---
</details>


<details>
<summary> Permutations (not recursive) </summary>

```cpp
vector<vector<int>> Permutations(vector<int> A) {
	vector<vector<int>> result;

	sort(begin(A), end(A));
	do {
		result.emplace_back(A);
	} while (next_permutation(begin(A), end(A)));
	return result;
}
```

---
- Time complexity: O(n x n!), n! to permute and n to store each one
---
</details>


<details>
<summary> Generate The Power Set </summary>

---
- Given an input set
- Return its power set (all subsets including the input set)
- Example: {0,1,2} -> {null, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}}
---

```cpp
vector<vector<int>> GeneratePowerSet(const vector<int>& input_set) {
	vector<vector<int>> power_set;
	DirectedPowerSet(input_set, 0, make_unique<vector<int>>().get(), &power_set);

	result power_set;
}

void DirectedPowerSet(const vector<int>& input_set, int to_be_selected, vector<int>* selected_so_far,
					  vector<vector<int>>* power_set) {

	if (to_be_selected == size(input_set)) {
		power_set->emplace_back(*selected_so_far);
		return;
	}

	// subsets that contains input
	selected_so_far->emplace_back(input_set[to_be_selected]);
	DirectedPowerSet(input_set, to_be_selected+1, selected_so_far, power_set);

	// subsets that does not contain input
	selected_so_far->pop_back();
	DirectedPowerSet(input_set, to_be_selected+1, selected_so_far, power_set);
}
```

---
- Time complexity: O(2^n)
- Space complexity: O(n * 2^n)
---
</details>


<details>
<summary> Generate The Power Set (non-recursive) </summary>

```cpp
vector<vector<int>> GeneratePowerSet(const vector<int>& input_set) {
	vector<vector<int>> power_set;

	for (int int_for_subset = 0; int_for_subset < (1 << size(input_set)); ++int_for_subset) {
		int bit_array = int_for_subset;
		vector<int> subset;

		while (bit_array) {
			subset_.emplace_back(input_set[log2(bit_array & ~(bit_array - 1))]); // push the first 1
			bit_array &= bit_array - 1; // get the next 1
		}
		power_set.emplace_back(subset);
	}
	return power_set;
}
```

---
- Time complexity: O(n2^n)
- Space complexity: O(n2^n), O(n) for just printing at the end
---
</details>


<details>
<summary> Generate All Subsets of Size K </summary>

---
- Given integer k and n
- Find all subset of size k from set {1, 2, ..., n}
---

```cpp
vector<vector<int>> Combinations(int n, int k) {
	vector<vector<int>> result;
	DirectedCombinations(n, k, 1, make_unique<vector<int>>().get(), &result);
	return result;
}


void DirectedCombinations(int n, int k, int offset, vector<int>* partial_combination, vector<vector<int>>* result) {
	if (size(*partial_combination) == k) {
		result->emplace_back(*partial_combination);
		return;
	}

	const int num_remaining = k - size(*partial_combination);
	for (int i = offset; i <= n && num_remaining <= n - i + 1; ++i) {
		partial_combination->emplace_back(i);
		DirectedCombinations(n, k, i+1, partial_combination, result);
		partial_combination->pop_back();
	}
}
```

---
- Time complexity: O(n(n, k))
---
</details>


<details>
<summary> Generate Strings of Matched Parens (need to review) </summary>

---
- Given an input number
- Generate all strings with that number of pairs of parens (parenthesis)
---

```cpp
vector<string> GenerateBalancedParentheses(int num_pairs) {
	vector<string> result;
	DirectedGenerateBalancedParentheses(num_pairs, num_pairs, "", & result);
	return result;
}

void DirectedGenerateBalancedParentheses(int num_left_parens_needed, int num_right_parens_needed,
										 const string& valid_prefix, vector<string>* result) {
	if (!num_right_parens_needed) {
		result->emplace_back(valid_prefix);
		return;
	}

	if (num_left_parens_needed > 0) {
		DirectedGenerateBalancedParentheses(num_left_parens_needed - 1, num_right_parens_needed,
											valid_prefix + '(', result);
	}

	if (num_left_parens_needed < num_right_parens_needed) {
		DirectedGenerateBalancedParentheses(num_left_parens_needed, num_right_parens_needed - 1,
											valid_prefix + ')', result);
	}
}
```

---
- Time complexity: O((2k)!/((k!(k+1)!)
---
</details>


<details>
<summary> Generate Palindromic Decomposition </summary>

---
- Given a string of characters
- Compute all possible decomposition
- Example: "611116" -> one case is "611", "11", "6"

---

```cpp
vector<vector<string>> PalindromeDecompositions(const string& input) {
	vector<vector<string>> result;
	DirectedPalindromeDecompositions(input, 0, make_unique<vector<string>>().get(), &result);
	return result;
}

void DirectedPalindromeDecompositions(const string& input, int offset, vector<string>* partial_partition,
									  vector<vector<string>>* result) {
	if (offset == size(input)) {
		result->emplace_back(*partial_partition);
		return;
	}
	

	for (int i = offset + 1; i <= size(input); ++i) {
		if (string prefix = input.substr(offset, i - offset); IsPalindrome(prefix)) {
			partial_partition->emplace_back(prefix);
			DirectedPalindromeDecompositions(input, i, partial_partition, result);
			partial_partition->pop_back();
		}
	}
}

bool IsPalindrome(const string& prefix) {
	for (int i = 0, j = size(prefix) - 1; i < j; ++i, --j) {
		if (prefix[i] != prefix[j]) {
			return false;
		}
	}
	return true;
}
```

---
- Time complexity: O(n2^n)
- Same complexity as brute force, but much better best-case (when there are fewer palindromic decomposition)
---
</details>


<details>
<summary> Generate Binary Tree (need to review) </summary>

---
- Given a number
- Return all distinct binary trees with that numbers

---

```cpp
vector<unique_ptr<BinaryTreeNode<int>>> GenerateAllBinaryTrees(int num_nodes) {
	vector<unique_ptr<BinaryTreeNode>>> result;
	if (num_nodes == 0) {
		result.emplace_back(null_ptr);
	}

	for (int num_left_tree_nodes = 0; num_left_tree_nodes < num_nodes; ++num_left_tree_nodes) {
		int num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes;
		auto left_subtrees = GenerateAllBinaryTrees(num_left_tree_nodes);
		auto right_subtrees = GenerateAllBinaryTrees(num_right_tree_nodes);

		for (auto& left : left_subtrees) {
			for (auto& right : right_subtrees) {
				result.emplace_back(make_unique<BinaryTreeNode<int>>(BinaryTreeNode<int>{0, Clone(left), Clone(right)}));
			}
		}
	}
	return result;
}

unique_ptr<BinaryTreeNode<int>> Clone(const unique_ptr<BinaryTreeNode<int>>& tree) {
	return tree ? make_unique<BinaryTreeNode<int>>(BinaryTreeNode<int>{0, Clone(tree->left), Clone(tree->right)}) : nullptr;
}
```

---
- Time complexity: O((2n)!/(n!(n+1)!))

---
</details>


<details>
<summary> Implement Sudoku Solver </summary>

```cpp
const int kEmptyEntry = 0;

bool SolveSudoku(vector<vector<int>>* partial_assignment) {
	return SolvePartialSudoku(0, 0, partial_assignment);
}

bool SolvePartialSudoku(int i, in j, vector<vector<int>>* partial_assignment) {
	if (i == size(*partial_assignment)) {
		i = 0;
		if (++j == size((*partial_assignment)[i])) {
			return true;
		}
	}

	if ((*partial_assignment)[i][j] != kEmptyEntry) {
		return SolvePartialSudoku(i + 1, j, partial_assignment);
	}

	for (int val = 1; val <= size(*partial_assignment); ++val) {
		if (ValidToAddVal(*partial_assignment, i, j, val)) {
			(*partial_assignment)[i][j] = val;

			if (SolvePartialSudoku(i+1, j, partial_assignment)) {
				return true;
			}
		}
	}

	(*partial_assignment)[i][j] = kEmptyEntry;
	return false;
}

bool ValidToAddVal(const vector<vector<int>>& partial_assignment, int i, int j, int val) {

	// check row
	if (any_of(begin(partial_assignment), end(partial_assignment), [val, j](const vector<int>& row) {return val == row[j]; })) {
		return false;
	}

	// check col
	if (find(Begin(partial_assignment[i]), end(partial_assignment[i]), val) != end(partial_assignment[i])) {
		return false;
	}

	int region_size = sqrt(size(partial_assignment));
	int I = i / region_size, J = j / region_size;

	for (int a = 0; a < region_size; ++a) {
		for (int b = 0; b < region_size; ++b) {
			if (val == partial_assignment[region_size * I + a][region_size * J + b]) {
				return false;
			}
		}
	}
	return true;
}
```

---
- No time complexity since it is fixed size board, but exponential
- NP complete

---
</details>


<details>
<summary> Compute a Gray Code (need to review) </summary>

---
- Given a number n
- Return n-bit gray code

- Gray Code: Sequence array where each successive integers differ only by 1 binary (as well as the wrap around)
- Example(n=3): {000,100,101,111,110,010,011,001} -> {0,4,5,7,6,2,3,1} or {0,1,3,2,6,7,5,4}
---

```cpp
vector<int> GrayCode(int num_bits) {
	vector<int> result({0});
	DirectedGrayCode(num_bits, unique_ptr<unordered_set<int>>{new unordered_set<int>{0}}.get(), &result);
	return result;
}

bool DirectedGrayCode(int num_bits, unordered_set<int>* history, vector<int>* result) {
	if (size(*result) == (1 << num_bits)) {
		return DiffersByOneBit(result->front(), result->back());
	}

	for (int i = 0; i < num_bits; ++i) {
		int previous_code = result->back();
		int candidate_next_code = previous_code ^ (1 << i);
		if (!history->count(candidate_next_code)) {
			history->emplace(candidate_next_code);
			result->emplace_back(candidate_next_code);
			if (DirectedGrayCode(num_bits, history, result)) {
				return true;
			}
		}
	}
	return false;
}

bool DiffersByOneBit(int x, int y) {
	int bit_difference = x ^ y;
	return bit_difference && !(bit_difference & (bit_difference - 1));
}
```

---

---
</details>


<details>
<summary> Gray Code (analytical solution) (need to review) </summary>

```cpp
vector<int> GrayCode(int num_bits) {
	if (num_bits == 0) {
		return {0};
	}

	vector<int> gray_code_num_bits_minus_1 = GrayCode(num_bits - 1);

	int leading_bit_one = 1 << (num_bits - 1);
	for (int i = size(gray_code_num_bits_minus_1) - 1; i >= 0; --i) {
		gray_code_num_bits_minus_1.emplace_back(leading_bit_one | gray_code_num_bits_minus_1[i]);
	}

	return gray_code_num_bits_minus_1;
}
```

---
- Time complexity: O(2^n)
---
</details>