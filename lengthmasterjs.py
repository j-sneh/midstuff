def lengthmaster(ls):
    total = 0
    for word in ls:
        print 'The length of ' + str(word) + ' is ' + str(len(word))
        print ' '
        total += len(word)
    print 'The total length of all your words is ' + str(total)

its_list_fam = []

for i in range(4):
    words = raw_input('Pick a word ')
    its_list_fam.append(words)

lengthmaster(its_list_fam)
