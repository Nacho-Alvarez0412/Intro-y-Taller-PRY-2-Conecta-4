###############################################################################################################################################################################
#   								    													      #
#		      																         	   	      #
#                                                                                TAREA PROGRAMADA II								              #
#										        CONNECT 4	                    	                                              #
#												  																			      #
#																					        																		      	  #
##############################################################################################################################################################################

# ======================================   Librerias   ======================================

import sys
import random
import pygame
import time


# ==========================================================================================#
# ============================   ALGORITMOS PARA ARCHIVOS   =================================
# ==========================================================================================#

# Guardar 1 archivo:

# E: el path del archivo, un string con formato de lista
# S: ninguna
# D: graba y guarda un archivo

def guardar(archivo, strLista):
    fo = open(archivo, 'w')
    # abre en forma de sobrescribirlo, si no existe, lo crea
    fo.write(strLista)
    fo.close()


# ============================================================================================
# leer 1 archivo:

# E: el path del archivo
# S: un string con el contenido del archivo
# D: lee un archivo

def leer(archivo):
    fo = open(archivo, 'r')  # abre pero solo en forma de lectura

    resultado = fo.read()
    fo.close()
    # retorna lo que leyo en el archivo
    return resultado


# ============================================================================================

# cargar 1 archivo:

# cargar archivo
# lee un archivo y hace las validaciones para colocarlo en la lista
# salida: retorna una lista de lo leido

def cargarArchivo(archivo):
    strResultado = leer(archivo)
    if strResultado != "":
        return eval(strResultado)
    else:
        return []


# =======================================================================================================
# ==========================================   Variables Globales   =====================================
# =======================================================================================================

# Estado de la partida
Victoria = False

# Turno de cada jugador
Turno = True

# Tablero
Tablero = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

IndiceV = [0, 1, 2, 3, 4, 5]

Indice = [0, 1, 2, 3, 4, 5, 6]

Columnas = 7
Filas = 6

# Variables del rango para llamar diversos indices de la matriz

Inicio = 0

Final = 7

InicioF = 0

FinalF = 6

Player1 = "nombre"
Player2 = "nombre"

# Lista de jugadores de formato: [[Nombre, Victorias]]

Jugadores = cargarArchivo("Jugadores.txt")

# Lista de la partida anterior de formato: [[Matriz],Player1,Player2,Turno]
PartidaGuardada = cargarArchivo("Partida.txt")


# ================================================================================================================
# =================================================   Funciones Tablero   ========================================
# ================================================================================================================

# Tablero

# E: nada
# S: 1 print
# D: Imprime la tabla


def board():
    global Tablero
    tablero = Tablero[::-1]
    cont = len(Tablero) - 1

    print(Indice)
    print()
    for row in tablero:
        print(row, " ", cont)
        cont -= 1


# --------------------------------------------------------------------------------------------------------------

# Agrandar Tablero Izquierda:

# E: nada
# S: 1 lista
# D: agranda la matriz por 7 a la izuqierda

def addIzquierda():
    global Tablero

    newTablero = []

    for fila in Tablero:
        newTablero += [[0, 0, 0, 0, 0, 0, 0] + fila]

    Tablero = newTablero


# --------------------------------------------------------------------------------------------------------------


# Agrandar Tablero Derecha:

# E: nada
# S: 1 lista
# D: agranda la matriz por 7 a la izuqierda

def addDerecha():
    global Tablero

    newTablero = []

    for fila in Tablero:
        newTablero += [fila + [0, 0, 0, 0, 0, 0, 0]]

    Tablero = newTablero


# --------------------------------------------------------------------------------------------------------------

# Agrandar Tablero hacia arriba:

# E: nada
# S: 1 lista
# D: agranda la matriz por 6 filas

def addArriba():
    global Tablero

    Tablero += [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]


# ================================================================================================================
# ======================================   Funciones para Colocar Ficha   ========================================
# ================================================================================================================

# Es valido?

# E: 1 numero
# S: 1 booleano
# D: Determina si hay alguna ficha almenos a 7 espacios de la columna elegida

def esValido(columna):
    global Tablero
    cont = 0

    if Tablero == [[0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0]]:
        return True

    for i in range(columna + 1, len(Tablero[0])):

        if Tablero[0][i] != 0:
            return True

        else:
            cont += 1

    if cont >= 7:
        return False

    else:
        cont = 0

        for i in range(0, columna):
            if Tablero[0][i] != 0:
                cont = 0
                continue

            else:
                cont += 1

        if cont >= 7:
            return False

        else:
            return True


# --------------------------------------------------------------------------------------------------------------


# Verificar Espacio

# E: 1 lista, 1 str
# S: 1 booleano
# D: Verifica si la posicion dada es valida

def verificarSlot(tablero, columna):
    global Tablero

    for fila in Tablero:
        if fila[columna - 1] == 0:
            return True
        else:
            continue
    False


# --------------------------------------------------------------------------------------------------------------


# Primer espacio vacio

# E: 1 lista, 1 str
# S: 1 str
# D: Analaiza la tabla y retorna la fila con el primer espacio disponible

def primerEspacio(tablero, columna):
    for fila in range(len(tablero)):
        if tablero[fila][columna] == 0:
            return fila


# --------------------------------------------------------------------------------------------------------------


# Colocar ficha

# E: 1 lista, 3 str
# S: 1 lista
# D: Coloca la ficha en el nuevo tablero

def colocarFicha(tablero, fila, columna, ficha):
    tablero[fila][columna] = ficha


# ================================================================================================================
# ==============================   Funciones de Victoria   ========================================================
# ================================================================================================================


# Victoria Horizontal

# E: 2 str
# S: 1 booleano
# D: Determina si existe una victoria de manera horizontal

def victoriaHorizontal(i, j):
    global Tablero

    for slot in range(1, 4):
        try:
            if Tablero[i][j + slot] != Tablero[i][j]:
                return False
        except:
            return False

    return True


# --------------------------------------------------------------------------------------------------------------


# Victoria Vertical

# E: 2 str
# S: 1 booleano
# D: Determina si existe una victoria de manera vertical

def victoriaVertical(i, j):
    global Tablero

    for slot in range(1, 4):
        try:
            if Tablero[i + slot][j] != Tablero[i][j]:
                return False
        except:
            return False

    return True


# --------------------------------------------------------------------------------------------------------------

# Victoria Diagonal Derecha

# E: 2 str
# S: 1 booleano
# D: Determina si existe una victoria de forma diagonal derecha

def victoriaDiagonalD(i, j):
    global Tablero

    for slot in range(0, 4):
        try:
            if Tablero[i - slot][j + slot] != Tablero[i][j]:
                return False
        except:
            return False
    return True


# --------------------------------------------------------------------------------------------------------------

# Victoria Diagonal Izquierda

# E: 2 str
# S: 1 booleano
# D: Determina si existe una victoria de forma diagonal izquierda

def victoriaDiagonalI(i, j):
    global Tablero

    for slot in range(1, 4):
        try:
            if Tablero[i - slot][j - slot] != Tablero[i][j]:
                return False
        except:
            return False
    return True


# --------------------------------------------------------------------------------------------------------------


# E: 2 strings
# S: 1 booleano
# D: un punto (i,j) que indica la fila y la columna analizada en ese moemnto

def hayFicha(i, j):
    global Tablero

    if Tablero[i][j] != 0:
        return True

    return False


# --------------------------------------------------------------------------------------------------------------


# E: nada
# S: 1 booleano
# D: Recorre la matriz y llama a hayFicha(i,j)

def recorreM():
    global Tablero

    for fila in range(0, len(Tablero)):
        for columna in range(0, len(Tablero[fila])):
            if hayFicha(fila, columna):
                if victoriaHorizontal(fila, columna) or victoriaVertical(fila, columna) or victoriaDiagonalD(fila,columna) or victoriaDiagonalI(fila, columna):
                    return True
    return False


# ================================================================================================================
# ===================================   Algoritmos para la maquina   =============================================
# ================================================================================================================


# Victoria Horizontal CPU

# E: 2 str
# S: 1 booleano si es falso o la posicion en el tablero del numero para la victoria faltante
# D: Determina si existe una posible victoria de manera horizontal

def posibleHorizontal(i, j):
    global Tablero

    for slot in range(3):
        try:
            if Tablero[i][j + slot] != Tablero[i][j]:
                return False
            if Tablero[i][j + 3] != 0:
                return False
        except:
            return False

    return True


# --------------------------------------------------------------------------------------------------------------


# Victoria Vertical CPU

# E: 2 str
# S: 1 booleano
# D: Determina si existe una posible victoria de manera vertical

def posibleVertical(i, j):
    global Tablero

    for slot in range(3):
        try:
            if Tablero[i + slot][j] != Tablero[i][j]:
                return False
        except:
            return False

    return True


# --------------------------------------------------------------------------------------------------------------


# Victoria Diagonal Derecha CPU

# E: 2 str
# S: 1 booleano
# D: Determina si existe una posible victoria de forma diagonal derecha

def posibleDiagonalD(i, j):
    global Tablero

    for slot in range(3):
        try:
            if Tablero[i - slot][j + slot] != Tablero[i][j]:
                return False
        except:
            return False
    return True


# --------------------------------------------------------------------------------------------------------------


# Victoria Diagonal Izquierda CPU

# E: 2 str
# S: 1 booleano
# D: Determina si existe una posible victoria de forma diagonal derecha

def posibleDiagonalI(i, j):
    global Tablero

    for slot in range(3):
        try:
            if Tablero[i - slot][j - slot] != Tablero[i][j]:
                return False
        except:
            return False
    return True


# --------------------------------------------------------------------------------------------------------------


# E: nada
# S: 1 numero
# D: Recorre la matriz y llama a hayFicha(i,j)

def recorreMCPU():
    global Tablero

    for fila in range(0, len(Tablero)):
        for columna in range(0, len(Tablero[fila])):
            if hayFicha(fila, columna):
                try:
                    if posibleHorizontal(fila, columna):
                        return columna + 3
                    elif posibleVertical(fila, columna) and Tablero[fila + 3][columna] == 0:
                        return columna
                    elif posibleDiagonalD(fila, columna) and Tablero[fila + 3][columna + 3] == 0:
                        return columna + 3
                    elif posibleDiagonalI(fila, columna) and Tablero[fila - 3][columna - 3] == 0:
                        return columna - 3
                except:
                    return random.choice(range(len(Tablero)))

    return random.choice(range(len(Tablero[0])))


# ================================================================================================================
# ========================================== Algoritmos del Ranking ==============================================
# ================================================================================================================


# E: 1 string
# S: la lista Jugadores actualizada
# D: Inserta un nuevo jugador a la lista

def insertarJugador(nombre):
    global Jugadores

    if Jugadores == []:
        Jugadores += [[nombre, 0]]
        return guardar('Jugadores.txt', str(Jugadores))

    for player in Jugadores:
        if player[0] == nombre:
            return

    Jugadores += [[nombre, 0]]
    return guardar('Jugadores.txt', str(Jugadores))


# --------------------------------------------------------------------------------------------------------------


# E: 1 string
# S: la lista Jugadores actualizada
# D: Agrega una victoria a la lista de Jugadores

def addVictoria(nombre):
    for player in Jugadores:
        if player[0] == nombre:
            player[1] += 1
            return guardar('Jugadores.txt', str(Jugadores))
        continue


# ================================================================================================================
# =======================================   Interfaz Grafica   ===================================================
# ================================================================================================================


# Inicializar pygame

pygame.display.init()
pygame.mixer.init()
pygame.font.init()

# ================================================================================================================
# =======================================   Variables Globales de Ventana   ======================================
# ================================================================================================================


# --------------------   Colores   ----------------------------------------

blanco = (255, 255, 255)

negro = (0, 0, 0)

celeste = (61, 231, 242)

rojo = (247, 1, 93)

purpura = (167, 17, 208)

# ----------------------   Ventanas   ------------------------------------

# Medidas
largo = 450

ancho = 800

largoG = 800

anchoG = 800

Cuadrado = 100

# Ventana Principal
conectaCuatro = pygame.display.set_mode((ancho, largo), pygame.NOFRAME)

# Caption de la ventana
pygame.display.set_caption("Conecta 4 by Ignacio Alvarez")

# Background de la ventana
background = pygame.image.load("Background.png")

# Reloj
reloj = pygame.time.Clock()

# Fuente para texto
fontObject = pygame.font.Font("Neon.ttf", 25)

fontRanks = pygame.font.Font("Neon.ttf", 40)

# ------------------------   Titulos   ------------------------------


# Principal
tituloPrincipal = pygame.image.load("Titulo.png")

# Modo de juego
tituloModo = pygame.image.load("Modo.png")

# Solitario
tituloSolitario = pygame.image.load("Solitario.png")

# Cooperativo
tituloCooperativo = pygame.image.load("Cooperativo.png")

# Jugar
tituloEmpezar = pygame.image.load("Jugar.png")

# Ranking
tituloRanking = pygame.image.load("Ranking.png")

# Salir
tituloSalir = pygame.image.load("Salir.png")

# Back
tituloBack = pygame.image.load("Back.png")

# Player 1
tituloPlayer1 = pygame.image.load("Player 1.png")

# Player 2
tituloPlayer2 = pygame.image.load("Player 2.png")

# Name
namePlayer = pygame.image.load("name.png")

# Background Game
gameBackground = pygame.image.load("BackgroundGame.png")

# Left Arrow
LeftArrow = pygame.image.load("LeftArrow.png")

# RightArrow
RightArrow = pygame.image.load("RightArrow.png")

# ArrowUp
ArrowUp = pygame.image.load("ArrowUp.png")

# ArrowDown
ArrowDown = pygame.image.load("ArrowDown.png")

# Correr Derecha
CorrerDerecha = pygame.image.load("correrDerecha.png")

# Correr Izquierda
CorrerIzquierda = pygame.image.load("correrIzquierda.png")

# Titulo Victorias
Victorias = pygame.image.load("Victorias.png")

# Ttitulo Jugador
Jugador = pygame.image.load("Jugador.png")

# Titulo Cargar Partida
CargarPartida = pygame.image.load("Cargar Partida.png")

# Titulo Nueva Partida
NuevaPartida = pygame.image.load("Nueva Partida.png")

# Titulo Seleccion de partida
SeleccionPartida = pygame.image.load("Partidas.png")


# Boton de cargar
# Guardar = pygame.image.load("Guardar.png")


# ------------------------   Imagenes   ------------------------------

# E: 2 ints
# S: Otra funcion
# D: Llama una funcion con los puntos dados para colocar los titulos de las imagenes

# def guardar(x,y):
# conectaCuatro.blit(Guardar,(x,y))

def seleccionarPartida(x, y):
    conectaCuatro.blit(SeleccionPartida, (x, y))


def cargarPartida(x, y):
    conectaCuatro.blit(CargarPartida, (x, y))


def nuevaPartida(x, y):
    conectaCuatro.blit(NuevaPartida, (x, y))


def titulo(x, y):
    conectaCuatro.blit(tituloPrincipal, (x, y))


def jugar(x, y):
    conectaCuatro.blit(tituloEmpezar, (x, y))


def ranking(x, y):
    conectaCuatro.blit(tituloRanking, (x, y))


def salir(x, y):
    conectaCuatro.blit(tituloSalir, (x, y))


def modo(x, y):
    conectaCuatro.blit(tituloModo, (x, y))


def solitario(x, y):
    conectaCuatro.blit(tituloSolitario, (x, y))


def cooperativo(x, y):
    conectaCuatro.blit(tituloCooperativo, (x, y))


def back(x, y):
    conectaCuatro.blit(tituloBack, (x, y))


def player1(x, y):
    conectaCuatro.blit(tituloPlayer1, (x, y))


def player2(x, y):
    conectaCuatro.blit(tituloPlayer2, (x, y))


def rightArrow(x, y):
    conectaCuatro.blit(RightArrow, (x, y))


def leftArrow(x, y):
    conectaCuatro.blit(LeftArrow, (x, y))


def arrowUp(x, y):
    conectaCuatro.blit(ArrowUp, (x, y))


def arrowDown(x, y):
    conectaCuatro.blit(ArrowDown, (x, y))


def correrIzquierda(x, y):
    conectaCuatro.blit(CorrerIzquierda, (x, y))


def correrDerecha(x, y):
    conectaCuatro.blit(CorrerDerecha, (x, y))


def victoria(x, y):
    conectaCuatro.blit(Victorias, (x, y))


def jugador(x, y):
    conectaCuatro.blit(Jugador, (x, y))


# ------------------------   Botones   ------------------------------

# E: 4 numeros
# S: otras funciones que imprimen en pantalla
# D: Son funciones que indican las operaciones a realizar por los botones

def botonJugar(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            tipoDePartida()


# --------------------------------------------------------------------------------------------------------------

def botonNuevaPartida(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            game()


# --------------------------------------------------------------------------------------------------------------

def botonCargarPartida(x, y, ancho, largo):
    global PartidaGuardada
    global Tablero
    global Player1
    global Player2
    global Turno

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            if PartidaGuardada == []:
                conectaCuatro.blit(fontRanks.render("No existen partidas guardadas", True, blanco), (100, 400))
                pygame.display.update()

            else:
                if PartidaGuardada[3] == "nombre":
                    Player1 = PartidaGuardada[1]
                    Tablero = PartidaGuardada[0]
                    Turno = PartidaGuardada[2]

                    return conecta4S(Player1, Tablero, Turno)

                else:
                    Player1 = PartidaGuardada[1]
                    Player2 = PartidaGuardada[3]
                    Tablero = PartidaGuardada[0]
                    Turno = PartidaGuardada[2]
                    return conecta4M(Player1, Player2, Tablero, Turno)


# --------------------------------------------------------------------------------------------------------------


def botonRanking(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            ranks()


# --------------------------------------------------------------------------------------------------------------


def botonSalir(x, y, ancho, largo):
    from sys import exit
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            pygame.mixer.music.stop()
            pygame.display.quit()
            return exit()


# --------------------------------------------------------------------------------------------------------------


def botonBack(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            intro()


# --------------------------------------------------------------------------------------------------------------


def botonCooperativo(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            Menucooperativo()


# --------------------------------------------------------------------------------------------------------------


def botonSolitario(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            Menusolitario()


# --------------------------------------------------------------------------------------------------------------


def botonBackGame(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            game()


# --------------------------------------------------------------------------------------------------------------


def botonPlay(x, y, ancho, largo):
    global Player1
    global Player2
    global Tablero
    global Tuurno
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if Player2 == "nombre":
                conecta4S(Player1, Tablero, Turno)

            if Player1 != "nombre" and Player2 != "nombre":
                conecta4M(Player1, Player2, Tablero, Turno)


# --------------------------------------------------------------------------------------------------------------


def botonInputPlayer1(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            inputPlayer1(x, y)


# --------------------------------------------------------------------------------------------------------------


def botonInputPlayer2(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            inputPlayer2(x, y)


# --------------------------------------------------------------------------------------------------------------


def botonAddDerecha(x, y, ancho, largo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            addDerecha()


# --------------------------------------------------------------------------------------------------------------


def botonAddIzquierda(x, y, ancho, largo):
    global Indice
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:
            addIzquierda()
            newLista = []
            for i in Indice:
                newLista += [i - 7]
            Indice = newLista


# --------------------------------------------------------------------------------------------------------------


def botonCorrerIzquierda(x, y, ancho, largo):
    global Inicio
    global Final
    global Indice

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if Inicio == 0:
                return
            else:
                Inicio = Inicio - 7
                Final = Final - 7
                newLista = []
                for i in Indice:
                    newLista += [i - 7]
                Indice = newLista
                print(Indice)


# --------------------------------------------------------------------------------------------------------------


def botonCorrerDerecha(x, y, ancho, largo):
    global Inicio
    global Final
    global Tablero
    global Indice

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if Final == len(Tablero[0]):
                return
            else:
                Inicio = Inicio + 7
                Final = Final + 7
                newLista = []
                for i in Indice:
                    newLista += [i + 7]
                Indice = newLista
                print(Indice)


# --------------------------------------------------------------------------------------------------------------


def botonCorrerArriba(x, y, ancho, largo):
    global InicioF
    global FinalF
    global Tablero
    global IndiceV

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if FinalF == len(Tablero):
                return
            else:
                InicioF += 6
                FinalF += 6
                newLista = []
                for i in IndiceV:
                    newLista += [i + 6]
                IndiceV = newLista


# --------------------------------------------------------------------------------------------------------------


def botonCorrerAbajo(x, y, ancho, largo):
    global InicioF
    global FinalF
    global Tablero
    global IndiceV

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + largo > mouse[1] > y:
        if click[0] == 1:

            if InicioF == 0:
                return
            else:
                InicioF -= 6
                FinalF -= 6
                newLista = []
                for i in IndiceV:
                    newLista += [i - 6]
                IndiceV = newLista


# --------------------------------------------------------------------------------------------------------------

# E: 2 strings 1 lista 1 booleano
# S: Creacion de un txt donde guarda la partida actual
# D: Guarda un txt con la ultima partida jugada

def botonGuardar(player1, tablero, turno, player2="nombre"):
    partidaGuardada = [tablero, player1, turno, player2]
    print(partidaGuardada)
    return guardar('Partida.txt', str(partidaGuardada))


# --------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------
# ------------------------   Inputs   ------------------------------
# ------------------------------------------------------------------

# E: nada
# S: un string
# D: Detecta cual tecla del teclado es presionada y la retorna

def tecla():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer1(x, y, message=Player1):
    global Player1
    global fontObject

    pygame.draw.rect(conectaCuatro, blanco, (x, y, 230, 60))
    pygame.draw.rect(conectaCuatro, negro, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        conectaCuatro.blit(fontObject.render(message, 1, blanco), (x + 70, y + 20))

    pygame.display.flip()


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer2(x, y, message=Player2):
    global Player2
    global fontObject

    pygame.draw.rect(conectaCuatro, blanco, (x, y, 230, 60))
    pygame.draw.rect(conectaCuatro, negro, (x + 3, y + 3, 230 - 7, 60 - 7))

    if len(message) != 0:
        conectaCuatro.blit(fontObject.render(message, 1, blanco), (x + 70, y + 20))

    pygame.display.flip()


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un tuple
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroVictoria(x, y, message, color):
    global fontObject

    if len(message) != 0:
        conectaCuatro.blit(fontRanks.render(message, 1, color), (x, y + 20))

    pygame.display.flip()


# --------------------------------------------------------------------------------------------------------------
# ------------------------------------   Algoritmos interfaz de Ranks   ----------------------------------------
# --------------------------------------------------------------------------------------------------------------


# E: 2 ints y 1 str
# S: prints en pantalla
# D: ordena los usuarios

def ordenPlayer(lista):
    res = []

    while lista != []:
        maximo = ["", 0]
        for player in lista:
            if player[1] >= maximo[1]:
                maximo = player
            else:
                continue
        res += [maximo]
        lista.remove(maximo)

    return res


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints y un string
# S: imprime un rectangulo en la pantalla
# D: Imprime un rectangulo negro donde se pueda escribir el numero del jugador

def cuadroPlayer(x, y, message):
    global fontRanks

    conectaCuatro.blit(fontRanks.render(message, True, blanco), (x, y))

    pygame.display.flip()


# --------------------------------------------------------------------------------------------------------------

# E: nada
# S: prints en pantalla
# D: ordena los usuarios

def printRanksP():
    global Jugadores
    contX = 40
    contY = 200

    for player in Jugadores:
        cuadroPlayer(contX, contY, player[0])

        contY += 50
    return


# --------------------------------------------------------------------------------------------------------------
# E: nada
# S: prints en pantalla
# D: ordena los usuarios

def printRanksV():
    global Jugadores
    contX = 630
    contY = 200

    for player in Jugadores:
        num = str(player[1])
        cuadroPlayer(contX, contY, num)

        contY += 50
    return


# --------------------------------------------------------------------------------------------------------------

# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer1(x, y):
    global Player1

    currentString = []
    string = ""
    cuadroPlayer1(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer1(x, y, string.join(currentString))
    Player1 = string.join(currentString)

    return Player1


# --------------------------------------------------------------------------------------------------------------


# E: 2 ints
# S: 1 string
# D: Crea una caja en pantalla para que el usuario digite su nombre

def inputPlayer2(x, y):
    global Player2

    currentString = []
    string = ""
    cuadroPlayer1(x, y, string.join(currentString))

    while 1:
        inkey = tecla()
        if inkey == pygame.K_BACKSPACE:
            currentString = currentString[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            currentString.append("_")
        elif inkey <= 127:
            currentString.append(chr(inkey))

        cuadroPlayer1(x, y, string.join(currentString))
    Player2 = string.join(currentString)

    return Player2


# ------------------------   Loop Intro Juego   ------------------------------

# E: nada
# S: una ventana de pygame
# D: Es el loop del menu principal del juego

def intro():
    global Jugadores

    Jugadores = ordenPlayer(Jugadores)

    # Musica de la ventana
    musicaIntro = pygame.mixer.music.load("Intro.mp3")

    # Dada el tamano de la ventana
    conectaCuatro = pygame.display.set_mode((800, 450), pygame.NOFRAME)
    pygame.display.update()

    # Pone la musica
    pygame.mixer.music.play(loops=-1, start=46.0)

    intro = True

    while intro:
        # Pone la imagen background como fondo
        conectaCuatro.blit(background, (0, 0))

        # Pone titulo
        titulo(100, 50)
        # Pone boton
        jugar(300, 180)
        # Pone boton
        ranking(280, 280)
        # Pone boton
        salir(20, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()

        # Boton de jugar (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(300,180,200,80))
        botonJugar(300, 190, 200, 80)

        # Boton de salir (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,180,80)))
        botonSalir(20, 380, 180, 80)

        # Boton de ranking (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(280,280,235,70)))
        botonRanking(280, 280, 235, 70)

        pygame.display.update()
        reloj.tick(5)


# -------------------------------   Interfaz de Ranks   -----------------------------------------

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame

def ranks():
    intro = True

    while intro:
        # Pone la imagen background como fondo
        conectaCuatro.blit(background, (0, 0))

        # Pone titulo
        ranking(280, 50)

        # Pone titulo
        jugador(25, 125)

        # Pone titulo
        victoria(480, 125)

        # Pone titulo
        back(700, 380)

        printRanksP()

        printRanksV()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()

        # Boton Back (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,170,70)))
        botonBack(700, 380, 170, 70)

        pygame.display.update()
        reloj.tick(5)


# -------------------------------   Interfaz del juego   -----------------------------------------

# E: 1 numero
# S: 1 numero
# D: Convierte la fila en un formato aceptable para paintTablero()

def filaOK(fila):
    while fila not in range(0, 6):
        fila -= 6
    return fila


# -------------------------------------------------------------------------------------------------

# E: 1 numero
# S: 1 numero
# D: Convierte la fila en un formato aceptable para paintTablero()

def columnaOK(columna):
    while columna not in range(0, 7):
        columna -= 7
    return columna


# -------------------------------------------------------------------------------------------------

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame con el tablero

def paintTablero():
    global Tablero
    global Columnas
    global Filas
    global Inicio
    global Final
    global Indice
    global IndiceV

    for columna in range(Columnas):
        conectaCuatro.blit(fontObject.render(str(Indice[columna]), True, blanco),
                           (columna * Cuadrado + Cuadrado - 10, 180))
        for fila in range(Filas):
            conectaCuatro.blit(fontObject.render(str(IndiceV[-(fila + 1)]), True, blanco), (35, fila * Cuadrado + 230))
            pygame.draw.circle(conectaCuatro, celeste, (
            50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                               int(Cuadrado / 2 - 2))
            pygame.draw.circle(conectaCuatro, negro, (
            50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                               int(Cuadrado / 2 - 5))

    for columna in range(Inicio, Final):
        for fila in range(InicioF, FinalF):
            if Tablero[fila][columna] == 1:
                if columna in range(0, 7) and fila in range(0, 6):
                    pygame.draw.circle(conectaCuatro, rojo, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 10))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 15))
                    pygame.draw.circle(conectaCuatro, rojo, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 30))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 32))
                else:
                    columnaO = columnaOK(columna)
                    filaO = filaOK(fila)

                    pygame.draw.circle(conectaCuatro, rojo, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 10))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 15))
                    pygame.draw.circle(conectaCuatro, rojo, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 30))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 32))

            if Tablero[fila][columna] == 2:
                if columna in range(0, 7) and fila in range(0, 6) and fila in range(0, 6):
                    pygame.draw.circle(conectaCuatro, purpura, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 10))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 15))
                    pygame.draw.circle(conectaCuatro, purpura, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 30))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columna * Cuadrado + Cuadrado / 2), anchoG - int(fila * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 32))
                else:
                    filaO = filaOK(fila)
                    columnaO = columnaOK(columna)

                    pygame.draw.circle(conectaCuatro, purpura, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 10))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 15))
                    pygame.draw.circle(conectaCuatro, purpura, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 30))
                    pygame.draw.circle(conectaCuatro, negro, (
                    50 + int(columnaO * Cuadrado + Cuadrado / 2), anchoG - int(filaO * Cuadrado + Cuadrado / 2)),
                                       int(Cuadrado / 2 - 32))


# ------------------------   Loop Menu de seleccion de modo   ------------------------------

# E: nada
# S: una ventana de pygame
# D: Es el loop del menu de modo del juego


def game():
    pygame.display.update()

    intro = True

    # Establece el tamaño correcto de la ventana
    conectaCuatro = pygame.display.set_mode((ancho, largo), pygame.NOFRAME)

    while intro:
        conectaCuatro.blit(background, (0, 0))

        # Pone titulo
        modo(100, 50)

        # Pone titulo
        solitario(250, 200)

        # Pone titulo
        cooperativo(210, 280)

        # Pone titulo
        back(700, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Boton Solitario (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(250,200,310,60)))
            botonSolitario(250, 200, 310, 60)

            # Boton Cooperativo (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(210,280,370,60)))
            botonCooperativo(210, 280, 370, 60)

            # Boton Back (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,170,70)))
            botonBack(700, 380, 170, 70)

        pygame.display.update()
        reloj.tick(5)


# -------------------------------   Loop de eleccion de tipo de partida   -----------------------------------------------


# E: nada
# S: una ventana de pygame
# D: Es el loop del menu de modo del juego


def tipoDePartida():
    pygame.display.update()

    intro = True

    while intro:
        conectaCuatro.blit(background, (0, 0))

        # Pone titulo
        nuevaPartida(180, 180)

        # Pone titulo
        cargarPartida(160, 310)

        # Pone titulo
        seleccionarPartida(250, 10)

        # Pone titulo
        back(700, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Boton Solitario (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(180,180,450,60))0)
            botonNuevaPartida(180, 180, 450, 60)

            # Boton Cooperativo (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(160,310,500,60)))
            botonCargarPartida(160, 310, 500, 60)

            # Boton Back (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,170,70)))
            botonBack(700, 380, 170, 70)

        pygame.display.update()
        reloj.tick(5)


# ------------------------   Loop Menu de nombre de jugador Solitario  ------------------------------

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def Menusolitario():
    pygame.display.update()

    intro = True

    while intro:
        conectaCuatro.blit(background, (0, 0))

        # print(Player1)

        # Pone titulo
        solitario(250, 50)

        # Pone titulo
        player1(50, 150)

        # Pone boton
        jugar(300, 350)

        # Pone titulo
        back(700, 380)

        # Pone titulo
        cuadroPlayer1(60, 220)

        # Ficha Player1
        pygame.draw.circle(conectaCuatro, rojo, (170, 350), int(Cuadrado / 2 - 10))
        pygame.draw.circle(conectaCuatro, negro, (170, 350), int(Cuadrado / 2 - 15))
        pygame.draw.circle(conectaCuatro, rojo, (170, 350), int(Cuadrado / 2 - 30))
        pygame.draw.circle(conectaCuatro, negro, (170, 350), int(Cuadrado / 2 - 32))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Boton input Player 1 (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(60,220,230,60)))
            botonInputPlayer1(60, 220, 230, 60)

            # Boton Back (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,170,70)))
            botonBackGame(700, 380, 170, 70)

            # Boton de jugar (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(300,180,200,80))
            botonPlay(300, 350, 200, 80)

        pygame.display.update()
        reloj.tick(5)


# ------------------------   Loop Menu de nombre de jugador Coop  ------------------------------

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame


def Menucooperativo():
    pygame.display.update()

    intro = True

    while intro:
        conectaCuatro.blit(background, (0, 0))

        # Pone titulo
        cooperativo(210, 50)

        # Pone titulo
        player1(25, 150)

        # Pone titulo
        player2(450, 150)

        # Pone titulo
        back(700, 380)

        # Pone boton
        jugar(300, 350)

        # Pone titulo
        cuadroPlayer1(60, 220)

        # Pone titulo
        cuadroPlayer2(500, 220)

        # Ficha Player1
        pygame.draw.circle(conectaCuatro, rojo, (170, 350), int(Cuadrado / 2 - 10))
        pygame.draw.circle(conectaCuatro, negro, (170, 350), int(Cuadrado / 2 - 15))
        pygame.draw.circle(conectaCuatro, rojo, (170, 350), int(Cuadrado / 2 - 30))
        pygame.draw.circle(conectaCuatro, negro, (170, 350), int(Cuadrado / 2 - 32))

        # Ficha Player 2
        pygame.draw.circle(conectaCuatro, purpura, (630, 350), int(Cuadrado / 2 - 10))
        pygame.draw.circle(conectaCuatro, negro, (630, 350), int(Cuadrado / 2 - 15))
        pygame.draw.circle(conectaCuatro, purpura, (630, 350), int(Cuadrado / 2 - 30))
        pygame.draw.circle(conectaCuatro, negro, (630, 350), int(Cuadrado / 2 - 32))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Boton nombre (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(220,50,82,232))
            botonInputPlayer1(60, 220, 230, 60)

            # Boton nombre (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(65,230,170,70))
            botonInputPlayer2(500, 220, 230, 60)

            # Boton Back (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(20,380,170,70)))
            botonBackGame(700, 380, 170, 70)

            # Boton de jugar (Rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(300,180,200,80))
            botonPlay(300, 350, 200, 80)

        pygame.display.update()
        reloj.tick(5)


# ------------------------   Loop Juego Multijugador  ------------------------------------------

# E: 2 strings
# S: 1 string
# D: Es el juego de conecta 4 para 2 personas

def conecta4M(player1, player2, tablero, turno):
    global Player1
    global Player2
    global Tablero
    global Victoria
    global Turno
    global Inicio
    global Final
    global PartidaGuardada
    global Indice
    global IndiceV
    global FinalF
    global InicioF

    insertarJugador(player1)
    insertarJugador(player2)

    # Musica del juego
    pygame.mixer.music.load("inGame.mp3")

    # Actualizan la ventana a la ventana del juego
    conectaCuatro = pygame.display.set_mode((largoG, anchoG))
    conectaCuatro.blit(gameBackground, (0, 0))

    pygame.mixer.music.play(loops=-1, start=19.0)
    paintTablero()

    pygame.display.update()

    while not Victoria:

        # Pone flecha:
        leftArrow(0, 470)

        # Pone flecha:
        rightArrow(740, 470)

        # Pone flecha
        arrowUp(680, 0)

        # Pone flecha
        arrowDown(730, 0)

        # Pone flecha
        correrIzquierda(0, 0)

        # Pone flecha
        correrDerecha(60, 0)

        # Pone Titulo
        # guardar(130,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()

            # Boton Add Derecha (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(740,470,60,60)))
            botonAddDerecha(740, 470, 60, 60)

            # Boton Add Izquierda (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(0,470,50,50)))
            botonAddIzquierda(0, 470, 50, 50)

            # Boton Correr Derecha (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(70,0,60,60)))
            botonCorrerDerecha(70, 0, 60, 60)

            # Boton Correr Izquierda (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(0,0,60,60)))
            botonCorrerIzquierda(0, 0, 60, 60)

            # Boton Correr Arriba (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(680,0,60,60)))
            botonCorrerArriba(730, 0, 60, 60)

            # Boton Correr Abajo (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(680,0,60,60)))
            botonCorrerAbajo(680, 0, 60, 60)

            paintTablero()

            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    botonGuardar(Player1, Tablero, Turno)
                if event.key == 101:
                    Victoria = not Victoria
                    Turno = True
                    # Regresa el tablero a original
                    Tablero = [[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0]]
                    Indice = [0, 1, 2, 3, 4, 5, 6]
                    IndiceV = [0, 1, 2, 3, 4, 5]
                    Inicio = 0
                    Final = 7
                    InicioF = 0
                    FinalF = 6
                    intro()

            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    botonGuardar(Player1, Tablero, Turno, Player2)
                if event.key == 101:
                    Victoria = True
                    Player1 = "nombre"
                    Player2 = "nombre"

            if Turno:
                conectaCuatro.blit(fontRanks.render('Turno de: ' + str(Player1), True, rojo),
                                   (120, int(Cuadrado / 2) + 80))
                pygame.draw.circle(conectaCuatro, rojo, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 10))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 15))
                pygame.draw.circle(conectaCuatro, rojo, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 30))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 32))

            else:
                conectaCuatro.blit(fontRanks.render('Turno de: ' + str(Player2), True, purpura),
                                   (120, int(Cuadrado / 2) + 80))
                pygame.draw.circle(conectaCuatro, purpura, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 10))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 15))
                pygame.draw.circle(conectaCuatro, purpura, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 30))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 32))

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                conectaCuatro.blit(gameBackground, (0, 0))

                # Jugador 1

                if Turno:
                    posX = event.pos[0]
                    posY = event.pos[1]

                    if 50 < posX < 750 and 100 < posY:
                        columna = ((50 + posX) // Cuadrado) - 1

                        while columna not in range(Inicio, Final + 1):
                            columna += 7

                        if verificarSlot(Tablero, columna):
                            try:
                                fila = primerEspacio(Tablero, columna)
                                if esValido(columna):
                                    colocarFicha(Tablero, fila, columna, 1)
                                else:
                                    conectaCuatro.blit(
                                        fontObject.render("La posicion ingresada no es valida.", True, blanco),
                                        (200, int(Cuadrado / 2)))
                                    Turno = False

                            except:
                                addArriba()
                                fila = primerEspacio(Tablero, columna)
                                colocarFicha(Tablero, fila, columna, 1)

                        if recorreM():
                            addVictoria(Player1)
                            cuadroVictoria(250, 0, player1 + " ha ganado!", rojo)
                            Victoria = not Victoria
                            Player1 = 'nombre'
                            Player2 = 'nombre'
                            pygame.display.update()

                        Turno = not Turno

                # Jugador 2

                else:
                    posX = event.pos[0]
                    posY = event.pos[1]

                    if 50 < posX < 750 and 100 < posY:
                        columna = ((50 + posX) // Cuadrado) - 1

                        if posX > 200 and columna >= 6:
                            columna = 6

                        while columna not in range(Inicio, Final + 1):
                            columna += 7

                        if verificarSlot(Tablero, columna):
                            try:
                                fila = primerEspacio(Tablero, columna)
                                if esValido(columna):
                                    colocarFicha(Tablero, fila, columna, 2)
                                else:
                                    conectaCuatro.blit(
                                        fontObject.render("La posicion ingresada no es valida.", True, blanco),
                                        (200, int(Cuadrado / 2)))
                                    Turno = True
                            except:
                                addArriba()
                                fila = primerEspacio(Tablero, columna)
                                colocarFicha(Tablero, fila, columna, 2)

                        if recorreM():
                            addVictoria(Player2)
                            cuadroVictoria(250, 0, player2 + " ha ganado!", purpura)
                            Victoria = not Victoria
                            Player1 = 'nombre'
                            Player2 = 'nombre'
                            pygame.display.update()

                        Turno = not Turno

        paintTablero()

        pygame.display.update()
        reloj.tick(5)

    pygame.time.wait(3000)

    Victoria = not Victoria
    Turno = True

    # Regresa el tablero a original
    Tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]
    Indice = [0, 1, 2, 3, 4, 5, 6]
    IndiceV = [0, 1, 2, 3, 4, 5]

    partidaGuardada = []
    guardar('Partida.txt', str(partidaGuardada))
    Inicio = 0
    Final = 7
    InicioF = 0
    FinalF = 6

    intro()


# ------------------------   Loop Juego Solitario  ------------------------------------------

# E: nada
# S: una ventana de pygame
# D: Crea una ventana de pygame

def conecta4S(player1, tablero, turno):
    global Player1
    global Player2
    global Tablero
    global Victoria
    global Turno
    global PartidaGuardada
    global Indice
    global IndiceV
    global Inicio
    global InicioF
    global Final
    global FinalF

    # Musica del juego
    pygame.mixer.music.load("inGame.mp3")

    # Actualizan la ventana a la ventana del juego
    conectaCuatro = pygame.display.set_mode((largoG, anchoG))
    conectaCuatro.blit(gameBackground, (0, 0))
    pygame.display.update()

    pygame.mixer.music.play(loops=-1, start=19.0)

    while not Victoria:

        # Pone flecha:
        leftArrow(0, 470)

        # Pone flecha:
        rightArrow(740, 470)

        # Pone flecha
        arrowUp(680, 0)

        # Pone flecha
        arrowDown(730, 0)

        # Pone flecha
        correrIzquierda(0, 0)

        # Pone flecha
        correrDerecha(60, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit()

            # Boton Add Derecha (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(740,470,60,60)))
            botonAddDerecha(740, 470, 60, 60)

            # Boton Add Izquierda (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(0,470,50,50)))
            botonAddIzquierda(0, 470, 50, 50)

            # Boton Correr Derecha (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(70,0,60,60)))
            botonCorrerDerecha(70, 0, 60, 60)

            # Boton Correr Izquierda (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(0,0,60,60)))
            botonCorrerIzquierda(0, 0, 60, 60)

            # Boton Correr Arriba (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(680,0,60,60)))
            botonCorrerArriba(730, 0, 60, 60)

            # Boton Correr Abajo (rectangulo invisible = pygame.draw.rect(conectaCuatro,blanco,(680,0,60,60)))
            botonCorrerAbajo(680, 0, 60, 60)

            paintTablero()

            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    botonGuardar(Player1, Tablero, Turno)
                if event.key == 101:
                    Victoria = not Victoria
                    Turno = True
                    # Regresa el tablero a original
                    Tablero = [[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0]]
                    Indice = [0, 1, 2, 3, 4, 5, 6]
                    IndiceV = [0, 1, 2, 3, 4, 5]
                    Inicio = 0
                    Final = 7
                    InicioF = 0
                    FinalF = 6
                    intro()

            if event.type == pygame.KEYDOWN:
                if event.key == 115:
                    botonGuardar(Player1, Tablero, Turno, "nombre")
                if event.key == 101:
                    Victoria = True
                    Player1 = "nombre"
                    Player2 = "nombre"

            if Turno:
                conectaCuatro.blit(fontRanks.render('Turno de: ' + str(Player1), True, rojo),
                                   (120, int(Cuadrado / 2) + 80))
                pygame.draw.circle(conectaCuatro, rojo, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 10))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 15))
                pygame.draw.circle(conectaCuatro, rojo, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 30))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 32))

            else:
                conectaCuatro.blit(fontRanks.render('Turno de: La computadora ', True, purpura),
                                   (120, int(Cuadrado / 2) + 80))
                pygame.draw.circle(conectaCuatro, purpura, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 10))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 15))
                pygame.draw.circle(conectaCuatro, purpura, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 30))
                pygame.draw.circle(conectaCuatro, negro, (60, int(Cuadrado / 2) + 100), int(Cuadrado / 2 - 32))

            if event.type == pygame.MOUSEBUTTONDOWN:
                conectaCuatro.blit(gameBackground, (0, 0))

                # Jugador 1

                if Turno:
                    posX = event.pos[0]
                    posY = event.pos[1]

                    if 50 < posX < 750 and 100 < posY:
                        columna = ((50 + posX) // Cuadrado) - 1

                        if posX > 200 and columna >= 6:
                            columna = 6

                        while columna not in range(Inicio, Final + 1):
                            columna += 7

                        if verificarSlot(Tablero, columna):
                            try:
                                fila = primerEspacio(Tablero, columna)
                                colocarFicha(Tablero, fila, columna, 1)
                            except:
                                addArriba()
                                fila = primerEspacio(Tablero, columna)
                                colocarFicha(Tablero, fila, columna, 1)

                        if recorreM():
                            cuadroVictoria(250, 0, str(player1) + " ha ganado!", rojo)
                            Victoria = not Victoria
                            Player1 = "nombre"
                            pygame.display.update()

                # Computadora

                else:

                    columna = recorreMCPU()

                    if verificarSlot(Tablero, columna):
                        fila = primerEspacio(Tablero, columna)
                        try:
                            colocarFicha(Tablero, fila, columna, 2)
                        except:
                            addArriba()
                            columna = random.choice(range(len(Tablero)))
                            colocarFicha(Tablero, fila, )

                    if recorreM():
                        cuadroVictoria(180, 0, "La computadora ha ganado!", purpura)
                        Player1 = "nombre"
                        Victoria = not Victoria
                        pygame.display.update()

                Turno = not Turno

        paintTablero()

        pygame.display.update()

    pygame.time.wait(3000)

    Victoria = not Victoria
    Turno = True
    # Regresa el tablero a original
    Tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]
    partidaGuardada = []
    guardar('Partida.txt', str(partidaGuardada))
    Indice = [0, 1, 2, 3, 4, 5, 6]
    IndiceV = [0, 1, 2, 3, 4, 5]
    Inicio = 0
    Final = 7
    InicioF = 0
    FinalF = 6

    intro()


# ================================================================================================================


intro()  # Llama al menu principal
