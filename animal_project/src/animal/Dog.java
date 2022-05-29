package animal;

public class Dog extends Animal {

	public Dog(String name) {
		this.name = name;
	}
	
	@Override
	public void sound() {
		System.out.println("Dog Sound");
	}
	
	
	public int speed() {
		return 10;
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return this.name;
	}

}
