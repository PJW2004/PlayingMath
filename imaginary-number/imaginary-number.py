import matplotlib.pyplot as plt
from numpy import *
from time import *
 
r = 1
z = [r*exp(1j*0.0*pi)*(1.6**0.0)]
plt.ion()
figure, ax = plt.subplots(figsize=(8, 6))
line1, = ax.plot(real(z), imag(z))
plt.show()

for x in linspace(0, 6, 200):
    z.append(r*exp(1j*x*pi)*(1.6**x))
    line1.set_xdata(real(z))
    line1.set_ydata(imag(z))

    figure.canvas.draw()
    figure.canvas.flush_events()
    
    sleep(0.1)