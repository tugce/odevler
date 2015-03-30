
public class PointerBasedStack {
	
	public Node head;
	public int listSize;
	
	public PointerBasedStack(){
		head = new Node();
		listSize = 0;
	}
	
	public void push(int x){
		System.out.println("push");
		Node yeni = new Node();
		Node temp = new Node();
		Node temp2 = new Node();
		yeni.value = x;
		System.out.println("head = " + head.toString());
		if(listSize == 0){
			head = yeni;
		}else if(head.getNext() == null){
			head.setNext(yeni);
			
		}else{
			
			temp = head.getNext();
			while(temp != null){
				System.out.println("get next null degil");
				temp2 = temp;
				temp = temp.getNext();
				
			}
			yeni.setNext(temp2.tail);
			temp2.setNext(yeni);
		}
		
		
		listSize = listSize + 1;
	}
	
	public Node pop(){
		System.out.println("pop");
		Node yeniHead = new Node();
		yeniHead = head;
		head = head.getNext();
		listSize = listSize -1;
		return yeniHead;
		
	}
	
	
	
	

}
