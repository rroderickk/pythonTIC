#### Semana2 25_04_2022
# Simple program for return cost and volume
<div style="padding: 40px;>
  <marquee>Hello world</marquee>

  <h1 style="color: crimson; font-weight: bold">Simple program to show price and volume of send packages</h1>
  <h2>The program</h2>

  ```py
  intro = """

  ---- Welcome Sr----
  ╦═╗┌─┐╦═╗┌─┐┌─┐┬┌┬┐┌─┐
  ╠╦╝├┤ ╠╦╝├─┤├─┘│ │││ │
  ╩╚═└─┘╩╚═┴ ┴┴  ┴─┴┘└─┘
  ---- Cost per Package --- 
  --- Depends of volume ---
  --- Price to customer depends of: Volumen*5  ---\n\n
  """

  COST = 5


  def main():
    print(intro)

    height = float(input("[?] Insert height: \n"))  #<- enter the height of the package
    width = float(input("[?] Insert width: "))      #<- enter the height of the package
    depth = float(input("[?] Insert depth: "))      #<- enter the height of the package

    volume = height * width * depth                 #<- calculate volume

    result = volume*COST                           #<- calculate cost

    print(result)                               #<- print result for users



  if __name__ == '__main__':            #<- if this file is run directly
    main()                          #<- run the main function how entry point 
  ```

  <br/>
  <br/>

  <h4>Now?, who contain?</h4>

  ```py
  if __name__ == '__main__':
    main()
  ```

  <p style="font-weight: bolder">This code snippet is the initial flow of the program that tells python that the entry point is the call to execution of the main() function.</p>
  <br/>
  <br/>

  <h4>Function main()?</h4>

  ```py
  def main():
    print(intro)

    height = float(input("[?] Insert height: \n"))
    width = float(input("[?] Insert width: "))
    depth = float(input("[?] Insert depth: "))

    volume = height * width * depth
    result = volume*COST

    print(result)

  ```

  <p>This code snippet is the code is the declaration that a function exists and contains the instructions to execute, from the user it takes 3 data that are the weight, width and depth, executes the functions of multiplying by the given cost and prints the result for the user to see</p>

  <br/>
  <br/>

  <h4>Declaration of constants</h4>

  ```py
  intro = """
  ---- Welcome Sr----
  ╦═╗┌─┐╦═╗┌─┐┌─┐┬┌┬┐┌─┐
  ╠╦╝├┤ ╠╦╝├─┤├─┘│ │││ │
  ╩╚═└─┘╩╚═┴ ┴┴  ┴─┴┘└─┘
  ---- Cost per Package --- 
  --- Depends of volume ---
  --- Price to customer depends of: Volumen*5  ---\n\n
  """

  COST = 5
  ```

  <p>Contains constant values for the main function to use, such as the intro banner, and COST</p>

  <br/>
  <br/>
</div>