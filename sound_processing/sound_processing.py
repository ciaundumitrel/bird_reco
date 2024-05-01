import numpy as np
import librosa
import os

from pydub.silence import split_on_silence
from scipy.io import wavfile
import noisereduce as nr
from pydub import AudioSegment


def reduce_noise_(sounds_path, sound_name):
    sound_path = sounds_path + '\\' + sound_name
    rate, data = wavfile.read(sound_path)
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    path = os.path.join('..', 'sounds')
    reduced_file_name = fr"{path}\{sound_name.split('.')[0]}_reduced.wav"
    wavfile.write(reduced_file_name, rate, reduced_noise)
    return reduced_file_name


def split(filepath):
    sound = AudioSegment.from_file(filepath)
    chunks = split_on_silence(
        sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS - 16,
        keep_silence = 250, # optional
    )

if __name__ == "__main__":
    file_path = os.path.join('..', 'sounds')
    sound_name = '724642.wav'

    reduce_noise_(file_path, sound_name)

