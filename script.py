import resolvedor
import time

alg= resolvedor.SA()

alpha = 0.97
iter=15
Tf = 1.0
To = 5.0
tempot = 0
custot = 0
custo = []
custob = 100000
layout = 'Layout.txt'
products = 'Products.txt'

file = open(layout, 'r')
arq2 = file.read().splitlines()
file = open(products, 'r')
arq3 = file.read().splitlines()

arquivo = open('instancias.txt','w')
arquivo.close()

arquivo = open('instancias.txt','a')
caminho = 'Instancias'
file = '\instances_d5_ord'
inst = []
for k in range(5,75):
    print(k)
    inst.append(caminho+file+str(k))
for i in range(len(inst)):
    file = open(inst[i], 'r')
    arq = file.read().splitlines() 
    alg.arm.leitura(arq2,arq3,arq)
    for j in range(5):
        timer_inicio = time.perf_counter()
        custo.append(alg.sa())
        timer_fim = time.perf_counter()
        tempoTotal = timer_fim-timer_inicio
        tempot+=tempoTotal
        custot+=custo[j]
        if custo[j]<custob:
            custob = custo[j]
        print(j)
    tempom=tempot/5
    custom = custot/5
    arquivo.write(inst[i]+"&"+str(alg.arm.cel*alg.arm.prt)+"&"+str(alg.arm.totalord)+"&"+str(alpha)+"&"+str(iter)+"&"+str(To)+"&"+str(Tf)+"&"+str(tempom)+"&"+str(custom)+"&"+str(custob)+"\n")
arquivo.close()
