#range(start,stop,step) = range(20,2, -2)

# for i in range(20,2, -2):
#     print(i)

text="pyxpyxpyx"
for letter in text:
    if letter == "x":
              continue
    print(letter, end=" ")

    x=0
    while x< 5:
           print("Not there yet, x=" +str(x))
           x=x+1
    print("x=",x)

    #bitwise operator
    var=17
    var_right= var>>1 #divide by 2
    var_left= var<<2 #multiply by 4
    print(var,var_right, var_left)