# CMPS 2200 Recitation 10## Answers

**Name:** Davis Voelkel
**Name:** Isaiah Kushner


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** With this assumption of n nodes and m edges (x and y in my code), The Work is $W(n) \in O(n+m)$, since the visited set ensures every node and edge is visited just once.

- **4)** Because connectedness requires every pair of nodes u and v to have a path from u to v and v to u, you only have to run reachable() once to determine connectedness so the "worst" case is just 1.

- **5)** This implementation of connected() does an O(1) comparison of O(n*m) reachable() and O(1) set creation of the edges. Therefore, $W(n) \in O(n+m)$.

- **7)** Because we have to scan a row of v nodes for every node, $W(n) \in O(V^2)$.
