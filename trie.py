"""Trie and Node implementations."""


class Node(object):

    """Trie node."""

    def __init__(self, letter, end=False):
        self.letter = letter
        self.children = {}
        self.is_end = end
        self.count = 1 if self.is_end else 0

    def __repr__(self):
        return self.letter


class Trie(object):

    """Trie object."""

    def __init__(self, root):
        self.root = root
        self.numnodes = 1

    def __repr__(self):
        results = sorted(self.bfs(self.root, '', []),
                         key=lambda x: x[1],
                         reverse=True)
        return '\n'.join([str(x) for x in results])

    def __len__(self):
        return self.numnodes

    def insert(self, word):
        """Insert word to trie structure.

        :param word: word to insert
        """
        tmp = self.root

        for idx in range(len(word)):
            char = word[idx]
            if char in tmp.children:
                tmp = tmp.children[char]
                if idx == len(word) - 1:
                    tmp.count += 1
            else:
                self.numnodes += 1
                if idx == len(word) - 1:
                    newnode = Node(char, end=True)
                else:
                    newnode = Node(char)
                tmp.children[char] = newnode
                tmp = tmp.children[char]

        return

    def get_suggestions(self, prefix):
        """Retrieve suggestions for words given a prefix.

        Prefix need not exist.

        :param prefix: string prefix
        :returns: list of tuples such that ('suggestion', freq:int)
        """
        suggestions_exist = True
        tmp = self.root
        for idx in range(len(prefix)):
            char = prefix[idx]
            if char in tmp.children:
                tmp = tmp.children[char]
            else:
                suggestions_exist = False
                break

        if suggestions_exist:
            # bfs for suggestion creation
            results = self.bfs(tmp, '', [])
            # form the result with frequency retained
            with_freq = [(prefix+''.join(suggestion_tup[0]),
                          suggestion_tup[1]) for suggestion_tup in results]
            with_freq.sort(key=lambda x: x[1], reverse=True)
            return with_freq[:3]  # return top 3 most used words
        return []

    def bfs(self, node, prefix, results):
        """Breadth-first-search to get suggestions from trie.

        :param node: Node instance
        :param prefix: prefix so far
        :param results: list of tuples of results so far
        :returns: list of tuples of suggestions, if any
        """
        if node.is_end:
            results.append((prefix, node.count))
            if not node.children:
                return results

        queue = list(node.children.keys())
        while queue:
            child = queue.pop()
            child_node = node.children[child]
            results = self.bfs(child_node, prefix+child, results)

        return results
