import AOCH

input8 = AOCH.ril('input8.txt')
# input8 = AOCH.ril('test')


temp = []
for i in range(len(input8)):
    temp.append(input8[i].split(' '))
    temp[i][1] = int(temp[i][1])


def run(itemlist):
    acc = 0
    visited = []
    k = 0
    while k < len(itemlist):
        if k in visited:
            return [acc, 0]
        elif itemlist[k][0] == 'acc':
            visited.append(k)
            acc += itemlist[k][1]
            k += 1
        elif itemlist[k][0] == 'jmp':
            visited.append(k)
            k += itemlist[k][1]
        elif itemlist[k][0] == 'nop':
            visited.append(k)
            k += 1
    return [acc, 1]


print('First part the acc reached ' + str(run(temp)[0]))


def run2(itemlist):
    for k in range(len(itemlist)):
        temp1 = itemlist.copy()
        if temp1[k][0] == 'jmp':
            temp1[k][0] = 'nop'
            save = run(temp1)
            if save[1] == 1:
                return save[0]
            else:
                temp1[k][0] = 'jmp'
            continue
        elif temp1[k][0] == 'nop':
            temp1[k][0] = 'jmp'
            save = run(temp1)
            if save[1] == 1:
                return save[0]
            else:
                temp1[k][0] = 'nop'
            continue

    return 0


print('First part the acc reached ' + str(run2(temp)) + ' where there whore no loops')
