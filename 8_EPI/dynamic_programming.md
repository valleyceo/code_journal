# Dynamic Programming


<details>
<summary> Find Max Subarray </summary>
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
</details>

<details>
<summary> Count the Number of Score Combinations </summary>
```cpp
int NumCombinationsForFinalScore(int final_score, 
								 const vector<int>& individual_play_scores) {
	vector<vector<int>> num_combinations_for_score(
								size(individual_play_scores), 
								vector<int>(final_score + 1, 0));

	for (int i = 0;  i < size(individual_play_scores); ++i) {
		num_combinations_for_score[i][0] = 1; // one way to reach 0
		
		for (int j = 1; j <= final_score; ++j) {
			int without_this_play = (i >= 1) ? 
						num_combinations_for_score[i-1][j] : 0;

			int with_this_play = (j >= individual_play_scores[i]) ?
						(num_combinations_for_score[i][j - individual_play_scores[i]]) : 0;

			num_combinations_for_score[i][j] = without_this_play + with_this_play;
		}
	}
	return num_combinations_for_score.back().back();
}
```
</details>

<details>
<summary> Knapsack </summary>
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
</details>
