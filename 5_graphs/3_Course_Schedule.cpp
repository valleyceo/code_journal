// Course Schedule

/*
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
*/

// my solution
class Solution {
    
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<Vertex>vertices(numCourses, Vertex());
        
        for (auto& p : prerequisites) {
            if (vertices[p.first].adj.find(p.second) == vertices[p.first].adj.end()) {
                vertices[p.first].adj.emplace(p.second);
                vertices[p.second].indegree++;
            }
        }
        
        queue<int> q;
        
        for (int i = 0; i < vertices.size(); i++) {
            if (vertices[i].indegree == 0) {
                q.push(i);
            }
        }
        
        int count = 0;
        
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            count++;
            
            for (int i : vertices[cur].adj) {
                if (--vertices[i].indegree == 0) {
                    q.push(i);
                }
            }
        }
        
        return count == numCourses;
    }
    
private:
    struct Vertex { 
    unordered_set<int> adj;
    int indegree;
    Vertex() : indegree(0) {}
    };
};