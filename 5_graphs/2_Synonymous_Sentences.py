"""
LC 1258. Synonymous Sentences

Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.

Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]

Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
Example 3:

Input: synonyms = [["a","b"],["c","d"],["e","f"]], text = "a c e"
Output: ["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]
Example 4:

Input: synonyms = [["a","QrbCl"]], text = "d QrbCl ya ya NjZQ"
Output: ["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[i][0] != synonyms[i][1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.
"""
class Solution:
    def findParent(self, x: str, parents: dict) -> int:
        if x not in parents:
            parents[x] = x
        
        while x != parents[x]:
            parents[x] = parents[parents[x]]
            x = parents[x]
            
        return x
            
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        parents = {}
        
        for u, v in synonyms:
            pu = self.findParent(u, parents)
            pv = self.findParent(v, parents)
            if pu != pv:
                parents[pv] = pu
                
        parents_to_childrens = defaultdict(list)
        
        for p in parents:
            parents_to_childrens[self.findParent(p, parents)].append(p)
                
        sentences = [""]
        for word in text.split(" "):
            parent = self.findParent(word, parents)
            
            if parent not in parents_to_childrens:
                parents_to_childrens[parent] = [parent]
            
            temp = []
            for sentence in sentences:
                for w in parents_to_childrens[parent]:
                    if len(sentence) > 0:
                        temp.append(sentence + " " + w)
                    else:
                        temp.append(w)
            
            sentences = temp
        
        sentences.sort()
        return sentences