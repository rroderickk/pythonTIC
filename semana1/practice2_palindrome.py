def palindrome(p):
  p = p.replace(" ", "").lower()
  
  if p[::] == p[::-1]:
    return True 
  else:
    return False


def main():
  palabra = input('\nwrite a word\n')

  is_palindrome = palindrome(palabra)

  if is_palindrome == True:
    print('true')
  else:
    print('false')


if __name__ == "__main__":
  main()