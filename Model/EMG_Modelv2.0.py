#Yuancheng2000
import numpy as np
import math
import scipy.signal as sig
import pylab

fs = 1024.0

mean = 0
stdi = math.sqrt(238.86)
num_samples = 20000

samplesi = np.random.normal(mean, stdi, size=num_samples)
ai = [1, -1.2368, 0.0950, 0.1105, 0.0792]
#rawi = filters.arfilter(samplesi, ai)
rawi = sig.lfilter([1], ai, samplesi)

stde = math.sqrt(39.65)
samplese = np.random.normal(mean, stde, size=num_samples)
ae = [1, -0.4970, -0.1159, -0.1127, -0.0666]
rawe = sig.lfilter([1], ae, samplese)

sig = 0.5
phi = -(math.pi/6)
T0 = 4.0
Tp = np.random.uniform(0.9, 1, size=1) * T0
t = np.array([(i/fs) for i in range(0, num_samples, 1)])
x = sig + np.sin(((2*math.pi*t)/Tp) + phi)
x[x <= 0.0] = 0.0

b1 = 1
b2 = 0

step1 = b1/(1+sig)
md = np.sqrt((step1*x) + b2)
mdi = md
mde = 1 - mdi
emgi = rawi*mdi
emge = rawe*mde
emg = emgi + emge
pylab.plot(t, emg)
pylab.xlabel('Time (sec)')
pylab.ylabel('EMG (a.u.)')
pylab.title('EMG')
pylab.show()
