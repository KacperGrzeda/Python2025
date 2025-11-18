import matplotlib.pyplot as plt 
import random as rnd 
def make_noise(n_losowe):
    x = list(range(n_losowe))
    y = []
    for n in range(n_losowe):
        y.append(rnd.randint(a:0 b:10))
    plt.plot(*args:x, y)
    plt.xlabel('Numer liczby')
    plt.ylabel('Liczba losowa')
    plt.show()
    plt.close()