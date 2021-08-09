import pygame, sys, os, datetime, time
from pygame.constants import K_KP_ENTER, K_SPACE
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from io import BytesIO
import tkinter as tk
from threading import Thread

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

global fala
fala = ""




class Relogio:
    def mostrarHoraAtual():
        atual = datetime.datetime.now()
        texto_hora = fonte_hora.render(str(atual.strftime('%H:%M:%S')), True, WHITE)
        posicao_hora = texto_hora.get_rect(center = (640, 360))
        tela.blit(texto_hora, posicao_hora)
        texto_auxiliar = fonte_texto.render("HR                 MIN               SEG", True, WHITE)
        posicao_tAux = texto_auxiliar.get_rect(center = (640, 200))
        tela.blit(texto_auxiliar, posicao_tAux)

class Acessibilidade:
    def ouvir_microfone():
        global fala
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            audio = microfone.listen(source)
        try:
            fala = microfone.recognize_google(audio,language='pt-BR')
        except:
            playsound('erro.mp3')

    def audio_menu():
        pygame.mixer.music.load("menu.mp3")
        pygame.mixer.music.play()

    def audio_guide():
        pygame.mixer.music.load("guide.mp3")
        pygame.mixer.music.play()

    def audio_hora_atual():
        now = datetime.datetime.now()
        tts = gTTS(str(now.hour) + " horas e " + str(now.minute) + " minutos.", lang='pt', tld='com.br')
        tts.save('atual.mp3')
        pygame.mixer.music.load("atual.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.load("atual_copia.mp3")
        os.remove('atual.mp3')           
        
    def audio_erro():
        pygame.mixer.music.load("erro.mp3")
        pygame.mixer.music.play()





pygame.mixer.init()

pygame.init()

largura_tela = 1280
altura_tela = 720

tela = pygame.display.set_mode((largura_tela, altura_tela))
tempo = pygame.time.Clock()
fonte_hora = pygame.font.SysFont('Arial', 192, bold = True)
fonte_texto = pygame.font.SysFont('Arial', 48, bold = False)

Acessibilidade.audio_guide()

while True:
    tela.fill(BLACK)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (evento.type == pygame.KEYDOWN and evento.key == K_SPACE):                
            Acessibilidade.audio_hora_atual()

        if evento.type == pygame.KEYDOWN and evento.key == K_KP_ENTER:
            Acessibilidade.audio_menu()
            Acessibilidade.ouvir_microfone()    
            if fala == "hora":
                Acessibilidade.audio_hora_atual()
                fala = ""
    
    Relogio.mostrarHoraAtual()
    pygame.display.update()
    tempo.tick(1)



