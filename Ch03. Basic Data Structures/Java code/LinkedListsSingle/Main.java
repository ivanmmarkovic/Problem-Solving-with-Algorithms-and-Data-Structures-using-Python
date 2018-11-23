public class Main{

    public static void main(String args[]){
        LinkedListSingle ls = new LinkedListSingle();

        ls.addToHead(5);
        ls.addToHead(1);
        ls.addToHead(2);
        ls.addToHead(3);
        ls.addToHead(99);
        ls.addToHead(4);
        ls.addToHead(101);
        ls.addToHead(5);
        ls.addToHead(5);
        ls.addToHead(31);
        ls.addToHead(6);
        ls.addToHead(7);
        ls.addToHead(17);
        ls.addToHead(8);
        ls.addToHead(9);
        ls.addToHead(5);

        ls.deleteNodesWithValue(5);
        ls.printAll();
    }

}