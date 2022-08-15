c = 1
win = 0
draw = 0
lose = 0
points = 0

while c <= 8:
    print('ٍEnter Match Points:', c)
    res = int(input())
    if res == 3:
        win += 1
        c += 1
        points += res
    elif res == 1:
        draw += 1
        c+= 1
        points += res
    elif res == 0:
        lose += 1
        c += 1
    else:
        print('It not acceptable')
print('Points of rezvan team: ', points)
print('Number of rezvan team wins: ', win)
print('Number of rezvan team losses: ', lose)
print('Number of rezvan team tied games : ', draw)