
public class LinkedListDouble {
	
	private Node head, tail;
	
	public LinkedListDouble(){
		this.head = this.tail = null;
	}
	public boolean isEmpty() {
		return this.head == null;
	}
	public int numberOfElements() {
		int counter = 0;
		for(Node tmp = this.head; tmp != null; tmp = tmp.next)
			counter++;
		return counter;
	}
	public void addToHead(int i) {
		if(this.isEmpty())
			this.head = this.tail = new Node(i, null, null);
		else {
			this.head = new Node(i, null, this.head);
			this.head.next.prev = this.head;
		}
	}
	public void addToTail(int i) {
		if(this.isEmpty())
			this.head = this.tail = new Node(i);
		else {
			this.tail.next = new Node(i, this.tail, null);
			this.tail = this.tail.next;
		}
	}
	public Integer removeFromHead() {
		if(this.isEmpty())
			return null;
		else {
			Integer i = this.head.info;
			if(this.tail == this.head)
				this.head = this.tail =  new Node(i, null, null);
			else {
				this.head = this.head.next;
				this.head.prev = null;
			}
			return i;
		}
	}
	public Integer removeFromTail() {
		if(this.isEmpty())
			return null;
		else {
			Integer i = this.tail.info;
			if(this.head == this.tail)
				this.head = this.tail = null;
			else {
				this.tail = this.tail.prev;
				this.tail.next = null;
			}
			return i;
		}
	}
	public void printAll() {
		for(Node tmp =this.head; tmp != null; tmp = tmp.next)
			System.out.print(tmp.print() + ", ");
		System.out.println();
	}
	public void deleteWithValues(int value) {
		if(this.isEmpty())
			return;
		else if(this.head != this.tail){
			Node currentNode = this.head;
			Node toDelete;
			while(currentNode.next != null) {
				if(currentNode.next.info == value) {
					if(currentNode.next.next == null) {
						toDelete = currentNode.next;
						currentNode.next = null;
					}
					else {
						toDelete = currentNode.next;
						currentNode.next = currentNode.next.next;
					}
					toDelete = null;
				}
				else {
					currentNode = currentNode.next;
				}
			}
			this.tail = currentNode;
		}
		if(this.head.info == value) {
			if(this.head == this.tail)
				this.head = this.tail = null;
			else {
				this.head = this.head.next;
				this.head.prev = null;
			}
		}
	}
	public void sort() {
		for(Node outer = this.head; outer != null; outer = outer.next) {
			for(Node inner = this.tail; inner != outer; inner = inner.prev) {
				if(inner.prev.info > inner.info) {
					int tmp = inner.prev.info;
					inner.prev.info = inner.info;
					inner.info = tmp;
				}
			}
		}
	}
	
}
