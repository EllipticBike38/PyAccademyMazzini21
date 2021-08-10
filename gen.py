import random
file=open('es3B.txt','w',encoding='utf-8')
for i in range(10):
    for i in range(10):
        print(random.randint(0,99),end=' ', file=file)
    print(file=file)
file.close()