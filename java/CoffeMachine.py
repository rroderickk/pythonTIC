"""
  # Simple coffee machine model by @CheatModes4
  @{name} -> Name of the coffee machine
"""
# ☕
class Cafetera:
  def __init__(self, name):
    self.name = name
    self.estado = 'off'
    self._lvl_water = 0
    self.__logo()
    print('[+] new CoffeMachine {}'.format(name))


  def __logo(self):
    logotipo = "\n╔╗╔┌─┐┌─┐┌┬┐═╗ ╦┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐\n║║║├┤ └─┐ │ ╔╩╦╝├─┘├┬┘├┤ └─┐└─┐│ │\n╝╚╝└─┘└─┘ ┴ ╩ ╚═┴  ┴└─└─┘└─┘└─┘└─┘\n"
    print(logotipo)


  def start(self):
    """
    It starts the game.
    """
    self.estado = 'on'
    self._greet_state()
    self.__check__status()
    self._lvl_water = self._controller()
    self.__check__status()


  def get_lvl_water(self):
    return self._lvl_water


  def stop(self):
    self.estado = 'off'
    self._greet_state()


  def _greet_state(self):
    print(self.name, '[+] machine state: ', self.estado)


  def __check__status(self):
    if self._lvl_water == 0:
      print('[!] water container empty -> [::fill water::]')
      self._warning_status()
    if self._lvl_water >= 1 and self._lvl_water < 20:
      print('[!] low level water  -> [::fill more water::]')
      self._warning_status()
    if self._lvl_water >= 20:
      self._stand_by()


  def _warning_status(self):
    print('[!] warning [!]')
    print('[!] warning [!]')
    self._lvl_water = self._controller()
    self.__check__status()


  def _controller(self):
    return int(input('\n[::insert amount of water::] ml: -> '))


  def _stand_by(self):
    print('\n\t--'*4, f'✔ {self.name} is ready to work','--'*10)
    return self.program()


  # 🍺
  def _off(self):
    self.__logo()
    print(f'[-] {self.name} is off.... Goodbye!')
    exit()


  def cafeteria(self, option):
    if option == 1:
      self._lvl_water -= 10
      self._xpresso()
    if option == 2:
      self._lvl_water -= 10
      self._hot_water()


  def _xpresso(self):
    print('\n\t--'*4, f'✔ {self.name} serving expresso','--'*10)
    print('\t\t ✔ done successfully')


  def _hot_water(self):
    print('\n\t--'*4, f'✔ {self.name} serving hot water','--'*10)
    print('\t\t ✔ done successfully')


  def program(self):

    if self.get_lvl_water() >= 20:
      option = ''
      while (option != 0):
        if self.get_lvl_water() < 20:
          break
        print(f'\n\t\t[1] Xpresso \n\t\t[2] Hot water \n\t\t[0] {self.name} off: \n\t\t')
        option = int(input('\t\t\t[?] Insert your option: -> '))
        if option != 0:
          self.cafeteria(option)

    if self.get_lvl_water() <= 20:
      self._warning_status()

    if option == 0:
      self._off()


def Its_Coffee_Time():
  """
    It creates a @Cafetera object called -> NestXpresso <- and then calls the start method on it.
  """
  NestXpresso = Cafetera('NestXpresso')
  NestXpresso.start() # 🔙 Start the machine.



# A way to make sure that the code in the if statement is only executed when the module is run
# directly, and not when it is imported by another module.
if __name__ == '__main__':
  Its_Coffee_Time() # 👈 It starts the game

