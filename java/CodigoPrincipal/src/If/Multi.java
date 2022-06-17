package If;

import java.util.Scanner;

public class Multi {
  public static void main(String[] args) {

    /**
     * Scan data user && Primitives
     */
    Scanner sc = new Scanner(System.in);
    int num1 = sc.nextInt(), num2 = sc.nextInt(), resultM, resultS;

    /**
     * Multiplication || sum
     */
    if (num1 < num2) {
      resultM = num1 * num2;
      System.out.println("El resultado de la multiplicación es: " + resultM);
    } else {
      resultS = num1 + num2;
      System.out.println("El resultado de la multiplicación es: " + resultS);
    }
    sc.close();
  }
}
