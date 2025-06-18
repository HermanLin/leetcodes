# Solution

### Aproach 1: Enumeration

### Intuition

We try every possible number of candies, `x`, that could be distributed to the first child. After, there are `n−x` candies left. At this point, we consider two scenarios:

- If `n−x > limit * 2`, then at least one of the remaining two children must receive more than limit candies. In this case, there is no valid distribution.

- If `n−x <= limit * 2`, then the second child must receive at least `max(0,n−x−limit)` candies to ensure the third child does not receive more than limit candies. At most, the second child can receive `min(limit,n−x)` candies.

For the second case, we can count all valid distributions

### Complexity Analysis

- Time complexity: `O(min(limit, n))`

    We iterate over all possible values of candies that can be given to the first child, which ranges from `0` to `min(limit,n)`. For each such value, we perform constant-time calculations.

- Space complexity: `O(1)`

    Only a few additional variables are needed.

---

### Approach 2: Inclusion-Exclusion Principle

### Intuition

We can also solve this using a classical counting method: subtracting the number of invalid distributions from the total number of possible distributions. By applying the inclusion-exclusion principle, we subtract the number of distributions in which at least one child receives more than `limit` candies. However, in doing so, we may subtract some distributions multiple times - specifically, the ones where *two or more children* receive more than `limit` candies. To correct this, we add back the number of cases where *at least two* children exceed the limit. But now we've overcounted the distributions where *all three* children exceed the limit, so we subtract those again.

Now let's go through each case in detail:

- Total number of unrestricted distributions:

    Since children are allowed to receive zero candies, distributing `n` candies among 3 children is equivalent to placing two dividers among `n` candies to split them into three groups. The number of such distributions is given by the combination:

    C $^{2}$ $_{n+2}$

- At least one child receives more than limit candies:

    We give limit + 1 candies to one child first, reducing the problem to distributing n−(limit+1) candies among 3 children (with possible zeroes). There are 3 choices for which child gets the extra candies, so:

    3 * C $^{2}$ $_{n−(limit+1)+2}$
​
- At least two children receive more than limit candies:

    We give limit + 1 candies to any two children, reducing the problem to distributing n−2×(limit+1) candies among 3 children. There are 3 ways to choose the two children:

    3 * C $^{2}$ $_{n−2×(limit+1)+2}$
​
- All three children receive more than limit candies:

    We give limit + 1 candies to each child, so we're left with n−3×(limit+1) candies to distribute among 3 children. The number of such distributions is:

    C $^{2}$ $_{n−3×(limit+1)+2}$

​
Finally, applying inclusion-exclusion gives the answer:

C $^{2}$ $_{n+2}$  - 3 * C $^{2}$ $_{n−(limit+1)+2}$  + 3 * C $^{2}$ $_{n−2×(limit+1)+2}$  - C $^{2}$ $_{n−3×(limit+1)+2}$
​
### Complexity Analysis

- Time complexity: `O(1)`.

    The result can be calculated directly.

- Space complexity: `O(1)`.

    Only a few additional variables are needed.