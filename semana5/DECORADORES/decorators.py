PASSWORD = "DiamondJackson1234"

def password_required(f):
  def wrapper():
    password = input('Ingrese la contraseña: ')

    if password == PASSWORD:
      return f()
    else:
      print('La contraseña es incorrecta')
  return wrapper

@password_required
def needs_password():
  print('La contraseña es correcta')




def upper(f):
  def wrapper(*args, **kwargs):
    result = f(*args, **kwargs)
    return result.upper()
  return wrapper


@upper
def say_my_name(name):
  return f'Hola {name}'



if __name__ == '__main__':
  print("┬  ┌─┐┌─┐┬┌┐┌")
  print("│  │ ││ ┬││││")
  print("┴─┘└─┘└─┘┴┘└┘")
  name = input ("Username: ")
  print(say_my_name(name))
  needs_password()