def quadform(a,b,c):
    if a*c*4 <= b**2:
      xone = (-1 * b + (b**2 - 4*a*c)**0.5)/2*a
      xtwo = (-1*b - (b**2 - 4*a*c)**0.5)/2*a
      if b**2 - 4*a*c > 0:
        print 'Root number one is (' +str(xone) +',0)'
        print 'Root number two is (' +str(xtwo) +',0)'
      elif b**2 - 4*a*c == 0:
        print 'The only root is (' +str(xone) +',0)'
    elif a*c*4 > b**2:
      print 'This parabola has no roots'

def pureint(alphanumeric):
    purified = []
    for character in alphanumeric:
        if character in '-.0123456789*/+%':
            purified.append(character)
    purified = ''.join(purified)
    return purified


def prompter():
  print "This calculator will remove anything that isn't a number or an arithmetic operator"
  a = raw_input('what is your a value?')
  b = raw_input('what is your b value?')
  c = raw_input('what is your c value?')
  
  

  if a == '' or b == '' or c == '':
      print 'One or more variables did not have a number assigned, try again'
  else:
      a = pureint(a)
      b = pureint(b)
      c = pureint(c)
      
      a = eval(a)
      b = eval(b)
      c = eval(c)
      print ' '
      print 'a is equal to ' + str(a)
      print 'b is equal to ' + str(b)
      print 'c is equal to ' + str(c)
      print ' '
      a = float(a)
      b = float(b)
      c = float(c)
      print 'calculating...'
      print quadform(a,b,c)
      print ' '
  prompter()

prompter()
