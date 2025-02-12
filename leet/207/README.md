# LeetCode Problem 207 - Course Schedule

## Problem Description
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`. Some courses may have prerequisites, for example, to take course `0` you have to first take course `1`, which is expressed as a pair: `[0, 1]`.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

## Example
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

## Constraints
- The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
- You may assume that there are no duplicate edges in the input prerequisites.

## Solution
To solve this problem, I used Depth-First Search (DFS) or Breadth-First Search (BFS) to detect cycles in a directed graph. If a cycle is detected, it means it is not possible to finish all courses.

## References
- [LeetCode Problem 207](https://leetcode.com/problems/course-schedule/)