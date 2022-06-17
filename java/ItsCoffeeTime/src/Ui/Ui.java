package Ui;

import java.util.Scanner;

import Machine.*;

public class Ui {

  private static String logotipo = "\n╔╗╔┌─┐┌─┐┌┬┐═╗ ╦┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐\n║║║├┤ └─┐ │ ╔╩╦╝├─┘├┬┘├┤ └─┐└─┐│ │\n╝╚╝└─┘└─┘ ┴ ╩ ╚═┴  ┴└─└─┘└─┘└─┘└ ─┘\n";

  /** 🍺
   * -> logo of the application
   */
  public static void getWellcome (String name) {
    System.out.println(logotipo);
    System.out.println(name + " is started");
  }


  /**
   * -> Checking if the machine is ready....
   * @> checking_status()
   */
  public static void checkStatus() {
    System.out.println("Checking if the machine is ready....");
  }


  /**
   * User interface for the user to interact with it
   */
  public static void userInterface() {
    System.out.println("\n[1]. Coffee expresso");
    System.out.println("\n[2]. Coffee latte");
    System.out.println("\n[3]. Hot water");
    System.out.println("\n[0]. Shutdown");
  }


  /** 💻
   * The 🤖 is a switch statement that takes an integer as input and calls the
   * appropriate function from the Machine class.
   */
  public static void controller() {
    /**
     * Scan data choice
     */
    System.out.println("\n[?] Enter number choice: ");
    Scanner sc = new Scanner(System.in);
    int choice = sc.nextInt();

    switch (choice) {
      case 1:
        Machine.coffee();
        break;
      case 2:
        Machine.latte();
        break;
      case 3:
        Machine.hotWater();
        break;
      case 0:
        Machine.shutDown();
        break;
      default:
        System.out.println("[!] Invalid choice");
    }
    enjoy();
    sc.close();
  }


  // A method that prints a message to the user.
  public static void enjoy() {
    System.out.println("\n[+] Enjoy your drink!");
  }




  // Prints the fibbonacci sequence.
  public static void fibbonacci() {
    double n0 = 0;
    double n1 = 1;
    for (int i = 1 ; i < 2000 ; i++) {
      double fib = n0 + n1;
      System.out.println(n0);
      n0 = n1;
      n1 = fib;
    }
  }
}
