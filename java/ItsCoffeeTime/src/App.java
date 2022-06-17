import CoffeMachine.CoffeMachine;

public class App {
	public static void main(String[] args) throws Exception {
		System.out.println("My new CoffeMachine in Java");

		/** ☕
		 * My new CoffeMachine in Java
		 */
		CoffeMachine NestXpresso = new CoffeMachine(
			"NestXpresso", 2000, "Full-Automatic"
		);

		NestXpresso.start(); 	// 👈🏼 Entry point

	}
}
