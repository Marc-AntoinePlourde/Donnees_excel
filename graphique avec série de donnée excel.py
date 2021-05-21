import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

fichier = "C:\\Users\\Utilisateur\\Downloads\\Genesis_Calibration_20mai2021 - Feuille 1.tsv"
# Paramètres à choisir dans la liste (numéro de colonne)
axe_1 = 0
axe_2 = 2
# région zoomée (None = automatique)
X_min = 0
X_max = 10
Y_min = 0
Y_max = None

def graphique_zoom(donnees, noms, xmin=0, xmax=10, ymin=None, ymax = None):
    don1, don2 = donnees[:, axe_1], donnees[:, axe_2]
    if ymax is None:
        ymax = xmax
        for i in range(len(donnees[:-1, axe_1])):
            if donnees[i + 1, axe_1] > xmax:
                ymax = donnees[i, axe_2]
                break
    if ymin is None:
        ymin = xmin
        for i in range(len(donnees[:-1, axe_1])):
            if donnees[i + 1, axe_1] > xmin:
                ymin = donnees[i, axe_2]
                break
    # Plot
    fig = plt.figure()
    plt.title(f"{noms[axe_2]} in relation to the {noms[axe_1]}")
    ax = plt.axes()
    ax.plot(don1, don2)

    ax.set_xlabel(f"{noms[axe_1]}")
    ax.set_ylabel(f"{noms[axe_2]}")
    axins = zoomed_inset_axes(ax, 10, loc=2, borderpad=2)
    axins.plot(don1, don2)
    axins.set_xlim(xmin, xmax)
    axins.set_ylim(ymin, ymax)
    plt.xticks(visible=True)
    plt.yticks(visible=True)
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
    plt.draw()
    plt.show()


file = open(fichier, "r")
noms = file.readline()[:-1].split("\t")
# for i in range(len(noms)):
#    if noms[i][-2:] == "\n":
#        noms[i] = noms[i][-2]
donnees = []
for ligne in file:
    linea = ligne
    for i in range(len(ligne)):
        if ligne[i] == ",":
            linea = linea[:i] + "." + linea[i + 1:]
    donnee = linea.split()
    for j in range(len(donnee)):
        donnee[j] = float(donnee[j])
    donnees.append(donnee)
donnees = np.array(donnees)
graphique_zoom(donnees, noms, xmin=X_min, xmax=X_max,ymin=Y_min, ymax=Y_max)

