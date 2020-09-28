import librosa
import matplotlib.pyplot as plt
import scipy
import numpy as np


filepath='data'
filename='untitled.mp3'

samples, sampling_rate = librosa.load(filepath+'/'+filename)
t=np.linspace(0,(len(samples)/sampling_rate),len(samples))
A=samples

fig=plt.figure()
ax_1=fig.add_subplot(2,1,1)

line_1_1=ax_1.plot(t,A,label='Waveform')
ax_1.set_xlabel('Elapsed time - [s]')
ax_1.set_ylabel('Amplitude - [-]')
ax_1.legend()
ax_1.grid()

n=len(A)
T=1/sampling_rate
yf = np.abs(scipy.fft.rfft(A))
yf=librosa.amplitude_to_db(yf,ref=np.max)
xf=np.linspace(0,sampling_rate/2,len(yf))

ax_2=fig.add_subplot(2,1,2)
line_2_1=ax_2.plot(xf,yf)
#ax_2.set_yscale('log')
#ax_2.set_xscale('log')
ax_2.set_xlabel('Frequency - [Hz]')
ax_2.set_ylabel('Magnitude - [-]')
ax_2.grid()