from SearchNode import SearchNode

class GameTree:
    def __init__(self, root = None, size = 0, depth = 0):
        self.size = size
        self.depth = depth
        self.root = SearchNode(0) if root == None else root


    def set_size(self, n):
        self.size = n
   
    def __str__(self):
        s = "Root: %s" % id(self.root)
        for cs in self.root.children:
            s = s[:] + "\n\t Node: %s Parent: %s term: %s" % (id(cs), id(cs.parent), cs.is_terminal())
            for i in cs.state:
                s += "\n\t State: %s" % (i) 
            for c in cs.children:
                s = s[:] + "\n\t\t Node: %s Parent: %s term: %s" % (id(c), id(c.parent), c.is_terminal())
                for x in c.state:
                    s += "\n\t\t State: %s" % (x)
        return s

