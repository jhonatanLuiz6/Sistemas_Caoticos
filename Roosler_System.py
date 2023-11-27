# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do sistema caótico de Roosler
# /*(Malha aberta)*/
# **************************************************************************************************************/

import numpy
#from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import *
from pylab import figure, show, setp
from mpl_toolkits.mplot3d import Axes3D

# constantes do sistema de Roosler
a = 0.2 #0.13
b = 0.2 #0.2
c = 5.7 #6.5

# declarações de variaveis
T = 0.01           # tempo de amostragem
numsteps = 10000    # número de iterações


x1 = numpy.zeros(numsteps)
x2 = numpy.zeros(numsteps)
x3 = numpy.zeros(numsteps)

u = numpy.zeros(numsteps)

tempo = numpy.zeros(numsteps)

# Condições iniciais
x1[0] = 4
x2[0] = 4
x3[0] = 1

# evolução do sistema
for k in range(1, numsteps, 1):
    x1[k] = x1[k - 1] - T * (x2[k - 1] + x3[k - 1])
    x2[k] = x2[k - 1] + T * (x1[k - 1] + a*x2[k - 1]) + T*u[k-1]
    x3[k] = x3[k - 1] + T * (b + x1[k - 1] * x3[k - 1] - c * x3[k - 1])

    tempo[k] = (k - 1) * T


plt.plot(tempo, x1, color='red', lw=2, label="x''")
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Simulação em Malha Aberta')
plt.legend(loc='lower right')
plt.show()

# Figura em 3D

fig = figure()
ax1 = fig.add_axes([0.1, 0.7, 0.4, 0.2])
ax2 = fig.add_axes([0.1, 0.4, 0.4, 0.2])
ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.2])
ax4 = fig.add_axes([0.55, 0.25, 0.35, 0.5],projection='3d')


ax1.plot(tempo, x1,color='red',lw=1,label='x(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('x(t)')
ax1.legend()
#ax1.axis((t_ini,t_fin,min(x1),max(x1)))

ax2.plot(tempo, x2,color='green',lw=1,label='y(t)')
ax2.set_xlabel('t')
ax2.set_ylabel('y(t)')
ax2.legend()
#ax2.axis((t_ini,t_fin,min(x2),max(x2)))

ax3.plot(tempo, x3,color='blue',lw=1,label='z(t)')
ax3.set_xlabel('t')
ax3.set_ylabel('z(t)')
ax3.legend()
#ax3.axis((t_ini,t_fin,min(x3),max(x3)))

ax4.plot(x1, x2, x3,color='black',lw=1,label='Evolution(t)')
ax4.set_xlabel('x(t)')
ax4.set_ylabel('y(t)')
ax4.set_zlabel('z(t)')
ax4.set_title('Diagrama de Fases')

show()

print(numpy.min(x1))