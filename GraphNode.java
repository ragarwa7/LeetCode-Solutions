class GraphNode{
	int val;
	GraphNode next;
	GraphNode[] neighbors;
	boolean visited;

	GraphNode(int val){
		this.val = val;
	}

	GraphNode(int val, GraphNode[] n){
		this.val = val;
		this.neighbors = n;
	}

	public String toString(){
		return "value: _" + this.val;
	}
}