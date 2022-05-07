"""
LC 269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. If the given input is invalid, return "". If there are multiple valid solutions, return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        nodes = set()
        for word in words:
            for ch in word:
                nodes.add(ch)
        
        graph = defaultdict(set)
        if not self.buildGraph(words, graph):
            return ""  # Error: input is not sorted valid 
        
        for node in nodes:
            if node not in graph:
                graph[node] = set()
                
        return self.topoSort(graph)
    
    def buildGraph(self, words, graph):
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            found = False
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    found = True
                    break
            
            if found == False and len(w1) > len(w2):
                return False
            
        return True
        
    def topoSort(self, graph):
        N = len(graph)
        visited = set()
        visiting = set()
        stack = []
        
        for node in graph.keys():
            if node not in visited:
                if self.dfs(node, graph, visited, visiting, stack):
                    return ""
            
        return "".join(stack[::-1])
        
    def dfs(self, currNode, graph, visited, visiting, stack):
        visited.add(currNode)
        visiting.add(currNode)
        
        for nextNode in graph[currNode]:
            if nextNode in visiting:
                return True  # cyclic graph, return ""
            
            if nextNode not in visited:
                if self.dfs(nextNode, graph, visited, visiting, stack):
                    return True
        
        stack.append(currNode)
        visiting.remove(currNode)