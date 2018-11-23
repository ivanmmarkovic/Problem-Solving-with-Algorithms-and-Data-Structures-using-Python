
public class Main {

	public static void main(String args[]) {
		Stack s = new Stack();
		for(int i = 0; i< 10; i++)
			s.push(i);
		
		System.out.println("Last added element is : " + s.peek());
		while(!s.isEmpty())
			System.out.print(s.pop() + ", ");
		System.out.println();
		System.out.println("------------------------------");
		
		Queue q = new Queue();
		for(int i = 100; i < 110; i++)
			q.enqueue(i);
		
		while(!q.isEmpty())
			System.out.print(q.dequeue() + ", ");
		
		
		
	}
}
