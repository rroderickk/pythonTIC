package Machine;

/**
 * The Machine class contains the methods that the machine will use to serve the coffee
 */
public class Machine {

  /**
   * The function `coffee()` prints the string `"[+] Serving coffe expresso"` to the console
   */
  public static void coffee() {
    System.out.println("[+] Serving coffe expresso");
  }
  /**
   * `latte()` is a function that prints out two lines of text
   */
  public static void latte() {
    System.out.println("[+] Serving expresso");
    System.out.println("[+] Adding milk latte");
  }
  /**
   * It prints a message to the console.
   */
  public static void hotWater() {
    System.out.println("[+] Inyecting Hot Water");
  }
  /**
   * It prints a message to the console and then exits the program
   */
  public static void shutDown() {
    System.out.println("----[+] Shutting down----");
    System.out.println("[+] Come back soon!");
    System.exit(0);
  }
}
