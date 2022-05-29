package animal;

public class Cat extends Animal implements Kingdom, Kingdom2{

	
	public Cat(String name) {
		super();
		this.name = name;
//		super();
//		System.out.println("Cat Created");
	}
	
	@Override
	public void sound() {
		System.out.println("Cat sound: Meow");
	}
	
	public int speed() {
		return 5;
	}
	
	@Override
	public String toString() {
		return this.name;
	}

	@Override
	public void f1() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void f2() {
		// TODO Auto-generated method stub
		
	}
}

