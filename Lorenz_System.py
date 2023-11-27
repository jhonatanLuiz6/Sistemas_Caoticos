
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do sistema caótico de Lorenz
# /*(Malha aberta)*/
# **************************************************************************************************************/

import numpy as np
import matplotlib.pyplot as plt

# declarações de variaveis

n = 1000  # número de iterações
T = 0.01  # tempo de amostragem
tempo = np.zeros(n)

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

# constantes da equação de lorenz
s = 10
b = 8 / 3
p = 28

# condições iniciais
x[0] = 0.1
y[0] = 0.2
z[0] = 0.3

# evolução do sistema
for k in range(1,n):
    x[k] = (-s * T + 1) * x[k - 1] + (s * T) * y[k - 1]
    y[k] = p * T * x[k - 1] + (-T + 1) * y[k - 1] - T * x[k - 1] * z[k - 1]
    z[k] = T * x[k - 1] * y[k - 1] + (-b * T + 1) * z[k - 1]

    tempo[k] = (k - 1) * T

# Plotagem das respostas sobrepostas

plt.plot(tempo, x, color='r', lw=2, label='x');
plt.plot(tempo, y, color='b', lw=2, label='y');
plt.plot(tempo, z, color='g', lw=2, label='z');
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Séries Temporais')
plt.legend()
plt.show()


ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z, lw=2)
plt.title('Diagrama de Fases')
plt.show()
