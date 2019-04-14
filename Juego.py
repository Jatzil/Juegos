#Se crea la clase padre, donde ésta misma tomará posteriormente los métodos para las clases hijas .
class Juego:
    __vidas = 0

    #Método constructor, el cual contiene la palabra init, seguida de sus respectivos atributos, con sus reglas para crear el mismo método.
    def __init__(self, vidas):
        self.__vidas = vidas

    #Método llamado Juega, con su respectivo retorno.
    def Juega(self):
        return 0

    #Método que se utiliza para restarle vidas al usuario, en cada una de las oportunidades de las que tiene y se equivoca.
    def QuitarVida(self):
        self.__vidas = self.__vidas - 1
        if (self.__vidas>0):
            return 0
        else:
            return False
#Clase JuegaAdivinaNumero con sus respectivos atributos.
class JuegaAdivinaNumero(Juego):
    __numeroAdivinar = 0
    __intentos = 0

    #Método que se utiliza para actualizar el método del jugador.
    def ActualizarRecord(self):
        self.__intentos = self.__intentos+1

    #Segundo método constructor, junto a su estructura.
    def __init__(self, vidas, numeroAdivinar):
        super().__init__(vidas)
        self.__numeroAdivinar = numeroAdivinar

    #Método Juega junto al bucle while donde se realizan una serie de condiciones poara evaluar las vidas, el récord, y los intentos del jugador (usuario).
    def Juega(self):
        while True:
            numero = int(input("Escribe el numero a adivinar"))
            if (numero==self.__numeroAdivinar):
                print("Acertaste!")
                self.ActualizarRecord()
                print("Intentos: ", self.__intentos)
                break
            else:
                if self.QuitarVida():
                    if numero > self.__numeroAdivinar:

                        #Mensaje que se manda al usuario para hacerle saber que el número que debe adivinar, es menor que el que ingresó.
                        print("Intentalo de nuevo. El numero a adivinar es menor")

                        # Mensaje que se manda al usuario para hacerle saber que el número que debe adivinar, es mayor que el que ingresó.
                    else:
                        print("Intentalo de nuevo. El numero a adivinar es mayor")
                else:
                    self.ActualizarRecord()
                    print("Intentos: ", self.__intentos)

                    break

#Pruebas unitarias que ayudan a la ejecución del programa.
if __name__=='__main__':
	import doctest
	doctest.testmod()