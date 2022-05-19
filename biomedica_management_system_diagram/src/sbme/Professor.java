package sbme;

public class Professor extends Human {
	
	public Professor(){
		System.out.println("empty constructor");
	}
	public Professor(String name){
		this.name = name;
	}
	public Professor(int age){
		this.age = age;
	}
	// Constructor
	public Professor(String name, int age){
		this.name = name;
		this.age = age;
		System.out.println("parametrized constructor");
	}
}
