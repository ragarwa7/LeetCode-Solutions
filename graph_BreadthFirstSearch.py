import Queue
class GraphNode:
    def __init__(self,value):
        self.val = value
        self.neighbors = None
        self.visited = False
        
    def neigbhors(self, neighbors):
        self.neighbors = neighbors

def breadthFirstSearch(root, val):
    s = None
    if root.val == val:
        s= "found in root"
    queue = Queue.Queue()
    queue.put(root)
    root.visited = True
    while not queue.empty():
        node = queue.get()
        for neighbor in node.neighbors: 
            if not neighbor.visited:
                print neighbor.val
                neighbor.visited = True
                if neighbor.val == val:
                    s= "found " + val
                queue.put(neighbor)
    return s          

if __name__ == "__main__":
    node1 = GraphNode("a")
    node2 = GraphNode("b")
    node3 = GraphNode("c")
    node4 = GraphNode("d")
    node5 = GraphNode("e")

    node1.neigbhors([node2,node4])
    node2.neigbhors([node3,node5])
    node3.neigbhors([node2,node4,node5])
    node4.neigbhors([node3,node5])
    node5.neigbhors([node2,node3,node4])

    print breadthFirstSearch(node1, "d")
