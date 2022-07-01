import numpy as np
import time
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(x, np.cos(x), 'r-')
line2, = ax.plot(x, np.sin(x), 'b-')
line3, = ax.plot(x, np.tan(x), 'g-')

plt.title("Sin, Cos, tan",fontsize=25)

p = 0
while 1:
    line1.set_ydata(np.cos(x-0.05*p))
    line2.set_ydata(np.sin(x-0.05*p))
    line3.set_ydata(np.tan(x-0.05*p))
    
    figure.canvas.draw()
    
    figure.canvas.flush_events()
    time.sleep(0.1)
    p+=1