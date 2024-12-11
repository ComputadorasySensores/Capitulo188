import time, board, digitalio
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut

audio = AudioOut(board.GP14)
ruta="sonidos/"
nombre_archivo="Campanas.wav"

with open(ruta + nombre_archivo, "rb") as archivo_wav:
    wav = WaveFile(archivo_wav)
    audio.play(wav)
    while audio.playing:
        pass

