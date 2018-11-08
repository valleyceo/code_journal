# Dynamic Programming

<details>
<summary> Find Max Subarray </summary>

---
- Given an array
- Return a subarray with maximum sum

---

```cpp

int FindMaximumSubarray(const vector<int>& A) {
	int min_sum = 0;
	int running_sum = 0;
	int max_sum = 0;

	for (int i = 0; i < size(A); ++i) {
		running_sum += A[i];
		if (running_sum < min_sum) {
			min_sum = running_sum;
		}

		if (running_sum - min_sum > max_sum) {
			max_sum = running_Sum - min_sum;
		}
	}

	return max_sum;
}

/*
ex. [1 2 3 -3 -3 2 10 -12 3 4]
run [1 3 6  3  0 2 13  1  4 8]
min [1 1 1  1  0 0  0  0  0 0]
max [0 2 5  2  0 2 13  1  4 8] -> max: 13

** not an array, updates every iteration to next step
** similar to stock market. you buy at the lowest running sum and find (running_sum - min)
*/
```

--- 
- Time complexity: O(n)
- Space complexity: O(1)
---
</details>


<details>
<summary> Count the Number of Score Combinations </summary>

---
- Given a final score and scores of individual plays
- Return number of combinations of plays that result in final score

- Example: American football (2,3,7 possible points) with final score of 12
- Solution: {6x2}, {2x3+3x2}, {2x1 + 3x1 + 7x1}, {3x4}

---
```cpp
int NumCombinationsForFinalScore(int final_score, const vector<int>& individual_play_scores) {

	vector<vector<int>> num_combinations_for_score(size(individual_play_scores),
												   vector<int>(final_score + 1, 0));

	for (int i = 0;  i < size(individual_play_scores); ++i) {
		// set begin to 1
		num_combinations_for_score[i][0] = 1; 

		for (int j = 1; j <= final_score; ++j) {
			// add from top row (starting from second row)
			int without_this_play = (i >= 1) ? num_combinations_for_score[i-1][j] : 0;

			// add from j-score step (starting from j column)
			int with_this_play = (j >= individual_play_scores[i]) ?
								 (num_combinations_for_score[i][j - individual_play_scores[i]]) : 0;

			num_combinations_for_score[i][j] = without_this_play + with_this_play;
		}
	}

	return num_combinations_for_score.back().back();
}
```

---
- Time complexity: O(sn), where s is possible scores
- Space complexity: O(sn)
- DP table:  

idx  -> 0 1 2 3 4 5 6 7 8 9 10 11 12  
2    -> 1 0 1 0 1 0 1 0 1 0 1  0  1  
2,3  -> 1 0 1 1 1 1 2 1 2 2 2  2  3  
2,3,7-> 1 0 1 1 1 1 2 2 2 3 3  3  4  

---

</details>

<details>
<summary> Levenshtein Distance </summary>

--- 
- Given two strings
- Compute minimum number of edits needed to transform one to another

---

```cpp
int LevenshteinDistance(const string& A, const string& B) {
	vector<vector<int>> distance_between_prefix(size(A), vector<int> (size(B), - 1));

	return ComputeDistance(A, size(A)-1, B, size(B)-1,
						make_unique<vector<vector<int>>>(size(A), vector<int>(size(B), -1)).get());
}

int ComputeDistance(const string& A, int A_idx, const string& B, int B_idx,
					vector<vector<int>>* ptr) {
	vector<vector<int>>& distance = *ptr;

	// base case
	if (A_idx < 0) {
		return B_idx + 1;
	} else if (B_idx < 0) {
		return A_idx + 1;
	}

	if (distance[A_idx][B_idx] == -1) {
		if (A[A_idx] == B[B_idx]) {
			// skip (move diagonally)
			distance_between_prefix[A_idx][B_idx] = ComputeDistance(A, A_idx-1, B, B_idx-1, ptr);
		} else {
			int substitute_last = ComputeDistance(A, A_idx-1, B, B_idx-1, ptr);
			int add_last = ComputeDistance(A, A_idx-1, B, B_idx, ptr);
			int delete_last = ComputeDistance(A, A_idx, B, B_idx-1, ptr);

			distance[A_idx][B_idx] = 1 + min({substitute_last, add_last, delete_last});
		}
	}

	return distance[A_idx][B_idx];
}
```

---
- Time complexity: O(ab)
- Space complexity: O(ab)
- Recurses from end to beginning

- E table
- Go left (insert), down (delete), diagonal (skip or substitute)
- Count every move except skip (when it is the same letter)

---
</details>


<details>
<summary> Count the Number of Ways To Traverse A 2D Array </summary>

---
- Given a 2D array grid
- Count how many ways you can go from top-left to bottom-right

---

```cpp
int NumberOfWays(int n, int m) {
	return ComputeNumberOfWaysToXY(n-1, m-1, make_unique<vector<vector<int>>>(n, vector<int>(m, 0)).get());
}

int ComputeNumberOfWaysToXY(int x, int y, vector<vector<int>>* number_of_ways_ptr) {
	if (x == 0 && y == 0) {
		return 1;
	}

	vector<vector<int>>& number_of_ways = *number_of_ways_ptr;

	if (number_of_ways[x][y] == 0) {
		// check 
		int ways_top = x == 0 ? 0 : ComputeNumberOfWaysToXY(x-1, y, number_of_ways_ptr);
		int ways_left = y == 0 ? 0 : ComputeNumberOfWaysToXY(x, y-1, number_of_ways_ptr);
		number_of_ways[x][y] = ways_top + ways_left;
	}

	return number_of_ways[x][y];
}
```

---
- Time complexity: O(nm)
- Space complexity: O(nm)
---
</details>


<details>
<summary> Compute Binomial Coefficient </summary>

---
- Compute C(n, k) efficiently
- Make sure it does not overflow
---

```cpp
int ComputeBinomialCoefficient(int n, int k) {
	return ComputeXChooseY{
		n, k, make_unique<vector<vector<int>>>(n+1, vector<int>(k+1, 0)).get();
	}
}

int ComputeXChooseY(int x, int y, vector<vector<int>>* x_choose_y_ptr) {
	if (y==0 || x==y) {
		return 1;
	}

	vector<vector<int>>& x_choose_y = *x_choose_y_ptr;
	if (x_choose_y[x][y] == 0) {
		int without_y = ComputeXChooseY(x-1, y, x_choose_y_ptr);
		int with_y = ComputeXChooseY(x-1, y-1, x_choose_y_ptr);
		x_choose_y[x][y] = without_y + with_y;
	}

	return x_choose_y[x][y];
}
```

---
- Time complexity: O(nk)
- Space complexity: O(nk)

- Key formula: C(n, k) = C(n-1, k) + C(n-1, k-1)
---
</details>


<details>
<summary> Search for a Sequence in a 2D Array (need to review) </summary>

---
- Given a 2D array and a 1D array
- Check if 1D array occurs in the 2D array

---

```cpp
struct HashTuple {
	size_t operator()(const tuple<int, int, int>& t) const {
		return hash<int>()(get<0>(t) ^ get<1>(t) * 1021 ^ get<2>(t) * 1048573)
	}
}

bool IsPatternContainedInGrid(const vector<vector<int>>& grid, const vector<int>& pattern) {
	for (int i = 0; i < size(grid); ++i) {
		for (int j = 0; j < size(grid[i]); ++j) {
			if (IsPatternSuffixContainedStartingAtXY(grid, i, j, pattern, 0, make_unique<unordered_set<tuple<int, int, int>, HashTuple().get())) {
				return true;
			}
		}
	}

	return false;
}


bool IsPatternSuffixContainedStartingAtXY(const vector<vector<int>>& grid, int x, int y, const vector<int>& pattern, int offset, unordered_set<tuple<int, int, int>, HashTuple>* previous_attempts) {
	if (size(pattern) == offset) {
		return true;
	}

	if (x < 0 || x >= size(grid) || y < 0 || y >= size(grid[x]) || 
		previous_attempts->find(make_tuple(x, y, offset)) != cend(*previous_attempts) ||
		grid[x][y] != pattern[offset]) {
		return false;
	}

	if (IsPatternSuffixContainedStartingAtXY(grid, x-1, y, pattern, offset+1, previous_attempts) ||
		IsPatternSuffixContainedStartingAtXY(grid, x+1, y, pattern, offset+1, previous_attempts) ||
		IsPatternSuffixContainedStartingAtXY(grid, x, y-1, pattern, offset+1, previous_attempts) ||
		IsPatternSuffixContainedStartingAtXY(grid, x, y+1, pattern, offset+1, previous_attempts)) {
		return true;
	}

	previous_attempts->emplace(x, y, offset);
	return false;
}
```

---
- Time complexity: O(nm|S|), nxm is the dimension of A, S is the number of call
- get<0>(tuple): returns a reference to the Ith element of tuple
---
</details>


<details>
<summary> Knapsack </summary>

---
- Given a set of items with value and weight
- Select the maximum value that satisfies the weight constraint

---
```cpp
struct Item {
	int weight, value;
}

int OptimumSubjectToCapacity(const vector<Item>& items, int capacity) {
	return OptimumSubjectToItemAndCapacity(items, size(items - 1), capacity,
		make_unique<vector<vector<int>>>(size(items), vector<int>(capacity + 1, -1)).get());
}

// returns optimum value from items[0, k] and have capacity of available_capacity
int OptimumSubjectToItemAndCapacity(const vector<Item>& items, int k,
									int available_capacity,
									vector<vector<int>>* V_ptr) {
	// no items can be chosen
	if (k < 0) {
		return 0;
	}

	// V[i][j] holds the optimum value when we choose from items [0, i] and have capacity of j
	vector<vector<int>>& V = *V_ptr;
	if (V[k][available_capacity] == -1) {
		int without_curr_item = OptimumSubjectToItemAndCapacity(
				items, k - 1, available_capacity, V_ptr);

		int with_curr_item = (available_capacity < items[k].weight) ?
							 0 : items[k].value + OptimumSubjectToItemAndCapacity(
													items, k - 1,
													available_capacity - items[k].weight,
													V_ptr);
		V[k][available_capacity] = max(without_curr_item, with_curr_item);
	}
	return V[k][available_capacity];
}
```

---
- Time complexity: O(nw)
- Space complexity: O(nw)

- Example:
ID Value Weight:  
a 60 5  
b 50 3  
c 70 4  
d 30 2  

- Table:
idx -> 0 1 2  3  4  5  
a   -> 0 0 0  0  0  60  
ab  -> 0 0 0  50 50 60  
abc -> 0 0 0  50 70 70  
abcd-> 0 0 30 50 70 80  

---
</details>


<details>
<summary> Bed Bath And Beyond problem (decompose into dictionary words) </summary>

---
- Given a dictionary set and a string
- Check if the string can be a sequence of dictionary words

---

```cpp
vector<string> DecomposeIntoDictionaryWords(const string& domain, const unordered_set<string>& dictionary) {
	vector<int> last_length(size(domain), -1);

	for (int i = 0; i < size(domain); ++i) { 
		if (dictionary.count(domain.substr(0, i+1))) {
			last_length[i] = i+1;
		}
	}

	if (last_length[i] == -1) {
		for (int j = 0; j < i; ++j) {
			if (last_length[j] != -1 && dictionary.count(domain.substr(j+1, i-j))) {
				last_length[i] = i-j;
				break;
			}
		}
	}

	vector<string> decomposition;
	if (last_length.back() != -1) {
		int idx = size(domain) - 1;
		while (idx >= 0) {
			decompositions.emplace_back(domain.substr(idx+1-last_length[idx], last_length[idx]));
			idx -= last_length[idx];
		}

		reverse(begin(decompositions), end(decompositions));
	}

	return decompositions;
}
```

---
- Time complexity: O(n^3)

---
</details>


<details>
<summary> Find the Minimum Weight Path in Triangle </summary>

---
- Given a triangle of numbers (2D)
- Return minimum path from top to bottom

---

```cpp
int MinimumPathWeight(const vector<vector<int>>& triangle) {
	if (empty(triangle)) {
		return 0;
	}

	vector<int> prev_row(triangle.front()); // first row

	for (int i = 1; i < size(triangle); ++i) {
		vector<int> curr_row(triangle[i]);
		curr_row.front() += prev_row.front(); // first value

		for (int j = 1; j < size(curr_row) - 1; ++j) {
			curr_row[j] += min(prev_row[j-1], prev_row[j]);
		}

		curr_row.back() += prev_row.back(); // last value
		prev_row.swap(curr_row); // current row becomes prev row
	}

	return *min_element(cbegin(prev_row), cend(prev_row));
}
```

---
- Time complexity: O(n^2)
- Space complexity: O(n)

- min_element: returns pointer to the element with smallest value
- vector::cbegin: returns pointer to the first element in the container
---
</details>


<details>
<summary> Pick Up Coins For Maximum Gain </summary>

---
- Given an array of numbers, two players take turns taking one coins from either end
- Design algorithm for computing maximum value for starting player

---

```cpp
int MaximumRevenue(const vector<int>& coins) {
	vector<vector<int>> maximum_revenue_for_range(size(coins), vector<int>(size(coins), 0));
	return ComputeMaximumRevenueForRange(coins, 0, size(coins)-1, make_unique<vector<vector<int>>>(size(coins), vector<int>(size(coins), 0)).get());
}

int ComputeMaximumRevenusForRange(const vector<int>& coins, int a, int b, vector<vector<int>>* maximum_revenue_for_range_ptr) {
	if (a > b) {
		return 0;
	}

	vector<vector<int>>& maximum_revenue_for_range = *maximum_revenue_for_range_ptr;

	if (maximum_revenue_for_range[a][b] == 0) {
		// picks beginning
		int max_revenue_a = coins[a] + 
							min(ComputeMaximumRevenueForRange(coins, a+2, b  , maximum_revenue_for_range_ptr), ComputeMaximumRevenueForRange(coins, a+1, b-1, maximum_revenue_for_range_ptr));
		// picks end
		int max_revenue_b = coins[b] + 
							min(ComputeMaximumRevenueForRange(coins, a+1, b-1, maximum_revenue_for_range_ptr), ComputeMaximumRevenueForRange(coins, a  , b-2, maximum_revenue_for_range_ptr));
		
		maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b);
	}

	return maximum_revenue_for_range[a][b];
}

```

---
- Time complexity: O(n^2)
- Space complexity: O(n^2)

- Using DP of 2D array (n x n of coins)
- Starting from top right and search top right triangle (all up to diagonal coordinate)


---
</details>


<details>
<summary> Count the Number of Moves to Climb Stairs </summary>

---
- You are climbinb up n-stairs and can advance 1 to k steps at a time
- Compute the number of ways to get to the last step

---

```cpp
int NumberOfWaysToTop(int top, int maximum_step) {
	return ComputeNumberOfWaysToH(top, maximum_step, make_unique<vector<int>>(top + 1, 0).get());
}

int ComputeNumberofWaysToH(int h, int maximum_step, vector<int>* number_of_ways_to_h_ptr) {
	if (h <= 1) {
		return 1;
	}

	vector<int>& number_of_ways_to_h = *number_of_ways_to_h_ptr;
	if (number_of_ways_to_h[h] == 0) {
		for (int i = 1; i <= maximum_step && h - i >= 0; ++i) {
			number_of_ways_to_h[h] += ComputeNumberofWaysToH(h-i, maximum_step, number_of_ways_to_h_ptr);
		}
	}

	return number_of_ways_to_h[h];
}
```

---
- Time complexity: O(kn), where k is the time to fill in each entry
- Space complexity: O(n)

- Formula: F(n,k) = sum(F(n-i,k)), i=1,2,...,k
---
</details>


<details>
<summary> The Pretty Printing Problem (need to review) </summary>

---
- Given a set of words to create a paragraph and max line length
- Create a paragraph such that messiness is minimized
- Messiness is measured by sum of number of blanks squared at end of each line

---

```cpp
int MinimumMessiness(const vector<string>& words, int line_length) { 
	vector<int> minimum_messiness(size(words), numeric_limits<int>::max());
	int num_remaining_blanks = line_length - size(words[0]);
	minimum_messiness[0] = num_remaining_blanks * num_remaining_blanks;

	for (int i = 1; i < size(words); ++i) {
		num_remaining_blanks = line_length - size(words[i]);
		minimum_messiness[i] = minimum_messiness[i-1] + num_remaining_blanks * num_remaining_blanks;

		for (int j = i-1; j>= 0; --j) {

			num_remaining_blanks -= (size(words[j]) + 1);
			
			if (num_remaining_blanks < 0) {
				break;
			}

			int first_j_messiness = j-1 < 0 ? 0 : minimum_messiness[j-1];
			int current_line_messiness = num_remaining_blanks * num_remaining_blanks;
			minimum_messiness[i] = min(minimum_messiness[i], first_j_messiness + current_line_messiness);
		}
	}

	return minimum_messiness.back();
}
```

---
- Time complexity: O(nL)
- Space complexity: O(n)

---
</details>


<details>
<summary> Find the Longest Nondecreasing Subsequence </summary>

---
- Given an array of numbers
- Return the length of longest nondecreasing subsequence

- Note: non-decreasing sequence are not required to immediately follow each other (can skip)
- Ex: {0,8,4,12,2,10,6,14,1,9} -> {0,4,10,14} or {0,2,6,9}

---

```cpp
int LongestNondecreasingSubsequenceLength(const vector<int>& A) {
	vector<int> max_length(size(A), 1);
	for (int i = 1; i < size(A); ++i) {
		for (int j = 0; j < i; ++j) {
			if (A[i] >= A[j]) {
				max_length[i] = max(max_length[i], max_length[j]+1);
			}
		}
	}
	return *max_element(begin(max_length), end(max_length));
}
```

---
- Time complexity: O(n^2)
- Space complexity: O(n)

---
</details>

