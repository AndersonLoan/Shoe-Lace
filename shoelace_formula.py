# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Anderson Loan
#                   Andrew Spears
#                   Spencer Jones
# Section:         574
# Assignment:   Lab 9.15
# Date:         25 10 2022
#

def getpoints(funkyString): #converts the string input to a list of lists of inputs
    funkyList = funkyString.split()
    spoints = [ [ i[:i.find(',')] , i[i.find(',')+1:] ] for i in funkyList ]
    values = [[int(j) for j in i] for i in spoints]
    return values
    

def cross(l1,l2): #performs a 2d cross product
    return  l1[0]*l2[1] - l1[1]*l2[0] 
    

def shoelace(values): #gets area of a simple polygon
    area = sum( [cross(values[i-1], values[i]) for i,j in enumerate(values)] )
    area *= .5
    return area
    

def main(): #main code
    points = getpoints(input('Please enter the vertices: '))
    print('The area of the polygon is ', shoelace(points))


if __name__ == '__main__': main()    