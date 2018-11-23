
public class Queue {

	private Node head, tail;
	public Queue() {
		this.head = this.tail = null;
	}
	public boolean isEmpty() {
		return this.head == null;
	}
	public int size() {
		int counter = 0;
		for(Node tmp = this.head; tmp != null; tmp  = tmp.next)
			counter++;
		return counter;
	}
	public Integer dequeue() {
		if(this.isEmpty())
			return null;
		else {
			Integer i = this.head.info;
			if(this.head == this.tail)
				this.head = this.tail = null;
			else {
				this.head = this.head.next;
			}
			return i;
		}
	}
	public void enqueue(int i) {
		if(this.isEmpty())
			this.head = this.tail = new Node(i);
		else {
			this.tail.next = new Node(i);
			this.tail = this.tail.next;
		}
	}
}
