import os
import pydub

from sound_processing.sound_processing import reduce_bird, to_wav
from utils import *


def main():

    for bird in birds:
        # to_wav(bird, os.getcwd())
        reduce_bird(bird, os.getcwd())


if __name__ == "__main__":
    main()
