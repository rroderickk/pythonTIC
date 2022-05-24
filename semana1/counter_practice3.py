
def counter(n,e):
  print('\n')
  for i in range(e):
    n += n
    print(n)


def main():
  n = int(input('[?] Insert number\n'))
  e = int(input('\n[!] Ending point\n\n'))

  counter(n,e)

if __name__ == '__main__':
  main()