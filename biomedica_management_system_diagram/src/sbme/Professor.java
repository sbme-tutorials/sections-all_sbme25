package sbme;

public class Professor {
	
	String name;
	int age;
	Professor(){
		System.out.println("empty constructor");
	}
	Professor(String name){
		this.name = name;
	}
	Professor(int age){
		this.age = age;
	}
	// Constructor
	Professor(String name, int age){
		this.name = name;
		this.age = age;
		System.out.println("parametrized constructor");
	}
}
