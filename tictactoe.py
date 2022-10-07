# write your code here
import math

x = False
o = False

statement = True
print("---------")
print("|       |")
print("|       |")
print("|       |")
print("---------")
i = 0
mat = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
while True:
    a, b = input().split()
    if str.isalpha(a) and str.isalpha(b):
        print("You should enter numbers!")
    elif int(a) > 3 or int(b) > 3:
        print("Coordinates should be from 1 to 3!")
    elif mat[int(a) - 1][int(b) - 1] != " ":
        print("This cell is occupied! Choose another one!")
    else:
        if i % 2 == 0:
            mat[int(a) - 1][int(b) - 1] = "X"
            print("---------")
            print(f"| {mat[0][0]} {mat[0][1]} {mat[0][2]} |")
            print(f"| {mat[1][0]} {mat[1][1]} {mat[1][2]} |")
            print(f"| {mat[2][0]} {mat[2][1]} {mat[2][2]} |")
            print("---------")
            i += 1
        else:
            mat[int(a) - 1][int(b) - 1] = "O"
            print("---------")
            print(f"| {mat[0][0]} {mat[0][1]} {mat[0][2]} |")
            print(f"| {mat[1][0]} {mat[1][1]} {mat[1][2]} |")
            print(f"| {mat[2][0]} {mat[2][1]} {mat[2][2]} |")
            print("---------")
            i += 1
        if mat[0][0] == mat[1][1] == mat[2][2] or mat[0][1] == mat[1][1] == mat[2][1] or mat[1][0] == mat[1][1] == \
                mat[1][2] or mat[0][2] == mat[1][1] == mat[2][0]:
            if mat[1][1] == 'X':
                x = True
            elif mat[1][1] == 'O':
                o = True
        if mat[0][0] == mat[0][1] == mat[0][2] or mat[0][0] == mat[1][0] == mat[2][0]:
            if mat[0][0] == 'X':
                x = True
            elif mat[0][0] == 'O':
                o = True
        if mat[2][0] == mat[2][1] == mat[2][2] or mat[0][2] == mat[1][2] == mat[2][2]:
            if mat[2][2] == 'X':
                x = True
            elif mat[2][2] == 'O':
                o = True
        if x:
            print("X wins")
            break
        elif o:
            print("O wins")
            break
        elif i == 9:
            print("Draw")
            break
