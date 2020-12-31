# Python TreeNode class
INF = 100000000
nINF = -100000000

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
            s = s[:] + "\n\t Node: %s Parent: %s val: %s term: %s" % (id(cs), id(cs.parent), cs.state, cs.is_terminal())
            for c in cs.children:
                s = s[:] + "\n\t\t Node: %s Parent: %s val: %s term: %s" % (id(c), id(c.parent), c.state, c.is_terminal())
        return s


class SearchNode:
    
    '''
    is_root
    is_terminal
    depth
    parent
    to_root
    children []
    insert
    insert_parent
    remove
    remove child
    '''
    
    def __init__(self, state=None, parent=None):
        self.state = state
        self.parent = parent
        self.children = [] 
        self.util_value = 0

    def __str__(self):
        s = "%s" % id(self) 
        return s
    
    def num_children(self):
        return len(self.children)

    def is_root(self):
        return True if self.parent == None else False

    def get_parent(self):
        return self.parent if self.parent != None else None

    def is_terminal(self):
        return True if self.num_children() == 0 else False

    def insert(self, node):
        self.children.append(node)
        node.parent = self
    def child(self, i):
        pass
        #points to ith child

    def remove(self, i):
        pass
        #remove subtree at child i


def minimax(node):
    MAX = max_value(node)
    return MAX

def min_value(node):
    if node.is_terminal():
        print "Terminal: %s" % (node) 
        return node.state
     
    v = INF
    for child in node.children:
        print "Sending child: %s MIN" % child
        v = min(v, max_value(child))
        print v
    return v
 
def max_value(node):
    if node.is_terminal(): 
        print "Terminal: %s" % (node) 
        return node.state
    
    v = nINF
    for child in node.children:
        print "Sending child: %s MAX" % child
        v = max(v, min_value(child))
    return v

if __name__ == '__main__':
    
    T = SearchNode(0)
    T.insert(SearchNode(0))
    T.insert(SearchNode(0))
    T.insert(SearchNode(0))
    
    ls = [11, 11, 8, 14, 19, 12, 13, 11, 8]
    ls.reverse()
    for child in T.children:
        for i in range(3):
            child.insert(SearchNode(ls.pop()))

    tree = GameTree(T, 3, 2)
    print tree 
    print minimax(tree.root)

