#%%
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# %%
def create_wave(sin_wave, sample_Hz, file_name):
    sin_wave = [int(x * 32767.0) for x in sin_wave]
    wave_bin = struct.pack("h" * len(sin_wave), *sin_wave)

    w = wave.Wave_write(file_name)
    p = (1, 2, sample_Hz, len(wave_bin), 'NONE', 'not comperssed')
    w.setparams(p)
    w.writeframes(wave_bin)
    w.close

# %%
t = np.arange(0, 1, 1/8000)
a = 0.8
f = 440
y = a * np.sin(2 * np.pi * f * t)

# %%
create_wave(y, 8000)

# %%
r = np.arange(100)
plt.plot(t[r], y[r])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# %%
fs = 8000
t = np.arange(0, 1, 1 / fs)
a = 0.3
y523 = a * np.sin(2 * np.pi * 523 * t)
y660 = a * np.sin(2 * np.pi * 660 * t)
y784 = a * np.sin(2 * np.pi * 784 * t)

yy = y523 + y660 + y784
create_wave(yy, fs, "add3wave.wav")

# %%
r = np.arange(100)
plt.plot(t[r], yy[r])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
# %%
fs = 8000
t = np.arange(0, 1, 1 / fs)
a = 0.4
y438 = a * np.sin(2 * np.pi * 438 * t)
y442 = a * np.sin(2 * np.pi * 442 * t)

yy = y438 + y442
create_wave(yy, fs, "wavefiles/add2wave.wav")

# %%
create_wave(np.hstack((y523, y660)), fs, "wavefiles/hstack.wav")

# %%
