def number_pad(numliist):
    #milestone project ques1
    pattern={'vertical1':'   |', 'vertical2':'     |', 'v3' :' |', 'horizontal':'-----------'}
    n=0
    for item in range(0,3):
        print(2*pattern['vertical1'])
        print(' ' + numliist[n] + pattern['v3'] + ' ' + numliist[n+1] + pattern['v3'] + ' '+numliist[n+2])
        print(2*pattern['vertical1'] )
        n=n+3
        if item != 2 :
            print(pattern['horizontal'])
    '''more simple way to do the same
     
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    '''
def place_marker(list,marker,position):
    '''
    :Desc: this function is use to change the notepad value(s)
    :param list: taking the test_list values
    :param marker: taking the character to change
    :param position: taking position where to change in the list
    :return: a modified list
    '''
    list[position-1]=marker

test_list =['4' , '2' ,'3', '4' ,'5' ,'6' , '7' , '8' ,'9']
number_pad(test_list)
print('after changing...')
place_marker(test_list,'@',6)
number_pad(test_list)

'''
output would be:
 4 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
after changing...
   |   |
 4 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | @
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
'''

