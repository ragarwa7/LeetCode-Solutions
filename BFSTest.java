class BFSTest{
	public static void main(String[] args){
		GraphNode n1 = new GraphNode(1);
		GraphNode n2 = new GraphNode(2);
		GraphNode n3 = new GraphNode(3);
		GraphNode n4 = new GraphNode(4);
		GraphNode n5 = new GraphNode(5);

		n1.neighbors = new GraphNode[]{n2,n3,n5};
		n2.neighbors = new GraphNode[]{n1,n4};
		n3.neighbors = new GraphNode[]{n1,n4,n5};
		n4.neighbors = new GraphNode[]{n2,n3,n5};
		n5.neighbors = new GraphNode[]{n1,n3,n5};

		bfs(n1,4);
	}

	public static void bfs(GraphNode root, int value){
		if(root.val == value){
			System.out.println("Root");
		}
		Queue queue = new Queue();
		root.visited = true;
		queue.enqueue(root);
		while(queue.first != null){
			GraphNode node = (GraphNode) queue.dequeue();
			for(GraphNode n : node.neighbors){
				if(!n.visited){
					System.out.println(n);
					if(n.val == value){
						System.out.println("Find"+n);
					}
					n.visited = true;
					queue.enqueue(n);
				}
			}
		}
	}
}