decryptionary = {
}

firste = raw_input('What should the value of 0 be?')
seconde = raw_input('What should the value of 1 be?')
thirde = raw_input('What should the value of space be?')

decryptionary['0']= firste
decryptionary['1'] = seconde
decryptionary[' ']= thirde
print decryptionary

def disencryptor(n):
  decryptlist = []
  for letter in n:
    if letter == decryptionary['0']:
      decryptlist.append('0')
    if letter == decryptionary['1']:
      decryptlist.append('1')
    if letter == decryptionary[' ']:
      decryptlist.append(' ')
  decryptedstring = ''.join(decryptlist)
  return decryptedstring
  

g = raw_input('input a thing to decrypt')
print disencryptor(g)
