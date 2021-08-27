    # -*- coding: utf-8 -*-
    """
    Created on Thu Aug 26 10:52:41 2021
    
    @author: Neto
    """
    class No(object):
        def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
            self.pai       = pai
            self.valor1    = valor1
            self.valor2    = valor2
            self.anterior  = anterior
            self.proximo   = proximo
        
    class lista(object):
        head = None
        tail = None
    
        # INSERE NO INÍCIO DA LISTA
        def inserePrimeiro(self, v1, v2, p):
            novo_no = No(p, v1, v2, None, None)
            if self.head == None:
                self.tail = novo_no
                self.head = novo_no
            else:
                novo_no.proximo = self.head
                self.head.anterior = novo_no
                self.head = novo_no
    
        # INSERE NO FIM DA LISTA
        def insereUltimo(self, v1, v2, p):
    
            novo_no = No(p, v1, v2, None, None)
    
            if self.head is None:
                self.head = novo_no
            else:
                self.tail.proximo = novo_no
                novo_no.anterior   = self.tail
            self.tail = novo_no
    
        # REMOVE NO INÍCIO DA LISTA
        def deletaPrimeiro(self):
            if self.head is None:
                return None
            else:
                no = self.head
                self.head = self.head.proximo
                if self.head is not None:
                    self.head.anterior = None
                else:
                    self.tail = None
                return no
    
        # REMOVE NO FIM DA LISTA
        def deletaUltimo(self):
            if self.tail is None:
                return None
            else:
                no = self.tail
                self.tail = self.tail.anterior
                if self.tail is not None:
                    self.tail.proximo = None
                else:
                    self.head = None
                return no
    
        def vazio(self):
            if self.head is None:
                return True
            else:
                return False
            
        def exibeLista(self):
            
            aux = self.head
            str = []
            while aux != None:
                temp = []
                temp.append(aux.valor1)
                temp.append(aux.valor2)
                str.append(temp)
                aux = aux.proximo
            
            return str
        
        def exibeCaminho(self):
            
            atual = self.tail
            caminho = []
            while atual.pai is not None:
                caminho.append(atual.valor1)
                atual = atual.pai
            caminho.append(atual.valor1)
            caminho = caminho[::-1]
            return caminho
        
        def exibeCaminho1(self,valor):
                    
            atual = self.head
            while atual.valor1 != valor:
                atual = atual.proximo
        
            caminho = []
            atual = atual.pai
            while atual.pai is not None:
                caminho.append(atual.valor1)
                atual = atual.pai
            caminho.append(atual.valor1)
            return caminho
    
        def primeiro(self):
            return self.head
        
        def ultimo(self):
            return self.tail
    
    class busca(object):
    
        def amplitude(self, inicio, fim):
    
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
                atual = l1.deletaPrimeiro()
                if atual is None: break
    
                ind = nos.index(atual.valor1)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):
    
                    novo = grafo[ind][i]
                    flag = True  # pressuponho que não foi visitado
    
                    # controle de nós repetidos
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
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("Fila:\n",l1.exibeLista())
                           # print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho
    
            return "caminho não encontrado"
    
    
    nos = ["ALENCAR","BORGES","CENTRO","DUARTE","ESTEVES","FREIRE",
           "GOMES","HOLANDA","INACIO","JACINTO","KAISER","LACERDA",
           "MACEDO","NOGUEIRA","OLIVEIRA","PACHECO","QUEIROZ","RIBEIRO",
           "SILVA","TEIXEIRA","UCHOA","VASCONCELOS","WAGNER","XAVIER",
           "YORK","ZAMBONI"]
    
    # ORDEM CRESCENTE
    
    grafo = [
                ["GOMES", "RIBEIRO"],                 #0
                ["JACINTO", "PACHECO", "QUEIROZ"],
                ["JACINTO", "KAISER", "TEIXEIRA","XAVIER"],
                ["MACEDO"],
                ["MACEDO","YORK"],
                ["OLIVEIRA", "WAGNER"],
                ["ALENCAR"],
                ["NOGUEIRA"],
                ["QUEIROZ"],
                ["BORGES", "CENTRO","SILVA"],
                ["CENTRO", "MACEDO","YORK"],
                ["OLIVEIRA","PACHECO","UCHOA"],
                ["DUARTE", "ESTEVES","KAISER","NOGUEIRA"],
                ["HOLANDA", "MACEDO", "TEIXEIRA"],
                ["FREIRE", "LACERDA", "XAVIER"],
                ["BORGES", "LACERDA",],
                ["BORGES", "INACIO"],
                ["ALENCAR", "TEIXEIRA"],
                ["JACINTO", "ZAMBONI"],
                ["CENTRO", "NOGUEIRA","RIBEIRO","WAGNER"],
                ["LACERDA"],
                ["YORK"],
                ["FREIRE","TEIXEIRA"],
                ["CENTRO","OLIVEIRA"],
                ["ESTEVES","KAISER","SILVA","VASCONCELOS"],
                ["SILVA"]
                
           ]
    
    sol = busca()
    caminho = []
    
    
   # |||||||||||||||||||||||||||||||||||||||||||
    origem  = "ALENCAR"
    destino = "SILVA"
    
    caminho = sol.amplitude(origem,destino)
    print("\nAmplitude...........: ",caminho)