[link](https://leetcode.com/problems/max-consecutive-ones-iii/description/)

# 1004: Max Consecutive Ones III

**Medium**

**Topics**: Array, Binary Search, Prefix Sum, Sliding Window

Given a binary array `nums` and an integer `k`, return _the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s_

### Example 1
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Example 2
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`
- `0 <= k <= nums.length`