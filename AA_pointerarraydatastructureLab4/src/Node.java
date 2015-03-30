
public class Node {
	
	Node tail;
	int value;
	
	public Node(){
		tail = null;
	}
	
	public Node getNext(){
		return tail;
	}
	
	public void setNext(Node next){
		tail = next;
	}

}
