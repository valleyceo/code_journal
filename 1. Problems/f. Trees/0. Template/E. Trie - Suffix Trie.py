# Suffix Trie Implementation
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.build(string)

    def build(self, string):
        
		for i in range(len(string)):
			self.addWord(string[i:])
		
	def addWord(self, string):
		head = self.root
		
		for c in string:
			if c not in head:
				head[c] = {}
			
			head = head[c]
		
		head[self.endSymbol] = True
	
    def contains(self, string):
        head = self.root
		
		for c in string:
			if c not in head:
				return False
			
			head = head[c]
		
		return self.endSymbol in head