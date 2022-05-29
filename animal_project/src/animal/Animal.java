package animal;

import java.util.ArrayList;
import java.util.List;

abstract public class Animal {
	static public List<Animal> animals = new ArrayList<Animal>();

	public String name;
	
	public Animal() {
//		System.out.println("Animal Created");
		animals.add(this);
	}
	
	public Animal(String a) {
		System.out.println("a");
	}
	
	public abstract void sound();
	abstract int speed();
	

}
