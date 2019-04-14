from Juego import *
from JuegaAdivinaNumero import JuegaAdivinaNumero
from JuegaAdivinaPar import JuegaAdivinaPar
from JuegaAdivinaImpar import JuegaAdivinaImpar

#Clase demasiado importante. la cual su utilidad es mandar a llamar a los tres juegos de éste programa desde lo que es el método main.
class Aplicacion():

    def main(self):

        while True:

            #Espacio que permite considerar si el jugador, o el usuario desea seguir jungando, o no.
            reiniciar = input('¿Deseas jugar?(S,N): ')
            if reiniciar == 'S':

                #Condición que permite reconocer que sólo se tiene tres vidas, y que los números disponibles están desde el 0 al 10 sólo en el juego JuegaAdivinaNumero.
                juego = JuegaAdivinaNumero(3, randrange(10))
                juego.Juega()

                # Condición que permite reconocer que sólo se tiene tres vidas, y que los números disponibles están desde el 0 al 10, pero sólo los números pares, que son los que se muestran, sólo en el juego JuegaAdivinaPar.
                juega = JuegaAdivinaPar(3, choice((2, 4, 6, 8, 10)))
                juega.Juega()

                # Condición que permite reconocer que sólo se tiene tres vidas, y que los números disponibles están desde el 0 al 10, pero sólo los números impares, que son los que se muestran, sólo en el juego JuegaAdivinaImpar.
                juega = JuegaAdivinaImpar(3, choice((1, 3, 5, 7, 9)))
                juega.Juega()
            else:
                break

        # Pruebas unitarias que ayudan a la ejecución del programa.
        if __name__ == '__main__':
            aplicacion = Aplicacion()
            aplicacion.main()