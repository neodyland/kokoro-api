from scipy.io.wavfile import write
from io import BytesIO
import numpy as np

rate = 24000


def pcm_to_wav(audio: np.ndarray):
    with BytesIO() as wav_io:
        write(wav_io, rate, audio)
        wav_io.seek(0)
        wav = wav_io.read()
    return wav
