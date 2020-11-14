#%%
import numpy as np
import wave
import matplotlib.pyplot as plt

import os
import subprocess
import logging
import traceback

#%%
outputdir = os.path.abspath("wavefiles")
for root, dirs, files in os.walk('.'):
    for f in files:
        path = os.path.join(root, f)
        base, ext = os.path.splitext(f)
        outputpath = os.path.join(outputdir, base + ".wav")
        if ext == '.m4a':
            print(f'converting {path} to {outputpath}')
            status, output = subprocess.getstatusoutput(f'ffmpeg -i {path} {outputpath}')
            if status:
                logging.error (output)

#%%
def read_wave(file_name):
    wavefile = wave.open(file_name, "r")
    framerate = wavefile.getframerate()
    data = wavefile.readframes(wavefile.getnframes())
    x = np.frombuffer(data, dtype="int16")
    return x, framerate

#%%
v, fs = read_wave("wavefiles/input.wav")
print(v.shape)

r = np.arange(200)
plt.plot(v[r])
plt.ylabel('Amplitude')
plt.show()
