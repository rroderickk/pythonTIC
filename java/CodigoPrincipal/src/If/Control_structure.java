package If;

import java.util.Scanner;

public class Control_structure {
  public static void main(String[] args) {

    /**
     * Scan data user
     */
    System.out.println("Enter a number: ");
    Scanner sc = new Scanner(System.in);

    /**
     * Primitive
     */
    Integer num1 = sc.nextInt();

    /**
     * Control Structure
     */
    if (num1 == 0 ) {
      System.out.println("The number is zero");
    } else if (num1 > 0) {
      System.out.println("The number is positive");
    } else {
      System.out.println("The number is negative");
    }
    sc.close();
  }
}
