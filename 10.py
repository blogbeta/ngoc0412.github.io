trashs = int(input('Số lượng file rác: '))
for i in range(trashs):
    file = open(r'file' + str(i) + '.txt', 'w', encoding = 'utf-8')
    file.write('<3 Thư <3')
    file.close()