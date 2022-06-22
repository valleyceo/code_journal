# LC 1948. Delete Duplicate Folders in System

'''
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z
However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
'''


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.deleted = False

    def addWord(self, word):
        curr = self

        for c in word:
            curr = curr.child[c]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        def serialize(root, seen):
            if not root.child:
                return ""

            keys = []

            for c, child in root.child.items():
                keys.append(c + ":" + serialize(child, seen))

            key = "(" + "".join(keys) + ")"
            seen[key].append(root)
            return key

        def dfsGetValidPaths(node, path, out):

            for c, child in node.child.items():
                if not child.deleted:
                    out.append(path + [c])
                    dfsGetValidPaths(child, path + [c], out)

        root = TrieNode()
        visited = defaultdict(list)

        for p in sorted(paths):
            root.addWord(p)

        serialize(root, visited)

        for nodes in visited.values():
            if len(nodes) >= 2:
                for node in nodes:
                    node.deleted = True

        res = []
        dfsGetValidPaths(root, [], res)

        return res

"""
Note:
- Source: https://leetcode.com/problems/delete-duplicate-folders-in-system/discuss/1365324/Python-Trie-and-Serialize-subtrees-Clean-and-Concise
"""
