#include <iostream>

// Recursive function for binary search with a call counter
int binarySearch(int arr[], int low, int high, int target, int& count) {
    // Increment the count for each recursive call
    count++;

    // Base case: if low exceeds high, the target is not in the array
    if (low > high) {
        return -1; // Target not found
    }

    // Calculate the middle index
    int mid = low + (high - low) / 2;

    // Check if the target is present at the mid index
    if (arr[mid] == target) {
        return mid; // Target found, return the index
    }

    // If the target is smaller than mid, it can only be in the left subarray
    if (target < arr[mid]) {
        return binarySearch(arr, low, mid - 1, target, count);
    }

    // Otherwise, the target can only be in the right subarray
    return binarySearch(arr, mid + 1, high, target, count);
}

int main() {
    // Example array (must be sorted for binary search to work)
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 10;

    // Initialize the counter
    int count = 0;

    // Call the binary search function
    int result = binarySearch(arr, 0, n - 1, target, count);

    // Output the result
    if (result != -1) {
        std::cout << "Element found at index " << result << std::endl;
    } else {
        std::cout << "Element not found in array" << std::endl;
    }

    // Output the number of recursive calls
    std::cout << "Number of recursive calls: " << count << std::endl;

    return 0;
}