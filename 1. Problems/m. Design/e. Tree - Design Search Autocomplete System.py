# 642. Design Search Autocomplete System

'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
'''
class TrieNode:
    def __init__(self):
        self.words = set()
        self.char = None
        self.next = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        node.words.add(word)

        for ch in word:
            if ch not in node.next:
                node.next[ch] = TrieNode()

            node = node.next[ch]
            node.words.add(word)

    def query(self, word: str) -> List[str]:
        node = self.root

        for ch in word:
            if ch not in node.next:
                return []

            node = node.next[ch]

        return node.words

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.wordCount = defaultdict(int)
        self.query = ""

        for i in range(len(sentences)):
            self.trie.addWord(sentences[i])
            self.wordCount[sentences[i]] += times[i]

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.addWord(self.query)
            self.wordCount[self.query] += 1
            self.query = ""
            return []

        self.query += c
        queryWords = self.trie.query(self.query)
        sortedQuery = sorted(queryWords, reverse=False)
        sortedQuery = sorted(sortedQuery, key = lambda word : self.wordCount[word], reverse=True)

        return sortedQuery[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
