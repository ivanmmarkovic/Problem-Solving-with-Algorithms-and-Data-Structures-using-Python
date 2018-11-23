public class LinkedListSingle {

    private Node head, tail;

    public LinkedListSingle(){
        this.head = this.tail = null;
    }
    public boolean isEmpty(){
        return this.head == null;
    }
    public int size(){
        int counter = 0;
        for(Node tmp = this.head; tmp != null; tmp = tmp.next)
            counter++;
        return counter;
    }
    public void addToHead(int i){
        this.head = new Node(i, this.head);
        if(this.tail == null)
            this.tail = this.head;
    }
    public void addToTail(int i){
        if(this.isEmpty())
            this.head =this.tail = new Node(i);
        else {
            this.tail.next = new Node(i);
            this.tail = this.tail.next;
        }
    }
    public Integer deleteFromHead(){
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
    public Integer deleteFromTail(){
        if(this.isEmpty())
            return null;
        else{
            Integer i = this.tail.info;
            if(this.head == this.tail)
                this.head = this.tail = null;
            else {
                Node tmp;
                for(tmp = this.head; tmp.next != this.tail; tmp = tmp.next);
                tmp.next = null;
                this.tail = tmp;
            }
            return i;
        }
    }
    public void printAll(){
        for(Node tmp = this.head; tmp != null; tmp = tmp.next)
            System.out.print(tmp.info + ", ");
    }
    public void deleteNodesWithValue(int value){
        if(this.isEmpty())
            return;
        else if(this.head != this.tail){
            Node currentNode = this.head;
            while(currentNode.next != null){
                if(currentNode.next.info == value){
                    if(currentNode.next.next == null)
                        currentNode.next = null;
                    else 
                        currentNode.next = currentNode.next.next;
                }
                else
                    currentNode = currentNode.next;
            }
            this.tail = currentNode;
        }  
        if(this.head.info == value){
            if(this.head == this.tail)
                this.head = this.tail = null;
            else 
                this.head = this.head.next;
        } 
    }
    public void sort(){
        for(Node outer = this.head; outer != null; outer = outer.next){
            boolean swapped = true;
            do{
                swapped = false;
                for(Node inner = this.head; inner.next != null; inner = inner.next){
                    if(inner.info > inner.next.info){
                        int tmp = inner.info;
                        inner.info = inner.next.info;
                        inner.next.info = tmp;
                        swapped = true;
                    }
                }
            }
            while(swapped == true);
        }
    }
}