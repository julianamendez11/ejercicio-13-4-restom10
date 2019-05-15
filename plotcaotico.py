import numpy as np
import matplotlib.pylab as plt
datos_caotico=np.genfromtxt("datoscaotico.dat", delimiter=",")
datos1_caotico=np.genfromtxt("datos1caotico.dat", delimiter=",")
datos2_caotico=np.genfromtxt("datos2caotico.dat", delimiter=",")
datos3_caotico=np.genfromtxt("datos3caotico.dat", delimiter=",")
x_caotico=datos_caotico[:,0]
y_caotico=datos_caotico[:,1]
x1_caotico=datos1_caotico[:,0]
y1_caotico=datos1_caotico[:,1]
x2_caotico=datos2_caotico[:,0]
y2_caotico=datos2_caotico[:,1]
x3_caotico=datos3_caotico[:,0]
y3_caotico=datos3_caotico[:,1]

plt.figure()
plt.plot(x1_caotico,y1_caotico, c="lime",label='theta =0.2')
plt.plot(x_caotico,y_caotico, c="pink",label='theta =0.1')
plt.xlabel("Tiempo(s)")
plt.ylabel("Ángulo theta")
plt.title("Regimen Caotic  theta= 0.1 y 0.2")
plt.legend()
plt.savefig("figurac.pdf")


plt.figure()
plt.plot(x2_caotico,y2_caotico, c="lime",label='theta =0.3')
plt.plot(x_caotico,y_caotico, c="pink",label='theta =0.1')
plt.xlabel("Tiempo(s)")
plt.ylabel("Ángulo theta")
plt.title("Regimen Caotico  theta= 0.1 y 0.3")
plt.legend()
plt.savefig("figurac1.pdf")


plt.figure()
plt.plot(x3_caotico,y3_caotico, c="lime",label='theta =0.4')
plt.plot(x_caotico,y_caotico, c="pink",label='theta =0.1')
plt.xlabel("Tiempo(s)")
plt.ylabel("Ángulo theta")
plt.title("Regimen Caotico para  theta= 0.1 y 0.4")
plt.legend()
plt.savefig("figurac2.pdf")



y2c=np.log(np.abs(y_caotico-y1_caotico))
plt.figure()
plt.scatter(x_caotico,y2c,c='lime',  s=0.5)
plt.title('Delta de angulos')
plt.xlabel('Tiempo')
plt.ylabel('Logaritmo del delta de theta= 0.1 y 0.2')
plt.savefig('DeltaAngulosCaoticos.pdf')


y2c2=np.log(np.abs(y_caotico-y2_caotico))
plt.figure()
plt.scatter(x_caotico,y2c2,c='lime',  s=0.5)
plt.title('Delta de angulos')
plt.xlabel('Tiempo')
plt.ylabel('Logaritmo del delta de theta= 0.1 y 0.3')
plt.savefig('DeltaAngulosCaoticos1.pdf')

y2c3=np.log(np.abs(y_caotico-y3_caotico))
plt.figure()
plt.scatter(x_caotico,y2c3,c='lime',  s=0.5)
plt.title('Delta de angulos')
plt.xlabel('Tiempo')
plt.ylabel('Logaritmo del delta de theta= 0.1 y 0.4')
plt.savefig('DeltaAngulosCaoticos2.pdf')


