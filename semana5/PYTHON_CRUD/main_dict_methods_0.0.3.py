import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []
# [ #// data dummie
#   { 'name': 'Juan',
#     'company': 'Google',
#     'email': 'pablo@google.com',
#     'position': 'Software Engineer',
#     'uid': 1
#   },
#   { 'name': 'Ricardo',
#     'company': 'Facebook',
#     'email': 'ricardo@facebook.com',
#     'position': 'Data Engineer',
#     'uid': 2
#   },
# ]

def _initialize_clients_from_storage():
  file_exists = os.path.isfile(CLIENT_TABLE)
  if not file_exists:
    fh = open(CLIENT_TABLE, "w")
    fh.close()

  with open(CLIENT_TABLE, mode='r') as f:
    reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
    for row in reader:
      clients.append(row)

def _save_clients_to_storage():
  tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
  with open(tmp_table_name, mode='w') as f:
    writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
    writer.writerows(clients)
    # writer.writerow(clients)                                #? una fila
  os.remove(CLIENT_TABLE)
  os.rename(tmp_table_name, CLIENT_TABLE)
  f.close()


def list_clients():
  print('[R] list_client ->\n\t', clients)

    
  # for idx, client in enumerate(clients):
  #   print('{uid} | {name} | {company} | {email} | {position}'.format(
  #     uid=idx, name=client['name'], company=client['company'],
  #     email=client['email'], position=client['position']
  #   ))


def _client_not_found(client_name):
	return print(f'[-] Client {client_name} is not in clients list')


def _updating_client(client, command2):
  if command2 == 'N':
    client['name'] = _get_client_field('name')
  elif command2 == 'C':
    client['company'] = _get_client_field('company')
  elif command2 == 'E':
    client['email'] = _get_client_field('email')
  elif command2 == 'P':
    client['position'] = _get_client_field('position')
  elif command2 == 'S':
    client['name'] = _get_client_field('name')
    client['company'] = _get_client_field('company')
    client['email'] = _get_client_field('email')
    client['position'] = _get_client_field('position') 


def Update(client_name):
  global clients
  for client in enumerate(clients):
    if client['name'] == client_name:
      while True:
        command2 = None
        while not (command2 == 'N' or command2 == 'C' or command2 =='E' or command2 == 'P' or command2 == 'S'):
          print('\n[?] What field do you want to update? ->',
            '\n[N]ame',
            '\n[C]ompany',
            '\n[E]mail',
            '\n[P]osition',
            '\n[S]obre_escribir'
          )
          command2 = input().upper()
          if not (command2 == 'N' or command2 == 'C' or command2 =='E' or command2 == 'P' or command2 == 'S'):
            print('\n[!] Invalid command')
        _updating_client(client, command2)
        while True:
          other_change = None
          while not (other_change == 'Y' or other_change == 'N'):
            other_change = input('\n[?] Do you want to update other field? [Y/N] : ').upper()
            if not (other_change == 'Y' or other_change == 'N'):
              print('\n[!] Invalid command')
          if other_change == 'Y':
            break
          elif other_change == 'N':
            return
  print("Client not in client's list")


def Delete(client_name_to_delete):
  global clients
  for client in clients:
    if client['name'] == client_name_to_delete:
      clients.remove(client)
      print(f'\n\t[D] Client {client_name_to_delete} -> deleted successfully\n')
      # return list_clients()
    else:
      _client_not_found(client_name_to_delete)
  # return list_clients()


def _print_method(client):
  print('{name} | {company} | {email} | {position}'.format(
    name=client['name'], company=client['company'],
    email=client['email'], position=client['position']
  ))


def create_client(client):
  global clients
  if client not in clients:
    clients.append(client)
    print('\n [C]reated client ->\n')
    _print_method(client)
  else:
    print('\n [-] Client already exist')


def Search(client_name_to_search):
  global clients
  for client in clients:
    if client['name'] != client_name_to_search:
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
  print(' -> [C]reate client' )
  print(' -> [R]ead clients'  )
  print(' -> [U]pdate client' )
  print(' -> [D]elete client' )
  print(' -> [S]earch client' )
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
  return client_name.capitalize()


def _get_client_field(field_name):
  field = None
  while not field:
    field = input(f'What is the client {field_name}? : ')
  return field

def _get_fields(): return {
    'name': _get_client_field('name').capitalize(),
    'company': _get_client_field('company').capitalize(),
    'email': _get_client_field('email'),
    'position': _get_client_field('position').capitalize()
  }



if __name__ == '__main__':

  _initialize_clients_from_storage()
  _print_welcome()
  global command_upper
  command_upper = input().upper()

  print('\n')
  if command_upper == 'C':
    client = _get_fields()
    create_client(client)

  elif command_upper == 'R':
    list_clients()

  elif command_upper == 'U':
    client_name,id = _get_client_name()
    Update(client_name)

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

  _save_clients_to_storage()