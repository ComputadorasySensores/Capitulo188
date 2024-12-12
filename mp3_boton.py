import time, board, digitalio
from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut

pin = digitalio.DigitalInOut(board.GP15)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

audio = AudioOut(board.GP14)
ruta="sonidos/"

nombre_archivo = "AudioMp3.mp3"
archivo_mp3 = open(ruta + nombre_archivo, "rb")
decoder = MP3Decoder(archivo_mp3)

def reproducir_mp3(nombre_archivo):
    decoder.file = open(ruta + nombre_archivo, "rb")
    audio.play(decoder)

while True:
    if pin.value == False:
        print("Reproduciendo ...")
        reproducir_mp3("AudioMp3.mp3")
        time.sleep(0.5)
