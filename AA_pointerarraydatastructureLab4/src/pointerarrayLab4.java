
public class pointerarrayLab4 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("pointer based stack");
		PointerBasedStack pbs = new PointerBasedStack();
		
		pbs.push(10);
		pbs.push(11);
		pbs.push(12);
		pbs.push(13);
		pbs.push(100);
		System.out.println(pbs.listSize);
		Node pop1 = pbs.pop();
		System.out.println("pop " + pop1.value);
		pop1 = pbs.pop();
		System.out.println("pop " + pop1.value);
		pop1 = pbs.pop();
		System.out.println("pop " + pop1.value);
		pop1 = pbs.pop();
		System.out.println("pop " + pop1.value);
	}

}
