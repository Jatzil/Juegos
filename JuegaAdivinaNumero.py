#Se importa la librería de random para usar randrange, y que posterioemente, el programa elija un número al azar entre el 0 al 10.
from random import randrange

#Se importa Juego para tomar métodos de la clase Juego.
from Juego import Juego

#Clase JuegaAdivinaNumerocon sus respectivos atributos
class JuegaAdivinaNumero(Juego):
    _numeroAdivinar = int(0)
    _vidas = int(0)
    _numero = 0

    #Método que se utiliza para realizar las operaciones al comenzar el juego, en otras palabras, llevar el conteo, dependiendo la diferencia.
    def Diferencia(self):
        if self._numero > self._numeroAdivinar:
            print("El numero a adivinar es menor")
        elif self._numero < self._numeroAdivinar:
            print("El numero a adivinar es mayor")

    #Método constructor para obtener valores del número que adivinaremos y de las vidas también.
    def __init__(self, numero, vidas):
        self._numeroAdivinar = numero
        self._vidas = vidas

    #Creación del método AdivinarNumero para comenzar con el juego.
    def AdivinarNumero(self):
        print("Vamos!! Adivina un número entre 0 y 10")

        #Realización del ciclo para que el usuario siga jugando mientras que aún tenga vidas.
        while self._vidas != 0:

            #Indicación para que el usuario ingrese el número de su preferencia.
            self._numero = int(input("Introduce un número :3: "))

            #Proceso para ver si el número que ingresa el usuario o el jugador es correcto.
            if (self._numero == self._numeroAdivinar):

                #Una vez que el usuario conteste correctamente, se le envía un mensaje haciéndole saber que está bien, y ha acertado.
                print ("Vaya, felicidades, al fin adivinaste!")
                break
            else:

                #En caso de que el número sea erróneo, se le resta una vida a sus tres, y se le envía un mensaje de advertencia para que lo intente una vez más.
                self._vidas = self._vidas - 1
                print ("Oh no! Intenta otra vez, ese no es el número 7n7")

                #Se realiza la operación de la diferencia de las vidas para ver qué tantas le quedan.
                self.Diferencia()

                #Cuando las vidas sean igual a 0, el programa envía un mensaje haciéndole saber al usuario o al jugador, que éstas se han terminado, y por lo tanto, el juego también.
                if(self._vidas == 0):
                    print("¿Qué crees? Perdiste, ánimo, seguro para el amor sí tienes suerte 7u7")

        #Posteriomente, se da a conocer el número que se debía adivinar.
        print ("El número a adivinar era:" , self._numeroAdivinar)

#Apartado que sirve para poder realizar la ejecución.
Juego = JuegaAdivinaNumero(randrange(10), 3)

#Identificación al primer juego.
Juego.AdivinarNumero()