import numpy as np
import math
import scipy as sp
from scipy import signal
import pylab

x = 0
cycles = 5
emg = []
fs = 1024.0
s1 = 1000
s2 = 500

for x in range(cycles):
    burst = np.random.uniform(-1, 1, size=s1) + 0.08
    t = sp.arange((len(burst)*2)) / fs
    d = np.sin((2 * math.pi * t)/2)
    burst = burst * d[0:(len(burst))]
    quiet = np.random.uniform(-0.05, 0.05, size=s2) + 0.08
    emg = np.concatenate([emg, burst, quiet])
#emg = np.concatenate([emg, (np.random.uniform(-0.05, 0.05, size=s2) + 0.08)])
time = np.array([(i/fs) for i in range(0, len(emg), 1)])
emg_correctmean = emg - np.mean(emg)
high = 10.0/1024.0
low = 500.0/1024.0
b, a = sp.signal.butter(4, [high, low], btype='bandpass')
emg_filtered = sp.signal.filtfilt(b, a, emg_correctmean)

pylab.figure(1)
pylab.plot(time, emg_filtered)
pylab.xlabel('Time (sec)')
pylab.ylabel('EMG (a.u.)')
pylab.title('EMG')
pylab.show()


