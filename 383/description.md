[link](https://leetcode.com/problems/ransom-note/)

# 383: Ransom Note

**Easy**

**Topics**: Counting, Hash Table, String

Given two strings `ransomNote` and `magazine`, return _`true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise._

Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1
```
ExamInput: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

### Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.