package sbme;

import java.util.List;

public class Course {

	private String name;
	private String code;
	List<String> chapters;
	int duration = 14;
	Professor main_prof;
	List<Professor> profs;
	
	Course(String name, String code){
		this.setName(name);
		this.code = code;
	}
	
	public String getName() {
		return this.name;
	}
	
	private void setName(String name) {
		if(name.length() < 4) {
			this.name = name;			
		} else {
			System.out.println("more than 4 letters");
			this.name = "undefined";
		}
	}
	
	
}
