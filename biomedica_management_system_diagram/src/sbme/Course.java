package sbme;

import java.util.List;

public class Course {

	private String name;
	private String code;
	private List<String> chapters;
	private int duration = 14;
	private Professor main_prof;
	private List<Professor> profs;
	
	private static String coursPrefix = "sbe_"; 
	
	public static String getCoursePrefix() {
		return Course.coursPrefix;
	}
	Course(String name, String courseNumber, Professor prof){
		this.setName(name);
//		this.code = code;
		this.setCode(courseNumber);
		this.main_prof = prof;
	}

	public void setCode(String courseNumber) {
		this.code = Course.coursPrefix + this.name.substring(0, 3) + courseNumber;
	}

	public String getCode() {
		return code;
	}
	
	public String getName() {
		return this.name;
	}
	
	private void setName(String name) {
		this.name = name.toLowerCase();
	
	}
	public int getDuration() {
		return duration;
	}
	
	public void setDuration(int duration, Professor prof) {
		if(this.main_prof.equals(prof)) {			
			this.duration = duration;
			System.out.println("duration changed");
		} else {
			System.out.println("not valid");
		}
	}

	
	
	

}
