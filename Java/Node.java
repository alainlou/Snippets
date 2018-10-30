package lou.alain;

public class Node{
	private Node next;
	private Object value;
	
	public Node(Object obj) {
		next = null;
		value = obj;
	}
	
	public Node getNext() {
		return next;	
	}
	
	public Object getValue() {
		return value;
	}
	
	public void setNext(Node n) {
		next = n;
	}
}
