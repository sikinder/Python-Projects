lines = int(input("Enter lines for pyramid: "))
space = " "
star = "* "
for i in range(0,lines+1):
    print((lines+1)*space, end = '')
    print(i*star)
    lines = lines - 1

