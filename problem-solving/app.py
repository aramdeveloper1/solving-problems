# Question 38 (Sliding Window): Maximum Sum Subarray of Size K
# LeetCode Link: (Not directly a LeetCode Problem but a common interview question to understand sliding window basics)
# Difficulty: Easy
# Description: Given an array of integers arr of size n, and an integer k, find the maximum sum of any contiguous subarray of size k
def maxSubarraySum(arr, k):
    n = len(arr)

    if k > n or k <= 0:
        return "Invalid Input"

    window_sum = sum(arr[0:k])
    print("window_sum: ", window_sum)
    max_sum = window_sum
    print("max_sum: ", max_sum)

    for i in range(k, n):
        print("i: ", i)
        window_sum = window_sum - arr[i-k] + arr[i]
        print("new window_sum: ", window_sum, "arr[i-k]: ", arr[i-k], "arr[i]: ", arr[i])
        max_sum = max(max_sum, window_sum)

    return max_sum

# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# k = 4
# result = maxSubarraySum(arr, k)
# print(f"Maximum subarray sum of size {k}: {result}")  # Output: Maximum subarray sum of size 4: 24



# Question 39 (Vigenere Cipher): Encrypt and Decrypt a message using Vigenere Cipher
# LeetCode Link: (Not directly a LeetCode Problem but a common interview question to understand encryption/decryption basics)
# Difficulty: Easy
# Description: Write a Python function to encrypt and decrypt a message using Vigenere Cipher. The Vigenere Cipher is a polyalphabetic substitution cipher that uses a series of interwoven Caesar ciphers, based on the letters of a keyword. The key is repeated periodically throughout the message. The encryption process involves substituting each letter of the message with the corresponding letter of the keyword, wrapping around to the beginning of the keyword if necessary. The decryption process involves substituting each letter of the message with the corresponding letter of the keyword, wrapping around to the beginning of the keyword if necessary.



def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    result = []
    key_index = 0

    for char in message.lower():
        if char.isalpha():
            shift = alphabet.index(key[key_index % len(key)])
            print("char: ", char, "shift: ", shift)
            index = alphabet.index(char)
            print("index: ", index)
            new_index = (index + shift * direction) % 26
            print("new_index: ", new_index)
            result.append(alphabet[new_index])
            print("result: ", result)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# Example usage
text = 'Aram'
custom_key = 'cde'

# encrypted = encrypt(text, custom_key)
# decrypted = decrypt(encrypted, custom_key)

# print(f'Original text : {text}')
# print(f'Encrypted text: {encrypted}')
# print(f'Decrypted text: {decrypted}')


# Question 40 (Container With Most Water): Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
# LeetCode Link: https://leetcode.com/problems/container-with-most-water/
def max_area(height):
    """
    Calculates the maximum area of water a container can hold.
    """
    left = 0
    right = len(height) - 1
    print("left: ", left, "right: ", right)
    max_area = 0

    while left < right:
        width = right - left
        print("width: ", width)
        print("left: ", left, "right: ", right)
        min_height = min(height[left], height[right])
        print("min_height: ", min_height)
        max_area = max(max_area, min_height * width)
        print("max_area: ", max_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example Usage:
# height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# result1 = max_area(height1)
# print(f"Input: height = {height1}, Output: {result1}")  # Output: Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7], Output: 49

# height2 = [1, 1]
# result2 = max_area(height2)
# print(f"Input: height = {height2}, Output: {result2}") #Output: Input: height = [1, 1], Output: 1

# height3 = [4,3,2,1]
# result3 = max_area(height3)
# print(f"Input: height = {height3}, Output: {result3}") # Output: Input: height = [4, 3, 2, 1], Output: 6


# def product_except_self(nums):
#     """
#     Calculates the product of all elements except self for each element.
#     """
#     n = len(nums)
#     answer = [1] * n  # Initialize an answer list with 1s

#     prefix_product = 1 # calculate the prefix product
#     for i in range(n):
#         answer[i] = prefix_product
#         prefix_product *= nums[i]
#         print("prefix_product: ", prefix_product, "answer: ", answer, "nums[i]: ", nums[i])
#     suffix_product = 1 # calculate the suffix product
#     for i in range(n - 1, -1, -1):
#         answer[i] *= suffix_product
#         suffix_product *= nums[i]
#         print("suffix_product: ", suffix_product, "answer: ", answer, "nums[i]: ", nums[i])

#     return answer

# # Example Usage:
# nums1 = [1, 2, 3, 4]
# result1 = product_except_self(nums1)
# print(f"Input: nums = {nums1}, Output: {result1}") # Output: Input: nums = [1, 2, 3, 4], Output: [24, 12, 8, 6]

def product_except_self(nums):
    # Get the number of elements in the input list
    n = len(nums)

    # Step 1: Initialize the result list
    # Create a list of the same size as 'nums', filled with 1s.
    # We start with 1 because 1 is the multiplicative identity (anything * 1 = itself).
    # This list will eventually hold our final products.
    result = [1] * n
    print(f"Initial result: {result}")

    # Step 2: First Loop - Calculate products of elements to the LEFT
    print("\n--- Starting Left Pass ---")
    # 'left' will store the cumulative product of elements encountered
    # so far, moving from left to right. It starts at 1.
    left = 1
    # Loop through the list from the beginning (index 0) to the end (index n-1)
    for i in range(n):
        print(f"  Iteration i = {i}:")
        # Before updating 'left' for the *next* iteration,
        # the current 'left' value represents the product of all elements
        # strictly to the *left* of index 'i'. Store this in result[i].
        result[i] = left
        print(f"    Set result[{i}] = left ({left}) -> result = {result}")

        # Now, update 'left' by multiplying it with the current element nums[i].
        # This updated 'left' will be used in the *next* iteration's assignment.
        left *= nums[i]
        print(f"    Update left = left * nums[{i}] ({left / nums[i]} * {nums[i]}) -> left = {left}")
        # Included print statement from the original code
        print("left ",left) # This shows the cumulative product including the current element

    print(f"--- Left Pass Complete ---")
    print(f"Result after left pass: {result}") # Shows products of elements to the left of each index

    # Step 3: Second Loop - Calculate products of elements to the RIGHT
    print("\n--- Starting Right Pass ---")
    # 'right' will store the cumulative product of elements encountered
    # so far, moving from right to left. It starts at 1.
    right = 1
    # Loop through the list BACKWARDS, from the end (index n-1) down to the beginning (index 0)
    # range(start, stop, step): starts at n-1, stops *before* -1, steps by -1 (goes backwards)
    for i in range(n - 1, -1, -1):
        print(f"  Iteration i = {i}:")
        # 'right' currently holds the product of all elements strictly to the
        # *right* of index 'i'.
        # result[i] already holds the product of elements to the *left* of 'i'.
        # Multiply result[i] by 'right' to get the final product (left_product * right_product).
        result[i] *= right
        print(f"    Update result[{i}] = result[{i}] * right ({result[i] / right} * {right}) -> result = {result}")
        # Included print statement from the original code
        print("result[i] ", result[i]) # Shows the final value for this index

        # Now, update 'right' by multiplying it with the current element nums[i].
        # This updated 'right' will be used in the *next* iteration (moving left).
        right *= nums[i]
        print(f"    Update right = right * nums[{i}] ({right / nums[i]} * {nums[i]}) -> right = {right}")
        # Included print statement from the original code
        print("right ",right) # This shows the cumulative product including the current element (from the right)

    print(f"--- Right Pass Complete ---")
    print(f"Final result: {result}")

    # Step 4: Return the final result list
    return result

# # Example
# nums = [1, 2, 3, 4]
# print(f"Input nums: {nums}\n")
# final_output = product_except_self(nums)
# print(f"\nFinal Output: {final_output}") # Output: [24, 12, 8, 6]


def climb_stairs(n):
    if n <= 1:
      return 1 # Base cases

    dp = [0] * (n + 1) # initialize an array to store result for sub problems
    
    dp[0] = 1 # base case: there is only 1 way to reach step 0
    dp[1] = 1 # base case: there is only 1 way to reach step 1
    print(f"dp array: {dp}")
    for i in range(2, n + 1):
      print(f"i: {i}", "dp[i-1]: ", dp[i - 1], "dp[i-2]: ", dp[i - 2])
      dp[i] = dp[i - 1] + dp[i - 2] # calculate number of ways to reach current step from previous two steps.

    return dp[n] # number of ways to reach n is stored at last position in dp array

# Example Usage:

# n4 = 4
# result4 = climb_stairs(n4)
# print(f"Input: n = {n4}, Output: {result4}") # Output: Input: n = 4, Output: 5
def coin_change(coins, amount):

    dp = [float('inf')] * (amount + 1) # Initialize dp array with infinity
    print(f"dp array: {dp}")
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    for i in range(1, amount + 1): # Loop for all values from 1 to amount
        for coin in coins: # loop over all coins
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1) # update current value of dp[i] if using coin results in less number of coins

    return dp[amount] if dp[amount] != float('inf') else -1 # return dp[amount] or -1 depending on whether result is present or not

# Example Usage:
# coins1 = [1, 2, 5]
# amount1 = 11
# result1 = coin_change(coins1, amount1)
# print(f"Input: coins = {coins1}, amount = {amount1}, Output: {result1}")  # Output: Input: coins = [1, 2, 5], amount = 11, Output: 3
def longest_increasing_subsequence(nums):
    """
    Calculates the length of the longest increasing subsequence using dynamic programming.
    """
    n = len(nums)
    if n == 0:
      return 0 # base condition

    dp = [1] * n  # Initialize dp array with 1s (every element by itself is of length 1)

    for i in range(1, n): # loop through nums
        for j in range(i): # loop through previous values
            if nums[i] > nums[j]:
                print(f"i: {i}", "j: ", j, "nums[i]: ", nums[i], "nums[j]: ", nums[j])
                print(f"dp[i]: {dp[i]}", "dp[j]: ", dp[j])
                dp[i] = max(dp[i], dp[j] + 1) # update current value from previous value
                print(f"dp[i]: {dp}")
    return max(dp) # return the maximum value in dp array

# Example Usage:
# nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
# result1 = longest_increasing_subsequence(nums1)
# print(f"Input: nums = {nums1}, Output: {result1}") # Output: Input: nums = [10, 9, 2, 5, 3, 7, 101, 18], Output: 4
def house_robber(nums):
    """
    Calculates the maximum amount of money that can be robbed without alerting police, using dynamic programming.
    """
    n = len(nums)
    if n == 0:
        return 0 # base case
    if n == 1:
        return nums[0] # base case
    if n == 2:
        return max(nums[0], nums[1]) # base case

    dp = [0] * n # initialize dp array
    
    dp[0] = nums[0] # for first house
    dp[1] = max(nums[0], nums[1]) # base case for 1st and 2nd house
    print(f"dp array: {dp}")
    for i in range(2, n):
        print(f"i: {i}", "dp[i-1]: ", dp[i - 1], "nums[i]: ", nums[i], "dp[i-2]: ", dp[i - 2])
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2]) # calculation of dp array
        print(f"dp[i]: {dp[i]}")
        print(f"dp array: {dp}")
    return dp[n - 1] # last value in dp array will have max money robbed

# Example Usage:
# nums1 = [1, 2, 3, 1]
# result1 = house_robber(nums1)
# print(f"Input: nums = {nums1}, Output: {result1}")  # Output: Input: nums = [1, 2, 3, 1], Output: 4

# nums2 = [2, 7, 9, 3, 1]
# result2 = house_robber(nums2)
# print(f"Input: nums = {nums2}, Output: {result2}") #Output: Input: nums = [2, 7, 9, 3, 1], Output: 12

# nums3 = [2, 1]
# result3 = house_robber(nums3)
# print(f"Input: nums = {nums3}, Output: {result3}") # Output: Input: nums = [2, 1], Output: 2

# nums4 = [2]
# result4 = house_robber(nums4)
# print(f"Input: nums = {nums4}, Output: {result4}")  # Output: Input: nums = [2], Output: 2

# nums5 = []
# result5 = house_robber(nums5)
# print(f"Input: nums = {nums5}, Output: {result5}")  # Output: Input: nums = [], Output: 0
class ListNode:
    """Represents a node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0) #dummy node to handle base cases
    dummy.next = head
    slow = dummy
    fast = dummy

    for _ in range(n): #advance the fast pointer to n steps
      fast = fast.next

    while fast and fast.next:
        slow = slow.next #move slow pointer
        fast = fast.next #move fast pointer

    slow.next = slow.next.next # remove the node
    return dummy.next # return the modified linked list head

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example Usage:
list1 = [1, 2, 3, 4, 5]
head1 = create_linked_list(list1)
# print("Original list:")
# print_linked_list(head1)
# modified_head1 = remove_nth_from_end(head1, 2)
# print("Modified list:")
# print_linked_list(modified_head1)
# Output:
# Original list:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# Modified list:
# 1 -> 2 ->

def evaluate_rpn(tokens):
    """
    Evaluates an RPN expression.
    """
    stack = [] # initialize the stack
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            print(f"token: {token}, stack: {stack}")
            second_operand = stack.pop() # pop second operand
            first_operand = stack.pop() # pop first operand
            print(f"first_operand: {first_operand}, second_operand: {second_operand}, token: {token}, stack: {stack}")
            if token == "+":
                stack.append(first_operand + second_operand)
                print(f"stack after +: {stack}")
            elif token == "-":
                 stack.append(first_operand - second_operand)
            elif token == "*":
                 stack.append(first_operand * second_operand)
                 print(f"stack after *: {stack}")
            elif token == "/":
              stack.append(int(first_operand / second_operand)) # use int to handle int divison, as requested in question
        else:
            stack.append(int(token))  # push the number in stack
    return stack[0] # return the final result

# Example Usage:
# tokens1 = ["2", "1", "+", "4", "*"]
# result1 = evaluate_rpn(tokens1)
# print(f"Input: tokens = {tokens1}, Output: {result1}") # Output: Input: tokens = ['2', '1', '+', '3', '*'], Output: 9
# def evaluate_2(tokens):
#     stack =[]
#     for token in tokens:
#         if token in ["+", "-", "*", "/"]:
#             second = stack.pop()
#             first = stack.pop()
#             if token == "+":
#                 stack.append(first + second)
#             elif token == "-":
#                 stack.append(first - second)
#             elif token == "*":
#                 stack.append(first * second)
#             elif token == "/":
#                 stack.append(int(first / second))
#         else:
#             stack.append(int(token))
#     return stack[0]