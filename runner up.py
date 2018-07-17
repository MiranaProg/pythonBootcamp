if __name__ == '__main__':
    '''code to decide a runner up
     for more details : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem'''
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr)) # use set function to make list of unique scores
    high_scores = max(scores)
    rem = 0

    for item in scores:
        print('for item' ,item)
        if item == high_scores:
            scores.remove(item)
            print('removing...' , item)
            print('after removing', scores)
        else:
            print('not removing...' ,item)
            print('no change' , scores)

        print('after removing',scores)



    print(scores)
    print(max(scores))

    '''
input
5
1 2 6 6 5
output
for item 1
not removing... 1
no change [1, 2, 5, 6]
after removing [1, 2, 5, 6]
for item 2
not removing... 2
no change [1, 2, 5, 6]
after removing [1, 2, 5, 6]
for item 5
not removing... 5
no change [1, 2, 5, 6]
after removing [1, 2, 5, 6]
for item 6
removing... 6
after removing [1, 2, 5]
after removing [1, 2, 5]
[1, 2, 5]
5
    '''