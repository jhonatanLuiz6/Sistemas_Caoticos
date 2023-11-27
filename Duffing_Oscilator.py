
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do sistema caótico Oscilador de Duffing
# /*(Malha aberta)*/
# **************************************************************************************************************/
import math
import numpy as np
import matplotlib.pyplot as plt

# variaveis do sistema
alpha = -1
beta = 1
omega = 1.2 #1.4 #2.75
delta = 0.3 #0.1 #0.2

# o caos depende da variavel gama (gama = 0.5)
gama = 0.5 # variar até 0.65

n = 5000    # número de amostras
T = 0.01  # periodo de amostragem

x1 = np.zeros(n)
x2 = np.zeros(n)
y = np.zeros(n)
tempo = np.zeros(n)
k = 1

x1[0] = 2
x2[0] = 0

#for k in range(n-1):
while (k<n):

    x1[k] = x1[k-1] + T*x2[k-1]

    x2[k] = (-alpha*T)*x1[k-1] + (-delta*T + 1)*x2[k-1] + gama*math.cos(omega*k*T) - (beta*T)*x1[k-1]*x1[k-1]*x1[k-1]

    y[k] = x1[k]

    tempo[k] = tempo[k-1]+T
    k+=1


# plotagem

plt.plot(tempo, x2, color='red', lw=1.5, label="x'")
plt.plot(tempo, x1, color='blue', lw=1.5, label="x''")
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Evolução temporal do Oscilador de Duffing')
plt.legend(loc='lower right')
plt.show()
#plt.plot(x1, x2, '.', color='green', label='Plano de Fase')
plt.plot(x1, x2, color='green', lw=2, label='Plano de Fase')

#plt.plot(x1, x2, color='green')
plt.title('Diagrama de Fases')
plt.xlabel("x'")
plt.ylabel("x''")

#plt.legend(loc='lower right')

plt.grid(True)
plt.show()
