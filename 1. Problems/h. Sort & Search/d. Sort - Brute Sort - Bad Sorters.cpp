// Bad Sorters

/*
				Best	Average	Worst
Selection Sort  O(n^2)	O(n^2)	O(n^2)
Bubble Sort     O(n)	O(n^2)	O(n^2)
Insertion Sort  O(n)	O(n^2)	O(n^2)

Selection Sort: repeatedly find minimum element and put it at the beginning

Bubble sort: reapetedly swap adjacent elements if they are in wrong order

Insertion sort: repeatedly move the card to the sorted left. similar to how we sort playing cars

*/

// code
void selectionSort(int arr[], int n) {
	int i, j, min_idx;

	for (i = 0; i < n-1; i++) {
		
		min_idx = i;
		for (j = i + 1; j < n; j++)
			if (arr[j] < arr[min_idx])
				min_idx = j;

		swap(&arr[min_idx], &arr[i]);
	}
}

void bubbleSort(int arr[], int n) {
	int i, j;
	bool swapped;

	for (int i = 0; i < n - 1; i++) {
		swapped = false;

		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j+1]) {
				swap(&arr[j], &arr[j+1]);
				swapped = true;
			}
		}

		if (swapped == false)
			break;
	}
}

void insertionSort(int arr[], int n) {
	int i, key, j;

	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i-1;

		while (j >= 0 && arr[j] > key) {
			arr[j+1] = arr[j];
			j--;
		}

		arr[j+1] = key;
	}
}