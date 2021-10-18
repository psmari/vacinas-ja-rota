from dados import *
from lista import lista


class busca(object):
    def amplitudeUnitario(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            if atual is None:
                break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafoCrescente[ind])):
                novo = grafoCrescente[ind][i]
                flag = True  # pressuponho que não foi visitado

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.valor2 + 1):
                            flag = False
                        else:
                            visitado[j][1] = atual.valor2 + 1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2 + 1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        # print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    def amplitudeMulti(self, inicio, fim):
        # total de objetivos
        tot_obj = len(fim)

        # contador de objetivo alcançado
        iob = 0

        # variável para retornar o caminho
        caminho = []

        while True:
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
    
            Flag4 = False
            while l1.vazio() is not None and Flag4==False:
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                if atual is None: break
    
                ind = nos.index(atual.valor1)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafoDecrescente[ind])):

                    novo = grafoDecrescente[ind][i]
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo in fim:
                            caminho += l2.exibeCaminho()
                            caminho.pop()
                            iob += 1
                            if iob==tot_obj:
                                caminho.append(novo)
                                return caminho
                            else:
                                inicio = novo
                                fim.remove(novo)
                                Flag4 = True

        return "caminho não encontrado"
    
    def profundidadeUnitario(self,inicio,fim):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafoDecrescente[ind])-1,-1,-1):

                novo = grafoDecrescente[ind][i]
                #print("\tFilho de atual: ",novo)
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                    
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"
    
    
    def profundidadeMulti(self, inicio, fim):
        
        # total de objetivos
        tot_obj = len(fim)

        # contador de objetivo alcançado
        iob = 0

        # variável para retornar o caminho
        caminho = []

        while True:

            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
    
            Flag4 = False
            while l1.vazio() is not None and Flag4==False:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual is None: break
    
                ind = nos.index(atual.valor1)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafoDecrescente[ind])-1,-1,-1):

                    novo = grafoDecrescente[ind][i]
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo in fim:
                            caminho += l2.exibeCaminho()
                            #return caminho
                            caminho.pop()
                            iob += 1
                            if iob==tot_obj:
                                caminho.append(novo)
                                return caminho
                            else:
                                inicio = novo
                                fim.remove(novo)
                                Flag4 = True

            return "caminho não encontrado"

    def profundidade_limitada(self, inicio, fim, limite):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            if atual.valor2 < limite:
                ind = nos.index(atual.valor1)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafoCrescente[ind])-1,-1,-1):
    
                    novo = grafoCrescente[ind][i]
                    #print("\tFilho de atual: ",novo)
                    flag = True  # pressuponho que não foi visitado
    
                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                        
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            #print("Árvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"




    def aprofundamento_iterativo(self, inicio, fim):
        
        for limite in range(len(nos)):
            caminho = []
    
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
    
            while l1.vazio() is not None:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual is None: break
    
                if (atual.valor2) < limite:
                    ind = nos.index(atual.valor1)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafoDecrescente[ind])-1,-1,-1):
        
                        novo = grafoDecrescente[ind][i]
                        #print("\tFilho de atual: ",novo)
                        flag = True  # pressuponho que não foi visitado
        
                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                            
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                #print("Árvore de busca:\n",l2.exibeLista())
                                return caminho

        return "caminho não encontrado"

    def bidirecional(self, inicio, fim):

        # listas para a busca a partir da origem - busca 1
        l1 = lista()      # busca na FILA
        l2 = lista()      # cópia da árvore completa

        # listas para a busca a partir da destino -  busca 2
        l3 = lista()      # busca na FILA
        l4 = lista()      # cópia da árvore completa

        # cria estrutura para controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
        linha = []
        linha.append(fim)
        linha.append(2)
        visitado.append(linha)
        
        while True:
            
            # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
            flag1 = True
            while flag1:
                atual = l1.deletaPrimeiro()
                ind = nos.index(atual.valor1)
                for i in range(len(grafoCrescente[ind])):
                    novo = grafoCrescente[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 1:    # visitado na mesma árvore
                                flag2 = False
                            else:                      # visitado na outra árvore
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l2.exibeCaminho()
                            #caminho = caminho[::-1]
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                        # if flag3
                    # if flag2
                # for i
                
                
                if(l1.vazio()!=True):
                    aux = l1.primeiro()
                    if aux.valor2 == atual.valor2:
                        flag1 = True
                    else:
                        flag1 = False                

            # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                if atual==None:
                    break
                ind = nos.index(atual.valor1)
                for i in range(len(grafoCrescente[ind])):
                    novo = grafoCrescente[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                        
                    if flag2:
                        l3.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l4.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l4.exibeArvore()
                            caminho = caminho[::-1]
                            caminho += l2.exibeArvore1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)
                        
                if(l3.vazio() != True):
                    aux = l3.primeiro()
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False

    def custo_uniforme(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(0,0,None,inicio)
        l2.insereUltimo(0,0,None,inicio)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafoPeso[ind])):
                novo = grafoPeso[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafoPeso[ind][i][1]
                v1 = v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            visitado[j][1]=v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1 , v1, atual)
                    l2.inserePos_X(novo, v1, v1, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      

    def greedy(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(0,0,None,inicio)
        l2.insereUltimo(0,0,None,inicio)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafoPeso[ind])):
                novo = grafoPeso[ind][i][0]
                ind1 = nos.index(grafoPeso[ind][i][0])

                # HEURÍSTICA DO NÓ ATUAL ATÉ O OBJETIVO
                v2 = atual.valor2 + grafoPeso[ind][i][1]
                v1 = heuristicas[nos.index(fim)][ind1]

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1

                        break
                
                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      

    
    def a_estrela(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(0,0,None,inicio)
        l2.insereUltimo(0,0,None,inicio)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for i in range(len(grafoPeso[ind])):
                novo = grafoPeso[ind][i][0]
                ind1 = nos.index(grafoPeso[ind][i][0])

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafoPeso[ind][i][1]
                v1 = v2 + heuristicas[nos.index(fim)][ind1]
                
                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1]=v1
                        break
                
                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"
