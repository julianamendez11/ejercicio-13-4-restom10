import numpy as np
import matplotlib.pylab as plt
from scipy import interpolate
datos=np.genfromtxt("datos.dat", delimiter=",")
datos1=np.genfromtxt("datos1.dat", delimiter=",")
x=datos[:,0]
y=datos[:,1]
x1=datos1[:,0]
y1=datos1[:,1]
plt.figure()
plt.plot(x1,y1, c="fuchsia",label='theta =0.3')
plt.plot(x,y, c="red",label='theta =0.1')
plt.xlabel("tiempo(s)")
plt.ylabel("Angulo theta")
plt.title("primer intento")
plt.savefig("figura.pdf")
plt.legend()
plt.show()
plt.close()


plt.figure()
plt.plot(x, y2, 'o')
plt.plot(x,p(x),c='red')
plt.plot(x,p(x),c='red',label='regresion')
plt.title('Delta de angulos en regimen no caotico')
plt.xlabel('Tiempo')
plt.ylabel('Log del delta de theta')
plt.savefig('DeltaAngulosNoCaotico.pdf')
plt.show()
plt.legend()
plt.close()

print("El coeficiente de Lyapunov: "+str(p[1])) 