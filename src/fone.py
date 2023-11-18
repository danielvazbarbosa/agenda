from identificador import Identificador

class Fone:

    def __init__(self, identificador: Identificador, numero: str):
        self.identificador = identificador
        self.numero = numero

    @staticmethod
    def validarNumero(numero) -> bool:
        for i in numero:
            if i not in '0123456789()-':
                return False
        return True

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getNumero(self) -> str:
        return self.numero
