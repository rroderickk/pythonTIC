package CoffeMachine;

import Ui.*;

/** 
 * <h1> ☕ CoffeMachine </h1>
 * The class CoffeMachine has three properties: name, price, and type.
 * It has three methods: getName(), getPrice(), and getType().
 * It has one constructor: CoffeMachine(String name, int price, String type).
 */
public class CoffeMachine {

  /**
   * @param args Primitives
   */
  String name;
  int price;
  String type;


  /**
   * Constructor CoffeMachine
   * @String {name}<-
   * @int {price}<-
   * @String {type}<-
   */
  public CoffeMachine(String name, int price, String type) {
    this.name = name;
    this.price = price;
    this.type = type;
  };


  /**
   * @Getters -> name, price, type
   */
  public String getName()  { return name;  };
  public int    getPrice() { return price; };
  public String getType()  { return type;  };


  /**
   * <h4>☕ Start </h4>
   */
  public void start() {
    Ui.getWellcome(this.name);
    Ui.checkStatus();
    Ui.userInterface();
    Ui.controller();
    // Ui.fibbonacci();
  }
}
