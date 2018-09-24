from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

#
infile = 'mod05_GAP_data_analysis.csv'
#


matrix2=np.loadtxt(infile)
# Number of sample points

N = matrix2.shape[0]

print N

# sample spacing

t=matrix2[:,0]

T = t[1]-t[0]

print T

x=matrix2[:,0]

y=matrix2[:,4]

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T*0.0068981/1000), N/2)
				 
#print xf[60]
#print xf[600]

fig1=plt.figure()

# for Leahy normalization
Nf = sum(y) 
print Nf
spectr=(2.0/Nf) * np.abs(yf[0:N/2]) ** 2
# xxxxxxxxxx

freq=xf[0:N/2]
#spectr=2.0/N * np.abs(yf[0:N/2])

# for Leahy normalization
plt.semilogy(xf[0:N/2], (2.0/Nf) * np.abs(yf[0:N/2]) ** 2 * xf[0:N/2])
# xxxxxxxxxx

#plt.plot(xf[0:N/2], np.log10(2.0/N * np.abs(yf[0:N/2]) * xf[0:N/2]))
#plt.semilogy(xf[0:N/2], np.log10(2.0/N * np.abs(yf[0:N/2]) * xf[0:N/2]))
#plt.plot(xf[0:N/2], 2.0/N * np.abs(yf[0:N/2]))
#plt.plot(xf[0:N/2], 2.0/N * np.abs(yf[0:N/2]) * xf[0:N/2])
#plt.semilogy(xf[0:N/2], 2.0/N * np.abs(yf[0:N/2]) * xf[0:N/2])
#plt.plot(xf[0:N/2], 1.0/4.0 * np.abs(yf[0:N/2]))
plt.xlim([-50,xf[706]])
plt.ylim([0.0005,100000.0])
plt.xticks([i*70 for i in range(20)])
#plt.yscale('log')

plt.xlabel(r"$\nu$ [Hz]")
plt.grid()
plt.show()

fig1.savefig('fig_power_mod05_GAP_M_1_4-leahy.png')


fig2=plt.figure()
plt.plot(x*0.0068981, y)
plt.xlabel(r"t [ms]")
plt.grid()
plt.show()

fig2.savefig('fig_dens_time_mod05_GAP_M_1_4-leahy.png')

np.savetxt("psd-mod05_GAP_M_1_4-leahy.dat",np.column_stack((freq,spectr)),header="frequency (hz) | PSD")
np.savetxt("rhomax-mod05_GAP_M_1_4-leahy.dat",np.column_stack((x*0.0068981,y)),header="time (ms) | density (geo)")
