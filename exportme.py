my_list = range(70000)

my_list = filter(lambda x: x**2 % 2 == 0, my_list)

f = open("output.txt", "w+")

for i in my_list:
    f.write(str(i) + '\n')

f.close()

