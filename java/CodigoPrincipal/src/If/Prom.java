package If;

import java.util.Scanner;

public class Prom {
  public static void main(String[] args) {

    /**
     * Scan data user
     */
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter notes:");
    System.out.println();

    /**
     * Primitive
     */
    double nota1 = sc.nextDouble();
    double nota2 = sc.nextDouble();
    double nota3 = sc.nextDouble();
    double nota4 = sc.nextDouble();
    double promedio;

    /**
     * Promedio
     */
    promedio = (nota1 + nota2 + nota3 + nota4) / 4;

    if (promedio > 7) System.out.println("The student is aproved");

    else if (promedio < 7) System.out.println("The student is not aproved");

    else System.out.println("Insert a valid note");

    sc.close();
  }
}
