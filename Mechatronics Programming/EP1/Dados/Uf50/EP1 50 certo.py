import random, time

def main(nome,tipo):
    interacoes=0
    arq=open(nome, 'r')
    linha=0
    cl=0
    form=[]
    vars=""

    for line in arq:
        temp=[]
        if line[0]=="p":
            formula=line.strip("\n")
            formula=formula.split(" ")
            variaveis=int(formula[2])
            clausulas=int(formula[4])

        elif line[0]!="c" and line[0]!="p" and cl<clausulas:
            if line[0]==" ":
                line=line[1:]
            claus=line.strip("\n")
            claus=claus.split(" ")
            for c in range(len(claus)):
                if claus[c]==" " or claus[c]=="0":
                    del claus[c]

                else:
                    temp.append(int(claus[c]))
                
            cl+=1
            form.append(temp)

    arq.close()
    #formula organizada em lista

    tam_clausula=len(form[0])
    possibilidades=2**variaveis
    cl=0

    if tipo=="brute":
        while interacoes<possibilidades and cl<clausulas:
            cl=0
            num=0
            vars=BruteForce(vars,interacoes,variaveis)
            interacoes+=1
            if interacoes==10000000000 or interacoes==1000000000 or interacoes==50000000 or interacoes==100000000 or interacoes==10000000:
                print(tipo + str(interacoes))

            while cl<clausulas and num<tam_clausula:
                num=0
                for n in range(tam_clausula):
                    if form[cl][n]==abs(form[cl][n]) and vars[abs(form[cl][n])-1]=="1":
                        break
                    if form[cl][n]!=abs(form[cl][n]) and vars[abs(form[cl][n])-1]=="0":
                        break
                    num+=1

                cl+=1

            if cl==clausulas:
                var_print=""
                for t in range(variaveis):
                    for s in range(len(str(t+1))):
                        parc=int(str(t+1)[s])
                        if s==0:
                            var_print+="x"+chr(8320+parc)
                        else:
                            var_print+=chr(8320+parc)

                    var_print+="=" + vars[t] + " "

                return "Interações: " + str(interacoes) + "\n" + "Combinação de variavéis:\n" + var_print 


        return "Não há possibilidade"
    else:
        while interacoes<possibilidades and cl<clausulas:
            cl=0
            num=0
            vars=RandomSearch(interacoes,variaveis)
            interacoes+=1
            if interacoes==10000000000 or interacoes==1000000000 or interacoes==50000000 or interacoes==100000000 or interacoes==10000000:
                print(tipo + str(interacoes))

            while cl<clausulas and num<tam_clausula:
                num=0
                for n in range(tam_clausula):
                    if form[cl][n]==abs(form[cl][n]) and vars[abs(form[cl][n])-1]=="1":
                        break
                    if form[cl][n]!=abs(form[cl][n]) and vars[abs(form[cl][n])-1]=="0":
                        break
                    num+=1

                cl+=1

            if cl==clausulas:
                var_print=""
                for t in range(variaveis):
                    for s in range(len(str(t+1))):
                        parc=int(str(t+1)[s])
                        if s==0:
                            var_print+="x"+chr(8320+parc)
                        else:
                            var_print+=chr(8320+parc)

                    var_print+="=" + vars[t] + " "

                return "Interações: " + str(interacoes) + "\n" + "Combinação de variavéis:\n" + var_print 


        return "Não há possibilidade"

def BruteForce(vars,interacoes,variaveis):
    if interacoes==0:
        for t in range(variaveis):
            vars+="1"
    else:
        vars=int(vars,2)
        vars+=-1
        vars=bin(vars)
        vars=vars[2:]
        if len(vars)!=variaveis:
            zeros=""
            for i in range(variaveis-len(vars)):
                zeros+="0"

            vars=zeros+vars
        

    return(vars)

def RandomSearch(interacoes,variaveis):
    vars=""
    random.seed(interacoes)
    for r in range(variaveis):
        vars+=str(random.randint(0,1))

    return(vars)

res=open('resultado50.txt', 'w', encoding='utf-8')
total=0.0
for y in range(5):
    tim=time.clock()
    res.write("Arquivo: uf50-0"+str(y+1)+".cnf\n"+"BruteForce:\n")
    res.write(main("uf50-0"+str(y+1)+".cnf","brute"))
    res.write("\n"+"Tempo(BruteForce):"+str(time.clock()-tim))
    total+=time.clock()-tim
    res.write("\n")

    res.write("RandomSearch:\n")
    tim=time.clock()
    res.write(main("uf50-0"+str(y+1)+".cnf","random"))
    res.write("\n"+"Tempo(RandomSearch):"+str(time.clock()-tim))
    total+=time.clock()-tim
    res.write("\n")
    res.write("\n")

res.write("\nTotal="+str(total))
res.close()
