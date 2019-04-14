#Se importa la librería de random para usar choice y que el programa elija un numero entre los número que nosotros decidimos dar.
from random import choice

#Se importa JuegaAdivinaNumero para tomar métodos de la clase JuegaAdivinaNumero.
from JuegaAdivinaNumero import JuegaAdivinaNumero

#Clase JuegaAdivinaImpar la cual corresponde a a la importación JuegaAdivinaNumero, con sus respectivos atributos.
class JuegaAdivinaImpar(JuegaAdivinaNumero):
    _numeroAdivinar = 0
    _vidas = 0
    _numero = 0

    # Método AdivinarNumero.
    def AdivinarNumero(self):

        # Mensaje en el cual se da las indicaciones al usuario, o al jugador.
        print("Vamos!! Adivina un número impar entre 0 y 10")

        # Realización del ciclo para que el usuario siga jugando mientras que aún tenga vidas.
        while self._vidas != 0:

            # Indicación para que el usuario introduzca el número de su preferencia.
            self._numero = int(input("Introduce tu número :3 : "))

            # Proceso para ver si el número que ingresa el usuario o el jugador es correcto.
            if (self._numero == self._numeroAdivinar):

                # Una vez que el usuario conteste correctamente, se le envía un mensaje haciéndole saber que está bien, y ha acertado.
                print ("Vaya, felicidades, al fin adivinaste!")
                break
            else:

                # En caso de que el número sea erróneo, se le resta una vida a sus tres, y se le envía un mensaje de advertencia para que lo intente una vez más.
                self._vidas = self._vidas - 1
                print ("Oh no, intenta otra vez, ese no es el número 7n7")

                # Se realiza la operación de la diferencia de las vidas para ver qué tantas le quedan.
                super().Diferencia()

                # Cuando las vidas sean igual a 0, el programa envía un mensaje haciéndole saber al usuario o al jugador, que éstas se han terminado, y por lo tanto, el juego también.
                if(self._vidas == 0):
                    print("¿Qué crees? Perdiste, ánimo, seguro para el amor sí tienes suerte 7u7")

        # Posteriomente, se da a conocer el número que se debía adivinar.
        print ("El número impar a adivinar era:", self._numeroAdivinar)


#Apartado que sirve para poder realizar la ejecución de JuegaAdivinaImpar.
Juego = JuegaAdivinaImpar((choice((1, 3, 5, 7, 9))),3)

#Identificación al tercer juego.
Juego.AdivinarNumero()