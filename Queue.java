class Queue{
	GraphNode first, last;
	public void enqueue(GraphNode node){
		if(first == null){
			first = node;
			last = first;
		}else{
			last.next = node;
			last = node;
		}
	}

	public GraphNode dequeue(){
		GraphNode temp;
		if (first == null){
			return null;
		}else{
			temp = first;
			first = first.next;
		}
		return temp;
	}
}