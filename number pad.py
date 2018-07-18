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
number_pad(['4' , '2' ,'3', '4' ,'5' ,'6' , '7' , '8' ,'9'])

