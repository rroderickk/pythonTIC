import codigo.*;
import java.util.Scanner;

public class App {
	public static void main(String[] args) {
		/**
		 * Openning
		 */
		System.out.println(Clase_Principal.c);
		System.out.println("Primitive variables and Scanner");
		System.out.println();


		/**
		 * Object creations && primitives
		 */
		Scanner sc = new Scanner(System.in);
		String name, lastName, email, address; 
		byte age;
		int phoneNumber;


		/**
		 * Scan data user
		 */
		System.out.println("Enter your name: ");
		name = sc.nextLine();

		System.out.println("Enter your last name: ");
		lastName = sc.nextLine();

		System.out.println("Enter your email: ");
		email = sc.nextLine();

		System.out.println("Enter your address: ");
		address = sc.nextLine();

		System.out.println("Enter your age: ");
		age = sc.nextByte();

		System.out.println("Enter your phoneNumber: ");
		phoneNumber = sc.nextInt();
		
		System.out.println("\n"+name+"\n"+lastName+"\n"+email
			+"\n"+address+"\n"+age+"\n"+phoneNumber
		);
		sc.close();
	}
}