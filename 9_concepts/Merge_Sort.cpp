// Merge Sort

/*
Divide and conquer algorithm. It uses two functions:
1. Divides until there is one or two items left
2. Merges each array in order

Time complexity:
T(n) = 2T(n/2) + O(n) 
-> O(n*log(n))

Space complexity: O(n) 

Application
- Sorting linked list in O(nlogn)
- Inversion count problem
- External sorting
*/

// code
void merge(int arr[], int l, int m, int r) {
	int i, j, k;
	int n1 = m - l + 1;
	int n2 = r - m;

	int L[n1], R[n2];

	for (i = 0; i < n1; i++)
		L[i] = arr[l + i];

	for (j = 0; j < n2; j++)
		R[j] = arr[m + 1 + j];

	i = 0; // first subarray
	j = 0; // second subarray
	k = l; // merged subarray

	while (i < n1 && j < n2) {
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			i++;
		} else {
			arr[k] = R[j];
			j++;
		}
		k++;
	}
	
	while (i < n1) {
		arr[k] = L[i];
		i++;
		k++;
	}

	while (j < n2) {
		arr[k] = R[j];
		j++;
		k++;
	}
}

void mergeSort(int arr[], int l, int r) {
	if (l < r) {
		int m = l + (r - l) / 2;

		mergeSort(arr, l, m);
		mergeSort(arr, m+l, r);

		merge(arr, l, m, r);
	}
}

int main() {
	int arr[] = {12, 11, 13, 5, 6, 7};
	int arr_size = sizeof(arr) / sizeof(arr[0]);

	mergeSort(arr, 0, arr_size - 1);

	return 0;
}