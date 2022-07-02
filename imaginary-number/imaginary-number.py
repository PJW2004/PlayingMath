import matplotlib.pyplot as plt
from numpy import *
from time import *
 
r = 1
z = []

for x in linspace(0, 6, 200):
    z.append(r*exp(1j*x*pi)*(1.6**x))
    print(plt.plot(real(z), imag(z)))
    plt.scatter(real(z), imag(z))
    plt.show()
    sleep(0.1)

'''plt.plot(real(Z), imag(Z))   # numpy에서 real과 imag 메소드 사용
plt.ylabel('Imaginary')
plt.xlabel('Real')

plt.show()'''