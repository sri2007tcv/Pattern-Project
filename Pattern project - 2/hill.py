row = 5
x = "#"
k = row - 1
for i in range (0, row):
    for j in range(0, k):
        print(end = " ")
    k = k -1
    for j in range (0, i +1):
        print('*', end  = " ")
    print('\r')