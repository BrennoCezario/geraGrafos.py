def grafosA():
    print('')
    
    n = int(input("n = "))
    m = int(input("m = "))
    Arestas.append(m)
    E = m * [0]
    i=0
    j=0
    
    for a in range(0,len(E)):
        print("--- Aresta", a+1,"---")
        i= int(input("V inicial: "))
        j= int(input("V final: "))
        E[a] = [i, j]
        print('')

    M = [0]*n
    for i in range(n):
        M[i] = [0]*n
    
    for a in E:
        for b in range(1):
            M[a[b]-1][a[b+1]-1] = 1
            M[a[b+1]-1][a[b]-1] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(n):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    k=0   
    for i in range(n):    
        print(k+1,"|",end=" ")
        k+=1
        for j in range(n):
            print(M[i][j],end=" ")
            if j+1==n:
                print("|",end=" ")
        print("")
    print("")
    print("m =",m)

    
def grafosB():
    
    G = input("Nome do Grafo: ")
    M = []
    for i in range(len(Grafo)):
        if Grafo[i] == G:
            M = Matriz[i]
            m = Arestas[i]

    i=0
    j=0
    for i in range(len(M)):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    k=0   
    for i in range(len(M)):    
        print(k+1,"|",end=" ")
        k+=1
        for j in range(len(M)):
            print(M[i][j],end=" ")
            if j+1==len(M):
                print("|",end=" ")
        print("")
    print("")
    print("m =",m)


def Completo():
    print("---Completo---")
    n= int(input("n: "))
    m = (n*(n-1))//2
    Arestas.append(m)
    
    M = [0]*n
    for i in range(n):
        M[i] = [0]*n
    
    for a in range(n):
        for b in range(n):
            if a!=b:
               M[a][b] = 1

        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(n):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(n):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(n):
            print(M[i][j],end=" ")
            if j+1==n:
                print("|",end=" ")
        print("")
    print("")
    print("m =",m)   
    

def BipartidoCompleto():
    print("---BipartidoCompleto---")
    n1= int(input("n1: "))
    n2= int(input("n2: "))
    m = n1*n2
    matrizSize = n1+n2
    Arestas.append(m)
    
    M = [0]*(matrizSize)
    for i in range(matrizSize):
        M[i] = [0]*matrizSize
    
    for a in range(matrizSize):
        for b in range(matrizSize):
            if(a!=b):
                if (a>=n1 and b<n1) or (a<n1 and b>=n1):
                   M[a][b] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)

def Estrela():
    print("---Estrela---")

    
    n= int(input("n: "))
    m = n
    matrizSize = n+1
    Arestas.append(m)
    
    M = [0]*(n+1)
    for i in range(n+1):
        M[i] = [0]*(n+1)
    
    for a in range(n+1):
        for b in range(n+1):
            if(a!=b):
                if (a>=1 and b<1) or (a<1 and b>=1):
                   M[a][b] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)

def Caminho():
    print("---Caminho---")

    
    n = int(input("n: "))
    m = n-1
    matrizSize = n
    Arestas.append(m)
    
    M = [0]*(n)
    for i in range(n):
        M[i] = [0]*(n)
    
    for a in range(n):
        for b in range(n):
            if(a!=b):
                if (a == b+1) or (b == a+1):
                   M[a][b] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)

def Ciclo():
    print("---Ciclo---")

    
    n= int(input("n: "))
    m = n
    matrizSize = n
    Arestas.append(m)
    
    M = [0]*(n+1)
    for i in range(n+1):
        M[i] = [0]*(n+1)
    
    for a in range(n):
        for b in range(n):
            if(a!=b):
                if ((a == b+1) or (b == a+1)) or ((a == 0 and b == n-1) or (b == 0 and a == n-1)):
                   M[a][b] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)

def Roda():
    print("---Roda---")

    
    n= int(input("n: "))
    m = 2*n
    matrizSize = n+1
    Arestas.append(m)
    
    M = [0]*(n+1)
    for i in range(n+1):
        M[i] = [0]*(n+1)
    
    for a in range(n+1):
        for b in range(n+1):
            if(a!=b):
                if ((a == b+1) or (b == a+1)) or ((a == 0 and b == n-1) or (b == 0 and a == n-1)) or ((a==n and b!=n) or (b==n and a!=n)):
                   M[a][b] = 1
        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        
        print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)

def Cubo():
    print("---Cubo---")

    
    n= int(input("n: "))
    m = (2**(n-1))*n
    matrizSize = 2**n
    Arestas.append(m)
    x = 2
    
    M = [0]*(2**n)
    for i in range(2**n):
        M[i] = [0]*(2**n)
    if n > 0:   
        M[0][1] = 1
        M[1][0] = 1
        if n > 1:
            while x <= n:
                for a in range(2**x):
                    for b in range(2**x):
                        if(a!=b):
                            if (a <= 2**x//2 and b <= 2**x//2):
                               if M[a][b] == 1:
                                   M[a+(2**x//2)][b+(2**x//2)] = 1
                i = 0
                j = 2**x-1
                while i < 2**x:
                    while j >= 0:
                        M[i][j] = 1
                        i = i + 1
                        j = j - 1
                x+=1

        
    Matriz.append(M)
        
    G = input("Nome do Grafo: ")
    Grafo.append(G)

    for i in range(matrizSize):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    j=0
    u=1
    for i in range(matrizSize):    
        if i >= 9:
            print(u,"|",end="")
        else:
            print(u,"|",end=" ")
        u+=1
        for j in range(matrizSize):
            if j >= 9:
                print(M[i][j],end="  ")
            else:
                print(M[i][j],end=" ")
            if j+1==matrizSize:
                print("|",end=" ")
        print("")
    print("")
    print("m = ",m)


def grafosD():
        
    G = input("Nome do Grafo: ")
    M = []
    for i in range(len(Grafo)):
        if Grafo[i] == G:
            M = Matriz[i]
            m = Arestas[i]

    i=0
    j=0
    for i in range(len(M)):
        if i == 0:
            print("   ",i+1,end=" ")
        else:
            print(i+1,end=" ")  
    print("")
    k=0   
    for i in range(len(M)):    
        print(k+1,"|",end=" ")
        k+=1
        for j in range(len(M)):
            print(M[i][j],end=" ")
            if j+1==len(M):
                print("|",end=" ")
        print("")
    print("")
    print("m =",m)
    cont = [0]*len(M)
    contVar = 0
    componentes = 0
    aux = []

    while i < len(M):
        while j < len(M):
            if M[i][j] == 1:
                 if contVar == 0:
                     cont[0] = i+1
                     contVar += 1
                 for k in range (len(cont)):
                     if j != cont[k]:                        
                          if k == len(cont)-1:
                             cont[contVar] = j+1
                             contVar += 1
                             
            if componentes > 1:
                for k in range (len(aux)):
                    if j == aux[k]:
                        j+=1
                        contVar = 0
                        cont = [0]*len(cont)
                
            else:
                j += 1
        if contVar == len(cont):
            componentes += 1 
        i += 1
        if contVar < len(cont) and contVar != 0:
            componentes += 1
            for k in range (len(cont)):
                aux.append(cont[k])
            contVar = 0
            cont = [0]*len(cont)
                    
    if componentes > 1:
        print("Grafo não é conexo e possui ", componentes, " componentes conexas")
    else:
        print("Grafo é conexo e possui ", "1", " componente conexa")

            
    
def escolha():
    print("")
    print("Escolha uma opcao: ")
    print("(a) Criar grafo")
    print("(b) Escolher grafo")
    print("(c) Produzir um grafo de uma classe especial")
    
    print("(e) Sair")
    opcao = input("Digite a opcao escolhida: ")

    while opcao != 'a' and opcao != 'A' and opcao != 'b' and opcao != 'B' and opcao != 'c' and opcao != 'C' and opcao != 'd' and opcao != 'D' and opcao != 'e' and opcao != 'E':
        print("Erro: digite apenas 'a', 'b', 'c', 'd' ou 'e'' ")
        opcao = input("Digite novamente: ")

    if opcao == 'a' or opcao == 'A':
        grafosA()
        return escolha()
    
    elif opcao == 'b' or opcao == 'B':
        if(len(Grafo)<1):
            print("Vamos criar o grafo primeiro!")
            print("")
            grafosA()
        else:
            grafosB()
        return escolha()

    elif opcao == 'c' or opcao == 'C':
        grafosC()
        return escolha()
    elif opcao == 'd' or opcao == 'D':
        grafosD()
     
    else:
        return exit

def grafosC():
    print("")
    print("Escolha uma opcao: ")
    print("1. Completo")
    print("2. Bipartido Completo")
    print("3. Estrela")
    print("4. Caminho")
    print("5. Ciclo")
    print("6. Roda")
    print("7. Cubo")

    opcao = input("Digite a opcao escolhida: ")
    if opcao == '1':
        Completo()
    elif opcao == '2':
        BipartidoCompleto()
    elif opcao == '3':
        Estrela()
    elif opcao == '4':
        Caminho()
    elif opcao == '5':
        Ciclo()
    elif opcao == '6':
        Roda()
    elif opcao == '7':
        Cubo()
    
    else:
        print("Apenas numeros de 1 a 7")
        return grafosC()

Grafo = []
Matriz = []
Arestas = []
escolha()
