[link](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/?envType=daily-question&envId=2025-06-04)

# 3170: Lexicographically Minimum String After Removing Stars

**Medium**

**Topics**: Hash Table, Heap (Priority Queue), Greedy, Stack, String

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

- Delete the leftmost `'*'` and the smallest non-`'*'` character to its left. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all `'*'` characters.

### Example 1
```
Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.
```

### Example 2
```
Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.
```

### Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters and `'*'`.
- The input is generated such that it is possible to delete all `'*'` characters.