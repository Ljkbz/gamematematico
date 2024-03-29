from random import randint


class Calcular:
    

    def __init__(self:object,dificuldade:int) -> None:
        self.__dificuldade: int= dificuldade
        self.__valor1:int=self._gerar_valor
        self.__valor2:int=self._gerar_valor
        self.operacao:int=randint(1,3)#1=somar,2=diminuir,3=multiplicar
        self.__resultado:int=self._gerar_resultado


    @property  
    def dificuldade(self:object) ->int:
        return self.__dificuldade  
    
    @property
    def __valor1(self:object) ->int:
        return self.__valor1
    
    @property
    def __valor2(self:object) ->int:
        return self.__valor2
    
    @property
    def operacao(self:object) ->int:
        return self.__operacao
    
    @property
    def resultado(self:object) ->int:
        return self.__resultado
    
    def __str(self: object) -> str:
        op:str=''
        if self.operacao==1:
            op='Somar'
        elif self.operacao==2:
            op='Diminuir'
        elif self.operacao ==3:
            op='Multiplicar'
        else:
            op='Operação Desconhecida' 
        return f'Valor 1:{self.valor1} \nValor2: {self.valor2} \nDificuldade:{self.dificuldade} \nOperação: {op}'   

    @property
    def _gerar_valor(self:object) -> int:
        pass

    @property
    def _gerar_resaultado(self:object) ->int:
        pass

    def checar_resultado(self:object,resposta: int) ->bool:
        pass

    def mostrar_operacao(self: object) ->None:
        pass       


