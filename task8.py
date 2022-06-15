rows = input('enter row number:')
rows=int(rows)

for i in range(1, rows+1):
    for j in range(i):
        print(i, end='')
    print('')
    