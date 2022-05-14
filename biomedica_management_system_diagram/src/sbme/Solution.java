package sbme;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int x =3;
		
		Professor first_prof = new Professor("Ahmed");
		first_prof.name = "Ahmed";
		first_prof.age = 19;
		
		
		Professor second_prof = new Professor();
		second_prof.name = "ali";
		
		Course first_course = new Course("circuits", "sbme_cir12");
//		first_course.name = "circuits";
//		first_course.code = "sbme_cir12";
		System.out.println(first_course.getName());
//		System.out.println(first_course.code);
//		System.out.println(first_prof.name);
//		System.out.println(first_prof.age);
//		System.out.println(second_prof.name);
//		System.out.println(second_prof.age);
//		System.out.println("success");
	}

}
