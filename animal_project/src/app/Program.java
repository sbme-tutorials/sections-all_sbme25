package app;

import java.util.ArrayList;
import java.util.List;

import animal.Animal;
import animal.Cat;
import animal.Dog;
import animal.Kingdom;

public class Program {

	public static void main(String[] args) {
				
		Cat c1 = new Cat("c1");
		Animal c2 = new Cat("c2");
		Dog d1 = new Dog("d1");
		Dog d2 = new Dog("d2");
		Kingdom c3 = new Cat("as");
		
		for(var a : Animal.animals) {
			System.out.println(a);
		}
//		System.out.println(c1 instanceof Cat);
	
	
		
	}

}
