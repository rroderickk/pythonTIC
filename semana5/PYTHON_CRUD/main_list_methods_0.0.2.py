import sys

clients = [ 'pablo', 'ricardo',]


def list_clients():
  for idx, client in enumerate(clients):
    print('[R] list_client ->\t {}: {}'.format(idx, client))


def _client_not_found(client_name):
	return print(f'[-] Client {client_name} is not in clients list')


def Update(client_name, updated_client_name):
  global clients

  if client_name in clients:
    index = clients.index(client_name)
    clients[index] = updated_client_name
    print('[U] Clients are updated: -> ',clients)
  else:
    _client_not_found(client_name)
  return list_clients()


def Delete(client_name):
  global clients
  if client_name in clients:
    print(f'[D] Delete {client_name} in clients -> ', clients)
    clients.remove(client_name)
  else:
    _client_not_found(client_name)
  return list_clients()


def create_client(client_name):
  global clients
  if client_name not in clients:
    clients.append(client_name)
    print('\n [C] created client ->',clients)
  else:
    print('\n [-] Client already exist')


def Search(client_name):
  global clients
  for client in clients:
    if client != client_name:
      continue
    else:
      idx = clients.index(client)
      return True, idx


def _print_welcome():
  print('\n')
  print('\t--' * 13)
  print('WELCOME TO PLATZI VENTAS')
  print('|' * 50)
  print('What would you like to do today?')
  print(' -> [C]reate client')
  print(' -> [R]ead clients')
  print(' -> [U]pdate client')
  print(' -> [D]elete client')
  print(' -> [S]earch client')
  print(' -> [salir] for exit')


def run(fn, *data):
  fn(data)


def _get_client_name():
  client_name = None

  while not client_name:
    client_name = input('What is the client name? : ')
    if client_name == 'exit':
      client_name = None
      break

  if not client_name:
    sys.exit()
  return client_name


def program():
  _print_welcome()
  global command_upper
  command_upper = input().upper()

  print('\n')
  if command_upper == 'C':
    client_name = _get_client_name()
    create_client(client_name)
  elif command_upper == 'R':
    list_clients()
  elif command_upper == 'U':
    client_name = _get_client_name()
    updated_client_name = input('What is the updated client name? : ')
    Update(client_name, updated_client_name)
  elif command_upper == 'D':
    client_name = _get_client_name()
    Delete(client_name)
  elif command_upper == 'S':
    client_name = _get_client_name()
    found = Search(client_name)
    if found:
      print(f'[+] {client_name}, is in the clients list -> id: {found[1]}')
    else:
      print(f'[-] {client_name} is not in the clients list')
  elif command_upper == 'SALIR':
    pass
  else:
    print('\n[!] Invalid command')


if __name__ == '__main__':
  command_upper = ''
  while command_upper != 'SALIR':
    program()