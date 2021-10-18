class No(object):
    def __init__(
        self,
        pai=None,
        valor1=None,
        valor2=None,
        anterior=None,
        proximo=None,
        estado=None
    ):
        self.pai = pai
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo
        self.estado = estado
