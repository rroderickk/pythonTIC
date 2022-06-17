package If;

import java.util.Scanner;

public class Estructuras_de_control {
  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);

    /**
     * Primitives
     */
    byte edad = sc.nextByte();


    /**
     * Business Logic
     */
    if (edad >= 18 && edad <= 65) {
      System.out.println("Eres mayor de edad");
    } else {
      System.out.println("Eres menor de edad");
    }
    sc.close();
  }
}
