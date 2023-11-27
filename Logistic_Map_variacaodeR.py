import numpy
import numpy as np
import matplotlib.pyplot as plt


def f(x, r):
    return r * x * (1 - x)


n = 100 # número elementos no array
#x = np.zeros(n)  # array com os elementos da função
x = [0.1]
x0 = 0.1  # condição inicial
r = 3.75  # número Malthusiano ( entre 3.56995 e 4 apresenta comportamento caotico)
tempo = np.arange(0.0, n, 1)

ys = []     # lista para adicionar os elementos do vetor
rs = np.linspace(0,4,800)       # array com a variação de r


for r in rs:
    x = 0.1

    for n in range(500):
        #x[n + 1] = f(x[n], r)
        x = f(x, r)

    for i in range(50):
        #x[n + 1] = f(x[n], r)
        x = f(x, r)
        ys.append([r, x])

ys = np.array(ys)

#plt.plot(ys, x, label='Indice')
plt.plot(ys[:,0], ys[:,1], '.')
plt.title('Diagrama de Bifurcação do Mapa Logístico')

plt.xlabel('r')
plt.ylabel('x_eq')

plt.show()