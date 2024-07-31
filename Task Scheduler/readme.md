You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.

Examples:

1. Input: tasks = ['C', 'E', 'C', 'E', 'E', 'C'], n =2

Output: 8 C, E, Idle, C, E, idle, C, E

2. Input: costs = ['C', 'E', 'C', 'E', 'E', 'C'],n=3

Output: 10

C, E, Idle, Idle, C, E, Idle, Idle, C, E
