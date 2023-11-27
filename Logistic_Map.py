
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do sistema caótico Mapa Logístico
# /*(Malha aberta)*/
# **************************************************************************************************************/
import numpy as np
import matplotlib.pyplot as plt

iteracoes = 100     # numero de iteracoes

## constantes
mi = 3.75   # número Malthusiano ( entre 3.56995 e 4 apresenta comportamento caotico)

## criacao das variaveis de estado
x = np.zeros(iteracoes)
n = np.zeros(iteracoes)

## condicoes iniciais
x[0] = 0.25
n[0] = 0

print('\nCondições iniciais: '+repr(x[0])+'\nConstante mi: '+repr(mi))

for k in range(1,iteracoes):
    x[k] = mi*x[k-1]*(1-x[k-1])
    n[k] = k+1

## grafico
plt.figure()
plt.plot(n,x)
##plt.xlim([0, 100])
##plt.ylim([0, 0.9])
plt.xlabel('iterações')
plt.ylabel('x')
plt.title('Mapa Logístico')
plt.grid(True)
plt.show()
