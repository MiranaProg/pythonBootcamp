def print_big(letter):
    patterns={1:'  *  ' ,2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'    *',7:' *   ',8:'*  * ',9:'*    ',10:'*  **', 11:'**  '}
    alphabet={'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],'F':[4,9,5,9,9],'G':[4,9,10,3,4],
              'H':[3,3,4,3,3],'I':[4,1,1,1,11],"K":[3,8,11,8,3]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('k') 


''' output of big.py"
*   *
*  * 
**  
*  * 
*   *
'''


