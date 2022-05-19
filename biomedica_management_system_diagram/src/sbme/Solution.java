package sbme;

public class Solution {

	public static void main(String[] args) {
				
		Professor first_prof = new Professor("Ahmed");
		first_prof.name = "Ahmed";
		first_prof.age = 19;
		
		
		Professor second_prof = new Professor();
		second_prof.name = "ali";
		
		Course first_course = new Course("CiRcUiTs", "12", first_prof);
//		first_course.name = "circuits";
//		first_course.code = "sbme_cir12";
//		System.out.println(first_course.getName());
		System.out.println(first_course.getCode());
//		System.out.println(first_course.code);
//		System.out.println(first_prof.name);
//		System.out.println(first_prof.age);
//		System.out.println(second_prof.name);
//		System.out.println(second_prof.age);
//		first_course.setDuration(10, first_prof);
		
		System.out.println("success");
		System.out.println(Course.getCoursePrefix());
		first_course.setDuration(10, first_prof);	
	}
}
