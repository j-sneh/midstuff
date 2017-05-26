decryptionary = {
}

firste = raw_input('What should the value of 0 be?')
seconde = raw_input('What should the value of 1 be?')
thirde = raw_input('What should the value of space be?')

decryptionary['0']= firste
decryptionary['1'] = seconde
decryptionary[' ']= thirde
print decryptionary

def encryptor(n):
  decryptlist = []
  for letter in n:
    if letter == '0':
      decryptlist.append(decryptionary['0'])
    if letter == '1':
      decryptlist.append(decryptionary['1'])
    if letter == decryptionary[' ']:
      decryptlist.append(decryptionary[' '])
  decryptedstring = ''.join(decryptlist)
  return decryptedstring
  

g = raw_input('input a thing to encrypt')
print encryptor(g)