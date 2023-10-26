#REALIZADO POR LORENA BRAVO

import pygame, sys
import random
from button import Button

pygame.init()

#constantes
ANCHO = 1280
ALTO = 600
COLOR_ROJO = (255,0,0)

#jugador
jugador_size = 60

#enemigo
enemigos_size = 50

#funcion tipo de letra
def get_font(size):
    return pygame.font.Font("imagenes/font.ttf", size)

#funcion color enemigos
def color_aleatorio():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


#ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Enemigos en el espacio - MENU")
fondo = pygame.transform.scale(pygame.image.load("imagenes/fondo.png").convert(), (ANCHO, ALTO))



#funcion para detectar choque
def detectar_choque(jugador_pos, enemigo_pos):
        jx =jugador_pos[0]
        jy = jugador_pos[1]
        ex = enemigo_pos[0]
        ey = enemigo_pos[1]

        if (ex >= jx and ex < (jx+jugador_size)) or (jx >= ex and jx < (ex + enemigos_size)):
            if (ey >= jy and ey < (jy+jugador_size)) or (jy >= ey and jy < (ey + enemigos_size)):
                return True
        return False


def juego_terminado(puntos):
    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    fondo = pygame.transform.scale(pygame.image.load("imagenes/juego terminado.png").convert(), (ANCHO, ALTO))
    ventana.blit(fondo, (0, 0))
    
    #puntuacion final
    PUNTUACION_FINAL = get_font(55).render("JUEGO TERMINADO", True, "#00FA9A")
    POSICION_PUNT = PUNTUACION_FINAL.get_rect(center=(740, 260))
    ventana.blit(PUNTUACION_FINAL, POSICION_PUNT)
    PUNTUACION_FINAL = get_font(45).render("PUNTUACIóN: "+str(puntos), True, "#00FA9A")
    POSICION_PUNT = PUNTUACION_FINAL.get_rect(center=(740, 360))
    ventana.blit(PUNTUACION_FINAL, POSICION_PUNT)

    #regresar al menú
    OPTIONS_BACK = Button(image=None, pos=(740, 460), 
                        text_input="Regresar", font=get_font(35), base_color="#FFA500", hovering_color="#FF8C00")

    OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
    OPTIONS_BACK.update(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                menu()

    pygame.display.update()

#funcion nivel 1
def nivel1(color,color2):
    #puntuacion
    puntos = 0
    
    #jugador
    jugador_pos = [ANCHO/2,ALTO-jugador_size*2]

    #enemigo
    enemigo_pos1 = [random.randint(0, ANCHO-enemigos_size),0]
    enemigo_pos2 = [random.randint(0, ANCHO-enemigos_size),0]
    enemigo_pos3 = [random.randint(0, ANCHO-enemigos_size),0]
    #juego
    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        pygame.display.set_caption("Enemigos en el espacio - NIVEL 1")
        fondo = pygame.transform.scale(pygame.image.load("imagenes/nivel1.png").convert(), (ANCHO, ALTO))
        ventana.blit(fondo, (0, 0))

        PUNTUACION = get_font(20).render("Puntuacion: "+str(puntos), True, "#ADFF2F")
        POSICION_PUNT = PUNTUACION.get_rect(center=(150, ALTO-20))
        ventana.blit(PUNTUACION, POSICION_PUNT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #mover jugador
            if event.type == pygame.KEYDOWN:
                x = jugador_pos[0]
                if event.key == pygame.K_LEFT:
                    if x >= 0:
                        x -= jugador_size
                if event.key == pygame.K_RIGHT:
                    if x+jugador_size <= ANCHO:
                        x += jugador_size
            
                jugador_pos[0] = x

        #movimiento enemigos
        if enemigo_pos1[1] >= 0 and enemigo_pos1[1] < ALTO:
            enemigo_pos1[1] += 30
        else:
            enemigo_pos1[0] =  random.randint(0, ANCHO-enemigos_size)
            enemigo_pos1[1] = 0
            puntos += 1
            color = color_aleatorio()

        if enemigo_pos2[1] >= 0 and enemigo_pos2[1] < ALTO:
            enemigo_pos2[1] += 20
        else:
            enemigo_pos2[0] =  random.randint(0, ANCHO-enemigos_size)
            enemigo_pos2[1] = 0
            puntos +=1
            color2 = color_aleatorio()

        #Detectar choque
        if detectar_choque(jugador_pos,enemigo_pos1) or detectar_choque(jugador_pos,enemigo_pos2):
            game_over = True

        #Dibujar enemigo1
        pygame.draw.rect(ventana,color, (enemigo_pos1[0], enemigo_pos1[1], enemigos_size, enemigos_size))
       
        #Dibujar enemigo2
        pygame.draw.rect(ventana,color2, (enemigo_pos2[0], enemigo_pos2[1], enemigos_size, enemigos_size))
       
        #Dibujar jugador
        nave = pygame.transform.scale(pygame.image.load("imagenes/nave.png"), (jugador_size,jugador_size))
        ventana.blit(nave,(jugador_pos[0],jugador_pos[1]))
       
        clock.tick(20)
        pygame.display.update()
    
    #juego terminado
    while True:
        juego_terminado(puntos)

#funcion nivel 2
def nivel2(color,color2,color3):
    #puntuacion
    puntos = 0

    #jugador
    jugador_pos = [ANCHO/2,ALTO-jugador_size*2]

    #enemigo
    enemigo_pos1 = [random.randint(0, ANCHO-enemigos_size),0]
    enemigo_pos2 = [random.randint(0, ANCHO-enemigos_size),0]
    enemigo_pos3 = [random.randint(0, ANCHO-enemigos_size),0]

    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        pygame.display.set_caption("Enemigos en el espacio - NIVEL 2")
        fondo = pygame.transform.scale(pygame.image.load("imagenes/nivel1.png").convert(), (ANCHO, ALTO))
        ventana.blit(fondo, (0, 0))

        PUNTUACION_FINAL = get_font(20).render("Puntuacion: "+str(puntos), True, "green")
        POSICION_PUNT = PUNTUACION_FINAL.get_rect(center=(150, ALTO-20))
        ventana.blit(PUNTUACION_FINAL, POSICION_PUNT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #mover jugador
            if event.type == pygame.KEYDOWN:
                x = jugador_pos[0]
                if event.key == pygame.K_LEFT:
                    if x >= 0:
                        x -= jugador_size
                if event.key == pygame.K_RIGHT:
                    if x+jugador_size <= ANCHO:
                        x += jugador_size
            
                jugador_pos[0] = x

        #movimiento enemigos
        if enemigo_pos1[1] >= 0 and enemigo_pos1[1] < ALTO:
            enemigo_pos1[1] += 50
        else:
            enemigo_pos1[0] =  random.randint(0, ANCHO-enemigos_size)
            enemigo_pos1[1] = 0
            puntos += 1
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if enemigo_pos2[1] >= 0 and enemigo_pos2[1] < ALTO:
            enemigo_pos2[1] += 40
        else:
            enemigo_pos2[0] =  random.randint(0, ANCHO-enemigos_size)
            enemigo_pos2[1] = 0
            puntos +=1
            color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
        if enemigo_pos3[1] >= 0 and enemigo_pos3[1] < ALTO:
            enemigo_pos3[1] += 30
        else:
            enemigo_pos3[0] =  random.randint(0, ANCHO-enemigos_size)
            enemigo_pos3[1] = 0
            puntos +=1
            color3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        #Detectar choque
        if detectar_choque(jugador_pos,enemigo_pos1) or detectar_choque(jugador_pos,enemigo_pos2) or detectar_choque(jugador_pos,enemigo_pos3):
            game_over = True

        #Dibujar enemigo
        pygame.draw.rect(ventana,color, (enemigo_pos1[0], enemigo_pos1[1], enemigos_size, enemigos_size))
       
        #Dibujar enemigo2
        pygame.draw.rect(ventana,color2, (enemigo_pos2[0], enemigo_pos2[1], enemigos_size, enemigos_size))
       
        #Dibujar enemigo3
        pygame.draw.rect(ventana,color3, (enemigo_pos3[0], enemigo_pos3[1], enemigos_size, enemigos_size))

        #Dibujar jugador
        nave = pygame.transform.scale(pygame.image.load("imagenes/nave.png"), (jugador_size,jugador_size))
        ventana.blit(nave,(jugador_pos[0],jugador_pos[1]))
        
        clock.tick(20)
        pygame.display.update()
    
    while True:
       juego_terminado(puntos)
       
def menu():
 
    #enemigos
    color = color_aleatorio()
    color2 = color_aleatorio()
    color3 = color_aleatorio()

    while True:
        ventana.blit(fondo, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MENU", True, "#ADFF2F")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        BOTON_NIVEL1 = Button(image=pygame.image.load("imagenes/rectangulo.png"), pos=(640, 240), 
                            text_input="NIVEL 1", font=get_font(75), base_color="#00FFFF", hovering_color="#008B8B")
        BOTON_NIVEL2 = Button(image=pygame.image.load("imagenes/rectangulo.png"), pos=(640, 380), 
                            text_input="NIVEL 2", font=get_font(75), base_color="#00FFFF", hovering_color="#008B8B")
        BOTON_SALIR = Button(image=pygame.image.load("imagenes/rectangulo.png"), pos=(640, 520), 
                            text_input="SALIR", font=get_font(75), base_color="#00FFFF", hovering_color="#008B8B")

        ventana.blit(MENU_TEXT, MENU_RECT)

        for button in [BOTON_NIVEL1, BOTON_NIVEL2, BOTON_SALIR]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(ventana)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_NIVEL1.checkForInput(MENU_MOUSE_POS):
                    nivel1(color,color2)
                if BOTON_NIVEL2.checkForInput(MENU_MOUSE_POS):
                    nivel2(color,color2,color3)
                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu()