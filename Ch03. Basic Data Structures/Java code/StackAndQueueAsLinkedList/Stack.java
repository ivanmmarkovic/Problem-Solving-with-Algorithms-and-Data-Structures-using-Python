
public class Stack {

	private Node stackPointer;
	
	public Stack() {
		this.stackPointer = null;
	}
	public boolean isEmpty() {
		return this.stackPointer == null;
	}
	public int size() {
		int counter = 0;
		for(Node tmp = this.stackPointer; tmp != null; tmp = tmp.next)
			counter++;
		return counter;
	}
	public void push(int i) {
		this.stackPointer = new Node(i, this.stackPointer);
	}
	public Integer pop() {
		if(this.isEmpty())
			return null;
		else {
			Integer i = this.stackPointer.info;
			this.stackPointer = this.stackPointer.next;
			return i;
		}
	}
	public Integer peek() {
		if(this.isEmpty())
			return null;
		else {
			Integer i = this.stackPointer.info;
			return i;
		}
	}
}
