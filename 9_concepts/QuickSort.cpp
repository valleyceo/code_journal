// QuickSort

/*
Divide and Conquer algorithm. Picks an element as pivot and partitions around the point.
Pivot can be picked by: 
- first element
- last element
- random element
- median

Time complexity:
T(n) = T(k) + T(n-k-1) + O(n)

worst case: when partition always picks the greatest or smallest pivot
T(n) = T(0) + T(n-1) + O(n) = T(n-1) + O(n)
-> O(n^2)

best case: when partition always picks the middle element pivot
T(n) = 2T(n/2) + O(n)
-> O(n * log(n))

average case (90% worse):
T(n) = T(n/10) + T(9n/10) + O(n)
-> O(n * log(n))

Space complexity:
O(1) - In-place sort
*/

// my solution
void swap(int* a, int* b) {
	int t = *a;
	*a = *b;
	*b = t;
}

int partition (int arr[], int low, int high) {
	int pivot = arr[high];
	int i = (low - 1);

	for (int j = low; j <= high-1; j++) {
		if (arr[j] <= pivot) {
			i++;
			swap(&arr[i], &arr[j]);
		}
	}


	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

void quickSort(int arr[], int low, int high) {
	if (low < high) {
		int pi = partition(arr, low, high);

		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

int main() {
	int arr[] = {10, 7, 8, 9, 1, 5};
	int n = sizeof(arr) / sizeof(arr[0]);
	quickSort(arr, 0, n-1);

	return 0;
}