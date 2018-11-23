
public class Main {
	
	public static void main(String args[]) {
		
		LinkedListDouble l = new LinkedListDouble();
		
		l.addToHead(1);
		l.addToHead(4);
		l.addToHead(53);
		l.addToHead(1);
		l.addToHead(117);
		l.addToHead(1);
		l.addToHead(21);
		l.addToHead(17);
		l.addToHead(31);
		l.addToHead(1);
		l.addToHead(1);
		
		l.printAll();
		l.deleteWithValues(1);
		l.printAll();
		l.sort();
		l.printAll();
		
	}

}
