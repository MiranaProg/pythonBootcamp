if __name__ == '__main__':
    """
    this code takes coordinates of 3D cuboid x,y,z along with 'n' integer and
     print a list of all possible coordinates(i,j,k) given by  on a 3D grid i+j+k where the sum of is not equal to . Here
     https://www.hackerrank.com/challenges/list-comprehensions/problem
    """
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    poosible_coordinates = []
    '''for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != n:
                    poosible_coordinates.append([i,j,k])
                else:
                    pass
                '''
    poosible_coordinates =[[ i, j, k] for i in range( x+1) for j in range( y+1) for k in range(z+1) if ((i+j+k) != n)]
    print(poosible_coordinates)
    print(type(poosible_coordinates))

    '''Sample Input 0
       1
       1
       1
       2
       Sample Output 0

       [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
       '''