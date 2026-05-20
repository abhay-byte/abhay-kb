---
layout: standalone
title: DSA
---

# 📐 Data Structures & Algorithms

A reference guide for essential DSA concepts. Dummy content to get started.

## 🏆 LeetCode Progress

### Quick Stats

[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/Abhay-byte)
[![Rank](https://img.shields.io/badge/Rank-1,084,364-808080?style=for-the-badge)](https://leetcode.com/Abhay-byte)
[![Easy](https://img.shields.io/badge/Easy-62-5CB85C?style=for-the-badge)](https://leetcode.com/Abhay-byte)
[![Medium](https://img.shields.io/badge/Medium-77-F0AD4E?style=for-the-badge)](https://leetcode.com/Abhay-byte)
[![Hard](https://img.shields.io/badge/Hard-7-D9534F?style=for-the-badge)](https://leetcode.com/Abhay-byte)
[![Total](https://img.shields.io/badge/Total%20Solved-146-FFA116?style=for-the-badge)](https://leetcode.com/Abhay-byte)

### Stats Overview

[![LeetCode Stats](https://leetcard.jacoblin.cool/Abhay-byte?theme=nord&font=Noto%20Sans)](https://leetcode.com/Abhay-byte)

### Recent Activity

[![LeetCode Activity](https://leetcard.jacoblin.cool/Abhay-byte?theme=nord&font=Noto%20Sans&ext=activity)](https://leetcode.com/Abhay-byte)

### Practice Heatmap

[![LeetCode Heatmap](https://leetcard.jacoblin.cool/Abhay-byte?theme=nord&font=Noto%20Sans&ext=heatmap)](https://leetcode.com/Abhay-byte)

### Contest Performance

[![LeetCode Contest](https://leetcard.jacoblin.cool/Abhay-byte?theme=nord&font=Noto%20Sans&ext=contest)](https://leetcode.com/Abhay-byte)

---

## ⚡ Codeforces Progress

### Quick Stats

[![Codeforces](https://img.shields.io/badge/Codeforces-445f9d?style=for-the-badge&logo=Codeforces&logoColor=white)](https://codeforces.com/profile/abhay.byte02)
[![Rating](https://img.shields.io/badge/dynamic/json?url=https://codeforces.com/api/user.info?handles=abhay.byte02&query=%24.result%5B0%5D.rating&label=Rating&color=808080&style=for-the-badge&cacheSeconds=86400)](https://codeforces.com/profile/abhay.byte02)
[![Rank](https://img.shields.io/badge/dynamic/json?url=https://codeforces.com/api/user.info?handles=abhay.byte02&query=%24.result%5B0%5D.rank&label=Rank&color=808080&style=for-the-badge&cacheSeconds=86400)](https://codeforces.com/profile/abhay.byte02)
[![Max Rating](https://img.shields.io/badge/dynamic/json?url=https://codeforces.com/api/user.info?handles=abhay.byte02&query=%24.result%5B0%5D.maxRating&label=Max%20Rating&color=445f9d&style=for-the-badge&cacheSeconds=86400)](https://codeforces.com/profile/abhay.byte02)
[![Max Rank](https://img.shields.io/badge/dynamic/json?url=https://codeforces.com/api/user.info?handles=abhay.byte02&query=%24.result%5B0%5D.maxRank&label=Max%20Rank&color=445f9d&style=for-the-badge&cacheSeconds=86400)](https://codeforces.com/profile/abhay.byte02)
[![Solved](https://img.shields.io/badge/Solved-25-445f9d?style=for-the-badge&cacheSeconds=86400)](https://codeforces.com/profile/abhay.byte02)
[![Contests](https://codeforces-readme-stats.vercel.app/api/badge?username=abhay.byte02&theme=dark)](https://codeforces.com/profile/abhay.byte02)

### Profile Overview

[![Codeforces Stats](https://codeforces-readme-stats.vercel.app/api/card?username=abhay.byte02&theme=dark)](https://codeforces.com/profile/abhay.byte02)

---

## Data Structures

### Arrays
- Contiguous memory, O(1) random access
- Insert/delete at end: O(1) amortized
- Insert/delete at arbitrary position: O(n)

### Linked Lists
- **Singly Linked**: each node has data + next pointer
- **Doubly Linked**: each node has data + next + prev pointers
- Operations: search O(n), insert at head O(1), delete O(n)

### Stacks
- LIFO (Last In, First Out)
- Operations: push, pop, peek — all O(1)
- Use cases: undo/redo, expression evaluation, DFS

### Queues
- FIFO (First In, First Out)
- Operations: enqueue, dequeue, front — all O(1)
- Variants: circular queue, deque, priority queue

### Hash Tables
- Key-value storage, average O(1) operations
- Collision resolution: chaining, open addressing
- Load factor determines resizing threshold

### Trees
| Type | Description |
|------|-------------|
| Binary Tree | Each node has ≤2 children |
| BST | Left < root < right; search O(log n) avg |
| AVL Tree | Self-balancing BST (height diff ≤1) |
| Red-Black Tree | Self-balancing with color constraints |
| Heap | Complete binary tree, min/max at root |
| Trie | Prefix tree for strings |

### Graphs
- **Representation**: adjacency matrix (O(V²) space), adjacency list (O(V+E) space)
- **Traversal**: BFS (queue, level-order), DFS (stack/recursion, depth-order)
- **Applications**: shortest path, connectivity, topological sort

## Algorithms

### Sorting
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

### Searching
- **Linear Search**: O(n)
- **Binary Search**: O(log n) — requires sorted array

### Graph Algorithms
- BFS / DFS — O(V+E) traversal
- Dijkstra's — shortest path, O((V+E) log V)
- Bellman-Ford — handles negative edges, O(VE)
- Floyd-Warshall — all-pairs shortest path, O(V³)
- Kruskal's / Prim's — MST, O(E log V)
- Topological Sort — DAG ordering, O(V+E)

### Dynamic Programming
- Optimal substructure + overlapping subproblems
- Top-down (memoization) vs bottom-up (tabulation)
- Classic problems: Fibonacci, Knapsack, LCS, LIS, Edit Distance

### String Algorithms
- KMP — pattern matching, O(n+m)
- Rabin-Karp — rolling hash, average O(n+m)
- Z-Algorithm — pattern matching, O(n)
- Manacher's — longest palindromic substring, O(n)

## Complexity Reference

| Notation | Name | Description |
|----------|------|-------------|
| O(1) | Constant | Direct access |
| O(log n) | Logarithmic | Binary search, balanced trees |
| O(n) | Linear | Single pass |
| O(n log n) | Linearithmic | Efficient sorting |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive subsets |
| O(n!) | Factorial | Permutations |

## Practice Sheets

- [**LeetCode**](./leetcode) — Solved LeetCode problems
- [**Codeforces**](./codeforces) — Codeforces problem archive by rating
- [**CSES**](./cses) — CSES Problem Set (300+ problems)
- [**CP-31**](./cp31) — TLE Eliminators CP-31 sheet (372 problems)
- [**NeetCode**](./neetcode) — NeetCode 150 roadmap
