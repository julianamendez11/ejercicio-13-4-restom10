import numpy as np
import matplotlib.pylab as plt
datos=np.genfromtxt("datos.dat", delimiter=",")
datos1=np.genfromtxt("datos1.dat", delimiter=",")

x=datos[:,0]
y=datos[:,1]
x1=datos1[:,0]
y1=datos1[:,1]
plt.figure()
plt.plot(x1,y1, c="fuchsia",label='theta =0.3')
plt.plot(x,y, c="red",label='theta =0')
plt.xlabel("tiempo(s)")
plt.ylabel("Angulo theta")
plt.title("primer intento")
plt.savefig("figura.pdf")
plt.legend()
plt.close()

y2=np.log(np.abs(y-y1))
plt.figure()
plt.scatter(x,y2,c='coral')
plt.title('Delta de angulos')
plt.xlabel('Tiempo')
plt.ylabel('Log del delta de theta')
plt.savefig('DeltaAngulos.pdf')
plt.close()