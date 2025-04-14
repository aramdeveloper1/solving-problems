def maxSubarraySum(arr, k):
    n = len(arr)

    if k > n or k <= 0:
        return "Invalid Input"

    window_sum = sum(arr[0:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
result = maxSubarraySum(arr, k)
print(f"Maximum subarray sum of size {k}: {result}")  # Output: Maximum subarray sum of size 4: 24