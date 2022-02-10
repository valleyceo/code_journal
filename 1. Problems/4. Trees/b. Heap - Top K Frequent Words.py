# LC 692. Top K Frequent Words

'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heapArr = []
        
        for key, val in count.items():
            heapq.heappush(heapArr, Word(key, val))
        
            if len(heapArr) > k:
                heapq.heappop(heapArr)
        
        res = []
        while heapArr:
            res.append(heapq.heappop(heapArr).word)
        
        return res[::-1]
        
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        
        return self.freq < other.freq