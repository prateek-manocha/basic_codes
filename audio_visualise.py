#Python script for visualising audio with respect to time

import librosa
import os
import matplotlib.pyplot as plt
import numpy as np
import argparse

def audio_visualise(audio):
    samples, sample_rate = librosa.load(audio, sr = 16000)
    fig = plt.figure(figsize=(12,4))
    ax = fig.add_subplot(211)
    ax.set_title('Raw wave of ' + audio)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.plot(np.linspace(0, sample_rate, num=len(samples)), samples)
    #plt.show()
    plt.savefig(os.path.splitext(audio)[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='audio to be visualised')
    args=parser.parse_args()
    audio_visualise(args.a)
