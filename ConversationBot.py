name = raw_input('My name is JPP, What is your name? ')

x = raw_input('Hello, ' + name +", How was your day? ").lower()

if "good" in x and 'not' not in x or 'great' in x and 'not' not in x:
    y = raw_input('Awesome! Mine was good aswell. Anyways, Do you like chocolate? ').lower()
elif "bad" in x or 'terrible' in x or 'not good' in x or 'horrible' in x:
    y = raw_input('That sucks. Anyways, Do you like chocolate? ').lower()
elif "good" not in x or "bad" not in x or "terrible" not in x or 'great' not in x:
    y = raw_input('Okay, do you like chocolate? ').lower()

if "yes" in y or 'yeah' in y or 'yep' in y:
    z = raw_input("So do I! High-five! Well, I would high-five you if I wasn't a computer program. I'm getting bored. Goodbye!").lower()
    if 'bye' in z or 'see' in z:
        print "Thanks for being polite and saying goodbye! You're really cool " + name
        print ' '
        print 'Shutting Down...'
    else:
        print 'This has been JPP'
        print 'Shutting Down...'
elif 'no' in y or 'hate' in y:
    print "Buzzkill, Go away. You know what? I'm leaving, I don't like you"
    print 'Shutting Down...'
else:
    z = raw_input("Cool, I guess... I'm getting bored. Bye!").lower()
    if 'bye' in z or 'see' in z:
        print "Thanks for being polite and saying bye! You're really cool " + name
        print 'Shutting Down...'
    else:
        print 'This has been JPP'
        print 'Shutting Down...'
