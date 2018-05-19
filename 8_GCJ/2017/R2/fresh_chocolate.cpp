// Fresh Chocolate

/*
Link: https://code.google.com/codejam/contest/5314486/dashboard

*/
// my solution

// Question:
/*
Problem A. Fresh Chocolate
This contest is open for practice. You can try every problem as many times as you like, though we won't keep track of which problems you solve. Read the Quick-Start Guide to get started.
Small input
6 points	
Solve A-small
Large input
10 points	
Solve A-large
Problem
You are the public relations manager for a chocolate manufacturer. Unfortunately, the company's image has suffered because customers think the owner is cheap and miserly. You hope to undo that impression by offering a free factory tour and chocolate tasting.

Soon after starting the new project, you realized that the company owner's reputation is well-deserved: he only agreed to give away free chocolate if you would minimize the cost. The chocolate to be given away comes in packs of P pieces. You would like to open new packs for each tour group, but the owner insists that if there are leftover pieces from one group, they must be used with the next tour group before opening up any new packs.

For instance, suppose that each pack contains P=3 pieces, and that a tour group with 5 people comes. You will open two packs to give one piece to each person, and you will have one piece left over. Suppose that after that, another tour group with 6 people comes. They will receive the leftover piece, and then you will open two more packs to finish giving them their samples, and so you will have one piece left over again. If two groups with 4 people each come right after, the first of those will get the leftover piece plus a full pack, and the last 4 person group will get their pieces from two newly opened packs. Notice that you cannot open new packs until all leftovers have been used up, even if you plan on using all of the newly opened pack immediately.

In the example above, 2 out of the 4 groups (the first and last groups) got all of their chocolate from freshly opened packs. The other 2 groups got some fresh chocolate and some leftovers. You know that giving out leftovers is not the best way to undo the owner's miserly image, but you had to accept this system in order to get your cheap boss to agree to the project. Despite the unfavorable context, you are committed to doing a good job.

You have requests from N groups, and each group has specified the number of people that will come into the factory. Groups will come in one at a time. You want to bring them in in an order that maximizes the number of groups that get only fresh chocolate and no leftovers. You cannot reject groups, nor have a group get chocolate more than once, and you need to give exactly one piece to each person in each group.

In the example above, if instead of 5, 6, 4, 4, the order were 4, 5, 6, 4, a total of 3 groups (all but the 5 person group) would get only fresh chocolate. For that set of groups, it is not possible to do better, as no arrangement would cause all groups to get only fresh chocolate.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line contains two integers N, the number of groups coming for a tour, and P, the number of pieces of chocolate per pack. The second line contains N integers G1, G2, ..., GN, the number of people in each of the groups.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of groups that will receive only fresh chocolate if you bring them in in an order that maximizes that number.

Limits
1 ≤ T ≤ 100.
1 ≤ N ≤ 100.
1 ≤ Gi ≤ 100, for all i.
Small dataset
2 ≤ P ≤ 3.
Large dataset
2 ≤ P ≤ 4.
Sample

Input 
 	
Output 

3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1

Case #1: 3
Case #2: 4
Case #3: 1
Sample Case #1 is the one explained in the statement. Besides the possible optimal order given above, other orders like 6, 5, 4, 4 also maximize the number of groups with only fresh chocolate, although the groups that get the fresh chocolate are not necesarily the same. Notice that we only care about the number of groups that get the best experience, not the total number of people in them.

In Sample Case #2, the groups are the same as in Case #1, but the packs contain two pieces each. In this case, several ways of ordering them — for instance, 4, 4, 6, 5 — make all groups get only fresh chocolate.

In Sample Case #3, all groups are single individuals, and they will all eat from the same pack. Of course, only the first one to come in is going to get a freshly opened pack.
*/
