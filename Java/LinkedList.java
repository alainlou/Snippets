public class LinkedList {

	private Node head;

	public LinkedList(Object o) {
		head = new Node(o);
	}

	public Node getHead(){
		return head;
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
			if(curr.getNext().getValue().equals(o)) {
				curr.setNext(curr.getNext().getNext());
				//TODO get garbage collection to recognize the unutilized node
				break;
			}
			curr = curr.getNext();
		}
	}

	@Override
	public String toString(){
		try{
			Node curr = head;
			StringBuilder sb = new StringBuilder();
			sb.append(curr.getValue());
			sb.append(" ");
			while(curr.getNext() != null){
				sb.append(curr.getNext().getValue());
				sb.append(" ");
				curr = curr.getNext();
			}
			return sb.toString();
		}
		catch(NullPointerException e){
			return e.toString();
		}
	}
}
