package lou.alain;

public class LinkedList {
	
	private Node head;
	
	public LinkedList(Object o) {
		head = new Node(o);
	}
	
	public void append(Object o) {
		Node next = new Node(o);
		Node curr = head;
		while(curr.getNext() != null) {
			curr = curr.getNext();
		}
		curr.setNext(next);
	}
	
	public void pop(Object o) {
		Node curr = head;
		while(true) {
			if(curr.getValue().equals(o)) {
				
			}
			curr = curr.getNext();
		}
	}
	
	public String toString() {
		Node tmp = head;
		StringBuilder sb = new StringBuilder();
		
	}
}
