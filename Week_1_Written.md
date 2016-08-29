## Alex Ring
## Alri7215
## Alri7215@colorado.edu
## Week 1

# Exercise 2.2
* Exercise 2.2 : For an NxN symmetric adjacency matrix A, describe an algorithm to find connected components. You may wish to examine connected components.m

Answer
--
The easiest way to determine if there are connected components in a graph is to run a depth first search on that graph. By running a DFS from a given node, you are going to visit all of the nodes that it is connected to. So, you could easily have an algorithm that visits and univisted node and starts a DFS from that node. Then, once the DFS finishes, you store the visited nodes as a connected component, C1, C2 ect.. Then the algorithm would look to see if any node has been unvisited if there exists such a node you just repeat the process of:

1. Visit an univisted node in the graph and do a DFS from that node.
2. Record all nodes in the DFS as part of a component.

In the end you would have a list of connected components and their associated nodes.

# Example

To do this with an adjacency matrix you would simply go row by row and do your search. For the example graph from figure 2.2 we have:

0 1 1 0

1 0 1 1

1 1 0 1

0 1 1 0

With the algorithm we would DFS this matrix. We start at row 1 and see that 1 is first connected to 2, we mark 1 as visted and go to row 2. We see 2 is connected to 3 and mark 2 as visited and go to row 3. We see 3 is connected to 1 which has already been visited, we then see that 3 is connected to 4. We mark 3 as visited and go to 4. We see 4 is connected to 2 and 3 which are both visted. We go back to node 2 and see it is connected to node 4 which has been visited. We go back to node 1 and see it is also connected to node 3 which has been visited. All connections in this DFS have been visited and a cycle of our algorithm has been completed. 

We store our visited nodes {1,2,3,4} as a component C1 and then look to start another DFS. The algorithm cannot find any univisted nodes that exist, so it return the component C1 as all connected components in this graph. 