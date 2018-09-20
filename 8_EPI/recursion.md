i# Recursion
--

<details>
<summary> Towers of Hanoi </summary>

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
</details>

<details>
<summary> N-Queens </summary>

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
			// column or diagonal constraint is violated;
			return false;
		}
	}

	return false;
}
```
</details>

<details>
<summary> Permutations </summary>

```cpp
vector<vector<int>> Permutations(vector<int> A) {
	vector<vector<int>> res;
	DirectedPermutations(0, &A, &res);
	return res;
}

void DirectedPermutations(int i, vector<int> *A_ptr,
						  vector<vector<int>> * result) {
	vector<int> &A = *A_ptr;

	// base case
	if (i == size(A) - 1) {
		result->emplace_back(A);
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

</details>	
