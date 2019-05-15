import numpy as np
import matplotlib.pylab as plt
datos_caotico=np.genfromtxt("datoscaotico.dat", delimiter=",")
datos1_caotico=np.genfromtxt("datos1caotico.dat", delimiter=",")

x_caotico=datos_caotico[:,0]
y_caotico=datos_caotico[:,1]
x1_caotico=datos1_caotico[:,0]
y1_caotico=datos1_caotico[:,1]


plt.figure()
plt.plot(x1_caotico,y1_caotico, c="lime",label='theta =0.3')
plt.plot(x_caotico,y_caotico, c="pink",label='theta =0')
plt.xlabel("Tiempo(s)")
plt.ylabel("Ángulo theta")
plt.title("Regimen Caotico")
plt.savefig("figurac.pdf")
plt.legend()
plt.close()

y2c=np.log(np.abs(y_caotico-y1_caotico))
plt.figure()
plt.scatter(x_caotico,y2c,c='lime',  s=0.5)
plt.title('Delta de angulos')
plt.xlabel('Tiempo')
plt.ylabel('Logaritmo del delta de theta')
plt.savefig('DeltaAngulosCaoticos.pdf')
plt.close()

