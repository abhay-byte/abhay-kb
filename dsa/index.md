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

## Pages

- [**Algorithms**](./algorithms) — Detailed algorithm implementations
- [**Problems**](./problems) — Classic DSA practice problems
