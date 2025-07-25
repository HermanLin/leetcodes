[link](anchor)

# 3: Longest Substring Without Repeating Characters

**Medium**

**Topics**: A,B,C

Given a string `s`, find the length of the **longest substring** without duplicate characters.

Note: A **substring** is a contiguous **non-empty** sequence of characters within a string.

### Example 1
```
ExamInput: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
```

### Example 2
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.