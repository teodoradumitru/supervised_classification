import matplotlib.pyplot as plt
import seaborn as sb


def distributie(t, vars, titlu="Distributia de probabilitate"):
    f = plt.figure(figsize=(10, 7))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=16)
    for v in vars:
        sb.kdeplot(t[v], shade=True, ax=ax, label=v)
    ax.set_xlabel("")
    ax.legend()


def show():
    plt.show()