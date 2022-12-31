
class Solution {

    int select(int arr[], int n) {
        // code here such that selectionSort() sorts arr[]

        return arr[n];
    }

    void selectionSort(int arr[], int n) {

        for (int i = 0; i < n - 1; i++) {

            int index = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < select(arr, i)) {
                    index = j;
                }
            }

            if (index != i) {
                int temp = arr[index];
                arr[index] = arr[i];
                arr[i] = temp;
            }
        }
    }
}