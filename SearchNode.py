class SearchNode:

    def __init__(self, state=None, action=None, util_value=0):
        self.state = state
        self.action = action
        self.util_value = util_value
        self.children = []
        self.depth = 0
        self.parent = None

    def __str__(self):
        return '<SearchNode %s %s>' % (id(self), self.state)

    def solution(self, initial_state):
        solution = []
        Node = self
        while Node.state != initial_state:
            solution.append(Node.parent.state)
            Node = Node.parent
        solution = solution[::-1]
        return solution
        
    def board(self):
        s = "%s" % self.state
        return s
        

    def is_root(self):
        return True if self.parent == None else False

    def is_terminal(self):
        return True if self.num_children() == 0 else False
    
    def get_depth(self):
        return self.depth

    def num_children(self):
        return len(self.children)

    def get_parent(self):
        return self.parent if self.parent != None else None

    def insert(self, node):
        self.children.append(node)
        node.parent = self
        node.depth = self.depth + 1
   
    #points to ith child
    def child(self, i):
        return self.children[i]

    #remove subtree at child i
    def remove(self, i):
        children[i].parent = None

if __name__ == '__main__':
    print "Testing (0,0) -> (1,0) -> (1,1) by actions ['E', 'S']"
    state00 = (0, 0)
    node00 = SearchNode(state00)
    state01 = (0, 1)
    node01 = SearchNode(state01, node00)
    state11 = (1, 1)
    node11 = SearchNode(state11, node01)
    print(node00)
    print(node01)
    print(node11)
    print(node11.solution(state00))
    print("Expected: ['E', 'S']")
    print node11.board()
